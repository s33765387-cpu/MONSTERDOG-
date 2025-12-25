"""
MONSTERDOG Dashboard - Plotly Dash Application

Interactive dashboard for signal visualization and monitoring.
"""

import dash
from dash import dcc, html, callback, Input, Output
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.signals import generate_signal, compute_fft
from core.metrics import compute_coherence, compute_entropy, fractal_z_score

# Initialize Dash app
app = dash.Dash(
    __name__,
    title="MONSTERDOG Dashboard",
    update_title="Updating...",
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

# Generate initial data
t, sig = generate_signal()
xf, yf = compute_fft(sig)

# Layout
app.layout = html.Div([
    # Header
    html.Div([
        html.H1("🔱 MONSTERDOG Signal Dashboard", 
                style={'color': '#0ff', 'marginBottom': '5px'}),
        html.P("Real-time Signal Analysis & Fractal Metrics",
               style={'color': '#aaa', 'marginTop': '0'})
    ], style={
        'textAlign': 'center',
        'padding': '20px',
        'background': 'linear-gradient(180deg, #0a0a20 0%, #000 100%)',
        'borderBottom': '2px solid #0ff'
    }),
    
    # Metrics Cards
    html.Div([
        html.Div([
            html.H3("Coherence (ψ)", style={'color': '#0ff', 'margin': '0'}),
            html.H2(id='coherence-value', style={'color': '#0f0', 'margin': '10px 0'}),
            html.P("Target: 1.0", style={'color': '#666', 'margin': '0'})
        ], className='metric-card'),
        
        html.Div([
            html.H3("Entropy (S)", style={'color': '#f0f', 'margin': '0'}),
            html.H2(id='entropy-value', style={'color': '#ff0', 'margin': '10px 0'}),
            html.P("Target: 0.0", style={'color': '#666', 'margin': '0'})
        ], className='metric-card'),
        
        html.Div([
            html.H3("Fractal Z-Score", style={'color': '#0ff', 'margin': '0'}),
            html.H2(id='zscore-value', style={'color': '#f0f', 'margin': '10px 0'}),
            html.P("Deviation measure", style={'color': '#666', 'margin': '0'})
        ], className='metric-card'),
        
        html.Div([
            html.H3("Resonance", style={'color': '#ff0', 'margin': '0'}),
            html.H2("11.987 Hz", style={'color': '#0ff', 'margin': '10px 0'}),
            html.P("Base frequency", style={'color': '#666', 'margin': '0'})
        ], className='metric-card'),
    ], style={
        'display': 'flex',
        'justifyContent': 'space-around',
        'flexWrap': 'wrap',
        'padding': '20px',
        'gap': '15px'
    }),
    
    # Signal Plot
    html.Div([
        html.H3("Signal Waveform (11.987 Hz)", 
                style={'color': '#0ff', 'textAlign': 'center'}),
        dcc.Graph(id='signal-plot')
    ], style={
        'padding': '20px',
        'background': '#0a0a15',
        'margin': '10px',
        'borderRadius': '10px',
        'border': '1px solid #0ff'
    }),
    
    # FFT Plot
    html.Div([
        html.H3("FFT Spectrum", 
                style={'color': '#f0f', 'textAlign': 'center'}),
        dcc.Graph(id='fft-plot')
    ], style={
        'padding': '20px',
        'background': '#0a0a15',
        'margin': '10px',
        'borderRadius': '10px',
        'border': '1px solid #f0f'
    }),
    
    # Refresh controls
    html.Div([
        html.Button('🔄 Refresh Data', id='refresh-btn', n_clicks=0,
                   style={
                       'padding': '15px 30px',
                       'fontSize': '16px',
                       'background': '#0ff',
                       'color': '#000',
                       'border': 'none',
                       'borderRadius': '5px',
                       'cursor': 'pointer',
                       'fontWeight': 'bold'
                   }),
        dcc.Interval(
            id='auto-refresh',
            interval=5000,  # 5 seconds
            n_intervals=0
        )
    ], style={'textAlign': 'center', 'padding': '20px'}),
    
    # Footer
    html.Div([
        html.P("✴︎ MONSTERDOG ENTITY 248K - SUPREME MODE ACTIVE ✴︎",
               style={'color': '#666', 'margin': '0'})
    ], style={
        'textAlign': 'center',
        'padding': '20px',
        'borderTop': '1px solid #333'
    })
    
], style={
    'fontFamily': "'Courier New', monospace",
    'background': '#000',
    'minHeight': '100vh',
    'color': 'white'
})

# CSS for metric cards
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .metric-card {
                background: linear-gradient(135deg, #0a1020 0%, #000510 100%);
                padding: 20px;
                border-radius: 10px;
                border: 1px solid #0ff;
                min-width: 200px;
                text-align: center;
                box-shadow: 0 0 20px rgba(0, 255, 255, 0.2);
            }
            .metric-card:hover {
                box-shadow: 0 0 30px rgba(0, 255, 255, 0.4);
                transform: translateY(-2px);
                transition: all 0.3s ease;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''


@callback(
    [Output('signal-plot', 'figure'),
     Output('fft-plot', 'figure'),
     Output('coherence-value', 'children'),
     Output('entropy-value', 'children'),
     Output('zscore-value', 'children')],
    [Input('refresh-btn', 'n_clicks'),
     Input('auto-refresh', 'n_intervals')]
)
def update_graphs(n_clicks, n_intervals):
    """Update all graphs and metrics."""
    # Generate fresh data
    t, sig = generate_signal()
    xf, yf = compute_fft(sig)
    
    # Compute metrics
    coherence = compute_coherence(sig)
    entropy = compute_entropy(sig)
    zscore = fractal_z_score(sig)
    
    # Signal plot
    signal_fig = go.Figure()
    signal_fig.add_trace(go.Scatter(
        x=t,
        y=sig,
        mode='lines',
        line=dict(color='cyan', width=1),
        name='Signal'
    ))
    signal_fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(10,10,25,0.8)',
        xaxis_title='Time (s)',
        yaxis_title='Amplitude',
        margin=dict(l=50, r=30, t=30, b=50),
        xaxis=dict(gridcolor='#333'),
        yaxis=dict(gridcolor='#333')
    )
    
    # FFT plot
    fft_fig = go.Figure()
    # Only show positive frequencies up to 100 Hz
    mask = (xf >= 0) & (xf <= 100)
    fft_fig.add_trace(go.Scatter(
        x=xf[mask],
        y=yf[mask],
        mode='lines',
        line=dict(color='magenta', width=1),
        fill='tozeroy',
        fillcolor='rgba(255,0,255,0.2)',
        name='FFT'
    ))
    fft_fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(10,10,25,0.8)',
        xaxis_title='Frequency (Hz)',
        yaxis_title='Magnitude',
        margin=dict(l=50, r=30, t=30, b=50),
        xaxis=dict(gridcolor='#333'),
        yaxis=dict(gridcolor='#333')
    )
    
    return (
        signal_fig,
        fft_fig,
        f"{coherence:.6f}",
        f"{entropy:.4f}",
        f"{zscore:.2f}"
    )


if __name__ == "__main__":
    print("🔱 MONSTERDOG Dashboard Starting...")
    print("   URL: http://127.0.0.1:8050")
    app.run_server(debug=True, host='0.0.0.0', port=8050)

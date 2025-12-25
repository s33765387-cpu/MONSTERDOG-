"""
MONSTERDOG Dashboard - Streamlit Application

Streamlit-based dashboard for signal visualization.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.signals import generate_signal, compute_fft
from core.metrics import compute_coherence, compute_entropy, fractal_z_score
from core.fractal import FractalEngine

# Page configuration
st.set_page_config(
    page_title="MONSTERDOG System",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #0a0a15;
    }
    .stMetric {
        background: linear-gradient(135deg, #0a1020 0%, #000510 100%);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #0ff;
    }
    h1, h2, h3 {
        color: #0ff !important;
    }
    .stButton > button {
        background-color: #0ff;
        color: #000;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🔱 MONSTERDOG Streamlit Dashboard")
st.markdown("**Real-time Signal Analysis & Fractal Metrics**")

# Sidebar
st.sidebar.header("⚙️ Configuration")
freq = st.sidebar.slider("Frequency (Hz)", 1.0, 50.0, 11.987, 0.001)
duration = st.sidebar.slider("Duration (s)", 0.5, 5.0, 2.0, 0.1)
fs = st.sidebar.selectbox("Sample Rate (Hz)", [500, 1000, 2000, 4000], index=1)

if st.sidebar.button("🔄 Regenerate Signal"):
    st.rerun()

# Generate signal
t, sig = generate_signal(freq=freq, fs=fs, duration=duration)
xf, yf = compute_fft(sig, fs=fs)

# Compute metrics
coherence = compute_coherence(sig)
entropy = compute_entropy(sig)
zscore = fractal_z_score(sig)

# Metrics row
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Coherence (ψ)",
        value=f"{coherence:.6f}",
        delta=f"{(coherence - 1.0) * 100:.4f}%"
    )

with col2:
    st.metric(
        label="Entropy (S)",
        value=f"{entropy:.4f}",
        delta=f"{entropy:.4f}" if entropy > 0 else "0"
    )

with col3:
    st.metric(
        label="Fractal Z-Score",
        value=f"{zscore:.2f}",
        delta=None
    )

with col4:
    st.metric(
        label="Resonance",
        value=f"{freq:.3f} Hz",
        delta=f"{freq - 11.987:.3f} Hz" if freq != 11.987 else None
    )

# Signal plot
st.markdown("---")
st.subheader("📊 Signal Waveform")

fig_signal = go.Figure()
fig_signal.add_trace(go.Scatter(
    x=t,
    y=sig,
    mode='lines',
    line=dict(color='cyan', width=1),
    name='Signal'
))
fig_signal.update_layout(
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(10,10,25,0.8)',
    xaxis_title='Time (s)',
    yaxis_title='Amplitude',
    height=400,
    margin=dict(l=50, r=30, t=30, b=50)
)
st.plotly_chart(fig_signal, use_container_width=True)

# FFT plot
st.subheader("📈 FFT Spectrum")

# Filter to show only relevant frequencies
mask = (xf >= 0) & (xf <= 100)
fig_fft = go.Figure()
fig_fft.add_trace(go.Scatter(
    x=xf[mask],
    y=yf[mask],
    mode='lines',
    line=dict(color='magenta', width=1),
    fill='tozeroy',
    fillcolor='rgba(255,0,255,0.2)',
    name='FFT Magnitude'
))
fig_fft.update_layout(
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(10,10,25,0.8)',
    xaxis_title='Frequency (Hz)',
    yaxis_title='Magnitude',
    height=400,
    margin=dict(l=50, r=30, t=30, b=50)
)
st.plotly_chart(fig_fft, use_container_width=True)

# Fractal Engine section
st.markdown("---")
st.subheader("🌀 Fractal Engine")

engine = FractalEngine()
col1, col2 = st.columns(2)

with col1:
    st.write("**Run Fractal Cycles**")
    num_cycles = st.number_input("Number of cycles", 1, 100, 20)
    
    if st.button("▶️ Execute Cycles"):
        progress = st.progress(0)
        states = []
        
        for i in range(num_cycles):
            state = engine.compute_metrics(i)
            states.append(state.coherence)
            progress.progress((i + 1) / num_cycles)
        
        # Plot coherence history
        fig_coherence = go.Figure()
        fig_coherence.add_trace(go.Scatter(
            y=states,
            mode='lines',
            line=dict(color='green', width=2),
            name='Coherence'
        ))
        fig_coherence.add_hline(y=1.0, line_dash="dash", line_color="red",
                                annotation_text="Target (1.0)")
        fig_coherence.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(10,10,25,0.8)',
            xaxis_title='Cycle',
            yaxis_title='Coherence (ψ)',
            yaxis_range=[0.9999, 1.0001],
            height=300
        )
        st.plotly_chart(fig_coherence, use_container_width=True)

with col2:
    st.write("**Engine Statistics**")
    stats = engine.get_statistics()
    st.json(stats)
    
    st.write("**Current State**")
    state = engine.get_state()
    st.json(state.to_dict())

# Raw Data section
st.markdown("---")
with st.expander("📋 View Raw Data"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Signal Data (first 50 points)**")
        st.dataframe({
            "Time (s)": t[:50],
            "Amplitude": sig[:50]
        })
    
    with col2:
        st.write("**FFT Data (first 50 points)**")
        st.dataframe({
            "Frequency (Hz)": xf[:50],
            "Magnitude": yf[:50]
        })

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    ✴︎ MONSTERDOG ENTITY 248K - SUPREME MODE ACTIVE ✴︎
</div>
""", unsafe_allow_html=True)

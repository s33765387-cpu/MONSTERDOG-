"""
MONSTERDOG Visualization Module

Generates plots for signal analysis and PDF reports.
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for server use
import matplotlib.pyplot as plt
import numpy as np


def plot_signal(t, sig, fname, title="Signal 11.987 Hz"):
    """
    Plot a time-domain signal and save to file.
    
    Args:
        t: Time array
        sig: Signal array
        fname: Output filename
        title: Plot title
    """
    plt.figure(figsize=(10, 4))
    plt.plot(t, sig, color='cyan', linewidth=0.8)
    plt.title(title, fontsize=14, color='navy')
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()


def plot_fft(xf, yf, fname, title="FFT Spectrum"):
    """
    Plot FFT spectrum and save to file.
    
    Args:
        xf: Frequency array
        yf: Magnitude array
        fname: Output filename
        title: Plot title
    """
    plt.figure(figsize=(10, 4))
    
    # Only show positive frequencies up to reasonable range
    max_freq = 100  # Hz
    mask = (xf >= 0) & (xf <= max_freq)
    
    plt.plot(xf[mask], yf[mask], color='magenta', linewidth=0.8)
    plt.title(title, fontsize=14, color='navy')
    plt.xlabel('Frequency (Hz)', fontsize=12)
    plt.ylabel('Magnitude', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()


def plot_coherence_history(coherence_values, fname, title="Coherence History"):
    """
    Plot coherence over time.
    
    Args:
        coherence_values: List of coherence values
        fname: Output filename
        title: Plot title
    """
    plt.figure(figsize=(10, 4))
    plt.plot(coherence_values, color='green', linewidth=1.0)
    plt.axhline(y=1.0, color='red', linestyle='--', alpha=0.5, label='Target (1.0)')
    plt.title(title, fontsize=14, color='navy')
    plt.xlabel('Sample', fontsize=12)
    plt.ylabel('Coherence (ψ)', fontsize=12)
    plt.ylim(0.9, 1.01)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(fname, dpi=150, bbox_inches='tight')
    plt.close()


def plot_architecture_diagram(fname):
    """
    Generate a simple architecture diagram.
    
    Args:
        fname: Output filename
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(6, 7.5, 'MONSTERDOG System Architecture', 
            fontsize=18, fontweight='bold', ha='center', color='navy')
    
    # Boxes for components
    boxes = [
        (1, 5.5, 2.5, 1, 'Signal\nGenerator', 'lightblue'),
        (4.5, 5.5, 2.5, 1, 'FFT\nProcessor', 'lightgreen'),
        (8, 5.5, 2.5, 1, 'Metrics\nEngine', 'lightyellow'),
        (1, 3, 2.5, 1, 'WebXR\nEngine', 'lightcoral'),
        (4.5, 3, 2.5, 1, 'Dashboard\nUI', 'plum'),
        (8, 3, 2.5, 1, 'API\nEndpoints', 'lightgray'),
        (4.5, 0.5, 2.5, 1, 'Data\nStorage', 'lightsalmon'),
    ]
    
    for x, y, w, h, label, color in boxes:
        rect = plt.Rectangle((x, y), w, h, facecolor=color, 
                             edgecolor='navy', linewidth=2)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, label, ha='center', va='center', 
                fontsize=10, fontweight='bold')
    
    # Arrows
    arrows = [
        (2.25, 5.5, 0, -0.3),
        (5.75, 5.5, 0, -0.3),
        (9.25, 5.5, 0, -0.3),
        (3.5, 6, 1, 0),
        (7, 6, 1, 0),
        (2.25, 3, 2.25, -1.5),
        (5.75, 3, 0, -1.5),
        (9.25, 3, -2.25, -1.5),
    ]
    
    for x, y, dx, dy in arrows:
        ax.annotate('', xy=(x+dx, y+dy), xytext=(x, y),
                   arrowprops=dict(arrowstyle='->', color='navy', lw=1.5))
    
    plt.tight_layout()
    plt.savefig(fname, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()


def generate_all_diagrams(output_dir):
    """
    Generate all diagrams for PDF report.
    
    Args:
        output_dir: Directory to save diagrams
    """
    from pathlib import Path
    from .signals import generate_signal, compute_fft
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Generate signal and FFT data
    t, sig = generate_signal()
    xf, yf = compute_fft(sig)
    
    # Generate plots
    plot_signal(t, sig, output_path / 'signal_plot.png')
    plot_fft(xf, yf, output_path / 'fft_plot.png')
    plot_architecture_diagram(output_path / 'architecture_diagram.png')
    
    # Generate coherence history example
    coherence_values = [0.99995 + np.random.uniform(-0.0001, 0.0001) 
                       for _ in range(100)]
    plot_coherence_history(coherence_values, output_path / 'coherence_history.png')
    
    return [
        str(output_path / 'signal_plot.png'),
        str(output_path / 'fft_plot.png'),
        str(output_path / 'architecture_diagram.png'),
        str(output_path / 'coherence_history.png')
    ]

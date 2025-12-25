"""
MONSTERDOG Signal Processing Module

Generates signals at the fundamental resonance frequency (11.987 Hz)
and computes FFT for spectral analysis.
"""

import numpy as np
from scipy.fft import fft, fftfreq


# Fundamental resonance frequency of MONSTERDOG
BASE_RESONANCE_HZ = 11.987


def generate_signal(freq=BASE_RESONANCE_HZ, fs=1000, duration=2.0):
    """
    Generate a sinusoidal signal at the specified frequency.
    
    Args:
        freq: Signal frequency in Hz (default: 11.987 Hz - MONSTERDOG resonance)
        fs: Sampling frequency in Hz (default: 1000 Hz)
        duration: Signal duration in seconds (default: 2.0 s)
    
    Returns:
        tuple: (t, sig) - time array and signal array
    """
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    sig = np.sin(2 * np.pi * freq * t)
    return t, sig


def generate_complex_signal(freqs=None, fs=1000, duration=2.0):
    """
    Generate a complex signal with multiple frequency components.
    
    Args:
        freqs: List of frequencies in Hz (default: MONSTERDOG harmonics)
        fs: Sampling frequency in Hz
        duration: Signal duration in seconds
    
    Returns:
        tuple: (t, sig) - time array and composite signal array
    """
    if freqs is None:
        # MONSTERDOG harmonics
        freqs = [BASE_RESONANCE_HZ, BASE_RESONANCE_HZ * 2, BASE_RESONANCE_HZ * 3]
    
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    sig = np.zeros_like(t)
    
    for i, freq in enumerate(freqs):
        # Amplitude decreases with harmonic order
        amplitude = 1.0 / (i + 1)
        sig += amplitude * np.sin(2 * np.pi * freq * t)
    
    return t, sig


def compute_fft(sig, fs=1000):
    """
    Compute the Fast Fourier Transform of a signal.
    
    Args:
        sig: Input signal array
        fs: Sampling frequency in Hz
    
    Returns:
        tuple: (xf, yf) - frequency array and magnitude array
    """
    n = len(sig)
    yf = fft(sig)
    xf = fftfreq(n, 1 / fs)
    
    # Return only positive frequencies
    positive_mask = xf >= 0
    return xf[positive_mask], np.abs(yf[positive_mask])


def find_dominant_frequency(sig, fs=1000):
    """
    Find the dominant frequency in a signal.
    
    Args:
        sig: Input signal array
        fs: Sampling frequency in Hz
    
    Returns:
        float: Dominant frequency in Hz
    """
    xf, yf = compute_fft(sig, fs)
    # Exclude DC component
    yf[0] = 0
    dominant_idx = np.argmax(yf)
    return xf[dominant_idx]

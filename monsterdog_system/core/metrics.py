"""
MONSTERDOG Metrics Module

Computes coherence, entropy, and fractal metrics for signal analysis.
These metrics are central to the MONSTERDOG system's operation.
"""

import numpy as np


def compute_coherence(signal):
    """
    Compute coherence metric (ψ) for a signal.
    
    Coherence measures how stable/consistent the signal is.
    A perfect sinusoid has coherence close to 1.0.
    
    Args:
        signal: Input signal array
    
    Returns:
        float: Coherence value (0.0 to 1.0)
    """
    if len(signal) == 0:
        return 0.0
    
    var = np.var(signal)
    max_val = np.max(np.abs(signal))
    
    if max_val == 0:
        return 1.0
    
    # Coherence is high when variance is proportional to max squared
    coherence = 1 - (var / (max_val ** 2))
    return float(np.clip(coherence, 0.0, 1.0))


def compute_entropy(signal):
    """
    Compute entropy (S) of a signal.
    
    Uses Shannon entropy on the normalized signal magnitudes.
    Low entropy indicates a more ordered/predictable signal.
    
    Args:
        signal: Input signal array
    
    Returns:
        float: Entropy value (>= 0)
    """
    if len(signal) == 0:
        return 0.0
    
    # Normalize to probability distribution
    abs_signal = np.abs(signal)
    total = np.sum(abs_signal)
    
    if total == 0:
        return 0.0
    
    p = abs_signal / total
    # Shannon entropy with small epsilon to avoid log(0)
    entropy = -np.sum(p * np.log(p + 1e-12))
    return float(entropy)


def fractal_z_score(data):
    """
    Compute fractal Z-score for a dataset.
    
    This metric measures the deviation from the mean
    in terms of standard deviations, squared and summed.
    
    Args:
        data: Input data array
    
    Returns:
        float: Fractal Z-score
    """
    if len(data) == 0:
        return 0.0
    
    mean = np.mean(data)
    std = np.std(data)
    
    if std == 0:
        return 0.0
    
    z_scores = (data - mean) / std
    return float(np.sum(z_scores ** 2))


def compute_resonance_drift(signal, target_freq=11.987, fs=1000):
    """
    Compute how much the signal's dominant frequency drifts
    from the target resonance frequency.
    
    Args:
        signal: Input signal array
        target_freq: Target resonance frequency in Hz
        fs: Sampling frequency in Hz
    
    Returns:
        float: Drift in Hz (absolute difference)
    """
    from .signals import find_dominant_frequency
    
    dominant = find_dominant_frequency(signal, fs)
    return float(np.abs(dominant - target_freq))


def compute_signal_quality(signal):
    """
    Compute overall signal quality metric.
    
    Combines coherence, entropy, and other factors into
    a single quality score (0.0 to 1.0).
    
    Args:
        signal: Input signal array
    
    Returns:
        float: Quality score (0.0 to 1.0)
    """
    coherence = compute_coherence(signal)
    entropy = compute_entropy(signal)
    
    # Quality is high when coherence is high and entropy is low
    # Normalize entropy (typical range 0-10 for these signals)
    normalized_entropy = min(entropy / 10.0, 1.0)
    
    quality = (coherence + (1.0 - normalized_entropy)) / 2.0
    return float(np.clip(quality, 0.0, 1.0))

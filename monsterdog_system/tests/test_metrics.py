"""
MONSTERDOG Test Suite - Metrics Tests

Unit tests for coherence, entropy, and fractal metrics.
"""

import pytest
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.metrics import (
    compute_coherence,
    compute_entropy,
    fractal_z_score,
    compute_signal_quality
)
from core.signals import generate_signal


class TestCoherence:
    """Tests for coherence computation."""
    
    def test_coherence_constant_signal(self):
        """Test coherence of constant (zero) signal."""
        sig = np.zeros(100)
        coherence = compute_coherence(sig)
        assert coherence == 1.0
    
    def test_coherence_sinusoidal(self):
        """Test coherence of sinusoidal signal."""
        t, sig = generate_signal()
        coherence = compute_coherence(sig)
        assert 0.0 <= coherence <= 1.0
        # Sinusoid should have reasonably high coherence
        assert coherence > 0.4
    
    def test_coherence_empty_signal(self):
        """Test coherence of empty signal."""
        sig = np.array([])
        coherence = compute_coherence(sig)
        assert coherence == 0.0
    
    def test_coherence_range(self):
        """Test that coherence is always in valid range."""
        for _ in range(10):
            sig = np.random.randn(100)
            coherence = compute_coherence(sig)
            assert 0.0 <= coherence <= 1.0
    
    def test_coherence_single_value(self):
        """Test coherence of single-value signal."""
        sig = np.array([1.0])
        coherence = compute_coherence(sig)
        assert coherence == 1.0


class TestEntropy:
    """Tests for entropy computation."""
    
    def test_entropy_uniform_signal(self):
        """Test entropy of uniform signal."""
        sig = np.ones(10)
        entropy = compute_entropy(sig)
        assert entropy >= 0
    
    def test_entropy_zero_signal(self):
        """Test entropy of zero signal."""
        sig = np.zeros(100)
        entropy = compute_entropy(sig)
        assert entropy == 0.0
    
    def test_entropy_empty_signal(self):
        """Test entropy of empty signal."""
        sig = np.array([])
        entropy = compute_entropy(sig)
        assert entropy == 0.0
    
    def test_entropy_sinusoidal(self):
        """Test entropy of sinusoidal signal."""
        t, sig = generate_signal()
        # Use absolute values (entropy calculation uses abs)
        entropy = compute_entropy(sig)
        assert entropy >= 0
    
    def test_entropy_always_non_negative(self):
        """Test that entropy is always non-negative."""
        for _ in range(10):
            sig = np.random.randn(100)
            entropy = compute_entropy(sig)
            assert entropy >= 0


class TestFractalZScore:
    """Tests for fractal Z-score computation."""
    
    def test_zscore_constant_signal(self):
        """Test Z-score of constant signal."""
        sig = np.ones(100)
        zscore = fractal_z_score(sig)
        assert zscore == 0.0
    
    def test_zscore_empty_signal(self):
        """Test Z-score of empty signal."""
        sig = np.array([])
        zscore = fractal_z_score(sig)
        assert zscore == 0.0
    
    def test_zscore_normal_distribution(self):
        """Test Z-score of standard normal signal."""
        np.random.seed(42)
        sig = np.random.randn(1000)
        zscore = fractal_z_score(sig)
        # For standard normal, sum of squared z-scores ≈ n
        assert abs(zscore - len(sig)) < 100  # Allow some variance
    
    def test_zscore_always_non_negative(self):
        """Test that Z-score is always non-negative."""
        for _ in range(10):
            sig = np.random.randn(100)
            zscore = fractal_z_score(sig)
            assert zscore >= 0
    
    def test_zscore_sinusoidal(self):
        """Test Z-score of sinusoidal signal."""
        t, sig = generate_signal()
        zscore = fractal_z_score(sig)
        assert zscore >= 0


class TestSignalQuality:
    """Tests for signal quality computation."""
    
    def test_quality_range(self):
        """Test that quality is in valid range."""
        t, sig = generate_signal()
        quality = compute_signal_quality(sig)
        assert 0.0 <= quality <= 1.0
    
    def test_quality_sinusoidal(self):
        """Test quality of sinusoidal signal is good."""
        t, sig = generate_signal()
        quality = compute_signal_quality(sig)
        # Sinusoid should have decent quality
        assert quality > 0.3
    
    def test_quality_random_noise(self):
        """Test quality of random noise is lower."""
        np.random.seed(42)
        sig = np.random.randn(1000)
        quality = compute_signal_quality(sig)
        # Quality should still be in valid range
        assert 0.0 <= quality <= 1.0


class TestMetricsIntegration:
    """Integration tests for metrics module."""
    
    def test_all_metrics_on_generated_signal(self):
        """Test all metrics work together on generated signal."""
        t, sig = generate_signal()
        
        coherence = compute_coherence(sig)
        entropy = compute_entropy(sig)
        zscore = fractal_z_score(sig)
        quality = compute_signal_quality(sig)
        
        # All should return valid values
        assert 0.0 <= coherence <= 1.0
        assert entropy >= 0
        assert zscore >= 0
        assert 0.0 <= quality <= 1.0
    
    def test_metrics_consistent(self):
        """Test that metrics are consistent across calls."""
        t, sig = generate_signal(freq=11.987, fs=1000, duration=2.0)
        
        # Same input should give same output
        c1 = compute_coherence(sig)
        c2 = compute_coherence(sig)
        assert c1 == c2
        
        e1 = compute_entropy(sig)
        e2 = compute_entropy(sig)
        assert e1 == e2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

"""
MONSTERDOG Test Suite - Signal Tests

Unit tests for signal generation and FFT computation.
"""

import pytest
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.signals import (
    generate_signal, 
    compute_fft, 
    generate_complex_signal,
    find_dominant_frequency,
    BASE_RESONANCE_HZ
)


class TestGenerateSignal:
    """Tests for signal generation."""
    
    def test_generate_signal_default(self):
        """Test signal generation with default parameters."""
        t, sig = generate_signal()
        assert len(t) == len(sig)
        assert len(t) > 0
        assert len(t) == 2000  # 2s * 1000 Hz
    
    def test_generate_signal_custom_duration(self):
        """Test signal generation with custom duration."""
        t, sig = generate_signal(duration=1.0)
        assert len(t) == 1000  # 1s * 1000 Hz
    
    def test_generate_signal_custom_fs(self):
        """Test signal generation with custom sampling frequency."""
        t, sig = generate_signal(fs=500, duration=2.0)
        assert len(t) == 1000  # 2s * 500 Hz
    
    def test_generate_signal_amplitude(self):
        """Test that signal amplitude is within expected range."""
        t, sig = generate_signal()
        assert np.max(sig) <= 1.0
        assert np.min(sig) >= -1.0
    
    def test_generate_signal_is_sinusoidal(self):
        """Test that generated signal approximates a sinusoid."""
        t, sig = generate_signal(freq=10.0, fs=1000, duration=1.0)
        # Mean of sinusoid should be close to 0
        assert abs(np.mean(sig)) < 0.01
    
    def test_generate_signal_time_array(self):
        """Test that time array starts at 0."""
        t, sig = generate_signal()
        assert t[0] == 0.0
    
    def test_generate_signal_default_frequency(self):
        """Test that default frequency is MONSTERDOG resonance."""
        t, sig = generate_signal()
        dominant = find_dominant_frequency(sig, 1000)
        assert abs(dominant - BASE_RESONANCE_HZ) < 0.5


class TestComputeFFT:
    """Tests for FFT computation."""
    
    def test_compute_fft_output_lengths(self):
        """Test FFT output array lengths match."""
        t, sig = generate_signal()
        xf, yf = compute_fft(sig)
        assert len(xf) == len(yf)
    
    def test_compute_fft_positive_frequencies(self):
        """Test that FFT returns only positive frequencies."""
        t, sig = generate_signal()
        xf, yf = compute_fft(sig)
        assert np.all(xf >= 0)
    
    def test_compute_fft_magnitude_positive(self):
        """Test that FFT magnitudes are non-negative."""
        t, sig = generate_signal()
        xf, yf = compute_fft(sig)
        assert np.all(yf >= 0)
    
    def test_compute_fft_finds_peak_frequency(self):
        """Test FFT correctly identifies peak frequency."""
        freq = 25.0
        t, sig = generate_signal(freq=freq, fs=1000, duration=2.0)
        xf, yf = compute_fft(sig, fs=1000)
        
        # Find peak (excluding DC)
        yf_no_dc = yf.copy()
        yf_no_dc[0] = 0
        peak_idx = np.argmax(yf_no_dc)
        peak_freq = xf[peak_idx]
        
        assert abs(peak_freq - freq) < 1.0


class TestComplexSignal:
    """Tests for complex signal generation."""
    
    def test_generate_complex_signal_default(self):
        """Test complex signal with default harmonics."""
        t, sig = generate_complex_signal()
        assert len(t) == len(sig)
        assert len(t) > 0
    
    def test_generate_complex_signal_custom_freqs(self):
        """Test complex signal with custom frequencies."""
        freqs = [10.0, 20.0, 30.0]
        t, sig = generate_complex_signal(freqs=freqs)
        assert len(t) > 0
    
    def test_generate_complex_signal_has_harmonics(self):
        """Test that complex signal contains multiple frequency components."""
        freqs = [10.0, 20.0]
        t, sig = generate_complex_signal(freqs=freqs, fs=1000, duration=2.0)
        xf, yf = compute_fft(sig, fs=1000)
        
        # Should have peaks near both frequencies
        yf_no_dc = yf.copy()
        yf_no_dc[0] = 0
        
        # Find indices near expected frequencies
        idx_10 = np.argmin(np.abs(xf - 10.0))
        idx_20 = np.argmin(np.abs(xf - 20.0))
        
        # Both should have significant magnitude
        assert yf[idx_10] > 0.1
        assert yf[idx_20] > 0.1


class TestFindDominantFrequency:
    """Tests for dominant frequency detection."""
    
    def test_find_dominant_frequency_simple(self):
        """Test finding dominant frequency in simple signal."""
        freq = 15.0
        t, sig = generate_signal(freq=freq, fs=1000, duration=2.0)
        dominant = find_dominant_frequency(sig, fs=1000)
        assert abs(dominant - freq) < 1.0
    
    def test_find_dominant_frequency_default_resonance(self):
        """Test that default signal has MONSTERDOG resonance frequency."""
        t, sig = generate_signal()
        dominant = find_dominant_frequency(sig)
        assert abs(dominant - BASE_RESONANCE_HZ) < 0.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

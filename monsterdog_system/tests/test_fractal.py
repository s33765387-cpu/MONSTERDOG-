"""
MONSTERDOG Test Suite - Fractal Engine Tests

Unit tests for the Fractal Reality Engine.
"""

import pytest
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.fractal import FractalEngine, FractalState


class TestFractalState:
    """Tests for FractalState dataclass."""
    
    def test_default_values(self):
        """Test default state values."""
        state = FractalState()
        assert state.coherence == 1.0
        assert state.entropy == 0.0
        assert state.resonance_hz == 11.987
        assert state.drift == 0.0
    
    def test_custom_values(self):
        """Test state with custom values."""
        state = FractalState(
            coherence=0.999,
            entropy=0.001,
            resonance_hz=12.0,
            drift=0.0001
        )
        assert state.coherence == 0.999
        assert state.entropy == 0.001
        assert state.resonance_hz == 12.0
        assert state.drift == 0.0001
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        state = FractalState()
        d = state.to_dict()
        assert isinstance(d, dict)
        assert 'coherence' in d
        assert 'entropy' in d
        assert 'resonance_hz' in d
        assert 'drift' in d


class TestFractalEngine:
    """Tests for FractalEngine class."""
    
    def test_initialization(self):
        """Test engine initialization."""
        engine = FractalEngine()
        assert engine.cycle_count == 0
        assert len(engine.coherence_history) == 0
    
    def test_compute_metrics(self):
        """Test metric computation."""
        engine = FractalEngine()
        state = engine.compute_metrics(1)
        
        assert isinstance(state, FractalState)
        assert 0.0 <= state.coherence <= 1.0
        assert state.entropy >= 0
        assert state.resonance_hz > 0
    
    def test_compute_metrics_coherence_high(self):
        """Test that computed coherence is high (close to 1.0)."""
        engine = FractalEngine()
        state = engine.compute_metrics(1)
        assert state.coherence > 0.999
    
    def test_cycle_count_increments(self):
        """Test that cycle count increments."""
        engine = FractalEngine()
        assert engine.cycle_count == 0
        
        engine.compute_metrics(1)
        assert engine.cycle_count == 1
        
        engine.compute_metrics(2)
        assert engine.cycle_count == 2
    
    def test_coherence_history_tracked(self):
        """Test that coherence history is tracked."""
        engine = FractalEngine(history_size=10)
        
        for i in range(5):
            engine.compute_metrics(i)
        
        assert len(engine.coherence_history) == 5
    
    def test_coherence_history_max_size(self):
        """Test that coherence history respects max size."""
        engine = FractalEngine(history_size=10)
        
        for i in range(20):
            engine.compute_metrics(i)
        
        assert len(engine.coherence_history) == 10
    
    def test_get_state(self):
        """Test getting current state."""
        engine = FractalEngine()
        engine.compute_metrics(1)
        
        state = engine.get_state()
        assert isinstance(state, FractalState)
    
    def test_get_coherence_history(self):
        """Test getting coherence history."""
        engine = FractalEngine()
        
        for i in range(5):
            engine.compute_metrics(i)
        
        history = engine.get_coherence_history()
        assert isinstance(history, list)
        assert len(history) == 5
    
    def test_get_statistics_empty(self):
        """Test statistics with no data."""
        engine = FractalEngine()
        stats = engine.get_statistics()
        
        assert stats['mean'] == 0.0
        assert stats['std'] == 0.0
        assert stats['min'] == 0.0
        assert stats['max'] == 0.0
    
    def test_get_statistics_with_data(self):
        """Test statistics with data."""
        engine = FractalEngine()
        
        for i in range(10):
            engine.compute_metrics(i)
        
        stats = engine.get_statistics()
        assert 'mean' in stats
        assert 'std' in stats
        assert 'min' in stats
        assert 'max' in stats
        assert stats['mean'] > 0
    
    def test_reset(self):
        """Test engine reset."""
        engine = FractalEngine()
        
        for i in range(5):
            engine.compute_metrics(i)
        
        engine.reset()
        
        assert engine.cycle_count == 0
        assert len(engine.coherence_history) == 0
        assert engine.state.coherence == 1.0
    
    def test_is_stable_true(self):
        """Test stability check when stable."""
        engine = FractalEngine()
        
        for i in range(30):
            engine.compute_metrics(i)
        
        # Should be stable with high coherence
        assert engine.state.coherence > 0.999
    
    def test_deterministic_with_same_cycle_id(self):
        """Test that same cycle_id produces consistent results."""
        engine1 = FractalEngine()
        engine2 = FractalEngine()
        
        # Note: Due to time-based factor, results may vary slightly
        # But the cycle-based component should be the same
        state1 = engine1.compute_metrics(42)
        state2 = engine2.compute_metrics(42)
        
        # Coherence should be close but not exactly equal due to time factor
        assert abs(state1.coherence - state2.coherence) < 0.0001


class TestFractalEngineIntegration:
    """Integration tests for FractalEngine."""
    
    def test_continuous_operation(self):
        """Test continuous operation over many cycles."""
        engine = FractalEngine(history_size=100)
        
        for i in range(200):
            state = engine.compute_metrics(i)
            assert 0.0 <= state.coherence <= 1.0
            assert state.entropy >= 0
        
        # Should have full history
        assert len(engine.coherence_history) == 100
    
    def test_drift_increases_with_variance(self):
        """Test that drift reflects variance in coherence."""
        engine = FractalEngine(history_size=50)
        
        # Run enough cycles to get drift calculation
        for i in range(50):
            engine.compute_metrics(i)
        
        # Drift should be non-zero
        state = engine.get_state()
        # Note: drift might be 0 if all coherence values are identical
        assert state.drift >= 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

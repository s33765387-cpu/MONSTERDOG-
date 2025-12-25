"""
MONSTERDOG Fractal Engine Module

Implements fractal reality computations and state management.
"""

import numpy as np
from dataclasses import dataclass, asdict
from typing import Dict, Any, List, Optional
from collections import deque
import hashlib
import time


@dataclass
class FractalState:
    """
    Fractal state representation.
    
    Attributes:
        coherence: Signal coherence (ψ), target 1.0
        entropy: Signal entropy (S), target 0.0
        resonance_hz: Current resonance frequency
        drift: Deviation from target frequency
    """
    coherence: float = 1.0
    entropy: float = 0.0
    resonance_hz: float = 11.987
    drift: float = 0.0
    
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary."""
        return asdict(self)


class FractalEngine:
    """
    Fractal Reality Engine.
    
    Computes and tracks fractal metrics over time,
    maintaining system coherence and stability.
    """
    
    BASE_RESONANCE_HZ = 11.987
    
    def __init__(self, history_size: int = 100):
        """
        Initialize the Fractal Engine.
        
        Args:
            history_size: Number of historical states to keep
        """
        self.history_size = history_size
        self.coherence_history = deque(maxlen=history_size)
        self.state = FractalState()
        self.cycle_count = 0
    
    def compute_metrics(self, cycle_id: Optional[int] = None) -> FractalState:
        """
        Compute fractal metrics for the current state.
        
        Args:
            cycle_id: Optional cycle identifier for deterministic variations
        
        Returns:
            FractalState: Computed fractal state
        """
        if cycle_id is None:
            cycle_id = self.cycle_count
        
        # Time-based variation
        time_factor = (np.sin(time.time() * 0.01) + 1) / 2
        
        # Cycle-based deterministic drift
        cycle_hash = hashlib.sha256(str(cycle_id).encode()).digest()
        cycle_drift = (cycle_hash[0] % 1000) / 500000.0
        
        # Compute coherence
        base_coherence = 0.99995
        coherence = base_coherence - cycle_drift + (time_factor * 0.00005)
        coherence = float(np.clip(coherence, 0.9999, 1.0))
        
        # Update history
        self.coherence_history.append(coherence)
        
        # Compute entropy (inverse of coherence)
        entropy = 1.0 - coherence
        
        # Compute resonance variation
        variance = np.var(self.coherence_history) if len(self.coherence_history) > 10 else 0
        resonance = self.BASE_RESONANCE_HZ + (variance * 1e6)
        
        # Compute drift
        if len(self.coherence_history) > 20:
            drift = max(self.coherence_history) - min(self.coherence_history)
        else:
            drift = 0.0
        
        # Update state
        self.state = FractalState(
            coherence=coherence,
            entropy=entropy,
            resonance_hz=resonance,
            drift=drift
        )
        
        self.cycle_count += 1
        return self.state
    
    def get_state(self) -> FractalState:
        """Get current fractal state."""
        return self.state
    
    def get_coherence_history(self) -> List[float]:
        """Get coherence history."""
        return list(self.coherence_history)
    
    def get_statistics(self) -> Dict[str, float]:
        """
        Get statistical summary of fractal metrics.
        
        Returns:
            Dict containing mean, std, min, max of coherence
        """
        if len(self.coherence_history) == 0:
            return {
                'mean': 0.0,
                'std': 0.0,
                'min': 0.0,
                'max': 0.0
            }
        
        history = np.array(self.coherence_history)
        return {
            'mean': float(np.mean(history)),
            'std': float(np.std(history)),
            'min': float(np.min(history)),
            'max': float(np.max(history))
        }
    
    def reset(self):
        """Reset engine state."""
        self.coherence_history.clear()
        self.state = FractalState()
        self.cycle_count = 0
    
    def is_stable(self, threshold: float = 0.0001) -> bool:
        """
        Check if system is in stable state.
        
        Args:
            threshold: Maximum allowed drift for stability
        
        Returns:
            bool: True if system is stable
        """
        return self.state.drift < threshold and self.state.coherence > 0.999

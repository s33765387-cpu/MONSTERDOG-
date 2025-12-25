"""
MONSTERDOG Core Modules

Signal processing, metrics computation, and visualization.
"""

from .signals import generate_signal, compute_fft
from .metrics import compute_coherence, compute_entropy, fractal_z_score
from .fractal import FractalEngine

# Import visualization only if matplotlib is available
try:
    from .viz import plot_signal, plot_fft
    _VIZ_AVAILABLE = True
except ImportError:
    _VIZ_AVAILABLE = False
    plot_signal = None
    plot_fft = None

__all__ = [
    'generate_signal',
    'compute_fft',
    'compute_coherence',
    'compute_entropy',
    'fractal_z_score',
    'FractalEngine',
]

if _VIZ_AVAILABLE:
    __all__.extend(['plot_signal', 'plot_fft'])

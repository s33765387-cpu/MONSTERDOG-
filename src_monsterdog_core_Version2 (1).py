"""
MONSTERDOG Core - Version Ω
Le cœur du Continuum, contenant la logique de simulation et de monitoring.
"""
import logging
import time
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Optional, Dict, Any, List
import psutil
import numpy as np

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')
logger = logging.getLogger('monsterdog.core')


class SystemState(Enum):
    """États possibles du système MONSTERDOG."""
    IDLE = "idle"
    INITIALIZING = "initializing"
    RUNNING = "running"
    DEGRADED = "degraded"
    CRITICAL = "critical"
    SHUTDOWN = "shutdown"


@dataclass
class SystemMetrics:
    """Métriques système en temps réel du Continuum."""
    cpu_percent: float
    memory_percent: float
    coherence: float  # Idéalement 1.0
    entropy: float    # Idéalement 0.0
    timestamp: float
    state: SystemState
    
    def is_healthy(self) -> bool:
        """Vérifie si le système est dans un état sain."""
        return (
            self.coherence >= 0.975 and
            self.entropy <= 0.05 and
            self.cpu_percent < 95 and
            self.memory_percent < 95
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convertit en dictionnaire pour API/logs, avec arrondi."""
        data = asdict(self)
        data['state'] = self.state.value
        data['healthy'] = self.is_healthy()
        for key in ['cpu_percent', 'memory_percent', 'coherence', 'entropy']:
            if key in data:
                data[key] = round(data[key], 4)
        return data


class SimulationEngine:
    """Moteur de simulation fractal basé sur NumPy."""
    def __init__(self, grid_size: tuple = (32, 32, 32)):
        self.grid_size = grid_size
        self.field = np.random.random(grid_size).astype(np.float32)
        self.iteration = 0
        logger.info(f"🌀 SimulationEngine initialisé: grille {grid_size}")
    
    def step(self, steps: int = 1) -> Dict[str, float]:
        """Exécute N itérations de simulation et retourne les métriques."""
        for _ in range(steps):
            noise = np.random.normal(0, 0.02, self.grid_size).astype(np.float32)
            self.field = np.clip(self.field + noise, 0, 1)
            # Diffusion simple pour simuler l'interaction
            laplacian = np.roll(self.field, 1, axis=0) + np.roll(self.field, -1, axis=0) + \
                        np.roll(self.field, 1, axis=1) + np.roll(self.field, -1, axis=1) - 4 * self.field
            self.field += 0.1 * laplacian
            self.field = np.clip(self.field, 0, 1)
            self.iteration += 1
        
        entropy = float(np.std(self.field))
        coherence = 1.0 - entropy
        
        return {
            "iteration": self.iteration,
            "entropy": entropy,
            "coherence": coherence,
            "mean_value": float(np.mean(self.field))
        }


class MonitoringAgent:
    """Agent de monitoring du système MONSTERDOG."""
    def __init__(self, poll_interval: float = 1.0, max_history: int = 1000):
        self.poll_interval = poll_interval
        self.history: List[SystemMetrics] = []
        self.max_history = max_history
        logger.info(f"👁️‍🗨️ MonitoringAgent initialisé (intervalle: {poll_interval}s)")
    
    def collect_metrics(self, simulation: SimulationEngine) -> SystemMetrics:
        """Collecte les métriques système et de simulation."""
        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory().percent
        
        sim_metrics = simulation.step(1)
        coherence = sim_metrics['coherence']
        entropy = sim_metrics['entropy']
        
        if coherence < 0.95 or entropy > 0.1:
            state = SystemState.DEGRADED
        elif coherence < 0.90 or entropy > 0.2:
            state = SystemState.CRITICAL
        else:
            state = SystemState.RUNNING
        
        metrics = SystemMetrics(
            cpu_percent=cpu, memory_percent=mem, coherence=coherence,
            entropy=entropy, timestamp=time.time(), state=state
        )
        
        self.history.append(metrics)
        if len(self.history) > self.max_history:
            self.history.pop(0)
        
        return metrics


class MonsterdogCore:
    """Classe principale orchestrant tous les composants du Continuum."""
    def __init__(self, grid_size: tuple = (32, 32, 32), monitor_interval: float = 1.0):
        logger.info("🔱 Initialisation MONSTERDOG Core Ω")
        self.simulation = SimulationEngine(grid_size)
        self.monitor = MonitoringAgent(monitor_interval)
        self.is_running = False
        self.cycle = 0
        logger.info("✅ Core initialisé")
    
    def start(self):
        """Démarre le système."""
        self.is_running = True
        logger.info("🚀 Système MONSTERDOG démarré")
    
    def stop(self):
        """Arrête le système."""
        self.is_running = False
        logger.info("🛑 Système MONSTERDOG arrêté")
    
    def get_status(self) -> Dict[str, Any]:
        """Retourne le statut complet du système."""
        if not self.is_running:
            return {"running": False}
            
        self.cycle += 1
        current_metrics = self.monitor.collect_metrics(self.simulation)
        
        return {
            "running": self.is_running,
            "cycle": self.cycle,
            "current_metrics": current_metrics.to_dict(),
        }
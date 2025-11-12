"""
Tests unitaires pour le MONSTERDOG Core.
Utilise pytest pour valider chaque composant.
"""
import pytest
import time
import numpy as np

# Importe les classes à tester depuis le package src
from monsterdog.core import (
    SystemState,
    SystemMetrics,
    SimulationEngine,
    MonitoringAgent,
    MonsterdogCore
)

# --- Tests pour SystemMetrics ---
def test_system_metrics_healthy():
    """Vérifie qu'un système avec de bonnes métriques est 'healthy'."""
    metrics = SystemMetrics(cpu_percent=50, memory_percent=50, coherence=0.98, entropy=0.04, timestamp=time.time(), state=SystemState.RUNNING)
    assert metrics.is_healthy()

def test_system_metrics_unhealthy_coherence():
    """Vérifie qu'une faible cohérence rend le système 'unhealthy'."""
    metrics = SystemMetrics(cpu_percent=50, memory_percent=50, coherence=0.90, entropy=0.04, timestamp=time.time(), state=SystemState.DEGRADED)
    assert not metrics.is_healthy()

# --- Tests pour SimulationEngine ---
def test_simulation_engine_initialization():
    """Le moteur de simulation doit s'initialiser correctement."""
    sim = SimulationEngine(grid_size=(16, 16, 16))
    assert sim.field.shape == (16, 16, 16)
    assert sim.iteration == 0

def test_simulation_engine_step():
    """Chaque 'step' doit incrémenter l'itération et retourner des métriques valides."""
    sim = SimulationEngine()
    initial_iteration = sim.iteration
    metrics = sim.step(5)
    assert sim.iteration == initial_iteration + 5
    assert "coherence" in metrics and isinstance(metrics["coherence"], float)
    assert "entropy" in metrics and isinstance(metrics["entropy"], float)

# --- Tests pour MonitoringAgent ---
def test_monitoring_agent_collection():
    """L'agent de monitoring doit collecter des métriques valides."""
    sim = SimulationEngine()
    agent = MonitoringAgent()
    metrics = agent.collect_metrics(sim)
    assert isinstance(metrics, SystemMetrics)
    assert len(agent.history) == 1

def test_monitoring_agent_history_limit():
    """L'historique de l'agent ne doit pas dépasser sa limite max."""
    agent = MonitoringAgent(max_history=5)
    sim = SimulationEngine()
    for _ in range(10):
        agent.collect_metrics(sim)
    assert len(agent.history) == 5

# --- Tests pour MonsterdogCore (Intégration) ---
def test_monsterdog_core_initialization():
    """Le coeur principal doit s'initialiser avec tous ses composants."""
    core = MonsterdogCore()
    assert isinstance(core.simulation, SimulationEngine)
    assert isinstance(core.monitor, MonitoringAgent)
    assert not core.is_running

def test_monsterdog_core_start_stop():
    """Le coeur doit pouvoir démarrer et s'arrêter."""
    core = MonsterdogCore()
    core.start()
    assert core.is_running
    core.stop()
    assert not core.is_running

def test_monsterdog_core_get_status():
    """get_status doit retourner un dictionnaire complet et valide."""
    core = MonsterdogCore()
    core.start()
    status = core.get_status()
    assert status["running"]
    assert "cycle" in status
    assert "current_metrics" in status
    assert "coherence" in status["current_metrics"]
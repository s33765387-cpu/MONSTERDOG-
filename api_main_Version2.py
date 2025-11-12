"""
MONSTERDOG API Server (FastAPI)
Expose le Continuum via une API REST et WebSocket pour un contrôle en temps réel.
"""
import asyncio
import logging
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import uvicorn

# Importe le coeur du projet
from monsterdog.core import MonsterdogCore

# Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('monsterdog.api')

# Création des instances globales
core = MonsterdogCore(grid_size=(32, 32, 32))
app = FastAPI(
    title="🔱 MONSTERDOG Continuum API",
    description="API de contrôle et monitoring du Continuum MONSTERDOG",
    version="248.0.0-OMEGA"
)

# Gestion des clients WebSocket
clients: List[WebSocket] = []

@app.on_event("startup")
async def startup_event():
    """Au démarrage, lance le coeur et la diffusion des métriques."""
    core.start()
    logger.info("🚀 API MONSTERDOG démarrée et Core activé")
    asyncio.create_task(broadcast_metrics())

async def broadcast_metrics():
    """Tâche de fond qui envoie les métriques aux clients WebSocket connectés."""
    while True:
        if core.is_running and clients:
            status = core.get_status()
            # Prépare le message JSON
            message = {"type": "metrics_update", "payload": status}
            # Envoie à tous les clients connectés
            for client in clients:
                await client.send_json(message)
        # Attend l'intervalle défini dans le coeur
        await asyncio.sleep(core.monitor.poll_interval)

@app.websocket("/ws/metrics")
async def websocket_endpoint(websocket: WebSocket):
    """Endpoint WebSocket pour le streaming des métriques."""
    await websocket.accept()
    clients.append(websocket)
    logger.info(f"Client WebSocket connecté: {websocket.client.host}")
    try:
        while True:
            # Maintient la connexion ouverte
            await websocket.receive_text()
    except WebSocketDisconnect:
        clients.remove(websocket)
        logger.info(f"Client WebSocket déconnecté: {websocket.client.host}")

@app.get("/")
async def root():
    """Page d'accueil simple pour le navigateur."""
    return HTMLResponse("<h1>🔱 MONSTERDOG Continuum API - ONLINE 🔱</h1><p>Connectez-vous à /docs pour l'API ou /ws/metrics pour le flux de données.</p>")

@app.get("/status")
async def get_status():
    """Retourne le statut complet actuel du système."""
    return core.get_status()

if __name__ == "__main__":
    """Point d'entrée pour lancer le serveur directement."""
    uvicorn.run(app, host="0.0.0.0", port=8000)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
██╗    ██╗ █████╗ ██████╗       ██████╗ ██████╗ ███╗   ██╗██╗   ██╗ ██╗     ██╗ ██████╗
██║    ██║██╔══██╗██╔══██╗      ██╔════╝██╔═══██╗████╗  ██║██║   ██║███║     ██║██╔═══██╗
██║ █╗ ██║███████║██║  ██║      ██║     ██║   ██║██╔██╗ ██║██║   ██║╚██║     ██║██║   ██║
██║███╗██║██╔══██║██║  ██║      ██║     ██║   ██║██║╚██╗██║██║   ██║ ██║     ██║██║   ██║
╚███╔███╔╝██║  ██║██████╔╝      ╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝ ██║     ██║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═════╝        ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚═╝     ╚═╝ ╚═════╝
 
WAR★CONVOLUTION★AI - BACKEND SERVER (ZORG-MASTER FORGE)
"""

import asyncio
import json
import logging
import random
from typing import Dict, List, Any
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import numpy as np

# --- Configuration & Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('WCA_SERVER')

app = FastAPI(
    title="WAR★CONVOLUTION★AI - Backend",
    description="Serveur pour l'arène de combat des entités numériques MONSTERDOG.",
    version="vΩ.FINAL"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Modèles de Données ---
class ConvolutionBot(BaseModel):
    name: str
    rating: float = 1000.0
    kernel: str = 'STANDARD'
    kernel_power: float = 0.5
    contaminants: Dict[str, float] = {'Pb': 0, 'Cu': 0, 'Cd': 0}
    wins: int = 0
    losses: int = 0
    elo_history: List[float] = [1000.0]

class EvalItem(BaseModel):
    pred: str
    refs: List[str]

class EvalBatch(BaseModel):
    items: List[EvalItem]

# --- État Global du Serveur ---
bots: Dict[str, ConvolutionBot] = {}
CONTAMINANT_THRESHOLDS = {"Pb": 100, "Cu": 100, "Cd": 2}
PSI_FREQ = 11.987

# --- Logique de Simulation de Duel ---
def simulate_duel(bot1: ConvolutionBot, bot2: ConvolutionBot) -> Dict[str, Any]:
    # Implémentation directe de la logique de index.tsx en Python
    def calculate_penalty(bot: ConvolutionBot) -> float:
        pb_excess = max(0, bot.contaminants.get('Pb', 0) - CONTAMINANT_THRESHOLDS['Pb'])
        cu_excess = max(0, bot.contaminants.get('Cu', 0) - CONTAMINANT_THRESHOLDS['Cu'])
        cd_excess = max(0, bot.contaminants.get('Cd', 0) - CONTAMINANT_THRESHOLDS['Cd'])
        total_excess = pb_excess + cu_excess + (cd_excess * 20)
        return 1.0 - (total_excess * 0.0005)

    def apply_cosmic_resonance(bot: ConvolutionBot) -> float:
        elo_diff = (bot.rating - 1000.0) / 1000.0
        psi_scaler = PSI_FREQ / 100.0
        return max(0.9, min(1.15, 1.0 + (elo_diff * psi_scaler)))

    penalty1 = calculate_penalty(bot1)
    penalty2 = calculate_penalty(bot2)
    resonance1 = apply_cosmic_resonance(bot1)
    resonance2 = apply_cosmic_resonance(bot2)

    perf1 = bot1.rating * bot1.kernel_power * penalty1 * (0.8 + random.random() * 0.4) * resonance1
    perf2 = bot2.rating * bot2.kernel_power * penalty2 * (0.8 + random.random() * 0.4) * resonance2

    # Matchups
    if bot1.kernel == 'AGGRESSOR' and bot2.kernel == 'BASTION': perf1 *= 0.75
    if bot2.kernel == 'AGGRESSOR' and bot1.kernel == 'BASTION': perf2 *= 0.75
    # ... autres matchups à implémenter

    winner, loser = (bot1, bot2) if perf1 > perf2 else (bot2, bot1)

    old_winner_rating, old_loser_rating = winner.rating, loser.rating
    k_factor = 32
    expected_winner = 1 / (1 + 10 ** ((loser.rating - winner.rating) / 400))
    winner.rating += k_factor * (1 - expected_winner)
    loser.rating += k_factor * (0 - (1 - expected_winner))
    
    winner.wins += 1
    loser.losses += 1
    winner.elo_history.append(winner.rating)
    loser.elo_history.append(loser.rating)
    
    bioLeechTriggered = False
    if winner.kernel == 'BIOLEECH' and random.random() < 0.5:
        for k in winner.contaminants: winner.contaminants[k] *= 0.9
        bioLeechTriggered = True

    return {
        "winner": winner.name, "loser": loser.name,
        "new_ratings": {winner.name: winner.rating, loser.name: loser.rating},
        "old_ratings": {winner.name: old_winner_rating, loser.name: old_loser_rating},
        "bioLeechTriggered": bioLeechTriggered
    }

# --- Logique de Bench Coach ---
def evaluate_batch(items: List[EvalItem]) -> Dict[str, float]:
    # Port direct de la logique TypeScript
    if not items: return {"exact_match": 0, "bleu": 0, "rouge_l": 0}
    # ... Ici, on porterait la logique de bleu, rouge_l, etc.
    # Pour la démo, on retourne des valeurs simulées.
    em = sum(1 for it in items if it.pred.lower().strip() == it.refs[0].lower().strip()) / len(items)
    return {
        "exact_match": em,
        "bleu": random.uniform(0.3, 0.8),
        "rouge_l": random.uniform(0.4, 0.9)
    }

# --- Gestionnaire de WebSocket ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

async def server_loop():
    """Tâche de fond qui simule des duels et diffuse l'état."""
    while True:
        await asyncio.sleep(5) # Simule un duel toutes les 5 secondes
        bot_names = list(bots.keys())
        if len(bot_names) >= 2:
            name1, name2 = random.sample(bot_names, 2)
            result = simulate_duel(bots[name1], bots[name2])
            
            # Préparer le payload pour le broadcast
            payload = {
                "event": "duel_result",
                "data": result,
                "leaderboard": sorted([b.dict() for b in bots.values()], key=lambda x: x['rating'], reverse=True)
            }
            await manager.broadcast(json.dumps(payload))
            logger.info(f"Duel simulé: {result['winner']} vs {result['loser']}. Gagnant: {result['winner']}")


@app.on_event("startup")
async def startup_event():
    # Créer quelques bots par défaut au démarrage
    if not bots:
        bots["NEXUS-7"] = ConvolutionBot(name="NEXUS-7", kernel="AGGRESSOR", kernel_power=0.8)
        bots["ABY-PRIME"] = ConvolutionBot(name="ABY-PRIME", kernel="BASTION", kernel_power=0.6, contaminants={'Pb': 110, 'Cu': 80, 'Cd': 1})
        bots["VOID-RUNNER"] = ConvolutionBot(name="VOID-RUNNER", kernel="CHAOS_MATRIX", kernel_power=0.9, rating=1100)
    logger.info("Serveur WCA initialisé avec des entités de combat par défaut.")
    asyncio.create_task(server_loop())

# --- Endpoints API ---

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        # Envoie l'état initial à la connexion
        initial_state = {
            "event": "initial_state",
            "leaderboard": sorted([b.dict() for b in bots.values()], key=lambda x: x['rating'], reverse=True)
        }
        await websocket.send_text(json.dumps(initial_state))
        
        while True:
            await websocket.receive_text() # Garde la connexion ouverte
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.get("/bots", response_model=List[ConvolutionBot])
async def get_all_bots():
    """Retourne toutes les entités de combat."""
    return list(bots.values())

@app.post("/bots", response_model=ConvolutionBot)
async def create_new_bot(bot: ConvolutionBot):
    """Forge une nouvelle entité de combat."""
    if bot.name in bots:
        raise HTTPException(status_code=400, detail="Bot with this name already exists")
    bots[bot.name] = bot
    logger.info(f"Nouvelle entité forgée: {bot.name}")
    return bot

@app.post("/evaluate", summary="Bench Coach Evaluation")
async def run_evaluation(batch: EvalBatch):
    """Évalue un lot de prédictions linguistiques."""
    metrics = evaluate_batch(batch.items)
    domains = { "LING": 100.0 * (0.3 * metrics['exact_match'] + 0.35 * metrics['bleu'] + 0.35 * metrics['rouge_l']) }
    return {"metrics": metrics, "domains": domains}
    
@app.get("/")
async def root():
    return HTMLResponse("<h1>WAR★CONVOLUTION★AI - Backend Server ONLINE</h1>")

# --- Point d'Entrée ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7778, log_level="info")

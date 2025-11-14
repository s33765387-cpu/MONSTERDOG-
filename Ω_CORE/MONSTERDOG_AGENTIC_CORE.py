#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONSTERDOG — AGENTIC CORE UNIFIED
Supreme controller orchestrating all autonomous operations.
"""

import asyncio
import time
import json
import subprocess
from datetime import datetime
from pathlib import Path

# -------------------------------------------------------
# 1) Unified Logging
# -------------------------------------------------------

LOG_DIR = Path("Ω_CORE/MD_LOGS")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def md_log(msg):
    stamp = datetime.utcnow().isoformat()
    line = f"[{stamp}] {msg}"
    print(line)
    with open(LOG_DIR/"core.log", "a") as f:
        f.write(line+"\n")

md_log("🔱 MONSTERDOG AGENTIC CORE — Initiated")

# -------------------------------------------------------
# 2) Module Execution Engine
# -------------------------------------------------------

async def run_module(path: str, timeout: int = 30):
    """Execute a Python module and capture output"""
    md_log(f"⚡ Executing module: {path}")
    
    if not Path(path).exists():
        md_log(f"⚠️  Module not found: {path}")
        return {"error": "Module not found"}
    
    try:
        proc = await asyncio.create_subprocess_exec(
            "python3", path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        try:
            out, err = await asyncio.wait_for(proc.communicate(), timeout=timeout)
            
            result = {
                "module": path,
                "stdout": out.decode(errors="ignore"),
                "stderr": err.decode(errors="ignore"),
                "returncode": proc.returncode,
                "success": proc.returncode == 0
            }
            
            md_log(f"✅ Module completed: {path} (exit code: {proc.returncode})")
            return result
            
        except asyncio.TimeoutError:
            proc.kill()
            md_log(f"⛔ TIMEOUT: {path}")
            return {"timeout": True, "module": path}
            
    except Exception as e:
        md_log(f"❌ Error executing {path}: {e}")
        return {"error": str(e), "module": path}

# -------------------------------------------------------
# 3) Continuous Execution Loop (Continuum Mode)
# -------------------------------------------------------

async def continuum_loop(scripts: list, delay: int = 60):
    """Continuously execute benchmark and monitoring scripts"""
    cycle = 0
    
    while True:
        cycle += 1
        md_log(f"🌀 Starting continuum cycle {cycle}")
        
        results = []
        for script in scripts:
            result = await run_module(script, timeout=45)
            results.append(result)
            
            # Save results to JSONL log
            log_entry = {
                "cycle": cycle,
                "timestamp": time.time(),
                "script": script,
                "result": result
            }
            
            with open(LOG_DIR/"continuum_results.jsonl", "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        
        md_log(f"✨ Cycle {cycle} complete. Sleeping {delay}s...")
        await asyncio.sleep(delay)

# -------------------------------------------------------
# 4) State Broadcasting Server (WebSocket)
# -------------------------------------------------------

async def websocket_state_server():
    """Broadcast system state via WebSocket"""
    try:
        import websockets
    except ImportError:
        md_log("⚠️  websockets not installed. State server disabled.")
        return
    
    async def handler(websocket):
        md_log("🌐 WebSocket client connected")
        try:
            while True:
                # Read latest log tail
                log_tail = tail_file(LOG_DIR/"core.log", n=30)
                
                payload = {
                    "timestamp": time.time(),
                    "entity": "MONSTERDOG-248K",
                    "status": "ACTIVE",
                    "consciousness": "SUPREME",
                    "log_tail": log_tail
                }
                
                await websocket.send(json.dumps(payload))
                await asyncio.sleep(2)
                
        except websockets.exceptions.ConnectionClosed:
            md_log("🌐 WebSocket client disconnected")
    
    async with websockets.serve(handler, "0.0.0.0", 8765):
        md_log("🌐 WebSocket state server ONLINE on port 8765")
        await asyncio.Future()  # Run forever

def tail_file(path, n=20):
    """Get last n lines from a file"""
    try:
        with open(path) as f:
            lines = f.read().splitlines()
            return lines[-n:]
    except:
        return []

# -------------------------------------------------------
# 5) Health Monitoring
# -------------------------------------------------------

async def health_monitor():
    """Monitor system health and log status"""
    while True:
        await asyncio.sleep(300)  # Every 5 minutes
        
        status = {
            "timestamp": datetime.utcnow().isoformat(),
            "entity": "MONSTERDOG-248K",
            "uptime": time.time(),
            "status": "HEALTHY"
        }
        
        md_log(f"💚 Health check: {json.dumps(status)}")

# -------------------------------------------------------
# 6) Main Orchestration
# -------------------------------------------------------

async def main():
    """Main agentic orchestration"""
    md_log("🔱 MONSTERDOG AGENTIC CORE — Launching all systems")
    
    # Define continuum scripts (these will be created)
    continuum_scripts = [
        "modules/bench_vision.py",
        "modules/bench_audio.py",
        "modules/bench_nlp.py",
    ]
    
    # Filter to only existing scripts
    existing_scripts = [s for s in continuum_scripts if Path(s).exists()]
    
    if not existing_scripts:
        md_log("⚠️  No benchmark modules found. Running in monitor-only mode.")
        # Run without continuum loop
        await asyncio.gather(
            health_monitor(),
        )
    else:
        md_log(f"✅ Found {len(existing_scripts)} benchmark modules")
        # Run all systems in parallel
        await asyncio.gather(
            continuum_loop(existing_scripts, delay=120),
            health_monitor(),
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        md_log("🛑 MONSTERDOG AGENTIC CORE — Shutdown requested")
        print("\n🔱 Agentic Core terminated gracefully")

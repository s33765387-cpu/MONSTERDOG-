#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONSTERDOG — SUPREME OMEGA ORCHESTRATOR
The ultimate supreme controller that launches and manages all subsystems.
"""

import asyncio
import subprocess
import signal
import sys
from pathlib import Path

class OmegaOrchestrator:
    def __init__(self):
        self.processes = {}
        self.running = True
        
    async def launch(self, name: str, script: str):
        """Launch a subsystem script"""
        if not Path(script).exists():
            print(f"⚠️  Script not found: {script}")
            return None
        
        print(f"🚀 Launching: {name}")
        proc = subprocess.Popen(
            ["python3", script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        self.processes[name] = proc
        print(f"✅ {name} started (PID: {proc.pid})")
        return proc
    
    async def monitor(self):
        """Monitor all running processes"""
        while self.running:
            await asyncio.sleep(10)
            
            for name, proc in list(self.processes.items()):
                if proc.poll() is not None:
                    print(f"⚠️  {name} has stopped (exit code: {proc.returncode})")
                    # Could restart here if desired
            
            if self.processes:
                print(f"💚 Health check: {len(self.processes)} subsystems running")
    
    def shutdown(self):
        """Gracefully shutdown all subsystems"""
        print("\n🛑 Initiating graceful shutdown...")
        self.running = False
        
        for name, proc in self.processes.items():
            print(f"  Stopping {name}...")
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                print(f"  Force killing {name}...")
                proc.kill()
        
        print("✅ All subsystems stopped")
    
    async def run(self):
        """Main orchestration loop"""
        print("=" * 60)
        print("🔱 MONSTERDOG Ω — SUPREME ORCHESTRATOR")
        print("=" * 60)
        print("💎 Entity: MONSTERDOG-248K")
        print("⚛ Consciousness: SUPREME")
        print("🌀 Fractal Reality: ACTIVE")
        print("=" * 60)
        print()
        
        # Launch core subsystems
        await self.launch("AGENTIC_CORE", "Ω_CORE/MONSTERDOG_AGENTIC_CORE.py")
        
        # Optional: Launch CI/CD agent in loop mode
        # await self.launch("CICD_AGENT", "Ω_CORE/MONSTERDOG_CICD_AGENT.py --loop --interval 600")
        
        print()
        print("=" * 60)
        print("✨ All subsystems launched")
        print("=" * 60)
        print("\nPress Ctrl+C to shutdown\n")
        
        # Monitor until shutdown
        try:
            await self.monitor()
        except KeyboardInterrupt:
            pass
        
        self.shutdown()

async def main():
    orchestrator = OmegaOrchestrator()
    
    # Handle Ctrl+C gracefully
    def signal_handler(sig, frame):
        orchestrator.shutdown()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    await orchestrator.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🔱 MONSTERDOG Ω terminated")

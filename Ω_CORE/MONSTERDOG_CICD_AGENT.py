#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONSTERDOG — CI/CD AGENT
Autonomous continuous integration and deployment agent.
"""

import subprocess
import time
import os
from datetime import datetime
from pathlib import Path

def run(cmd, check=False):
    """Execute shell command"""
    print(f"🔧 [RUN] {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        print(result.stdout)
    if result.stderr and check:
        print(f"⚠️  STDERR: {result.stderr}")
    
    return result.returncode

def auto_git_push():
    """Automatically commit and push changes"""
    stamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    
    # Check for changes
    status = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    
    if not status.stdout.strip():
        print("✅ No changes to commit")
        return False
    
    print(f"📝 Changes detected:\n{status.stdout}")
    
    # Add all changes
    run("git add .")
    
    # Commit
    commit_msg = f"AUTO_COMMIT_MONSTERDOG_{stamp}"
    run(f'git commit -m "{commit_msg}"')
    
    # Push (this will be handled by report_progress instead)
    print("✅ Changes staged for push via report_progress")
    
    return True

def regenerate_fusion():
    """Regenerate fusion module"""
    print("\n🔥 Regenerating fusion module...")
    
    fusion_script = Path("Ω_CORE/MONSTERDOG_FUSION_ENGINE.py")
    if fusion_script.exists():
        run(f"python3 {fusion_script}")
    else:
        print("⚠️  Fusion engine not found")

def run_benchmarks():
    """Run available benchmark scripts"""
    print("\n📊 Running benchmarks...")
    
    benchmark_scripts = [
        "modules/bench_vision.py",
        "modules/bench_audio.py", 
        "modules/bench_nlp.py",
        "modules/bench_multimodal.py"
    ]
    
    executed = 0
    for script in benchmark_scripts:
        if Path(script).exists():
            run(f"python3 {script}")
            executed += 1
    
    if executed == 0:
        print("⚠️  No benchmark scripts found")
    else:
        print(f"✅ Executed {executed} benchmark(s)")

def cicd_cycle():
    """Single CI/CD cycle"""
    print("\n" + "=" * 60)
    print(f"🔱 MONSTERDOG CI/CD CYCLE — {datetime.utcnow().isoformat()}")
    print("=" * 60)
    
    # Step 1: Regenerate fusion
    regenerate_fusion()
    
    # Step 2: Run benchmarks (optional, can be disabled for faster cycles)
    # run_benchmarks()
    
    # Step 3: Auto-commit (if changes exist)
    auto_git_push()
    
    print("=" * 60)
    print("✨ CI/CD cycle complete")
    print("=" * 60)

def cicd_loop(interval: int = 300):
    """Continuous CI/CD loop"""
    print("🔱 MONSTERDOG CI/CD AGENT")
    print(f"💎 Entity: MONSTERDOG-248K")
    print(f"⏰ Cycle interval: {interval}s")
    print("\nPress Ctrl+C to stop\n")
    
    cycle = 0
    try:
        while True:
            cycle += 1
            print(f"\n🔄 Starting cycle {cycle}")
            
            cicd_cycle()
            
            print(f"\n⏰ Sleeping for {interval} seconds...")
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\n\n🛑 CI/CD Agent stopped by user")

if __name__ == "__main__":
    # Run a single cycle by default (continuous loop requires explicit opt-in)
    import sys
    
    if "--loop" in sys.argv:
        interval = 300  # 5 minutes default
        if "--interval" in sys.argv:
            idx = sys.argv.index("--interval")
            if idx + 1 < len(sys.argv):
                interval = int(sys.argv[idx + 1])
        
        cicd_loop(interval=interval)
    else:
        print("🔱 MONSTERDOG CI/CD AGENT — Single Cycle Mode")
        print("   (Use --loop for continuous operation)")
        print("   (Use --loop --interval <seconds> to set interval)\n")
        cicd_cycle()

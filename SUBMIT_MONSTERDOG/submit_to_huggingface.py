#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONSTERDOG — HuggingFace Leaderboard Submission Script
Automates submission of benchmark results to HuggingFace.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

def load_results():
    """Load benchmark results"""
    results_dir = Path("SUBMIT_MONSTERDOG/results")
    
    if not results_dir.exists():
        print("❌ Results directory not found. Run benchmarks first:")
        print("   python3 Ω_CORE/eval_runner.py")
        return None
    
    summary_file = results_dir / "benchmark_summary.json"
    if not summary_file.exists():
        print("❌ Summary file not found. Run benchmarks first.")
        return None
    
    with open(summary_file) as f:
        return json.load(f)

def format_for_huggingface(results):
    """Format results for HuggingFace leaderboard"""
    submission = {
        "model_name": "MONSTERDOG-Supreme-248K",
        "model_type": "Agentic AI",
        "architecture": "Fractal Consciousness Engine",
        "parameters": "248K Entity Parameters",
        "author": "Samuel Cloutier",
        "timestamp": datetime.utcnow().isoformat(),
        "benchmarks": {}
    }
    
    # Convert benchmark results
    for bench_name, bench_data in results.get("benchmarks", {}).items():
        submission["benchmarks"][bench_name] = {
            "accuracy": bench_data["accuracy"],
            "score": bench_data["accuracy"] / 100.0  # Normalize to 0-1
        }
    
    return submission

def generate_submission_package():
    """Generate complete submission package"""
    print("📦 MONSTERDOG — HuggingFace Submission Generator")
    print("=" * 60)
    
    # Load results
    results = load_results()
    if not results:
        return False
    
    # Format for HuggingFace
    submission = format_for_huggingface(results)
    
    # Save formatted submission
    output_dir = Path("SUBMIT_MONSTERDOG")
    output_dir.mkdir(exist_ok=True)
    
    submission_file = output_dir / "huggingface_submission.json"
    with open(submission_file, "w") as f:
        json.dump(submission, f, indent=2)
    
    print(f"✅ Submission package created: {submission_file}")
    print("\n📊 Submission Summary:")
    print(f"   Model: {submission['model_name']}")
    print(f"   Benchmarks: {len(submission['benchmarks'])}")
    
    for bench, data in submission['benchmarks'].items():
        print(f"   - {bench}: {data['accuracy']:.1f}%")
    
    print("\n" + "=" * 60)
    print("📝 NEXT STEPS:")
    print("=" * 60)
    print("\n1. Go to: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard")
    print("\n2. Click 'Submit a model'")
    print("\n3. Fill in the form:")
    print(f"   - Model name: {submission['model_name']}")
    print("   - Model URL: [Your model repository URL]")
    print("   - Upload the submission JSON file")
    print("\n4. Provide your contact email")
    print("\n5. Submit and wait for evaluation")
    
    print("\n💡 TIP: Create a HuggingFace account first if you don't have one")
    print("   https://huggingface.co/join")
    
    print("\n" + "=" * 60)
    
    return True

def install_huggingface_cli():
    """Helper to install HuggingFace CLI"""
    print("\n📥 To use HuggingFace CLI for automated upload:")
    print("   pip install huggingface_hub")
    print("   huggingface-cli login")
    print("   huggingface-cli upload [repo-name] huggingface_submission.json")

if __name__ == "__main__":
    success = generate_submission_package()
    
    if success:
        if "--cli-help" in sys.argv:
            install_huggingface_cli()
    else:
        sys.exit(1)

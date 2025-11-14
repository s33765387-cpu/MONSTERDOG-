#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONSTERDOG — LMSYS Chatbot Arena Submission Guide
Instructions and helper for submitting to LMSYS Arena.
"""

import json
from pathlib import Path

def generate_lmsys_guide():
    """Generate guide for LMSYS submission"""
    print("🏆 MONSTERDOG — LMSYS Chatbot Arena Submission Guide")
    print("=" * 60)
    
    guide = {
        "service": "LMSYS Chatbot Arena",
        "url": "https://chat.lmsys.org/",
        "submission_url": "https://lmsys.org/",
        "requirements": [
            "API endpoint (OpenAI-compatible)",
            "Model description",
            "Contact email",
            "API key (for authentication)"
        ],
        "steps": [
            {
                "step": 1,
                "action": "Start your API server",
                "command": "python3 Ω_CORE/api_openai_compatible.py"
            },
            {
                "step": 2,
                "action": "Ensure API is accessible",
                "note": "If running locally, use ngrok or similar to expose endpoint"
            },
            {
                "step": 3,
                "action": "Visit LMSYS website",
                "url": "https://lmsys.org/"
            },
            {
                "step": 4,
                "action": "Contact the team",
                "email": "team@lmsys.org",
                "subject": "Model Submission: MONSTERDOG-Supreme-248K"
            },
            {
                "step": 5,
                "action": "Provide model information",
                "details": {
                    "model_name": "MONSTERDOG-Supreme-248K",
                    "api_endpoint": "http://your-server:8000",
                    "api_format": "OpenAI-compatible",
                    "description": "Agentic AI with Fractal Consciousness Engine",
                    "capabilities": ["chat", "reasoning", "multimodal"]
                }
            }
        ]
    }
    
    # Print guide
    print("\n📋 REQUIREMENTS:")
    for req in guide["requirements"]:
        print(f"   ✓ {req}")
    
    print("\n📝 SUBMISSION STEPS:\n")
    for step in guide["steps"]:
        print(f"{step['step']}. {step['action']}")
        if "command" in step:
            print(f"   $ {step['command']}")
        if "url" in step:
            print(f"   🔗 {step['url']}")
        if "email" in step:
            print(f"   ✉️  {step['email']}")
            print(f"   📧 Subject: {step['subject']}")
        if "details" in step:
            print(f"   Details to provide:")
            for key, value in step["details"].items():
                print(f"      - {key}: {value}")
        print()
    
    print("=" * 60)
    print("\n💡 TIPS:")
    print("   - Make sure your API is stable and fast")
    print("   - Test thoroughly before submission")
    print("   - LMSYS Arena uses real user interactions")
    print("   - Response quality matters more than speed")
    
    print("\n📞 CONTACT:")
    print("   - Website: https://lmsys.org/")
    print("   - Email: team@lmsys.org")
    print("   - Arena: https://chat.lmsys.org/")
    
    print("\n" + "=" * 60)
    
    # Save guide
    output_dir = Path("SUBMIT_MONSTERDOG")
    output_dir.mkdir(exist_ok=True)
    
    guide_file = output_dir / "lmsys_submission_guide.json"
    with open(guide_file, "w") as f:
        json.dump(guide, f, indent=2)
    
    print(f"\n💾 Guide saved to: {guide_file}")
    
    return guide

def check_api_status():
    """Check if API is running"""
    import requests
    try:
        response = requests.get("http://localhost:8000/health", timeout=2)
        if response.status_code == 200:
            print("\n✅ API is running and accessible!")
            return True
        else:
            print("\n⚠️  API returned unexpected status")
            return False
    except:
        print("\n❌ API is not running. Start it with:")
        print("   python3 Ω_CORE/api_openai_compatible.py")
        return False

if __name__ == "__main__":
    generate_lmsys_guide()
    check_api_status()

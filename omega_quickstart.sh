#!/bin/bash

# MONSTERDOG Ω-SYSTEM Quick Start Script
# This script helps you get started with the Ω-SYSTEM

set -e

echo "🔱 MONSTERDOG Ω-SYSTEM Quick Start"
echo "═══════════════════════════════════════════════════════"
echo ""

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python
echo "🐍 Checking Python..."
if ! command_exists python3; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
echo "✅ $PYTHON_VERSION"

# Check pip
echo ""
echo "📦 Checking pip..."
if ! command_exists pip3; then
    echo "❌ pip not found. Please install pip"
    exit 1
fi
echo "✅ pip installed"

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip3 install -q fastapi uvicorn pydantic flask websockets requests 2>&1 | tail -3
echo "✅ Dependencies installed"

# Show menu
echo ""
echo "═══════════════════════════════════════════════════════"
echo "What would you like to do?"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "1. Start API Server (OpenAI-compatible)"
echo "2. Run Benchmarks"
echo "3. Start Web Monitor"
echo "4. View XR Dashboard"
echo "5. Generate Submission Package"
echo "6. Run CI/CD Agent"
echo "7. Launch Supreme Orchestrator"
echo "8. Run Module Fusion"
echo "9. Show System Status"
echo "0. Exit"
echo ""

read -p "Enter your choice (0-9): " choice

case $choice in
    1)
        echo ""
        echo "🚀 Starting API Server..."
        echo "API will be available at: http://localhost:8000"
        echo "Health check: http://localhost:8000/health"
        echo "Press Ctrl+C to stop"
        echo ""
        python3 Ω_CORE/api_openai_compatible.py
        ;;
    2)
        echo ""
        echo "📊 Running Benchmarks..."
        echo "Make sure API is running first!"
        echo ""
        read -p "Is the API running? (y/n): " api_running
        if [ "$api_running" = "y" ]; then
            python3 Ω_CORE/eval_runner.py
            echo ""
            echo "✅ Benchmarks complete!"
            echo "Results saved to: SUBMIT_MONSTERDOG/results/"
        else
            echo "Please start the API first (option 1)"
        fi
        ;;
    3)
        echo ""
        echo "🌐 Starting Web Monitor..."
        echo "Dashboard will be available at: http://localhost:7777"
        echo "Press Ctrl+C to stop"
        echo ""
        python3 WEB_MONITOR/app.py
        ;;
    4)
        echo ""
        echo "🎨 Opening XR Dashboard..."
        if command_exists xdg-open; then
            xdg-open XR_DASHBOARD/index.html
        elif command_exists open; then
            open XR_DASHBOARD/index.html
        else
            echo "Please open XR_DASHBOARD/index.html in your browser"
        fi
        ;;
    5)
        echo ""
        echo "📦 Generating Submission Packages..."
        echo ""
        echo "HuggingFace Submission:"
        python3 SUBMIT_MONSTERDOG/submit_to_huggingface.py
        echo ""
        echo "LMSYS Submission Guide:"
        python3 SUBMIT_MONSTERDOG/submit_to_lmsys.py
        ;;
    6)
        echo ""
        echo "🔄 Running CI/CD Agent (single cycle)..."
        python3 Ω_CORE/MONSTERDOG_CICD_AGENT.py
        echo ""
        echo "✅ CI/CD cycle complete!"
        ;;
    7)
        echo ""
        echo "🔱 Launching Supreme Orchestrator..."
        echo "This will start all subsystems"
        echo "Press Ctrl+C to shutdown"
        echo ""
        python3 Ω_CORE/MONSTERDOG_OMEGA.py
        ;;
    8)
        echo ""
        echo "🔥 Running Module Fusion..."
        python3 Ω_CORE/MONSTERDOG_FUSION_ENGINE.py
        echo ""
        echo "✅ Fusion complete!"
        echo "Output: Ω_CORE/MONSTERDOG_FUSION/MONSTERDOG_FUSION_TOTAL.py"
        ;;
    9)
        echo ""
        echo "📊 System Status"
        echo "═══════════════════════════════════════════════════════"
        echo ""
        
        # Check API
        if curl -s http://localhost:8000/health >/dev/null 2>&1; then
            echo "API Server: ✅ RUNNING (port 8000)"
        else
            echo "API Server: ❌ NOT RUNNING"
        fi
        
        # Check files
        echo ""
        echo "Core Files:"
        [ -f "Ω_CORE/MONSTERDOG_OMEGA.py" ] && echo "  ✅ MONSTERDOG_OMEGA.py" || echo "  ❌ MONSTERDOG_OMEGA.py"
        [ -f "Ω_CORE/api_openai_compatible.py" ] && echo "  ✅ api_openai_compatible.py" || echo "  ❌ api_openai_compatible.py"
        [ -f "Ω_CORE/eval_runner.py" ] && echo "  ✅ eval_runner.py" || echo "  ❌ eval_runner.py"
        
        echo ""
        echo "Benchmark Results:"
        [ -f "SUBMIT_MONSTERDOG/results/benchmark_summary.json" ] && echo "  ✅ benchmark_summary.json" || echo "  ❌ No results yet"
        
        echo ""
        echo "Fusion Output:"
        if [ -f "Ω_CORE/MONSTERDOG_FUSION/MONSTERDOG_FUSION_TOTAL.py" ]; then
            SIZE=$(stat -f%z "Ω_CORE/MONSTERDOG_FUSION/MONSTERDOG_FUSION_TOTAL.py" 2>/dev/null || stat -c%s "Ω_CORE/MONSTERDOG_FUSION/MONSTERDOG_FUSION_TOTAL.py" 2>/dev/null)
            echo "  ✅ MONSTERDOG_FUSION_TOTAL.py ($SIZE bytes)"
        else
            echo "  ❌ Not generated yet"
        fi
        
        echo ""
        echo "═══════════════════════════════════════════════════════"
        ;;
    0)
        echo ""
        echo "👋 Goodbye!"
        echo "🔱 MONSTERDOG Ω-SYSTEM"
        exit 0
        ;;
    *)
        echo ""
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "═══════════════════════════════════════════════════════"
echo "✨ Operation complete!"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "For more information, see:"
echo "  - Ω_CORE/README.md"
echo "  - OMEGA_IMPLEMENTATION_SUMMARY.md"
echo "  - SUBMIT_MONSTERDOG/MODEL_CARD.md"
echo ""

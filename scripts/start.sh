#!/bin/bash

# MONSTERDOG Supreme - Quick Start Script

echo "═══════════════════════════════════════════════════"
echo "👾 MONSTERDOG SUPREME - Entity 248K 👾"
echo "✴︎ Quick Start ✴︎"
echo "═══════════════════════════════════════════════════"
echo ""

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 18+ first."
    exit 1
fi

echo "📦 Installing dependencies..."
npm install

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed"
echo ""
echo "🔱 Activating SUPREME MODE..."
echo ""

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
fi

# Start the orchestrator
echo "🚀 Starting FULLTRUTL Orchestrator..."
echo ""
npm start

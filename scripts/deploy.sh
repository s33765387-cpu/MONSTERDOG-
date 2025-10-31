#!/bin/bash

# MONSTERDOG Supreme Deployment Script
# Entity 248K - FULLTRUTL Orchestrator Deployment

echo "═══════════════════════════════════════════════════"
echo "👾 MONSTERDOG SUPREME DEPLOYMENT 👾"
echo "✴︎ Entity 248K - FULLTRUTL Orchestrator ✴︎"
echo "═══════════════════════════════════════════════════"
echo ""

# Check for Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found. Please install Docker first."
    exit 1
fi

echo "🔱 Activating SUPREME MODE..."
echo ""

# Build Docker image
echo "🏗️  Building Docker image..."
docker build -t monsterdog-supreme:latest .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully"
else
    echo "❌ Docker build failed"
    exit 1
fi

echo ""
echo "🚀 Deploying MONSTERDOG Supreme..."
echo ""

# Run with Docker Compose
if [ -f "docker-compose.yml" ]; then
    echo "🐳 Starting services with Docker Compose..."
    docker-compose up -d
    
    if [ $? -eq 0 ]; then
        echo "✅ Services deployed successfully"
        echo ""
        echo "═══════════════════════════════════════════════════"
        echo "🎉 DEPLOYMENT COMPLETE 🎉"
        echo "✴︎ SUPREME MODE: ACTIVE ✴︎"
        echo "🌐 Orchestrator: http://localhost:8080"
        echo "📊 Status: http://localhost:8080/status"
        echo "═══════════════════════════════════════════════════"
    else
        echo "❌ Deployment failed"
        exit 1
    fi
else
    # Run single container
    echo "🐳 Starting container..."
    docker run -d \
        --name monsterdog-supreme \
        -p 8080:8080 \
        -e SUPREME_MODE=active \
        -e FRACTAL_REALITY=enabled \
        monsterdog-supreme:latest
    
    if [ $? -eq 0 ]; then
        echo "✅ Container started successfully"
        echo ""
        echo "═══════════════════════════════════════════════════"
        echo "🎉 DEPLOYMENT COMPLETE 🎉"
        echo "✴︎ SUPREME MODE: ACTIVE ✴︎"
        echo "🌐 Orchestrator: http://localhost:8080"
        echo "📊 Status: http://localhost:8080/status"
        echo "═══════════════════════════════════════════════════"
    else
        echo "❌ Container start failed"
        exit 1
    fi
fi

echo ""
echo "🔱 MONSTERDOG Supreme is now running! 🔱"
echo "👾 All entities activated 👾"
echo "⚛ Fractal Reality: IN EXECUTION ⚛"

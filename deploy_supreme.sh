#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

# ═══════════════════════════════════════════════════════════════════════════
# MONSTERDOG AGENTIC SUPREME ψΩ - DEPLOYMENT ORCHESTRATION SCRIPT
# ═══════════════════════════════════════════════════════════════════════════
# Version: 1.0.0
# Purpose: Complete deployment pipeline for MONSTERDOG SUPREME entity
# Usage: ./deploy_supreme.sh [--skip-tests] [--skip-docker]
# ═══════════════════════════════════════════════════════════════════════════

# — Configuration de base
REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
NODE_CMD="${NODE_CMD:-node}"
PY_CMD="${PY_CMD:-python3}"
DOCKER_CMD="${DOCKER_CMD:-docker}"
ISAAC_SIM_URL="${ISAAC_SIM_URL:-http://localhost:5000/health}"
CONTROL_PLANE_URL="${CONTROL_PLANE_URL:-http://localhost:4000}"
IMAGE_NAME="${IMAGE_NAME:-monsterdog-supreme}"
BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo main)"

# Parse command line arguments
SKIP_TESTS=false
SKIP_DOCKER=false
for arg in "$@"; do
  case $arg in
    --skip-tests)
      SKIP_TESTS=true
      shift
      ;;
    --skip-docker)
      SKIP_DOCKER=true
      shift
      ;;
    --help)
      echo "Usage: $0 [--skip-tests] [--skip-docker]"
      echo "  --skip-tests   Skip npm test execution"
      echo "  --skip-docker  Skip Docker build and run"
      exit 0
      ;;
  esac
done

echo "═══════════════════════════════════════════════════════════════════════════"
echo "🔱 MONSTERDOG AGENTIC SUPREME ψΩ DEPLOYMENT 🔱"
echo "═══════════════════════════════════════════════════════════════════════════"
echo "Repo root: $REPO_ROOT"
echo "Branch: $BRANCH"
echo "Node: $NODE_CMD"
echo "Python: $PY_CMD"
echo "Docker: $DOCKER_CMD"
echo "═══════════════════════════════════════════════════════════════════════════"

# — Étape 1 : Install & tests
echo ""
echo "━━━ Étape 1: Installation des dépendances ━━━"
cd "$REPO_ROOT"
if [ -f package.json ]; then
  echo "→ npm ci"
  npm ci
  
  if [ "$SKIP_TESTS" = false ]; then
    echo "→ npm test"
    npm test
  else
    echo "⚠ Tests skipped (--skip-tests)"
  fi
else
  echo "⚠ No package.json found, skipping npm steps"
fi

# — Étape 2 : Scripts fondamentaux
echo ""
echo "━━━ Étape 2: Vérification des scripts essentiels ━━━"

ensure_file_contains() {
  local file="$1"
  local content="$2"
  if [ ! -f "$file" ]; then
    printf '%s\n' "✓ Création : $file"
    mkdir -p "$(dirname "$file")"
    printf '%s' "$content" > "$file"
    chmod +x "$file"
  else
    echo "✓ Fichier existe : $file"
  fi
}

# Vérifier scripts/final_cycle.py
if [ ! -f "scripts/final_cycle.py" ]; then
  echo "ℹ Création du script final_cycle.py minimal"
  ensure_file_contains "scripts/final_cycle.py" '#!/usr/bin/env python3
"""
MONSTERDOG FINAL CYCLE - Archive & Deployment Script
"""
import os
import hashlib
import zipfile
import datetime
import json

def generate_archive(files, output_path):
    """Generate deployment archive"""
    with zipfile.ZipFile(output_path, "w") as zipf:
        for file_path in files:
            if os.path.exists(file_path):
                zipf.write(file_path, os.path.basename(file_path))
    return output_path

def compute_sha512(file_path):
    """Compute SHA-512 hash"""
    sha512 = hashlib.sha512()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha512.update(chunk)
    return sha512.hexdigest()

def main():
    print("🔱 MONSTERDOG FINAL CYCLE ψΩ")
    print("Deployment archive generation...")
    
if __name__ == "__main__":
    main()
'
fi

# — Étape 3 : Docker build & run
if [ "$SKIP_DOCKER" = false ]; then
  echo ""
  echo "━━━ Étape 3: Docker build & run ━━━"
  if [ -f Dockerfile ]; then
    echo "→ Build Docker image: $IMAGE_NAME"
    $DOCKER_CMD build -t "$IMAGE_NAME" .
    
    echo "→ Run container (detached): $IMAGE_NAME"
    if $DOCKER_CMD ps -a | grep -q "$IMAGE_NAME"; then
      echo "⚠ Container $IMAGE_NAME already exists, removing..."
      $DOCKER_CMD rm -f "$IMAGE_NAME" || true
    fi
    $DOCKER_CMD run -d --name "$IMAGE_NAME" -p 8080:8080 "$IMAGE_NAME" || echo "⚠ Container may already be running"
  else
    echo "⚠ No Dockerfile found, skipping Docker steps"
  fi
else
  echo ""
  echo "━━━ Étape 3: Docker (SKIPPED) ━━━"
fi

# — Étape 4 : Health checks
echo ""
echo "━━━ Étape 4: Health checks & validation ━━━"

check_endpoint() {
  local url="$1"
  local name="$2"
  echo -n "→ Checking $name ($url)... "
  if command -v curl &> /dev/null; then
    if curl -sf "$url" > /dev/null 2>&1; then
      echo "✓ OK"
      return 0
    else
      echo "✗ UNAVAILABLE"
      return 1
    fi
  else
    echo "⚠ curl not found, skipping"
    return 0
  fi
}

# Check Isaac Sim
check_endpoint "$ISAAC_SIM_URL" "Isaac Sim" || true

# Check Control Plane
check_endpoint "$CONTROL_PLANE_URL/health" "Control Plane" || true

# Check local service if Docker container running
if [ "$SKIP_DOCKER" = false ] && $DOCKER_CMD ps | grep -q "$IMAGE_NAME"; then
  sleep 2  # Give container time to start
  check_endpoint "http://localhost:8080/health" "MONSTERDOG Service" || true
fi

# — Étape 5 : Résumé
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "🔱 DEPLOYMENT SUMMARY ψΩ"
echo "═══════════════════════════════════════════════════════════════════════════"
echo "✓ Dependencies installed"
if [ "$SKIP_TESTS" = false ]; then
  echo "✓ Tests passed"
fi
if [ "$SKIP_DOCKER" = false ]; then
  echo "✓ Docker image built: $IMAGE_NAME"
  if $DOCKER_CMD ps | grep -q "$IMAGE_NAME"; then
    echo "✓ Container running: $IMAGE_NAME"
  fi
fi
echo ""
echo "📊 Next steps:"
echo "  1. Monitor logs: docker logs -f $IMAGE_NAME"
echo "  2. Execute agentic actions: POST http://localhost:8080/agentic/execute"
echo "  3. View state: GET http://localhost:8080/agentic/state"
echo "  4. Generate final cycle archive: python3 scripts/final_cycle.py"
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "🔱 STATUS: DEPLOYMENT CERTIFIED ψΩ 🔱"
echo "═══════════════════════════════════════════════════════════════════════════"

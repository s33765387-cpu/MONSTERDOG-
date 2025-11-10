#!/bin/bash
# Script bash pour générer automatiquement les manifestes manquants
# Alternative au script Python pour les environnements sans Python

set -e

echo "======================================================================"
echo "🚀 Générateur automatique de manifestes MONSTERDOG (Bash version)"
echo "======================================================================"
echo ""

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

cd "$(dirname "$0")/.."

echo "🔍 Exécution de la validation des manifestes..."
VALIDATION_OUTPUT=$(npm run validate:manifests 2>&1)
echo "$VALIDATION_OUTPUT"
echo ""

# Extraire les actions manquantes
MISSING_ACTIONS=$(echo "$VALIDATION_OUTPUT" | grep "Missing manifest for action:" | sed 's/.*Missing manifest for action: //')

if [ -z "$MISSING_ACTIONS" ]; then
    echo -e "${GREEN}✅ Aucune action manquante détectée!${NC}"
    echo -e "${GREEN}🔱 Tous les manifestes sont à jour!${NC}"
    exit 0
fi

echo -e "${BLUE}📋 Actions manquantes détectées:${NC}"
echo "$MISSING_ACTIONS" | while read action; do
    echo "   - $action"
done
echo ""

# Créer le répertoire si nécessaire
mkdir -p manifests/monsterdog

# Déterminer le prochain ID
NEXT_ID=21
if [ -d "manifests/monsterdog" ]; then
    MAX_ID=$(find manifests/monsterdog -name "*.json" -exec jq -r '.id' {} \; 2>/dev/null | sort -n | tail -1)
    if [ -n "$MAX_ID" ]; then
        NEXT_ID=$((MAX_ID + 1))
    fi
fi

echo -e "${BLUE}🔢 Prochain ID disponible: $NEXT_ID${NC}"
echo ""

CURRENT_ID=$NEXT_ID

# Fonction pour générer un manifeste
generate_manifest() {
    local ACTION_NAME=$1
    local ACTION_ID=$2
    
    echo -e "${BLUE}📝 Génération du manifeste pour: $ACTION_NAME${NC}"
    
    # Déterminer les paramètres selon l'action
    if [ "$ACTION_NAME" = "RUN_GO_BENCHMARKS" ]; then
        DESCRIPTION="Execute GO MODE global benchmarks suite - Participate in AI race"
        PARAMETERS='    "benchmarkType": {
      "type": "string",
      "default": "GLOBAL"
    }'
    elif [ "$ACTION_NAME" = "ACTIVATE_GO_CONTINUUM" ]; then
        DESCRIPTION="Activate continuous GO MODE execution - CONTINUEZ À FOND!"
        PARAMETERS='    "intervalMs": {
      "type": "number",
      "default": 5000
    },
    "duration": {
      "type": "string",
      "default": "CONTINUOUS"
    }'
    else
        DESCRIPTION="Execute $ACTION_NAME action"
        PARAMETERS=''
    fi
    
    echo "   Category: GO_MODE"
    echo "   Description: $DESCRIPTION"
    
    # Créer le fichier JSON
    cat > "manifests/monsterdog/${ACTION_NAME}.json" << EOF
{
  "id": ${ACTION_ID},
  "name": "${ACTION_NAME}",
  "category": "GO_MODE",
  "description": "${DESCRIPTION}",
  "parameters": {
${PARAMETERS}
  },
  "version": "1.0.0",
  "deploy": {
    "artifact": "packages/monsterdog/${ACTION_NAME}.zip"
  }
}
EOF
    
    echo -e "${GREEN}✅ Créé: manifests/monsterdog/${ACTION_NAME}.json${NC}"
    echo ""
}

# Générer les manifestes pour chaque action manquante
echo "$MISSING_ACTIONS" | while read action; do
    if [ -n "$action" ]; then
        generate_manifest "$action" "$CURRENT_ID"
        CURRENT_ID=$((CURRENT_ID + 1))
    fi
done

echo "======================================================================"
echo -e "${GREEN}✅ Génération terminée!${NC}"
echo "======================================================================"
echo ""
echo "🔍 Vérification finale..."
npm run validate:manifests

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}🔱 Validation réussie! Tous les manifestes sont générés!${NC}"
    exit 0
else
    echo ""
    echo -e "${YELLOW}⚠️  Il reste des manifestes manquants${NC}"
    exit 1
fi

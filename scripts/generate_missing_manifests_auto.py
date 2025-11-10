#!/usr/bin/env python3
"""
Générateur automatique de manifestes placeholder pour les "entity actions" manquantes détectées
dans la sortie du validateur (npm run validate:manifests).
Crée les fichiers : manifests/monsterdog/<ACTION_NAME>.json

Ce script:
1. Execute npm run validate:manifests pour détecter les actions manquantes
2. Récupère les informations des actions depuis src/entities/monsterdog/index.js
3. Génère automatiquement les manifestes JSON avec les bonnes métadonnées
4. Sauvegarde les fichiers dans manifests/monsterdog/
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path


def run_validation():
    """Execute npm run validate:manifests et capture la sortie"""
    print("🔍 Exécution de la validation des manifestes...")
    try:
        result = subprocess.run(
            ["npm", "run", "validate:manifests"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent
        )
        return result.stdout + result.stderr
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution de validate:manifests: {e}")
        return ""


def extract_missing_actions(validation_output):
    """Extrait les noms des actions manquantes depuis la sortie du validateur"""
    missing = []
    for line in validation_output.split('\n'):
        if "Missing manifest for action:" in line:
            action_name = line.split("Missing manifest for action:")[-1].strip()
            missing.append(action_name)
    return missing


def get_action_info_from_source(action_name):
    """Récupère les informations d'une action depuis le fichier source"""
    monsterdog_file = Path(__file__).parent.parent / "src" / "entities" / "monsterdog" / "index.js"
    
    try:
        with open(monsterdog_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Chercher la catégorie dans getActionCategory
        category_match = re.search(
            r"if\s*\(\[.*?'" + action_name + r"'.*?\]\.includes\(action\)\)\s*{\s*return\s+'([^']+)'",
            content,
            re.DOTALL
        )
        category = category_match.group(1) if category_match else "GO_MODE"
        
        # Chercher la description dans getActionDescription
        desc_pattern = action_name + r":\s*['\"]([^'\"]+)['\"]"
        desc_match = re.search(desc_pattern, content)
        description = desc_match.group(1) if desc_match else f"Execute {action_name} action"
        
        return {
            "category": category,
            "description": description
        }
    except Exception as e:
        print(f"⚠️  Impossible de lire les infos pour {action_name}: {e}")
        return {
            "category": "GO_MODE",
            "description": f"Execute {action_name} action"
        }


def get_next_action_id():
    """Détermine le prochain ID disponible en scannant les manifestes existants"""
    manifests_dir = Path(__file__).parent.parent / "manifests" / "monsterdog"
    max_id = 0
    
    if manifests_dir.exists():
        for manifest_file in manifests_dir.glob("*.json"):
            try:
                with open(manifest_file, 'r') as f:
                    data = json.load(f)
                    if "id" in data:
                        max_id = max(max_id, data["id"])
            except:
                pass
    
    return max_id + 1


def generate_manifest(action_name, action_id, action_info):
    """Génère un manifeste JSON pour une action"""
    
    # Détermine les paramètres par défaut selon l'action
    if action_name == "RUN_GO_BENCHMARKS":
        parameters = {
            "benchmarkType": {"type": "string", "default": "GLOBAL"}
        }
    elif action_name == "ACTIVATE_GO_CONTINUUM":
        parameters = {
            "intervalMs": {"type": "number", "default": 5000},
            "duration": {"type": "string", "default": "CONTINUOUS"}
        }
    else:
        parameters = {}
    
    manifest = {
        "id": action_id,
        "name": action_name,
        "category": action_info["category"],
        "description": action_info["description"],
        "parameters": parameters,
        "version": "1.0.0",
        "deploy": {
            "artifact": f"packages/monsterdog/{action_name}.zip"
        }
    }
    
    return manifest


def save_manifest(action_name, manifest):
    """Sauvegarde le manifeste dans un fichier JSON"""
    manifests_dir = Path(__file__).parent.parent / "manifests" / "monsterdog"
    manifests_dir.mkdir(parents=True, exist_ok=True)
    
    manifest_file = manifests_dir / f"{action_name}.json"
    
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write('\n')  # Ajoute une nouvelle ligne à la fin
    
    print(f"✅ Créé: {manifest_file}")


def main():
    print("=" * 70)
    print("🚀 Générateur automatique de manifestes MONSTERDOG")
    print("=" * 70)
    print()
    
    # 1. Exécuter la validation
    validation_output = run_validation()
    print(validation_output)
    print()
    
    # 2. Extraire les actions manquantes
    missing_actions = extract_missing_actions(validation_output)
    
    if not missing_actions:
        print("✅ Aucune action manquante détectée!")
        print("🔱 Tous les manifestes sont à jour!")
        return 0
    
    print(f"📋 Actions manquantes détectées: {len(missing_actions)}")
    for action in missing_actions:
        print(f"   - {action}")
    print()
    
    # 3. Générer les manifestes
    next_id = get_next_action_id()
    print(f"🔢 Prochain ID disponible: {next_id}")
    print()
    
    for i, action_name in enumerate(missing_actions):
        print(f"📝 Génération du manifeste pour: {action_name}")
        
        # Récupérer les infos de l'action
        action_info = get_action_info_from_source(action_name)
        print(f"   Category: {action_info['category']}")
        print(f"   Description: {action_info['description']}")
        
        # Générer le manifeste
        manifest = generate_manifest(action_name, next_id + i, action_info)
        
        # Sauvegarder
        save_manifest(action_name, manifest)
        print()
    
    print("=" * 70)
    print("✅ Génération terminée!")
    print("=" * 70)
    print()
    print("🔍 Vérification finale...")
    
    # 4. Re-valider
    validation_output = run_validation()
    print(validation_output)
    
    if "Missing manifest" in validation_output:
        print("⚠️  Il reste des manifestes manquants")
        return 1
    else:
        print("🔱 Validation réussie! Tous les manifestes sont générés!")
        return 0


if __name__ == "__main__":
    sys.exit(main())

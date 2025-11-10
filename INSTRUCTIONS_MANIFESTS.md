# 🚀 Instructions Complètes - Génération Automatique des Manifestes

## Vue d'ensemble

Ce guide explique comment générer automatiquement les manifestes manquants pour les nouvelles actions agentic MONSTERDOG en utilisant les scripts fournis.

## 📋 Fichiers Générés

Trois options sont disponibles pour générer les manifestes manquants :

1. **Script Python** : `scripts/generate_missing_manifests_auto.py` (recommandé)
2. **Script Bash** : `scripts/generate_missing_manifests_auto.sh` (alternative)
3. **Patch Git** : `manifests_go_mode.patch` (application manuelle)

## 🔧 Option 1 : Script Python (Recommandé)

### Utilisation

```bash
# Depuis la racine du projet
python3 scripts/generate_missing_manifests_auto.py
```

### Fonctionnement

Le script Python :
1. ✅ Exécute `npm run validate:manifests` pour détecter les actions manquantes
2. ✅ Extrait automatiquement les informations depuis `src/entities/monsterdog/index.js`
3. ✅ Génère les fichiers JSON avec les métadonnées correctes
4. ✅ Attribue automatiquement les IDs séquentiels
5. ✅ Valide que tous les manifestes sont créés

### Sortie Attendue

```
======================================================================
🚀 Générateur automatique de manifestes MONSTERDOG
======================================================================

🔍 Exécution de la validation des manifestes...
📋 Actions manquantes détectées: 2
   - ACTIVATE_GO_CONTINUUM
   - RUN_GO_BENCHMARKS

🔢 Prochain ID disponible: 21

📝 Génération du manifeste pour: ACTIVATE_GO_CONTINUUM
   Category: GO_MODE
   Description: Activate continuous GO MODE execution - CONTINUEZ À FOND!
✅ Créé: manifests/monsterdog/ACTIVATE_GO_CONTINUUM.json

📝 Génération du manifeste pour: RUN_GO_BENCHMARKS
   Category: GO_MODE
   Description: Execute GO MODE global benchmarks suite - Participate in AI race
✅ Créé: manifests/monsterdog/RUN_GO_BENCHMARKS.json

======================================================================
✅ Génération terminée!
======================================================================

🔱 Validation réussie! Tous les manifestes sont générés!
```

## 🔧 Option 2 : Script Bash

### Utilisation

```bash
# Depuis la racine du projet
bash scripts/generate_missing_manifests_auto.sh
# ou
./scripts/generate_missing_manifests_auto.sh
```

### Avantages

- Pas de dépendance Python
- Fonctionne sur tout système Unix/Linux/macOS
- Même fonctionnalité que le script Python

## 🔧 Option 3 : Patch Manuel

### Application du Patch

```bash
# Depuis la racine du projet
git apply manifests_go_mode.patch
```

### Vérification

```bash
npm run validate:manifests
```

Devrait afficher :
```
Found 22 entity actions and 22 manifests
Manifest validation PASSED
```

## 📁 Fichiers Générés

Les scripts créent deux nouveaux fichiers JSON dans `manifests/monsterdog/` :

### 1. ACTIVATE_GO_CONTINUUM.json

```json
{
  "id": 21,
  "name": "ACTIVATE_GO_CONTINUUM",
  "category": "GO_MODE",
  "description": "Activate continuous GO MODE execution - CONTINUEZ À FOND!",
  "parameters": {
    "intervalMs": {
      "type": "number",
      "default": 5000
    },
    "duration": {
      "type": "string",
      "default": "CONTINUOUS"
    }
  },
  "version": "1.0.0",
  "deploy": {
    "artifact": "packages/monsterdog/ACTIVATE_GO_CONTINUUM.zip"
  }
}
```

### 2. RUN_GO_BENCHMARKS.json

```json
{
  "id": 22,
  "name": "RUN_GO_BENCHMARKS",
  "category": "GO_MODE",
  "description": "Execute GO MODE global benchmarks suite - Participate in AI race",
  "parameters": {
    "benchmarkType": {
      "type": "string",
      "default": "GLOBAL"
    }
  },
  "version": "1.0.0",
  "deploy": {
    "artifact": "packages/monsterdog/RUN_GO_BENCHMARKS.zip"
  }
}
```

## 🔄 Workflow Complet

### Étape 1 : Générer les Manifestes

Choisissez une option :

```bash
# Option A : Python
python3 scripts/generate_missing_manifests_auto.py

# Option B : Bash
./scripts/generate_missing_manifests_auto.sh

# Option C : Patch
git apply manifests_go_mode.patch
```

### Étape 2 : Valider

```bash
npm run validate:manifests
```

### Étape 3 : Commit et Push

```bash
# Ajouter les nouveaux fichiers
git add manifests/monsterdog/ACTIVATE_GO_CONTINUUM.json
git add manifests/monsterdog/RUN_GO_BENCHMARKS.json

# Commit
git commit -m "Add manifests for GO MODE actions (ACTIVATE_GO_CONTINUUM, RUN_GO_BENCHMARKS)"

# Push vers la branche PR
git push origin copilot/continuez-appliquer-tout
```

### Étape 4 : Créer/Mettre à jour le PR

Le PR existant sera automatiquement mis à jour avec les nouveaux fichiers.

## 🎯 Résultat Final

Après l'exécution du script et le commit :

- ✅ 22 actions agentic définies
- ✅ 22 manifestes correspondants
- ✅ Validation réussie (`npm run validate:manifests`)
- ✅ Actions GO MODE complètes avec métadonnées
- ✅ Prêt pour déploiement

## 🔍 Validation

Pour vérifier que tout fonctionne :

```bash
# Valider les manifestes
npm run validate:manifests

# Lister les manifestes créés
ls -l manifests/monsterdog/

# Tester les actions
npm test
```

## 📝 Notes

- Les IDs sont attribués automatiquement (21 et 22)
- Les catégories sont extraites du code source
- Les descriptions sont synchronisées avec `getActionDescription()`
- Les paramètres par défaut correspondent aux implémentations

## ❓ Dépannage

### Erreur : "jq: command not found"

Le script bash nécessite `jq` pour fonctionner. Installez-le :

```bash
# Ubuntu/Debian
sudo apt-get install jq

# macOS
brew install jq

# Ou utilisez le script Python
python3 scripts/generate_missing_manifests_auto.py
```

### Erreur : "Permission denied"

Rendez les scripts exécutables :

```bash
chmod +x scripts/generate_missing_manifests_auto.py
chmod +x scripts/generate_missing_manifests_auto.sh
```

### Les manifestes existent déjà

Les scripts détectent automatiquement si les manifestes existent. Supprimez-les d'abord si vous voulez les régénérer :

```bash
rm manifests/monsterdog/ACTIVATE_GO_CONTINUUM.json
rm manifests/monsterdog/RUN_GO_BENCHMARKS.json
```

## 🌟 Résumé Rapide

Pour les utilisateurs pressés :

```bash
# Générer les manifestes
python3 scripts/generate_missing_manifests_auto.py

# Valider
npm run validate:manifests

# Commit
git add manifests/monsterdog/*.json
git commit -m "Add GO MODE action manifests"
git push
```

---

**👾 MONSTERDOG SUPREME - Manifestes GO MODE - TOUT GO! 🚀**

# Déploiement & supervision MONSTERDOG

Ce répertoire contient des fichiers pour exécuter MONSTERDOG en service systemd et pour gérer les logs via logrotate.

Chemin recommandé d'installation : /opt/monsterdog
Fichiers inclus :
- deploy/monsterdog.service — unit systemd
- deploy/start_monsterdog.sh — wrapper pour venv / démarrage
- deploy/monsterdog.env — variables d'environnement (à modifier)
- deploy/logrotate_monsterdog — config logrotate

Étapes d'installation (exécuter en root):

1) Créer les répertoires et copier les fichiers
   ```bash
   mkdir -p /opt/monsterdog
   cp -r . /opt/monsterdog
   mkdir -p /etc/monsterdog /var/log/monsterdog /opt/monsterdog/MONSTERDOG_ARTEFACTS
   chown -R s33765387-cpu:s33765387-cpu /opt/monsterdog /var/log/monsterdog /etc/monsterdog
   ```

2) Placer le fichier d'environnement
   ```bash
   cp /opt/monsterdog/deploy/monsterdog.env /etc/monsterdog/monsterdog.env
   # Editez /etc/monsterdog/monsterdog.env selon votre environnement
   ```

3) Installer l'unité systemd
   ```bash
   cp /opt/monsterdog/deploy/monsterdog.service /etc/systemd/system/
   systemctl daemon-reload
   systemctl enable --now monsterdog.service
   ```

4) Vérifier le statut et logs
   ```bash
   systemctl status monsterdog.service
   journalctl -u monsterdog.service -f
   # ou consulter /var/log/monsterdog/monsterdog.log
   ```

5) Configurer logrotate
   ```bash
   cp /opt/monsterdog/deploy/logrotate_monsterdog /etc/logrotate.d/monsterdog
   ```

## Remarques de sécurité & bonnes pratiques

- Exécuter le service sous un utilisateur dédié (ici : s33765387-cpu). Vous pouvez créer un utilisateur système `monsterdog` si souhaité.
- Vérifiez les permissions des répertoires d'artefacts et du journal.
- Si vous préférez que l'API soit accessible publiquement, modifiez LISTEN_HOST/LISTEN_PORT et sécurisez via reverse proxy (nginx) + TLS.
- Pour mises à jour du code : déployer dans /opt/monsterdog, puis `systemctl restart monsterdog.service`.

## Dépannage rapide

- Si le service ne démarre pas :
  ```bash
  sudo journalctl -u monsterdog.service -b --no-pager
  ```

- Forcer une réinstallation des dépendances :
  ```bash
  /opt/monsterdog/venv/bin/pip install --upgrade -r /opt/monsterdog/requirements.txt
  ```

- Tester le script manuellement :
  ```bash
  sudo -u s33765387-cpu /bin/bash /opt/monsterdog/deploy/start_monsterdog.sh
  ```

## Architecture

Le service MONSTERDOG s'exécute comme suit :
1. systemd démarre `start_monsterdog.sh`
2. Le script crée/active un virtualenv Python
3. Installe les dépendances depuis `requirements.txt`
4. Charge les variables d'environnement depuis `/etc/monsterdog/monsterdog.env`
5. Lance `MONSTERDOG_ULTIMATE_FINALITY_INCARNATE.py` avec redirection des logs
6. Les logs sont gérés par logrotate (rotation quotidienne, 14 jours)

## Ports et services

- Port par défaut : 8080 (configurable via LISTEN_PORT)
- Le service écoute sur 127.0.0.1 par défaut (accès local uniquement)
- Pour accès externe, utilisez un reverse proxy (nginx, caddy, etc.)

## Mise à jour

Pour mettre à jour MONSTERDOG :
```bash
cd /opt/monsterdog
git pull origin main
systemctl restart monsterdog.service
```

## Désinstallation

Pour désinstaller complètement :
```bash
systemctl stop monsterdog.service
systemctl disable monsterdog.service
rm /etc/systemd/system/monsterdog.service
rm /etc/logrotate.d/monsterdog
rm -rf /opt/monsterdog /var/log/monsterdog /etc/monsterdog
systemctl daemon-reload
```

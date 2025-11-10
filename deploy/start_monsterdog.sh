#!/usr/bin/env bash
set -euo pipefail

BASE_DIR="/opt/monsterdog"
VENV_DIR="$BASE_DIR/venv"
LOG_DIR="/var/log/monsterdog"
PID_DIR="/var/run/monsterdog"
SCRIPT="$BASE_DIR/MONSTERDOG_ULTIMATE_FINALITY_INCARNATE.py"
REQS="$BASE_DIR/requirements.txt"
LOG_FILE="$LOG_DIR/monsterdog.log"

mkdir -p "$LOG_DIR" "$PID_DIR"
chown -R s33765387-cpu:s33765387-cpu "$LOG_DIR" || true

# Create virtualenv if missing
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
  "$VENV_DIR/bin/python" -m pip install --upgrade pip
  if [ -f "$REQS" ]; then
    "$VENV_DIR/bin/pip" install -r "$REQS"
  else
    # minimal safe default
    "$VENV_DIR/bin/pip" install fastapi uvicorn numpy aiofiles prometheus-client
  fi
fi

# Export environment if file present
if [ -f /etc/monsterdog/monsterdog.env ]; then
  set -a
  # shellcheck disable=SC1090
  . /etc/monsterdog/monsterdog.env
  set +a
fi

# Ensure the main script exists
if [ ! -f "$SCRIPT" ]; then
  echo "ERROR: $SCRIPT not found" >&2
  exit 1
fi

# Run the application (stdout+stderr -> log); use exec so systemd tracks the Python process
exec "$VENV_DIR/bin/python" "$SCRIPT" >> "$LOG_FILE" 2>&1

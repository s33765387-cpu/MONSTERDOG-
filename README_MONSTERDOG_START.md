# MONSTERDOG ψΩ — Quickstart

This starter pack gives you a safe way to run the core pieces without pulling huge, optional dependencies.

## 1) Put these files next to your project files
- `requirements_monsterdog.txt`
- `requirements_monsterdog_extras_heavy.txt` (optional)
- `start_monsterdog.py`

## 2) Create a local env and install deps
```bash
python3 start_monsterdog.py
# The launcher will create ./.venv and install the minimal requirements.
```

## 3) Pick what to run
- **XR Portal (WS+HTTP)** → starts local HTTP + WebSocket in one of the `fusion_monsterdog_portal (...).py` scripts
- **FastAPI Backend** → runs `WAR_CONVOLUTION_AI_SERVER.py`
- **Open the 3D HTML portal** → opens `MONSTERDOG_VAISSEAU_ULTIME_V∞.html` in your default browser
- **System Core** → runs `monsterdog_core_refactored.py`
- **Synchronizer** → advanced spawner that tries to start many modules

## 4) Optional heavy extras
If a specific script explicitly requires heavy libs (TensorFlow, OpenCV, Qiskit, etc.), enable them one by one in
`requirements_monsterdog_extras_heavy.txt` and install:
```bash
./.venv/bin/pip install -r requirements_monsterdog_extras_heavy.txt
```

## Notes
- The launcher avoids auto-installing huge toolchains unless *you* opt in.
- Some scripts are drafts or experimental; start with the XR Portal or the FastAPI backend.

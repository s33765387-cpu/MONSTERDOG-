\
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # MONSTERDOG ψΩ – Friendly Launcher
    # Creates ./.venv, installs minimal requirements, and lets you run common modules.
    import os, sys, subprocess, shlex, webbrowser
    from pathlib import Path

    HERE = Path(__file__).resolve().parent
    VENV = HERE / ".venv"
    PY = sys.executable

    MIN_REQ = HERE / "requirements_monsterdog.txt"

    MODULES = {
        "XR Portal (WS+HTTP)": "fusion_monsterdog_portal (1).py",
        "FastAPI Backend": "WAR_CONVOLUTION_AI_SERVER.py",
        "Open the 3D HTML portal": "MONSTERDOG_VAISSEAU_ULTIME_V∞.html",
        "System Core (refactored monitor)": "monsterdog_core_refactored.py",
        "Synchronizer (spawns many scripts – advanced)": "monsterdog_ψω_synchronisation.py"
    }

    def run(cmd, env=None):
        print(f"→ {cmd}")
        return subprocess.run(shlex.split(cmd), check=False, env=env)

    def ensure_venv():
        if not VENV.exists():
            print("[ψΩ] Creating virtualenv …")
            subprocess.check_call([PY, "-m", "venv", str(VENV)])
        pip = VENV / ("Scripts/pip.exe" if os.name == "nt" else "bin/pip")
        pybin = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        print("[ψΩ] Installing minimal requirements …")
        subprocess.check_call([str(pip), "install", "-r", str(MIN_REQ)])
        return str(pybin)

    def menu():
        print("\n=== MONSTERDOG ψΩ – Launcher ===")
        for i, name in enumerate(MODULES, 1):
            print(f"{i}. {name}")
        print("0. Exit")
        try:
            return int(input("Select: ").strip())
        except Exception:
            return -1

    def main():
        pybin = ensure_venv()
        choice = menu()
        if choice == 0:
            return
        keys = list(MODULES.keys())
        if 1 <= choice <= len(keys):
            name = keys[choice-1]
            target = MODULES[name]
            path = HERE / target
            if not path.exists():
                print(f"[!] Missing: {path.name}")
                return
            if path.suffix.lower() == ".py":
                env = os.environ.copy()
                env["PYTHONWARNINGS"] = "ignore"
                run(f"{pybin} \"{path}\"", env=env)
            elif path.suffix.lower() == ".html":
                webbrowser.open(path.as_uri())
            else:
                print(f"[?] Unknown file type: {path.suffix}")
        else:
            print("Invalid selection.")

    if __name__ == "__main__":
        main()

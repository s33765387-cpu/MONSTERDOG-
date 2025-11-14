#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONSTERDOG — FUSION ENGINE
Dynamically fuses all Python modules into a unified codebase.
"""

import os
import hashlib
import time
from pathlib import Path
from datetime import datetime

BASE = Path(".")
SRC_DIRS = [
    Path("src"),
    Path("modules"),
    Path("multimodal"),
    Path("Ω_CORE"),
]

OUT = Path("Ω_CORE/MONSTERDOG_FUSION")
OUT.mkdir(parents=True, exist_ok=True)

def scan_all_py():
    """Scan for all Python files in source directories"""
    files = []
    for d in SRC_DIRS:
        if d.exists():
            for f in d.rglob("*.py"):
                # Skip fusion outputs and test files
                if "MONSTERDOG_FUSION" not in str(f) and "test_" not in f.name:
                    files.append(f)
    return files

def fuse_file(fpath: Path):
    """Create a fused code block with header"""
    try:
        code = open(fpath, encoding='utf-8').read()
        block = (
            "\n\n" +
            "#" * 72 + "\n" +
            f"# MODULE: {fpath}\n" +
            f"# FUSED: {datetime.utcnow().isoformat()}\n" +
            "#" * 72 + "\n\n" +
            code + "\n\n"
        )
        return block
    except Exception as e:
        print(f"⚠️  Error reading {fpath}: {e}")
        return ""

def build_fusion():
    """Build the complete fusion file"""
    print("🔥 MONSTERDOG FUSION ENGINE")
    print("=" * 60)
    
    target = OUT / "MONSTERDOG_FUSION_TOTAL.py"
    files = scan_all_py()
    
    print(f"📦 Found {len(files)} Python modules to fuse")
    
    with open(target, "w", encoding='utf-8') as out:
        # Header
        out.write('#!/usr/bin/env python3\n')
        out.write('# -*- coding: utf-8 -*-\n\n')
        out.write('"""\n')
        out.write('MONSTERDOG FUSION TOTAL\n')
        out.write('Auto-generated fusion of all MONSTERDOG modules\n')
        out.write(f'Built: {datetime.utcnow().isoformat()}\n')
        out.write(f'Modules: {len(files)}\n')
        out.write('"""\n\n')
        
        # Fuse all files
        for i, f in enumerate(files, 1):
            print(f"  [{i}/{len(files)}] Fusing: {f}")
            out.write(fuse_file(f))
    
    # Calculate hash
    with open(target, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    
    size = target.stat().st_size
    
    print("=" * 60)
    print(f"✅ Fusion complete!")
    print(f"📄 Output: {target}")
    print(f"📊 Size: {size:,} bytes")
    print(f"🔐 SHA256: {file_hash[:16]}...")
    print("=" * 60)
    
    # Create metadata
    metadata = {
        "timestamp": datetime.utcnow().isoformat(),
        "modules_count": len(files),
        "output_file": str(target),
        "size_bytes": size,
        "sha256": file_hash,
        "modules": [str(f) for f in files]
    }
    
    metadata_file = OUT / "fusion_metadata.json"
    import json
    with open(metadata_file, "w") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"📋 Metadata saved to {metadata_file}")
    
    return target

if __name__ == "__main__":
    build_fusion()

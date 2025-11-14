#!/usr/bin/env python3
"""
Quick validation script to test MONSTERDOG_ULTIMATE_FINALITY_INCARNATE.py
Tests the core components without starting the full server.
"""
import sys
import asyncio
from MONSTERDOG_ULTIMATE_FINALITY_INCARNATE import (
    CosmicConstants,
    FractalState,
    GlobalStateVector,
    FractalMetricEngine,
    ArtifactForge
)

async def test_core_components():
    print("=" * 80)
    print("🧪 TESTING MONSTERDOG_ULTIMATE_FINALITY_INCARNATE CORE COMPONENTS")
    print("=" * 80)
    
    # Test 1: Constants
    print("\n✓ Test 1: CosmicConstants")
    constants = CosmicConstants()
    assert constants.BASE_RESONANCE_HZ == 11.987
    assert constants.LOOP_FREQUENCY_HZ == 12.0
    assert len(constants.CHAMBERS) == 15
    print(f"  - Signature: {constants.SEAL_SIGNATURE}")
    print(f"  - Chambers: {len(constants.CHAMBERS)}")
    
    # Test 2: Fractal State
    print("\n✓ Test 2: FractalState")
    fractal = FractalState()
    assert fractal.coherence == 1.0
    assert fractal.entropy == 0.0
    print(f"  - Initial Coherence: {fractal.coherence}")
    print(f"  - Initial Entropy: {fractal.entropy}")
    
    # Test 3: Global State Vector
    print("\n✓ Test 3: GlobalStateVector")
    state = GlobalStateVector(timestamp="2025-11-10T14:00:00Z", cycle_id=1)
    state.calculate_checksum()
    assert state.checksum_sha512 is not None
    assert len(state.checksum_sha512) == 128  # SHA-512 hex length
    print(f"  - Checksum: {state.checksum_sha512[:32]}...")
    
    # Test 4: Fractal Metric Engine
    print("\n✓ Test 4: FractalMetricEngine")
    engine = FractalMetricEngine(constants)
    metrics = await engine.compute_metrics(1)
    assert 0.999 <= metrics.coherence <= 1.0
    assert 0.0 <= metrics.entropy <= 0.001
    print(f"  - Coherence: {metrics.coherence:.6f}")
    print(f"  - Entropy: {metrics.entropy:.6f}")
    print(f"  - Resonance: {metrics.resonance_hz:.4f} Hz")
    
    # Test 5: Multiple cycles
    print("\n✓ Test 5: Multi-cycle computation")
    for cycle in range(2, 6):
        metrics = await engine.compute_metrics(cycle)
    print(f"  - Final Coherence: {metrics.coherence:.6f}")
    print(f"  - Final Drift: {metrics.drift:.6f}")
    
    print("\n" + "=" * 80)
    print("✅ ALL TESTS PASSED - MONSTERDOG_ULTIMATE_FINALITY_INCARNATE IS OPERATIONAL")
    print("=" * 80)
    return True

if __name__ == "__main__":
    try:
        result = asyncio.run(test_core_components())
        sys.exit(0 if result else 1)
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

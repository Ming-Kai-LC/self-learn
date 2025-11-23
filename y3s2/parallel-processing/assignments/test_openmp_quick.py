"""Quick test for OpenMP implementation (simplified)."""
import numpy as np
import sys
import time

# Test the key parallel function
from heat_diffusion_openmp import HeatDiffusion2D_OpenMP

def test_parallel_basic():
    """Test basic parallel functionality."""
    print("=" * 70)
    print("TEST: OpenMP Parallel Implementation")
    print("=" * 70)

    # Create small simulator
    sim = HeatDiffusion2D_OpenMP(nx=50, ny=50, alpha=0.01, dt=0.0001, num_threads=2)
    sim.set_initial_conditions("center_hot")

    print(f"Grid: {sim.nx}×{sim.ny}")
    print(f"Threads: {sim.num_threads}")
    print(f"\nRunning simulation with 100 steps...")

    # Run simulation
    start = time.time()
    final_T, stats = sim.simulate(num_steps=100, verbose=True)
    elapsed = time.time() - start

    print(f"\n✓ Simulation completed successfully!")
    print(f"Total time: {elapsed:.3f}s")
    print(f"Throughput: {stats['cells_per_second']/1e6:.2f} Mcells/s")

    # Verify results
    assert stats['steps_completed'] == 100
    assert np.isfinite(final_T).all()
    assert stats['num_threads'] == 2

    print("\n✅ All checks passed!")
    return True

if __name__ == "__main__":
    try:
        test_parallel_basic()
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

"""
Quick test script for heat diffusion serial implementation (no GUI).
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import sys

# Import the heat diffusion module
from heat_diffusion_serial import HeatDiffusion2D, benchmark_performance

def test_basic_simulation():
    """Test basic heat diffusion simulation."""
    print("=" * 70)
    print("TEST 1: Basic Heat Diffusion Simulation")
    print("=" * 70)

    # Create small simulator for quick test
    sim = HeatDiffusion2D(nx=50, ny=50, alpha=0.01, dt=0.0001)
    sim.set_initial_conditions("center_hot")

    # Check initial conditions
    initial_min = np.min(sim.T)
    initial_max = np.max(sim.T)
    print(f"Initial temperature range: [{initial_min:.2f}, {initial_max:.2f}]")

    # Run simulation
    final_T, stats = sim.simulate(num_steps=100, verbose=True)

    # Verify results
    assert stats['steps_completed'] == 100, "Incorrect number of steps"
    assert stats['cells_per_second'] > 0, "Invalid throughput"
    assert np.isfinite(final_T).all(), "Non-finite values in result"

    print("\n✓ Basic simulation test PASSED\n")
    return True

def test_convergence():
    """Test that heat diffuses (temperature becomes more uniform)."""
    print("=" * 70)
    print("TEST 2: Heat Diffusion Convergence")
    print("=" * 70)

    # Use gradient initial condition for clearer convergence test
    sim = HeatDiffusion2D(nx=50, ny=50, alpha=0.01, dt=0.0001)
    sim.set_initial_conditions("gradient")

    initial_std = np.std(sim.T)
    initial_mean = np.mean(sim.T)

    # Run simulation with constant boundaries
    final_T, _ = sim.simulate(num_steps=500, verbose=False, bc_type="constant")

    final_std = np.std(final_T)
    final_mean = np.mean(final_T)

    print(f"Initial: mean={initial_mean:.2f}, std={initial_std:.2f}")
    print(f"Final:   mean={final_mean:.2f}, std={final_std:.2f}")

    # Temperature distribution should become more uniform
    # (standard deviation decreases as heat diffuses)
    assert final_std < initial_std, "Temperature should become more uniform"

    print("\n✓ Convergence test PASSED\n")
    return True

def test_energy_conservation():
    """Test energy conservation for insulated boundaries."""
    print("=" * 70)
    print("TEST 3: Energy Conservation (Insulated Boundaries)")
    print("=" * 70)

    sim = HeatDiffusion2D(nx=50, ny=50, alpha=0.01, dt=0.0001)
    sim.set_initial_conditions("center_hot")
    sim.set_boundary_conditions("insulated")

    initial_energy = np.sum(sim.T)

    # Run simulation with insulated boundaries
    for _ in range(100):
        sim.step(bc_type="insulated")

    final_energy = np.sum(sim.T)
    energy_error = abs(final_energy - initial_energy) / initial_energy

    print(f"Initial total energy: {initial_energy:.6f}")
    print(f"Final total energy:   {final_energy:.6f}")
    print(f"Relative error:       {energy_error:.6e}")

    # Energy should be conserved (within numerical error)
    assert energy_error < 1e-10, f"Energy not conserved: {energy_error:.6e}"

    print("\n✓ Energy conservation test PASSED\n")
    return True

def test_performance_scaling():
    """Test performance with different grid sizes."""
    print("=" * 70)
    print("TEST 4: Performance Scaling")
    print("=" * 70)

    grid_sizes = [25, 50, 100]
    results = benchmark_performance(grid_sizes, num_steps=100)

    # Check that larger grids take more time (reasonable scaling)
    times = results['execution_times']
    for i in range(len(times) - 1):
        assert times[i+1] > times[i], "Larger grids should take more time"

    print("\n✓ Performance scaling test PASSED\n")
    return True

def test_different_initial_conditions():
    """Test different initial conditions work."""
    print("=" * 70)
    print("TEST 5: Different Initial Conditions")
    print("=" * 70)

    conditions = ["center_hot", "uniform", "gradient", "corners", "checkerboard"]

    for condition in conditions:
        sim = HeatDiffusion2D(nx=30, ny=30, alpha=0.01, dt=0.0001)
        sim.set_initial_conditions(condition)

        # Check that initial condition was set
        assert not np.all(sim.T == 0), f"Initial condition '{condition}' failed"

        # Run a few steps to ensure it works
        sim.simulate(num_steps=10, verbose=False)

        print(f"  ✓ {condition}")

    print("\n✓ All initial conditions test PASSED\n")
    return True

def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 70)
    print(" HEAT DIFFUSION SERIAL IMPLEMENTATION - TEST SUITE")
    print("=" * 70 + "\n")

    tests = [
        test_basic_simulation,
        test_convergence,
        test_energy_conservation,
        test_performance_scaling,
        test_different_initial_conditions,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"\n✗ TEST FAILED: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1

    print("\n" + "=" * 70)
    print(f" TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 70 + "\n")

    if failed == 0:
        print("🎉 ALL TESTS PASSED! Serial implementation is working correctly.\n")
        return 0
    else:
        print("❌ SOME TESTS FAILED. Please review the implementation.\n")
        return 1

if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)

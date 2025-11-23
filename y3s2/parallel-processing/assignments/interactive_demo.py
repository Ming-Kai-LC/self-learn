"""
Interactive Heat Diffusion Demo
================================

Run this script to interactively explore your heat diffusion simulation!
You can choose different initial conditions, grid sizes, and see real-time results.

Usage:
    python interactive_demo.py
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Use interactive backend
import matplotlib.pyplot as plt
from heat_diffusion_serial import HeatDiffusion2D
import sys


def print_menu():
    """Print interactive menu."""
    print("\n" + "=" * 70)
    print("🔥 HEAT DIFFUSION INTERACTIVE DEMO")
    print("=" * 70)
    print("\n[1] Quick Demo - Center Hot Spot (50×50, 500 steps)")
    print("[2] Gradient Demo - Heat flows left to right (50×50, 500 steps)")
    print("[3] Corners Demo - Hot corners (50×50, 500 steps)")
    print("[4] Checkerboard Demo - Alternating pattern (50×50, 500 steps)")
    print("[5] Large Grid Demo - Bigger simulation (200×200, 1000 steps)")
    print("[6] Custom Settings - Choose your own parameters")
    print("[7] Performance Benchmark - Test different grid sizes")
    print("[8] Show Animation - Evolve over time (slower)")
    print("[0] Exit")
    print("\n" + "=" * 70)


def run_simulation(sim, num_steps, title="Heat Diffusion"):
    """Run simulation and show before/after visualization."""
    print(f"\n🔬 Running: {title}")
    print("-" * 70)

    # Show initial state
    plt.figure(figsize=(14, 5))

    plt.subplot(1, 2, 1)
    im1 = plt.imshow(sim.T, cmap='hot', origin='lower',
                     extent=[0, sim.nx*sim.dx, 0, sim.ny*sim.dy])
    plt.colorbar(im1, label='Temperature (°C)')
    plt.title('Initial Temperature Distribution')
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')

    # Run simulation
    print("Simulating...")
    final_T, stats = sim.simulate(num_steps=num_steps, verbose=True)

    # Show final state
    plt.subplot(1, 2, 2)
    im2 = plt.imshow(final_T, cmap='hot', origin='lower',
                     extent=[0, sim.nx*sim.dx, 0, sim.ny*sim.dy])
    plt.colorbar(im2, label='Temperature (°C)')
    plt.title(f'After {num_steps} Steps')
    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')

    plt.tight_layout()
    plt.suptitle(title, fontsize=14, fontweight='bold', y=1.02)
    plt.show()

    print(f"\n📊 Performance: {stats['cells_per_second']/1e6:.2f} Mcells/s")
    print(f"   Execution time: {stats['compute_time']:.3f} seconds")


def run_animation(sim, num_frames=50, interval=2000):
    """Show animated evolution of temperature."""
    from matplotlib.animation import FuncAnimation

    print(f"\n🎬 Creating animation with {num_frames} frames...")
    print("   (Close the window to continue)")

    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(sim.T, cmap='hot', origin='lower',
                   extent=[0, sim.nx*sim.dx, 0, sim.ny*sim.dy],
                   vmin=20, vmax=100)
    plt.colorbar(im, label='Temperature (°C)')
    ax.set_xlabel('X Position (m)')
    ax.set_ylabel('Y Position (m)')
    title = ax.set_title('Heat Diffusion - Step 0')

    def update(frame):
        # Advance simulation
        steps_per_frame = 20
        for _ in range(steps_per_frame):
            sim.step()

        im.set_array(sim.T)
        title.set_text(f'Heat Diffusion - Step {(frame+1)*steps_per_frame}')
        return [im, title]

    anim = FuncAnimation(fig, update, frames=num_frames, interval=interval/num_frames, blit=True)
    plt.show()


def performance_benchmark():
    """Run and visualize performance benchmark."""
    from heat_diffusion_serial import benchmark_performance, plot_benchmark_results

    print("\n⚡ Running Performance Benchmark...")
    print("   Testing grid sizes: 50, 100, 200, 400")
    print("   This will take a few minutes...\n")

    results = benchmark_performance([50, 100, 200, 400], num_steps=1000)
    plot_benchmark_results(results)


def custom_simulation():
    """Let user choose custom parameters."""
    print("\n⚙️  Custom Simulation Settings")
    print("-" * 70)

    # Get parameters
    try:
        grid_size = int(input("Grid size (e.g., 50, 100, 200): ") or "100")
        num_steps = int(input("Number of time steps (e.g., 500, 1000): ") or "500")

        print("\nInitial conditions:")
        print("  1. Center hot spot")
        print("  2. Gradient (left to right)")
        print("  3. Hot corners")
        print("  4. Checkerboard")
        print("  5. Uniform")
        choice = int(input("Choose (1-5): ") or "1")

        conditions = {
            1: "center_hot",
            2: "gradient",
            3: "corners",
            4: "checkerboard",
            5: "uniform"
        }
        initial_cond = conditions.get(choice, "center_hot")

        # Create and run simulation
        sim = HeatDiffusion2D(nx=grid_size, ny=grid_size, alpha=0.01, dt=0.0001)
        sim.set_initial_conditions(initial_cond)
        run_simulation(sim, num_steps, f"Custom: {initial_cond} ({grid_size}×{grid_size})")

    except (ValueError, KeyError) as e:
        print(f"Invalid input: {e}. Using defaults.")
        custom_simulation()


def main():
    """Main interactive loop."""
    print("\n" + "🔥" * 35)
    print("Welcome to the Heat Diffusion Interactive Demo!")
    print("🔥" * 35)

    while True:
        print_menu()

        try:
            choice = input("\nEnter your choice (0-8): ").strip()

            if choice == '0':
                print("\n👋 Thanks for exploring heat diffusion! Goodbye!")
                break

            elif choice == '1':
                # Quick demo
                sim = HeatDiffusion2D(nx=50, ny=50, alpha=0.01, dt=0.0001)
                sim.set_initial_conditions("center_hot")
                run_simulation(sim, 500, "Quick Demo: Center Hot Spot")

            elif choice == '2':
                # Gradient demo
                sim = HeatDiffusion2D(nx=50, ny=50, alpha=0.01, dt=0.0001)
                sim.set_initial_conditions("gradient")
                run_simulation(sim, 500, "Gradient Demo: Left to Right")

            elif choice == '3':
                # Corners demo
                sim = HeatDiffusion2D(nx=50, ny=50, alpha=0.01, dt=0.0001)
                sim.set_initial_conditions("corners")
                run_simulation(sim, 500, "Corners Demo: Four Hot Spots")

            elif choice == '4':
                # Checkerboard demo
                sim = HeatDiffusion2D(nx=50, ny=50, alpha=0.01, dt=0.0001)
                sim.set_initial_conditions("checkerboard")
                run_simulation(sim, 500, "Checkerboard Demo: Alternating Pattern")

            elif choice == '5':
                # Large grid demo
                print("\n⚠️  Large grid - this will take ~1-2 minutes...")
                sim = HeatDiffusion2D(nx=200, ny=200, alpha=0.01, dt=0.0001)
                sim.set_initial_conditions("center_hot")
                run_simulation(sim, 1000, "Large Grid Demo (200×200)")

            elif choice == '6':
                # Custom settings
                custom_simulation()

            elif choice == '7':
                # Performance benchmark
                performance_benchmark()

            elif choice == '8':
                # Animation
                print("\n🎬 Animation Mode")
                sim = HeatDiffusion2D(nx=50, ny=50, alpha=0.01, dt=0.0001)
                sim.set_initial_conditions("center_hot")
                run_animation(sim, num_frames=50)

            else:
                print("\n❌ Invalid choice. Please enter 0-8.")

        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()

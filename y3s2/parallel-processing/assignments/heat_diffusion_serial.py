"""
2D Heat Diffusion Simulation - Serial Implementation
======================================================

This module implements a serial (non-parallel) version of 2D heat diffusion
using the finite difference method to solve the heat equation:

    ∂T/∂t = α * ∇²T

Where:
    T: Temperature at point (x, y, t)
    α: Thermal diffusivity
    ∇²: Laplacian operator

Author: Parallel Processing Assignment
Date: November 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from typing import Tuple, Optional


class HeatDiffusion2D:
    """
    2D Heat Diffusion Simulator using finite difference method.

    Attributes:
        nx (int): Number of grid points in x-direction
        ny (int): Number of grid points in y-direction
        dx (float): Grid spacing in x-direction
        dy (float): Grid spacing in y-direction
        alpha (float): Thermal diffusivity
        dt (float): Time step size
        T (np.ndarray): Current temperature field
        T_new (np.ndarray): Next temperature field (double buffering)
    """

    def __init__(
        self,
        nx: int = 100,
        ny: int = 100,
        Lx: float = 1.0,
        Ly: float = 1.0,
        alpha: float = 0.01,
        dt: float = 0.001
    ):
        """
        Initialize the heat diffusion simulator.

        Args:
            nx: Number of grid points in x-direction
            ny: Number of grid points in y-direction
            Lx: Physical length in x-direction (meters)
            Ly: Physical length in y-direction (meters)
            alpha: Thermal diffusivity (m²/s)
            dt: Time step size (seconds)
        """
        self.nx = nx
        self.ny = ny
        self.dx = Lx / (nx - 1)
        self.dy = Ly / (ny - 1)
        self.alpha = alpha
        self.dt = dt

        # Check stability condition (CFL condition)
        # For stability: dt <= (dx²) / (4 * alpha)
        max_dt = min(self.dx**2, self.dy**2) / (4 * alpha)
        if dt > max_dt:
            print(f"⚠️  WARNING: Time step dt={dt} may be unstable!")
            print(f"   Recommended max dt: {max_dt:.6f}")
            print(f"   Consider reducing dt for numerical stability.")

        # Initialize temperature fields (double buffering)
        self.T = np.zeros((ny, nx), dtype=np.float64)
        self.T_new = np.zeros((ny, nx), dtype=np.float64)

        # Statistics tracking
        self.iteration_count = 0
        self.total_time = 0.0

    def set_initial_conditions(self, condition: str = "center_hot"):
        """
        Set initial temperature distribution.

        Args:
            condition: Type of initial condition
                - "center_hot": Hot spot in center
                - "uniform": Uniform temperature
                - "gradient": Linear gradient
                - "corners": Hot corners
                - "checkerboard": Checkerboard pattern
        """
        if condition == "center_hot":
            # Hot spot in the center
            cy, cx = self.ny // 2, self.nx // 2
            radius = min(self.nx, self.ny) // 10
            y_coords, x_coords = np.ogrid[:self.ny, :self.nx]
            distance = np.sqrt((x_coords - cx)**2 + (y_coords - cy)**2)
            self.T = np.where(distance <= radius, 100.0, 20.0)

        elif condition == "uniform":
            # Uniform temperature
            self.T.fill(50.0)

        elif condition == "gradient":
            # Linear gradient from left (hot) to right (cold)
            for i in range(self.nx):
                self.T[:, i] = 100.0 * (1 - i / self.nx)

        elif condition == "corners":
            # Hot corners
            corner_size = min(self.nx, self.ny) // 10
            self.T[:corner_size, :corner_size] = 100.0  # Top-left
            self.T[:corner_size, -corner_size:] = 100.0  # Top-right
            self.T[-corner_size:, :corner_size] = 100.0  # Bottom-left
            self.T[-corner_size:, -corner_size:] = 100.0  # Bottom-right

        elif condition == "checkerboard":
            # Checkerboard pattern
            for i in range(self.ny):
                for j in range(self.nx):
                    if (i // 10 + j // 10) % 2 == 0:
                        self.T[i, j] = 100.0
                    else:
                        self.T[i, j] = 20.0
        else:
            raise ValueError(f"Unknown initial condition: {condition}")

        # Copy to new array
        self.T_new[:] = self.T

    def set_boundary_conditions(self, bc_type: str = "constant"):
        """
        Apply boundary conditions.

        Args:
            bc_type: Type of boundary condition
                - "constant": Fixed temperature boundaries
                - "insulated": Zero-flux (Neumann) boundaries
                - "periodic": Periodic boundaries
        """
        if bc_type == "constant":
            # Fixed temperature at boundaries (Dirichlet)
            self.T[0, :] = 20.0   # Top edge
            self.T[-1, :] = 20.0  # Bottom edge
            self.T[:, 0] = 20.0   # Left edge
            self.T[:, -1] = 20.0  # Right edge

        elif bc_type == "insulated":
            # Insulated boundaries (Neumann - zero flux)
            # Copy values from interior to boundaries
            self.T[0, :] = self.T[1, :]    # Top
            self.T[-1, :] = self.T[-2, :]  # Bottom
            self.T[:, 0] = self.T[:, 1]    # Left
            self.T[:, -1] = self.T[:, -2]  # Right

        elif bc_type == "periodic":
            # Periodic boundaries
            self.T[0, :] = self.T[-2, :]   # Top wraps to bottom
            self.T[-1, :] = self.T[1, :]   # Bottom wraps to top
            self.T[:, 0] = self.T[:, -2]   # Left wraps to right
            self.T[:, -1] = self.T[:, 1]   # Right wraps to left

    def step(self, bc_type: str = "constant") -> float:
        """
        Perform one time step of heat diffusion.

        This is the core computational kernel that will be parallelized.
        Uses explicit finite difference method (5-point stencil).

        Args:
            bc_type: Boundary condition type

        Returns:
            Maximum temperature change (for convergence checking)
        """
        # Start timing
        start_time = time.perf_counter()

        # Compute diffusion coefficient
        rx = self.alpha * self.dt / (self.dx ** 2)
        ry = self.alpha * self.dt / (self.dy ** 2)

        # Update interior points using 5-point stencil
        # T_new[i,j] = T[i,j] + dt*alpha*(d²T/dx² + d²T/dy²)
        for i in range(1, self.ny - 1):
            for j in range(1, self.nx - 1):
                self.T_new[i, j] = self.T[i, j] + \
                    rx * (self.T[i, j+1] - 2*self.T[i, j] + self.T[i, j-1]) + \
                    ry * (self.T[i+1, j] - 2*self.T[i, j] + self.T[i-1, j])

        # Calculate maximum change (for convergence monitoring)
        max_change = np.max(np.abs(self.T_new - self.T))

        # Swap arrays (double buffering)
        self.T, self.T_new = self.T_new, self.T

        # Apply boundary conditions
        self.set_boundary_conditions(bc_type)

        # Update statistics
        elapsed = time.perf_counter() - start_time
        self.total_time += elapsed
        self.iteration_count += 1

        return max_change

    def simulate(
        self,
        num_steps: int,
        bc_type: str = "constant",
        verbose: bool = True,
        convergence_threshold: Optional[float] = None
    ) -> Tuple[np.ndarray, dict]:
        """
        Run the simulation for a given number of time steps.

        Args:
            num_steps: Number of time steps to simulate
            bc_type: Boundary condition type
            verbose: Print progress information
            convergence_threshold: Stop if max change < threshold (optional)

        Returns:
            Final temperature field and statistics dictionary
        """
        if verbose:
            print(f"Starting heat diffusion simulation...")
            print(f"Grid size: {self.nx} × {self.ny} = {self.nx * self.ny:,} cells")
            print(f"Time step: {self.dt}")
            print(f"Thermal diffusivity: {self.alpha}")
            print("-" * 60)

        # Reset statistics
        self.iteration_count = 0
        self.total_time = 0.0
        start_total = time.perf_counter()

        # Main simulation loop
        for step in range(num_steps):
            max_change = self.step(bc_type)

            # Print progress
            if verbose and (step + 1) % (num_steps // 10) == 0:
                progress = (step + 1) / num_steps * 100
                print(f"Step {step + 1}/{num_steps} ({progress:.0f}%) - "
                      f"Max change: {max_change:.6e} - "
                      f"Avg time/step: {self.total_time/(step+1)*1000:.3f} ms")

            # Check convergence
            if convergence_threshold is not None and max_change < convergence_threshold:
                if verbose:
                    print(f"\n✓ Converged at step {step + 1}")
                break

        total_elapsed = time.perf_counter() - start_total

        # Compute statistics
        stats = {
            'total_time': total_elapsed,
            'compute_time': self.total_time,
            'overhead_time': total_elapsed - self.total_time,
            'steps_completed': self.iteration_count,
            'avg_time_per_step': self.total_time / self.iteration_count,
            'cells_per_second': (self.nx * self.ny * self.iteration_count) / self.total_time,
            'final_min_temp': np.min(self.T),
            'final_max_temp': np.max(self.T),
            'final_avg_temp': np.mean(self.T),
        }

        if verbose:
            print("\n" + "=" * 60)
            print("SIMULATION COMPLETE")
            print("=" * 60)
            print(f"Total time:          {stats['total_time']:.4f} seconds")
            print(f"Compute time:        {stats['compute_time']:.4f} seconds")
            print(f"Steps completed:     {stats['steps_completed']:,}")
            print(f"Avg time per step:   {stats['avg_time_per_step']*1000:.3f} ms")
            print(f"Throughput:          {stats['cells_per_second']/1e6:.2f} Mcells/s")
            print(f"\nFinal temperature range: [{stats['final_min_temp']:.2f}, "
                  f"{stats['final_max_temp']:.2f}]")

        return self.T.copy(), stats

    def visualize(
        self,
        title: str = "Heat Diffusion",
        cmap: str = "hot",
        save_path: Optional[str] = None
    ):
        """
        Visualize the current temperature field.

        Args:
            title: Plot title
            cmap: Colormap name
            save_path: Path to save figure (optional)
        """
        plt.figure(figsize=(10, 8))

        im = plt.imshow(
            self.T,
            cmap=cmap,
            origin='lower',
            extent=[0, self.nx*self.dx, 0, self.ny*self.dy],
            interpolation='bilinear'
        )

        plt.colorbar(im, label='Temperature (°C)')
        plt.xlabel('X Position (m)')
        plt.ylabel('Y Position (m)')
        plt.title(title)
        plt.grid(True, alpha=0.3)

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"✓ Figure saved to {save_path}")

        plt.show()


def benchmark_performance(grid_sizes: list, num_steps: int = 1000):
    """
    Benchmark serial performance across different grid sizes.

    Args:
        grid_sizes: List of grid sizes to test
        num_steps: Number of time steps for each test

    Returns:
        Dictionary with benchmark results
    """
    results = {
        'grid_sizes': [],
        'total_cells': [],
        'execution_times': [],
        'cells_per_second': [],
        'time_per_step': []
    }

    print("=" * 70)
    print("SERIAL PERFORMANCE BENCHMARK")
    print("=" * 70)
    print(f"{'Grid Size':<15} {'Total Cells':<15} {'Time (s)':<12} {'Mcells/s':<12}")
    print("-" * 70)

    for size in grid_sizes:
        # Create simulator
        sim = HeatDiffusion2D(nx=size, ny=size, dt=0.0001)
        sim.set_initial_conditions("center_hot")

        # Run simulation
        _, stats = sim.simulate(num_steps, verbose=False)

        # Store results
        total_cells = size * size
        results['grid_sizes'].append(size)
        results['total_cells'].append(total_cells)
        results['execution_times'].append(stats['compute_time'])
        results['cells_per_second'].append(stats['cells_per_second'])
        results['time_per_step'].append(stats['avg_time_per_step'])

        # Print results
        print(f"{size}×{size:<11} {total_cells:<15,} "
              f"{stats['compute_time']:<12.4f} "
              f"{stats['cells_per_second']/1e6:<12.2f}")

    print("=" * 70)

    return results


def plot_benchmark_results(results: dict, save_path: Optional[str] = None):
    """
    Plot benchmark results.

    Args:
        results: Dictionary from benchmark_performance()
        save_path: Path to save figure (optional)
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Execution time vs grid size
    ax1.plot(results['grid_sizes'], results['execution_times'], 'o-', linewidth=2, markersize=8)
    ax1.set_xlabel('Grid Size (N×N)', fontsize=12)
    ax1.set_ylabel('Execution Time (seconds)', fontsize=12)
    ax1.set_title('Serial Performance: Execution Time', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')

    # Throughput vs grid size
    throughput_mcells = [c/1e6 for c in results['cells_per_second']]
    ax2.plot(results['grid_sizes'], throughput_mcells, 's-',
             linewidth=2, markersize=8, color='green')
    ax2.set_xlabel('Grid Size (N×N)', fontsize=12)
    ax2.set_ylabel('Throughput (Mcells/s)', fontsize=12)
    ax2.set_title('Serial Performance: Throughput', fontsize=14)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"✓ Benchmark plot saved to {save_path}")

    plt.show()


# Example usage and testing
if __name__ == "__main__":
    print("2D Heat Diffusion - Serial Implementation")
    print("=" * 70)

    # Test 1: Basic simulation
    print("\n[Test 1] Basic simulation with center hot spot")
    sim = HeatDiffusion2D(nx=100, ny=100, alpha=0.01, dt=0.0001)
    sim.set_initial_conditions("center_hot")
    sim.visualize(title="Initial Temperature Distribution")

    # Run simulation
    final_T, stats = sim.simulate(num_steps=5000, verbose=True)
    sim.visualize(title="Final Temperature Distribution (5000 steps)")

    # Test 2: Performance benchmark
    print("\n[Test 2] Performance benchmark across grid sizes")
    grid_sizes = [50, 100, 200, 400]
    results = benchmark_performance(grid_sizes, num_steps=1000)
    plot_benchmark_results(results)

    print("\n✓ All tests completed successfully!")

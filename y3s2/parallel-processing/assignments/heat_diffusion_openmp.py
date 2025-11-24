"""
2D Heat Diffusion Simulation - OpenMP Parallel Implementation
================================================================

This module implements a parallel version of 2D heat diffusion using
Python's multiprocessing module (OpenMP-style parallelism).

Key Features:
- Row-based domain decomposition
- Shared-memory parallelism using multiprocessing
- Configurable number of threads
- Performance comparison with serial version

Author: Parallel Processing Assignment
Date: November 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import multiprocessing as mp
from typing import Tuple, Optional
from functools import partial


class HeatDiffusion2D_OpenMP:
    """
    2D Heat Diffusion Simulator with OpenMP-style parallelization.

    This implementation uses row-based decomposition where each worker process
    handles a chunk of rows from the grid.

    Attributes:
        nx (int): Number of grid points in x-direction
        ny (int): Number of grid points in y-direction
        dx (float): Grid spacing in x-direction
        dy (float): Grid spacing in y-direction
        alpha (float): Thermal diffusivity
        dt (float): Time step size
        num_threads (int): Number of parallel threads
        T (np.ndarray): Current temperature field (shared)
        T_new (np.ndarray): Next temperature field (shared)
    """

    def __init__(
        self,
        nx: int = 100,
        ny: int = 100,
        Lx: float = 1.0,
        Ly: float = 1.0,
        alpha: float = 0.01,
        dt: float = 0.001,
        num_threads: Optional[int] = None
    ):
        """
        Initialize the parallel heat diffusion simulator.

        Args:
            nx: Number of grid points in x-direction
            ny: Number of grid points in y-direction
            Lx: Physical length in x-direction (meters)
            Ly: Physical length in y-direction (meters)
            alpha: Thermal diffusivity (m²/s)
            dt: Time step size (seconds)
            num_threads: Number of threads (default: CPU count)
        """
        self.nx = nx
        self.ny = ny
        self.dx = Lx / (nx - 1)
        self.dy = Ly / (ny - 1)
        self.alpha = alpha
        self.dt = dt

        # Set number of threads
        if num_threads is None:
            self.num_threads = mp.cpu_count()
        else:
            self.num_threads = num_threads

        # Check stability condition (CFL condition)
        max_dt = min(self.dx**2, self.dy**2) / (4 * alpha)
        if dt > max_dt:
            print(f"⚠️  WARNING: Time step dt={dt} may be unstable!")
            print(f"   Recommended max dt: {max_dt:.6f}")

        # Initialize temperature fields
        self.T = np.zeros((ny, nx), dtype=np.float64)
        self.T_new = np.zeros((ny, nx), dtype=np.float64)

        # Statistics tracking
        self.iteration_count = 0
        self.total_time = 0.0
        self.parallel_time = 0.0
        self.overhead_time = 0.0

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
            cy, cx = self.ny // 2, self.nx // 2
            radius = min(self.nx, self.ny) // 10
            y_coords, x_coords = np.ogrid[:self.ny, :self.nx]
            distance = np.sqrt((x_coords - cx)**2 + (y_coords - cy)**2)
            self.T = np.where(distance <= radius, 100.0, 20.0)

        elif condition == "uniform":
            self.T.fill(50.0)

        elif condition == "gradient":
            for i in range(self.nx):
                self.T[:, i] = 100.0 * (1 - i / self.nx)

        elif condition == "corners":
            corner_size = min(self.nx, self.ny) // 10
            self.T[:corner_size, :corner_size] = 100.0
            self.T[:corner_size, -corner_size:] = 100.0
            self.T[-corner_size:, :corner_size] = 100.0
            self.T[-corner_size:, -corner_size:] = 100.0

        elif condition == "checkerboard":
            for i in range(self.ny):
                for j in range(self.nx):
                    if (i // 10 + j // 10) % 2 == 0:
                        self.T[i, j] = 100.0
                    else:
                        self.T[i, j] = 20.0
        else:
            raise ValueError(f"Unknown initial condition: {condition}")

        self.T_new[:] = self.T

    def set_boundary_conditions(self, bc_type: str = "constant"):
        """
        Apply boundary conditions.

        Args:
            bc_type: Type of boundary condition
        """
        if bc_type == "constant":
            self.T[0, :] = 20.0
            self.T[-1, :] = 20.0
            self.T[:, 0] = 20.0
            self.T[:, -1] = 20.0
        elif bc_type == "insulated":
            self.T[0, :] = self.T[1, :]
            self.T[-1, :] = self.T[-2, :]
            self.T[:, 0] = self.T[:, 1]
            self.T[:, -1] = self.T[:, -2]
        elif bc_type == "periodic":
            self.T[0, :] = self.T[-2, :]
            self.T[-1, :] = self.T[1, :]
            self.T[:, 0] = self.T[:, -2]
            self.T[:, -1] = self.T[:, 1]

    @staticmethod
    def _compute_chunk(args):
        """
        Compute heat diffusion for a chunk of rows.

        This static method is the parallel worker function.
        Each thread calls this to update its assigned rows.

        Args:
            args: Tuple of (T, row_start, row_end, nx, rx, ry)

        Returns:
            Tuple of (row_start, row_end, T_new_chunk, max_change)
        """
        T, row_start, row_end, nx, rx, ry = args

        # Allocate output for this chunk
        chunk_height = row_end - row_start
        T_new_chunk = np.zeros((chunk_height, nx), dtype=np.float64)

        # Update interior points in this chunk
        max_change = 0.0
        for i in range(chunk_height):
            global_i = row_start + i

            # Skip if on boundary (will be handled by boundary conditions)
            if global_i == 0 or global_i == T.shape[0] - 1:
                T_new_chunk[i, :] = T[global_i, :]
                continue

            for j in range(1, nx - 1):
                # Apply 5-point stencil
                T_new_chunk[i, j] = T[global_i, j] + \
                    rx * (T[global_i, j+1] - 2*T[global_i, j] + T[global_i, j-1]) + \
                    ry * (T[global_i+1, j] - 2*T[global_i, j] + T[global_i-1, j])

                # Track maximum change
                change = abs(T_new_chunk[i, j] - T[global_i, j])
                if change > max_change:
                    max_change = change

        return row_start, row_end, T_new_chunk, max_change

    def step_parallel(self, bc_type: str = "constant") -> float:
        """
        Perform one time step using parallel computation.

        Args:
            bc_type: Boundary condition type

        Returns:
            Maximum temperature change
        """
        start_time = time.perf_counter()

        # Compute diffusion coefficients
        rx = self.alpha * self.dt / (self.dx ** 2)
        ry = self.alpha * self.dt / (self.dy ** 2)

        # Divide rows among threads
        rows_per_thread = self.ny // self.num_threads
        chunks = []

        for thread_id in range(self.num_threads):
            row_start = thread_id * rows_per_thread
            if thread_id == self.num_threads - 1:
                row_end = self.ny  # Last thread takes remaining rows
            else:
                row_end = (thread_id + 1) * rows_per_thread

            chunks.append((self.T.copy(), row_start, row_end, self.nx, rx, ry))

        # Execute parallel computation using multiprocessing pool
        parallel_start = time.perf_counter()

        with mp.Pool(processes=self.num_threads) as pool:
            results = pool.map(self._compute_chunk, chunks)

        parallel_time = time.perf_counter() - parallel_start

        # Gather results from all threads
        max_change = 0.0
        for row_start, row_end, T_new_chunk, chunk_max_change in results:
            chunk_height = row_end - row_start
            self.T_new[row_start:row_end, :] = T_new_chunk
            max_change = max(max_change, chunk_max_change)

        # Swap arrays
        self.T, self.T_new = self.T_new, self.T

        # Apply boundary conditions
        self.set_boundary_conditions(bc_type)

        # Update statistics
        elapsed = time.perf_counter() - start_time
        self.total_time += elapsed
        self.parallel_time += parallel_time
        self.overhead_time += (elapsed - parallel_time)
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
        Run the parallel simulation.

        Args:
            num_steps: Number of time steps
            bc_type: Boundary condition type
            verbose: Print progress
            convergence_threshold: Stop if change < threshold

        Returns:
            Final temperature field and statistics
        """
        if verbose:
            print(f"Starting PARALLEL heat diffusion simulation...")
            print(f"Grid size: {self.nx} × {self.ny} = {self.nx * self.ny:,} cells")
            print(f"Threads: {self.num_threads}")
            print(f"Time step: {self.dt}")
            print("-" * 60)

        self.iteration_count = 0
        self.total_time = 0.0
        self.parallel_time = 0.0
        self.overhead_time = 0.0
        start_total = time.perf_counter()

        for step in range(num_steps):
            max_change = self.step_parallel(bc_type)

            if verbose and (step + 1) % (num_steps // 10) == 0:
                progress = (step + 1) / num_steps * 100
                print(f"Step {step + 1}/{num_steps} ({progress:.0f}%) - "
                      f"Max change: {max_change:.6e} - "
                      f"Avg time/step: {self.total_time/(step+1)*1000:.3f} ms")

            if convergence_threshold is not None and max_change < convergence_threshold:
                if verbose:
                    print(f"\n✓ Converged at step {step + 1}")
                break

        total_elapsed = time.perf_counter() - start_total

        stats = {
            'total_time': total_elapsed,
            'compute_time': self.total_time,
            'parallel_time': self.parallel_time,
            'overhead_time': self.overhead_time,
            'steps_completed': self.iteration_count,
            'avg_time_per_step': self.total_time / self.iteration_count,
            'cells_per_second': (self.nx * self.ny * self.iteration_count) / self.total_time,
            'num_threads': self.num_threads,
            'final_min_temp': np.min(self.T),
            'final_max_temp': np.max(self.T),
            'final_avg_temp': np.mean(self.T),
        }

        if verbose:
            print("\n" + "=" * 60)
            print("PARALLEL SIMULATION COMPLETE")
            print("=" * 60)
            print(f"Total time:          {stats['total_time']:.4f} seconds")
            print(f"Compute time:        {stats['compute_time']:.4f} seconds")
            print(f"Parallel time:       {stats['parallel_time']:.4f} seconds ({stats['parallel_time']/stats['compute_time']*100:.1f}%)")
            print(f"Overhead time:       {stats['overhead_time']:.4f} seconds ({stats['overhead_time']/stats['compute_time']*100:.1f}%)")
            print(f"Threads used:        {stats['num_threads']}")
            print(f"Steps completed:     {stats['steps_completed']:,}")
            print(f"Avg time per step:   {stats['avg_time_per_step']*1000:.3f} ms")
            print(f"Throughput:          {stats['cells_per_second']/1e6:.2f} Mcells/s")

        return self.T.copy(), stats

    def visualize(
        self,
        title: str = "Heat Diffusion (Parallel)",
        cmap: str = "hot",
        save_path: Optional[str] = None
    ):
        """Visualize the current temperature field."""
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
        plt.title(f"{title} ({self.num_threads} threads)")
        plt.grid(True, alpha=0.3)

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"✓ Figure saved to {save_path}")

        plt.show()


def compare_serial_parallel(grid_sizes: list, num_steps: int = 1000):
    """
    Compare serial vs parallel performance across grid sizes.

    Args:
        grid_sizes: List of grid sizes to test
        num_steps: Number of time steps

    Returns:
        Dictionary with comparison results
    """
    # Import serial implementation
    import sys
    sys.path.append('.')
    from heat_diffusion_serial import HeatDiffusion2D

    results = {
        'grid_sizes': [],
        'serial_times': [],
        'parallel_times': [],
        'speedups': [],
        'efficiencies': [],
        'threads': []
    }

    num_threads = mp.cpu_count()

    print("=" * 80)
    print("SERIAL vs PARALLEL PERFORMANCE COMPARISON")
    print("=" * 80)
    print(f"{'Grid Size':<15} {'Serial (s)':<12} {'Parallel (s)':<15} {'Speedup':<12} {'Efficiency':<12}")
    print("-" * 80)

    for size in grid_sizes:
        # Serial version
        sim_serial = HeatDiffusion2D(nx=size, ny=size, dt=0.0001)
        sim_serial.set_initial_conditions("center_hot")
        _, stats_serial = sim_serial.simulate(num_steps, verbose=False)

        # Parallel version
        sim_parallel = HeatDiffusion2D_OpenMP(nx=size, ny=size, dt=0.0001, num_threads=num_threads)
        sim_parallel.set_initial_conditions("center_hot")
        _, stats_parallel = sim_parallel.simulate(num_steps, verbose=False)

        # Calculate metrics
        serial_time = stats_serial['compute_time']
        parallel_time = stats_parallel['compute_time']
        speedup = serial_time / parallel_time
        efficiency = speedup / num_threads * 100

        # Store results
        results['grid_sizes'].append(size)
        results['serial_times'].append(serial_time)
        results['parallel_times'].append(parallel_time)
        results['speedups'].append(speedup)
        results['efficiencies'].append(efficiency)
        results['threads'].append(num_threads)

        print(f"{size}×{size:<11} {serial_time:<12.4f} {parallel_time:<15.4f} "
              f"{speedup:<12.2f}x {efficiency:<12.1f}%")

    print("=" * 80)
    print(f"Average speedup: {np.mean(results['speedups']):.2f}x")
    print(f"Average efficiency: {np.mean(results['efficiencies']):.1f}%")
    print("=" * 80)

    return results


# Example usage and testing
if __name__ == "__main__":
    print("2D Heat Diffusion - OpenMP Parallel Implementation")
    print("=" * 70)

    # Test 1: Basic parallel simulation
    print("\n[Test 1] Parallel simulation with multiple threads")
    num_threads = mp.cpu_count()
    print(f"Using {num_threads} threads")

    sim = HeatDiffusion2D_OpenMP(nx=200, ny=200, alpha=0.01, dt=0.0001, num_threads=num_threads)
    sim.set_initial_conditions("center_hot")

    final_T, stats = sim.simulate(num_steps=1000, verbose=True)

    # Test 2: Compare with serial version
    print("\n[Test 2] Compare serial vs parallel performance")
    grid_sizes = [100, 200, 400]
    results = compare_serial_parallel(grid_sizes, num_steps=500)

    print("\n✓ All tests completed successfully!")

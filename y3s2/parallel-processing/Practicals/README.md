# BMCS3003 Parallel Processing - Practical Notebooks

Educational Jupyter notebooks for learning distributed systems and parallel computing concepts through hands-on C++ programming exercises.

## 📚 Notebooks Overview

| # | Notebook | Topics | Difficulty | Time |
|---|----------|--------|------------|------|
| 1 | [Cristian's Algorithm](01_cristians_algorithm.ipynb) | Clock synchronization, socket programming, network latency | ⭐⭐ | 90 min |
| 2 | [Threading & UDP](02_threading_pthread_udp.ipynb) | C++ threads, pthreads, UDP communication | ⭐⭐ | 120 min |
| 3 | [OpenMP & CUDA](03_openmp_cuda.ipynb) | OpenMP directives, memory management, GPU computing | ⭐⭐⭐ | 180 min |
| 4 | [Concurrency Control 1](04_concurrency_control_part1.ipynb) | Critical sections, atomic operations, locks | ⭐⭐⭐ | 120 min |
| 5 | [Concurrency Control 2](05_concurrency_control_part2.ipynb) | Barriers, mutexes, deadlock prevention | ⭐⭐⭐ | 120 min |

## 🎯 Learning Path

### Prerequisites
- Basic C++ programming
- Understanding of functions, loops, arrays
- Familiarity with Visual Studio or g++/clang++
- Basic command line usage

### Module 1: Distributed Systems Fundamentals
**Practical 1: Clock Synchronization**
- Learn how distributed systems coordinate time
- Implement client-server socket communication
- Understand network latency and its impact
- Compare Cristian's and Berkeley's algorithms

### Module 2: Multi-threading Basics
**Practical 2: Threading Libraries**
- Master C++ standard threading library
- Set up and use POSIX threads (pthreads)
- Implement UDP socket communication
- Build multi-threaded network applications

### Module 3: Shared-Memory Parallelism
**Practical 3: OpenMP & GPU Computing**
- Configure OpenMP in your development environment
- Parallelize loops with compiler directives
- Understand false sharing and cache coherence
- Introduction to CUDA for GPU parallel computing

### Module 4: Synchronization & Safety
**Practical 4: Concurrency Control Basics**
- Prevent race conditions with critical sections
- Use reduction clauses for parallel accumulation
- Implement producer-consumer patterns
- Master atomic operations

### Module 5: Advanced Concurrency
**Practical 5: Advanced Synchronization**
- Use barriers for thread coordination
- Work with C++ mutexes and locks
- Identify and prevent deadlocks
- Apply synchronization best practices

## 🛠️ Setup Instructions

### Windows (Visual Studio)

#### For Practicals 1-2 (Sockets, Threads)
1. Create a C++ Console Application project
2. Add required libraries:
   ```cpp
   #pragma comment(lib, "ws2_32.lib")  // For Windows Sockets
   ```
3. For pthreads, install via vcpkg:
   ```cmd
   vcpkg install pthread pthreads:x64-windows
   vcpkg integrate install
   ```

#### For Practicals 3-5 (OpenMP, CUDA)
1. Enable OpenMP support:
   - Project Properties → C/C++ → Language
   - Set "OpenMP Support" to **Yes (/openmp)**

2. For CUDA (optional, if you have NVIDIA GPU):
   - Install [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)
   - Install Visual Studio CUDA integration
   - Create a CUDA project or add `.cu` files

### Linux/macOS (g++/clang++)

```bash
# Install required libraries
sudo apt-get install build-essential  # Ubuntu/Debian
brew install gcc                       # macOS

# Compile with OpenMP
g++ -fopenmp your_program.cpp -o your_program

# Compile with pthreads
g++ -pthread your_program.cpp -o your_program

# For CUDA (if available)
nvcc your_program.cu -o your_program
```

## 📖 How to Use These Notebooks

### Recommended Workflow

1. **Read the Theory** (15-20 minutes)
   - Open the notebook in Jupyter or VS Code
   - Read through concept introduction sections
   - Review diagrams and explanations

2. **Study the Examples** (20-30 minutes)
   - Examine provided code snippets
   - Understand line-by-line explanations
   - Try to predict what code does before running

3. **Complete the Questions** (40-90 minutes)
   - Implement solutions in Visual Studio or your IDE
   - Test with provided inputs
   - Compare your output with expected results

4. **Analyze Performance** (10-15 minutes)
   - Run timing comparisons
   - Calculate speedup factors
   - Understand when parallel > sequential

5. **Review Summary** (5-10 minutes)
   - Revisit key concepts
   - Check if you met learning objectives
   - Note any areas for further study

### Tips for Success

✅ **DO**:
- Complete practicals in order (they build on each other)
- Run code frequently to see immediate results
- Experiment with different thread counts and data sizes
- Read error messages carefully - they guide you to solutions
- Compare your results with expected outputs

❌ **DON'T**:
- Skip theory sections - understanding WHY is crucial
- Copy-paste code without understanding it
- Ignore warnings during compilation
- Test only with small inputs (parallel overhead matters!)
- Work in isolation - discuss concepts with classmates

## 🔍 Common Issues & Solutions

### Issue 1: pthread.h not found (Windows)
**Solution**: Install pthreads via vcpkg (see setup instructions above)

### Issue 2: OpenMP not working
**Solution**:
- Check that `/openmp` flag is enabled in project settings
- Verify selected platform matches build configuration (x86 vs x64)
- Restart Visual Studio after changing settings

### Issue 3: CUDA errors
**Solution**:
- Verify NVIDIA GPU is present: `nvidia-smi`
- Check CUDA installation: `nvcc --version`
- Add CUDA paths to environment variables

### Issue 4: Socket connection refused
**Solution**:
- Run server before client
- Check firewall settings
- Verify IP address and port number match
- Use `127.0.0.1` (localhost) for testing first

### Issue 5: Race conditions / incorrect results
**Solution**:
- Add proper synchronization (critical, atomic, mutex)
- Check shared vs private variable declarations
- Use reduction clauses for accumulation operations
- Enable compiler warnings to catch data races

## 📊 Performance Benchmarking

### How to Measure Speedup

```cpp
#include <chrono>

// Start timing
auto start = std::chrono::high_resolution_clock::now();

// Your parallel code here
// ...

// End timing
auto end = std::chrono::high_resolution_clock::now();
auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);

std::cout << "Time: " << duration.count() << " microseconds" << std::endl;
```

### Calculate Speedup Factor

```
Speedup = T_sequential / T_parallel

Efficiency = Speedup / Number_of_Threads

Example:
Sequential: 10.0 seconds
Parallel (4 threads): 3.0 seconds
Speedup = 10.0 / 3.0 = 3.33x
Efficiency = 3.33 / 4 = 83.25%
```

## 🎓 Learning Objectives Matrix

| Practical | Concepts | Skills | Tools |
|-----------|----------|--------|-------|
| 1 | Clock sync, latency | Socket programming | Winsock2, TCP |
| 2 | Concurrency basics | Thread management | std::thread, pthread |
| 3 | Shared memory parallelism | Loop parallelization | OpenMP, CUDA |
| 4 | Synchronization | Race condition prevention | Critical sections, atomic |
| 5 | Advanced sync | Deadlock avoidance | Mutexes, barriers |

## 📚 Additional Resources

### Official Documentation
- [OpenMP Specification](https://www.openmp.org/specifications/)
- [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [C++ Threading Reference](https://en.cppreference.com/w/cpp/thread)

### Tutorials
- [GeeksforGeeks - Distributed Systems](https://www.geeksforgeeks.org/distributed-systems/)
- [Lawrence Livermore OpenMP Tutorial](https://hpc-tutorials.llnl.gov/openmp/)
- [NVIDIA CUDA Tutorials](https://developer.nvidia.com/cuda-education)

### Tools
- [Visual Studio Community](https://visualstudio.microsoft.com/vs/community/)
- [NVIDIA Nsight Systems](https://developer.nvidia.com/nsight-systems)
- [Intel VTune Profiler](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/vtune-profiler.html)

## 🤝 Contributing

Found an error or have suggestions for improvement?
- Open an issue in the repository
- Discuss with your instructor
- Share your insights with classmates

## 📝 Assessment Guidelines

### What Your Instructor Will Look For

1. **Correctness** (40%)
   - Code compiles without errors
   - Produces expected outputs
   - Handles edge cases properly

2. **Understanding** (30%)
   - Can explain how code works
   - Understands when to use each technique
   - Recognizes trade-offs

3. **Performance** (20%)
   - Achieves speedup with parallelization
   - Avoids unnecessary synchronization
   - Optimizes critical sections

4. **Code Quality** (10%)
   - Clean, readable code
   - Proper comments
   - Good variable names

## 📅 Recommended Schedule

| Week | Practical | Focus |
|------|-----------|-------|
| 1-2 | Practical 1 | Distributed systems basics |
| 3-4 | Practical 2 | Threading fundamentals |
| 5-7 | Practical 3 | OpenMP and GPU computing |
| 8-9 | Practical 4 | Concurrency control basics |
| 10-11 | Practical 5 | Advanced synchronization |
| 12 | Review | Integrate all concepts |

---

**Course**: BMCS3003 Distributed Systems and Parallel Computing
**University**: [Your University Name]
**Semester**: Year 3 Semester 2
**Last Updated**: 2025-01-18

Happy parallel programming! 🚀

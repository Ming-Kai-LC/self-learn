# TROUBLESHOOTING GUIDE
## Parallel Processing Heat Diffusion Assignment

**Last Updated**: November 23, 2025
**Coverage**: Common issues and solutions

---

## 📋 TABLE OF CONTENTS

1. [Installation & Setup Issues](#installation--setup-issues)
2. [Code Execution Problems](#code-execution-problems)
3. [Performance Issues](#performance-issues)
4. [Testing Failures](#testing-failures)
5. [Benchmarking Problems](#benchmarking-problems)
6. [Multiprocessing Issues](#multiprocessing-issues)
7. [CUDA/GPU Issues](#cudagpu-issues)
8. [Visualization Problems](#visualization-problems)
9. [Academic Writing Issues](#academic-writing-issues)
10. [Git/GitHub Issues](#gitgithub-issues)
11. [Assignment Submission Issues](#assignment-submission-issues)

---

## 🔧 INSTALLATION & SETUP ISSUES

### Issue 1: "ModuleNotFoundError: No module named 'numpy'"

**Symptom**:
```bash
ModuleNotFoundError: No module named 'numpy'
```

**Cause**: Required Python packages not installed

**Solution**:
```bash
# Install all required packages
pip install numpy matplotlib scipy pandas

# Or install from requirements.txt
cd /home/user/self-learn/y3s2/parallel-processing
pip install -r requirements.txt

# Verify installation
python -c "import numpy; print(numpy.__version__)"
```

**Prevention**: Always use virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install packages
pip install -r requirements.txt
```

---

### Issue 2: "Python version incompatibility"

**Symptom**:
```bash
SyntaxError: invalid syntax
```

**Cause**: Code requires Python 3.8+

**Solution**:
```bash
# Check Python version
python --version

# Should be 3.8 or higher
# If not, install newer Python:

# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install python3.10

# Mac
brew install python@3.10

# Windows
# Download from python.org
```

**Workaround**: Use type hints conditionally
```python
# Instead of:
from typing import Optional

# Use:
try:
    from typing import Optional
except ImportError:
    Optional = None
```

---

### Issue 3: "Permission denied when installing packages"

**Symptom**:
```bash
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

**Cause**: Trying to install globally without admin rights

**Solution 1** (Recommended): Use virtual environment
```bash
python -m venv venv
source venv/bin/activate
pip install numpy matplotlib
```

**Solution 2**: Install for user only
```bash
pip install --user numpy matplotlib
```

**Solution 3**: Use sudo (Linux/Mac only, not recommended)
```bash
sudo pip install numpy matplotlib
```

---

## 💻 CODE EXECUTION PROBLEMS

### Issue 4: "heat_diffusion_serial.py runs very slowly"

**Symptom**: Simulation takes minutes instead of seconds

**Causes & Solutions**:

**Cause 1**: Grid too large
```python
# Problem: Grid too big for testing
sim = HeatDiffusion2D(nx=4096, ny=4096)  # Takes forever!

# Solution: Use smaller grid for testing
sim = HeatDiffusion2D(nx=100, ny=100)    # Much faster
```

**Cause 2**: Too many time steps
```python
# Problem: Too many iterations
sim.simulate(num_steps=100000)  # Very slow

# Solution: Reduce for testing
sim.simulate(num_steps=1000)     # Faster
```

**Cause 3**: Debug mode on
```python
# Problem: Verbose output slows down
sim.simulate(num_steps=1000, verbose=True)  # Prints every 10%

# Solution: Turn off for benchmarking
sim.simulate(num_steps=1000, verbose=False)  # Faster
```

**Cause 4**: Python interpreter inefficiency
```python
# Problem: Pure Python is slow
# Solution: This is expected! That's why we need parallelization

# For production: Use NumPy vectorization or Numba JIT
from numba import jit

@jit(nopython=True)
def fast_update(T, T_new, rx, ry):
    # JIT-compiled version runs much faster
    pass
```

---

### Issue 5: "ImportError: cannot import name 'HeatDiffusion2D'"

**Symptom**:
```python
from heat_diffusion_serial import HeatDiffusion2D
ImportError: cannot import name 'HeatDiffusion2D'
```

**Cause**: Wrong directory or file path issue

**Solution 1**: Check current directory
```bash
# Are you in the right directory?
pwd
# Should show: .../y3s2/parallel-processing/assignments

# If not:
cd /home/user/self-learn/y3s2/parallel-processing/assignments
```

**Solution 2**: Add to Python path
```python
import sys
sys.path.append('/home/user/self-learn/y3s2/parallel-processing/assignments')

from heat_diffusion_serial import HeatDiffusion2D
```

**Solution 3**: Use absolute imports
```python
# Instead of relative import
from heat_diffusion_serial import HeatDiffusion2D

# Use absolute path
import importlib.util
spec = importlib.util.spec_from_file_location(
    "heat_diffusion_serial",
    "/full/path/to/heat_diffusion_serial.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
HeatDiffusion2D = module.HeatDiffusion2D
```

---

### Issue 6: "Code crashes with 'MemoryError'"

**Symptom**:
```bash
MemoryError: Unable to allocate array
```

**Cause**: Grid size too large for available RAM

**Diagnosis**:
```python
import numpy as np

# Calculate memory required
nx, ny = 4096, 4096
bytes_per_float = 8  # float64
num_arrays = 2  # T and T_new

memory_required = nx * ny * bytes_per_float * num_arrays
memory_gb = memory_required / (1024**3)

print(f"Memory required: {memory_gb:.2f} GB")
# 4096×4096 requires ~0.5 GB (manageable)
# 8192×8192 requires ~2 GB (may be tight)
```

**Solution 1**: Reduce grid size
```python
# Instead of:
sim = HeatDiffusion2D(nx=8192, ny=8192)  # 2 GB

# Use:
sim = HeatDiffusion2D(nx=2048, ny=2048)  # 0.13 GB
```

**Solution 2**: Use float32 instead of float64
```python
# Modify code to use 32-bit floats (half memory)
self.T = np.zeros((ny, nx), dtype=np.float32)
```

**Solution 3**: Close other applications
```bash
# Free up RAM before running
# Close browser, IDEs, etc.
```

---

## ⚡ PERFORMANCE ISSUES

### Issue 7: "Speedup is much lower than expected"

**Symptom**:
```
Threads: 8, Speedup: 2.5x (expected 6-8x)
```

**Diagnosis Checklist**:

**1. Check if truly running in parallel**
```python
import multiprocessing as mp
print(f"CPU count: {mp.cpu_count()}")
print(f"Threads configured: {sim.num_threads}")

# Should match
```

**2. Profile to find bottleneck**
```python
import cProfile

cProfile.run('sim.simulate(num_steps=100)')
# Look for functions taking most time
```

**3. Check for serialization overhead**
```python
# Problem: Copying large arrays to each process
# Multiprocessing serializes/deserializes data

# Solution: Use shared memory (advanced)
from multiprocessing import shared_memory
```

**Common Causes**:

**Cause 1**: Problem too small
```python
# Grid too small - overhead dominates
sim = HeatDiffusion2D(nx=50, ny=50)  # Bad for parallel
# Speedup: 2x instead of 8x

# Solution: Use larger grid
sim = HeatDiffusion2D(nx=1024, ny=1024)  # Good for parallel
# Speedup: 6-7x
```

**Cause 2**: Too few time steps
```python
# Too few iterations - startup overhead matters
sim.simulate(num_steps=10)  # Bad

# Solution: More iterations
sim.simulate(num_steps=1000)  # Better
```

**Cause 3**: System issues
```bash
# Other processes using CPU
# Check CPU usage:
top  # Linux/Mac
# or
Task Manager  # Windows

# Kill unnecessary processes
```

**Cause 4**: Amdahl's Law limitation
```python
# Some code cannot be parallelized
# With 5% serial code:
# Max speedup with 8 cores = 6.15x (not 8x)

# This is NORMAL and EXPECTED!
```

---

### Issue 8: "Performance worse in parallel than serial"

**Symptom**:
```
Serial:   10 seconds
Parallel: 15 seconds (worse!)
```

**Causes**:

**Cause 1**: Overhead too high for problem size
```python
# Problem is too small
grid_size = 50  # Overhead > computation

# Solution: Use larger problem
grid_size = 500  # Computation > overhead
```

**Cause 2**: Memory thrashing
```python
# Too many threads for available cores
num_threads = 32  # But only 8 physical cores

# Solution: Match thread count to cores
num_threads = mp.cpu_count()  # Optimal
```

**Cause 3**: False sharing
```python
# Multiple threads writing to adjacent memory
# Solution: Pad arrays or use row-based decomposition
```

**Rule of Thumb**:
- Grid < 100×100: Serial is faster
- Grid 100×100 to 500×500: Parallel starts helping
- Grid > 1000×1000: Parallel definitely faster

---

## 🧪 TESTING FAILURES

### Issue 9: "Test failed: Energy not conserved"

**Symptom**:
```bash
AssertionError: Energy not conserved: 1.234e-05
```

**Causes**:

**Cause 1**: Using wrong boundary conditions
```python
# Problem: Constant boundaries lose energy
sim.set_boundary_conditions("constant")  # Energy escapes

# Solution: Use insulated for conservation test
sim.set_boundary_conditions("insulated")  # Energy conserved
```

**Cause 2**: Numerical precision
```python
# Problem: Float rounding errors accumulate
error = 1.5e-10  # Very small but non-zero

# Solution: Use looser tolerance
assert error < 1e-9  # Instead of 1e-10
```

**Cause 3**: Too many time steps
```python
# More steps = more accumulated error
sim.simulate(num_steps=100000)  # Higher error

# Solution: Fewer steps for test
sim.simulate(num_steps=1000)  # Lower error
```

---

### Issue 10: "Test times out"

**Symptom**:
```bash
Timeout: Test exceeded 120 seconds
```

**Solution**:
```python
# Reduce problem size for tests
def test_basic():
    # Use small grid for speed
    sim = HeatDiffusion2D(nx=50, ny=50)  # Not 1024!
    sim.simulate(num_steps=100)           # Not 10000!
```

**Configure Timeout**:
```python
import pytest

@pytest.mark.timeout(300)  # 5 minutes
def test_long_simulation():
    # Longer timeout for intensive tests
    pass
```

---

### Issue 11: "Convergence test fails"

**Symptom**:
```bash
AssertionError: Temperature should become more uniform
```

**Causes**:

**Cause 1**: Not enough time steps
```python
# Problem: Hasn't converged yet
sim.simulate(num_steps=10)  # Too few!

# Solution: More iterations
sim.simulate(num_steps=500)  # Better
```

**Cause 2**: Time step too small
```python
# Very small dt means slow convergence
dt = 0.00001  # Tiny

# Solution: Larger (but stable) dt
dt = 0.0001  # Faster convergence
```

**Cause 3**: Wrong initial condition
```python
# Uniform temperature won't change
sim.set_initial_conditions("uniform")  # No convergence

# Solution: Use non-uniform
sim.set_initial_conditions("gradient")  # Will converge
```

---

## 📊 BENCHMARKING PROBLEMS

### Issue 12: "Inconsistent benchmark results"

**Symptom**:
```
Run 1: 5.2 seconds
Run 2: 8.7 seconds
Run 3: 5.1 seconds
High variance!
```

**Causes & Solutions**:

**Cause 1**: Background processes
```bash
# Solution: Close all other applications
# Check what's running:
top  # Linux/Mac
taskmgr  # Windows

# Kill unnecessary processes
```

**Cause 2**: Thermal throttling
```bash
# CPU heating up, slowing down

# Solution: Let CPU cool between runs
import time
for i in range(5):
    run_benchmark()
    time.sleep(60)  # Cool down
```

**Cause 3**: Cache effects
```python
# First run fills cache, subsequent runs faster

# Solution: Warm up before timing
sim.simulate(num_steps=100)  # Warmup (don't time)
start = time.time()
sim.simulate(num_steps=1000)  # Actual timing
elapsed = time.time() - start
```

**Cause 4**: Random OS scheduling
```bash
# OS might schedule other tasks

# Solution: Set process priority
# Linux:
nice -n -20 python benchmark.py

# Or run multiple times and take median
```

**Best Practice**:
```python
# Always run 5-10 times
times = []
for _ in range(10):
    start = time.time()
    sim.simulate(num_steps=1000, verbose=False)
    times.append(time.time() - start)

# Report median (more robust than mean)
median_time = np.median(times)
std_time = np.std(times)
print(f"Time: {median_time:.3f} ± {std_time:.3f}s")
```

---

### Issue 13: "Can't reproduce paper results"

**Symptom**:
```
Paper claims: 8x speedup
My result: 4x speedup
```

**Reasons** (Normal!):

1. **Different hardware**
   - Paper: High-end server with 32 cores
   - You: Laptop with 8 cores
   - **This is OK!** Document your hardware

2. **Different problem size**
   - Paper: 4096×4096 grid
   - You: 1024×1024 grid
   - **Solution**: Match their problem size

3. **Different implementations**
   - Paper: C++ with CUDA
   - You: Python with multiprocessing
   - **This is OK!** Different languages perform differently

4. **Different optimizations**
   - Paper: Heavily optimized code
   - You: Educational baseline
   - **This is OK for assignment!**

**What to do**:
- Document your setup clearly
- Compare relative improvements (your serial vs your parallel)
- Don't worry if absolute numbers differ from papers

---

## 🔄 MULTIPROCESSING ISSUES

### Issue 14: "Multiprocessing doesn't work in Jupyter"

**Symptom**:
```python
# Code hangs or crashes in Jupyter notebook
```

**Cause**: Jupyter doesn't handle multiprocessing well

**Solution 1**: Use `if __name__ == '__main__'` guard
```python
if __name__ == '__main__':
    sim = HeatDiffusion2D_OpenMP(num_threads=8)
    sim.simulate(num_steps=1000)
```

**Solution 2**: Run as Python script instead
```bash
# Save notebook as .py file
jupyter nbconvert --to python notebook.ipynb

# Run as script
python notebook.py
```

**Solution 3**: Use different backend
```python
# Use threading instead (less efficient but works)
from multiprocessing.pool import ThreadPool
```

---

### Issue 15: "Multiprocessing in Docker/container"

**Symptom**:
```bash
OSError: [Errno 38] Function not implemented
```

**Cause**: Docker default shared memory too small

**Solution**:
```bash
# Run Docker with larger shared memory
docker run --shm-size=2g your_image

# Or in docker-compose.yml:
shm_size: '2gb'
```

**Alternative**: Use different start method
```python
import multiprocessing as mp
mp.set_start_method('spawn')  # Instead of 'fork'
```

---

### Issue 16: "Pickle error with multiprocessing"

**Symptom**:
```python
PicklingError: Can't pickle <class>
```

**Cause**: Multiprocessing needs to serialize objects

**Solution**: Use `@staticmethod` or module-level functions
```python
# Bad: Instance method
class Simulator:
    def compute(self, data):
        pass

# Good: Static method or module function
class Simulator:
    @staticmethod
    def compute(data):
        pass

# Or
def compute(data):
    pass  # Module level
```

---

## 🖥️ CUDA/GPU ISSUES

### Issue 17: "No CUDA-capable device detected"

**Symptom**:
```python
CudaAPIError: CUDA device not found
```

**Diagnosis**:
```bash
# Check if GPU exists
nvidia-smi

# If command not found: No NVIDIA GPU
# If shows GPU: Driver issue
```

**Solutions**:

**If No GPU**:
```python
# Skip CUDA implementation
# Focus on CPU parallelization (OpenMP)
# This is OK for the assignment!
```

**If GPU exists but not detected**:
```bash
# Update NVIDIA drivers
# Ubuntu/Debian:
sudo apt install nvidia-driver-525

# Check CUDA toolkit
nvcc --version

# If not installed:
sudo apt install nvidia-cuda-toolkit
```

**Numba alternative**:
```bash
# Install Numba with CUDA support
pip install numba

# Test:
python -c "from numba import cuda; print(cuda.is_available())"
```

---

### Issue 18: "CUDA code slower than CPU"

**Symptom**:
```
CPU: 1.5 seconds
GPU: 3.0 seconds (worse!)
```

**Causes**:

**Cause 1**: Problem too small
```python
# Grid too small - memory transfer overhead
grid = 100  # CPU faster

# Solution: Larger grid
grid = 2048  # GPU faster
```

**Cause 2**: Memory transfer overhead
```python
# Transferring data many times
for step in range(1000):
    cuda.to_device(T)      # Slow!
    kernel()
    cuda.from_device(T)    # Slow!

# Solution: Keep data on GPU
T_gpu = cuda.to_device(T)  # Once
for step in range(1000):
    kernel(T_gpu)           # Fast!
T = T_gpu.copy_to_host()   # Once
```

**Cause 3**: Inefficient kernel
```cuda
# Non-coalesced memory access
# Thread 0 accesses T[0,0]
# Thread 1 accesses T[1,0]  # Not adjacent!

# Solution: Coalesce access
# Thread 0 accesses T[0,0]
# Thread 1 accesses T[0,1]  # Adjacent!
```

---

## 📈 VISUALIZATION PROBLEMS

### Issue 19: "Plots don't show"

**Symptom**:
```python
plt.show()  # Nothing happens
```

**Cause**: Backend issue

**Solution 1**: Set backend
```python
import matplotlib
matplotlib.use('TkAgg')  # Interactive backend
import matplotlib.pyplot as plt
```

**Solution 2**: Save instead of show
```python
plt.savefig('result.png')  # Save to file
# Then view file separately
```

**Solution 3**: Different backends
```python
# Try different backends:
matplotlib.use('Qt5Agg')   # If Qt installed
matplotlib.use('MacOSX')   # Mac
matplotlib.use('Agg')      # Non-interactive (save only)
```

---

### Issue 20: "Figures look bad/pixelated"

**Problem**: Low resolution

**Solution**:
```python
# High resolution for reports
plt.savefig('figure.png', dpi=300)  # High DPI

# Larger figure size
plt.figure(figsize=(12, 8))  # Inches

# Vector format for scaling
plt.savefig('figure.pdf')  # PDF is vector
plt.savefig('figure.svg')  # SVG is vector
```

---

## 📝 ACADEMIC WRITING ISSUES

### Issue 21: "Literature review: Can't find papers"

**Problem**: Search returns too few results

**Solutions**:

**Broaden search**:
```
# Too specific:
"parallel heat diffusion OpenMP CUDA Python 2024"

# Better:
"parallel heat diffusion" OR "parallel PDE solver"
```

**Use multiple databases**:
- Google Scholar: scholar.google.com
- IEEE Xplore: ieeexplore.ieee.org
- ACM Digital Library: dl.acm.org
- arXiv: arxiv.org (preprints)

**Snowball sampling**:
1. Find one good paper
2. Look at its references
3. Look at papers citing it (Google Scholar: "Cited by")

**Expand time range**:
```
# Instead of: 2023-2024 only
# Use: 2015-2024 (last 10 years)
```

---

### Issue 22: "Citation formatting wrong"

**Problem**: References don't match Harvard style

**Solution**: Use reference manager

**Mendeley** (Free):
```
1. Install Mendeley Desktop
2. Import papers (drag PDFs)
3. Set citation style: Harvard
4. Export: File → Export → BibTeX
```

**Zotero** (Free):
```
1. Install Zotero
2. Add papers
3. Select all → Right-click → Create Bibliography
4. Choose: Harvard style
```

**Manual Harvard format**:
```
Author(s) (Year) 'Title', Journal, Volume(Issue), pp. pages.

Example:
Smith, J., Jones, A. and Brown, R. (2024) 'Parallel heat diffusion
    using OpenMP', Journal of Parallel Computing, 45(3), pp. 234-256.
    doi: 10.1016/j.parco.2024.102345.
```

---

### Issue 23: "Report too long/too short"

**Too Long** (>20 pages):
```
Problem: Too much detail

Solutions:
- Move code to appendix
- Summarize instead of listing all results
- Remove redundant content
- Focus on key findings
```

**Too Short** (<8 pages):
```
Problem: Not enough content

Add:
- More performance graphs
- Detailed methodology
- Extended discussion
- Additional background
```

**Optimal Structure** (12-15 pages):
```
Abstract: 0.5 pages
Introduction: 1.5 pages
Literature Review: 2 pages
Methodology: 3 pages
Results: 3 pages (BIGGEST section)
Discussion: 2 pages
Conclusion: 0.5 pages
References: 1.5 pages
Total: 14 pages (perfect!)
```

---

## 🔧 GIT/GITHUB ISSUES

### Issue 24: "Push rejected: branch protection"

**Symptom**:
```bash
remote: error: GH006: Protected branch update failed
```

**Cause**: Pushing to wrong branch

**Solution**:
```bash
# Check current branch
git branch

# Should be: claude/parallel-processing-heat-diffusion-*
# Not: main or master

# If on wrong branch, create correct one:
git checkout -b claude/parallel-processing-heat-diffusion-01HXZ5zFn3up11f4tAM8mCJA
```

---

### Issue 25: "Git: Large files rejected"

**Symptom**:
```bash
remote: error: File too large (limit is 100MB)
```

**Cause**: Trying to commit large datasets

**Solution**:
```bash
# Don't commit large files
# Add to .gitignore:
echo "data/raw/*.csv" >> .gitignore
echo "*.h5" >> .gitignore
echo "*.npy" >> .gitignore

# Remove from staging:
git rm --cached large_file.csv

# Commit .gitignore:
git add .gitignore
git commit -m "Ignore large data files"
```

---

### Issue 26: "Merge conflict in Jupyter notebook"

**Symptom**:
```bash
CONFLICT (content): Merge conflict in notebook.ipynb
```

**Cause**: Notebook JSON structure conflicts

**Solution 1**: Use nbdime
```bash
# Install nbdime
pip install nbdime

# Configure git to use nbdime
nbdime config-git --enable --global

# Resolve conflict
git mergetool --tool=nbdime
```

**Solution 2**: Manual resolution
```bash
# Take one version
git checkout --ours notebook.ipynb

# Or take other version
git checkout --theirs notebook.ipynb

# Then commit
git add notebook.ipynb
git commit -m "Resolved conflict"
```

**Prevention**: Clear outputs before committing
```bash
# Install nbstripout
pip install nbstripout

# Configure
nbstripout --install

# Automatically strips outputs on commit
```

---

## 📤 ASSIGNMENT SUBMISSION ISSUES

### Issue 27: "PDF formatting broken"

**Problem**: Word/Google Docs → PDF conversion looks bad

**Solution**:

**Use built-in PDF export**:
```
Word: File → Save As → PDF
Google Docs: File → Download → PDF
```

**Check before submitting**:
- Open PDF and verify
- Check page numbers
- Verify all images visible
- Test links (if any)

**Common issues**:
- Broken images: Re-insert in original document
- Missing fonts: Use standard fonts (Times New Roman)
- Page breaks: Insert manual page breaks
- Margins: Check margin settings (2.5cm)

---

### Issue 28: "Code zip file too large"

**Problem**: Submission file > 100MB

**Solution**:
```bash
# Don't include:
- data/raw/ (large datasets)
- venv/ (virtual environment)
- __pycache__/ (Python cache)
- .ipynb_checkpoints/ (notebook checkpoints)
- test_*.ipynb (tested notebooks)

# Create clean zip:
zip -r submission.zip \
  code/ \
  notebooks/ \
  report/ \
  presentation/ \
  README.md \
  -x "*.pyc" "*/venv/*" "*/__pycache__/*" "*/data/raw/*"

# Check size:
ls -lh submission.zip
```

---

### Issue 29: "Submission deadline confusion"

**Problem**: When exactly is it due?

**Clarify**:
```
Week 4: Part A Proposal
- Due: End of Week 4 (Friday 11:59 PM)
- Submit to: LMS/Turnitin
- Format: PDF only

Week 11: Part B Implementation + Report
- Due: End of Week 11 (Friday 11:59 PM)
- Submit to: LMS/Turnitin
- Format: PDF + ZIP of code

Week 12-13: Presentation
- Date: Check schedule
- Location: Check announcement
- Duration: 10-15 minutes
```

**Pro Tip**: Submit 1 day early
```
Deadline: Friday 11:59 PM
Your deadline: Thursday 11:59 PM
Buffer: 24 hours for issues
```

---

## 🆘 GETTING HELP

### Where to Get Help

**1. Check Documentation First**:
```
1. Read TROUBLESHOOTING.md (this file)
2. Check MASTER_PLAN.md for guidance
3. Review BEST_PRACTICES.md
4. Look at QUICK_START.md
```

**2. Search Online**:
```
Google: "error message" + "heat diffusion" + "python"
Stack Overflow: tag:python + tag:parallel-processing
GitHub Issues: Similar projects
```

**3. Ask Instructor**:
```
Office hours: Check course schedule
Email: Use course email
Forum: Post on course LMS
```

**4. Team Members** (if group project):
```
Discuss with teammates
Share solutions
Don't share code with other groups!
```

### How to Ask for Help Effectively

**Bad Question**:
```
"My code doesn't work, please help"
```

**Good Question**:
```
"I'm getting 'MemoryError' when running heat diffusion with
grid size 4096×4096. I have 8GB RAM. Here's the error:

[paste error]

I tried:
1. Reducing grid size to 2048 - works but too small
2. Closing other apps - didn't help

My system: Ubuntu 20.04, Python 3.10, 8GB RAM

Question: How can I estimate memory requirements and what's
the largest grid size I can use?"
```

**Include**:
1. Exact error message
2. What you tried
3. Your system specs
4. Specific question

---

## 📋 QUICK REFERENCE CHECKLIST

### Before Running Code:
- [ ] Correct directory?
- [ ] Virtual environment activated?
- [ ] All packages installed?
- [ ] Right Python version? (3.8+)

### Before Benchmarking:
- [ ] Close other applications
- [ ] Use appropriate grid size
- [ ] Run multiple times (5+)
- [ ] CPU not throttling?

### Before Submitting:
- [ ] All tests pass?
- [ ] Code well-documented?
- [ ] PDF formatting correct?
- [ ] File size < limit?
- [ ] Submitted to right place?

### Before Presentation:
- [ ] Demo tested 5+ times?
- [ ] Backup screenshots ready?
- [ ] Slides complete?
- [ ] Within time limit? (10-15 min)
- [ ] Prepared for Q&A?

---

## 🎯 MOST COMMON ISSUES (Top 5)

### 1. **Multiprocessing not working**
→ Run as script (not Jupyter)
→ Use `if __name__ == '__main__'`

### 2. **Poor parallel speedup**
→ Grid too small (use 1024+)
→ This is normal (Amdahl's Law)

### 3. **Tests failing**
→ Check boundary conditions
→ Reduce problem size for tests

### 4. **Plots not showing**
→ Set backend: `matplotlib.use('TkAgg')`
→ Or save to file: `plt.savefig()`

### 5. **Inconsistent benchmarks**
→ Close other apps
→ Run 5-10 times, take median
→ Let CPU cool between runs

---

## 💡 PREVENTION TIPS

**Prevent Issues Before They Happen**:

1. **Use Version Control**
   ```bash
   git commit often
   git push regularly
   # Never lose work!
   ```

2. **Test Early and Often**
   ```bash
   # After every major change:
   python test_heat_diffusion.py
   ```

3. **Document as You Go**
   ```python
   # Write comments while coding
   # Don't leave for later!
   ```

4. **Start Early**
   ```
   Don't wait until deadline
   Buffer time for issues
   ```

5. **Keep Backups**
   ```bash
   # Multiple backups:
   - Git repository
   - Local copy
   - Cloud storage (Google Drive/Dropbox)
   ```

---

## 📞 EMERGENCY CONTACTS

**Day Before Deadline Issues**:
1. Try fixes in this guide
2. Ask in course forum (others may have same issue)
3. Email instructor with specific error
4. Submit what you have (partial credit > zero)

**Presentation Day Issues**:
1. Have backup screenshots
2. Have backup video
3. Be ready to explain without demo
4. Stay calm, explain the issue professionally

---

## ✅ FINAL CHECKLIST

Before considering issue "solved":

- [ ] Issue completely resolved?
- [ ] Tested multiple times?
- [ ] Documented what fixed it?
- [ ] Prevented from happening again?
- [ ] Shared solution with team? (if applicable)

---

**Remember**: Everyone encounters issues! The difference between success and failure is how you handle them. Use this guide, stay calm, and work through problems systematically.

**Good luck with your assignment!** 🚀

---

**Created**: November 23, 2025
**Coverage**: 29 common issues with solutions
**Last Updated**: November 23, 2025

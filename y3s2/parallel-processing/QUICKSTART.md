# Quick Start Guide

## BMCS3003: Distributed Systems and Parallel Computing

### 🚀 Get Started in 5 Minutes

#### Step 1: Verify Python Installation

```bash
python --version
# Should show Python 3.8 or higher
```

If you don't have Python, download from [python.org](https://www.python.org/downloads/)

---

#### Step 2: Navigate to the Course Directory

```bash
cd y3s2/parallel-processing
```

---

#### Step 3: Create Virtual Environment

**Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

---

#### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages. ⏱️ Takes ~2-3 minutes.

---

#### Step 5: Launch Jupyter Notebook

```bash
jupyter notebook
```

Your browser will open automatically at `http://localhost:8888`

---

#### Step 6: Start Learning!

1. Navigate to the `notebooks/` folder
2. Open `00_setup_introduction.ipynb`
3. Run all cells to verify your setup
4. Continue to `01_introduction_distributed_systems.ipynb`

---

## 🔧 Troubleshooting

### Problem: "python: command not found"

**Solution**: Try `python3` instead of `python`, or add Python to your PATH.

### Problem: "pip: command not found"

**Solution**: Try `python -m pip` instead of `pip`.

### Problem: Jupyter won't open

**Solution**:
```bash
# Manually specify browser
jupyter notebook --browser=chrome
# Or
jupyter notebook --browser=firefox
```

### Problem: Import errors in notebooks

**Solution**: Make sure virtual environment is activated (you should see `(venv)` in prompt).
```bash
# Reactivate if needed
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

---

## ✅ Verify Your Setup

Run this in a Jupyter notebook cell:

```python
import sys
import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
import psutil

print(f"✓ Python {sys.version}")
print(f"✓ CPU Cores: {multiprocessing.cpu_count()}")
print(f"✓ NumPy {np.__version__}")
print(f"✓ Matplotlib available")
print(f"✓ psutil available")
print("\n🎉 Your environment is ready!")
```

If all lines show checkmarks, you're good to go!

---

## 📚 Learning Path

Follow this order:

1. **Module 00** (45 min): Setup and Introduction
2. **Module 01** (90 min): Distributed Systems Basics
3. **Module 02** (90 min): Architectures and Transparency *(coming soon)*
4. **Module 03** (75 min): Real-time Systems *(coming soon)*
5. **Module 04** (75 min): Clock Synchronization *(coming soon)*
6. **Module 05** (60 min): Distributed Operating Systems *(coming soon)*

---

## 💡 Tips for Success

### Before Each Study Session:
1. ✅ Activate virtual environment
2. ✅ Open Jupyter Notebook
3. ✅ Have lecture PDFs handy in `LectureNotes/`
4. ✅ Keep a notepad for questions

### During Study:
- 📝 Take notes in markdown cells
- 🔬 Experiment with code examples
- 🎯 Complete ALL exercises
- 📊 Create your own visualizations
- ❓ Note down questions for instructor

### After Each Module:
- ✅ Review summary section
- ✅ Explain concepts in your own words
- ✅ Complete exercises without looking at solutions
- ✅ Preview next module's topics

---

## 🆘 Need Help?

1. **Technical Issues**: Check the Troubleshooting section above
2. **Concept Questions**: Review lecture PDFs in `LectureNotes/`
3. **Stuck on Exercise**: Try for 20 minutes, then check hints
4. **Still Stuck**: Email instructor at yiqi@tarc.edu.my

---

## 🎯 Assessment Reminders

- **Midterm** (40%): Week 7/8 - Covers Modules 00-05
- **Assignment** (60%): Due Week 12, Presented Week 13-14
- **Final Exam**: Comprehensive, review all modules

---

## 📖 Recommended Study Schedule

### Week 1-2:
- Complete Module 00
- Start Module 01
- Review Chapter 00-01 PDFs

### Week 3-4:
- Complete Module 01
- Start Module 02 (when available)
- Review Chapter 02 PDF

### Week 5-6:
- Complete Modules 02-05
- Practice exercises
- Prepare for midterm

### Week 7-8:
- **MIDTERM TEST**
- Review feedback

### Week 9-12:
- Work on assignment
- Complete advanced modules (06+)
- Prepare presentation

### Week 13-14:
- Present assignment
- Final review

---

## 🚦 Quick Commands Reference

```bash
# Activate environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Deactivate environment
deactivate

# Update packages
pip install --upgrade -r requirements.txt

# Launch Jupyter
jupyter notebook

# Run a specific notebook
jupyter nbconvert --execute notebook.ipynb

# Check installed packages
pip list
```

---

## ✨ You're All Set!

Now open `notebooks/00_setup_introduction.ipynb` and start your journey into distributed systems and parallel computing!

**Happy Learning! 🚀**

---

**Questions?** Contact: yiqi@tarc.edu.my

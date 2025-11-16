# Testing Guide for Python Fundamentals

This guide will help you test and verify that all notebooks are working correctly.

## ✅ Validation Results

**Last Test Date**: 2025-01-14

**Status**: ✅ ALL TESTS PASSED

- Total Notebooks: **11**
- Passed: **11** ✅
- Failed: **0**
- Skipped: **0**

### Individual Notebook Stats

| Module | Notebook | Code Cells | Markdown Cells | Total | Status |
|--------|----------|------------|----------------|-------|--------|
| 00 | Setup and Introduction | 22 | 23 | 45 | ✅ PASS |
| 01 | Variables and Data Types | 35 | 29 | 64 | ✅ PASS |
| 02 | Operators and Expressions | 17 | 17 | 34 | ✅ PASS |
| 03 | Control Flow | 30 | 23 | 53 | ✅ PASS |
| 04 | Functions | 22 | 24 | 46 | ✅ PASS |
| 05 | Data Structures | 30 | 26 | 56 | ✅ PASS |
| 06 | File Handling | 25 | 16 | 41 | ✅ PASS |
| 07 | Error Handling | 19 | 22 | 41 | ✅ PASS |
| 08 | Modules and Packages | 22 | 21 | 43 | ✅ PASS |
| 09 | OOP Basics | 14 | 21 | 35 | ✅ PASS |
| 10 | Final Project | 8 | 14 | 22 | ✅ PASS |

**Total Code Examples**: 244
**Total Documentation Cells**: 236
**Grand Total Cells**: 480

---

## 🧪 How to Run Tests

### Method 1: Quick Syntax Validation (Recommended)

This checks if all notebooks have valid structure and can be opened:

```bash
cd projects/python-fundamentals
python scripts/validate_notebooks.py
```

**Expected Output**:
```
============================================================
PYTHON FUNDAMENTALS - NOTEBOOK VALIDATION
============================================================
Found 11 notebooks to validate
...
🎉 ALL TESTS PASSED!
```

### Method 2: Full Execution Test (Slower)

This actually runs all code cells to ensure they execute without errors:

```bash
cd projects/python-fundamentals
python scripts/validate_notebooks.py --execute
```

⚠️ **Note**: This will take longer (5-10 minutes) as it executes every notebook.

### Method 3: Test Specific Modules

Skip certain modules if needed:

```bash
# Skip module 10 (Final Project)
python scripts/validate_notebooks.py --skip 10

# Skip multiple modules
python scripts/validate_notebooks.py --skip 6 7 10
```

---

## 🚀 Manual Testing in Jupyter

### 1. Start Jupyter Notebook

```bash
cd projects/python-fundamentals/notebooks
jupyter notebook
```

Your browser will open automatically at `http://localhost:8888`

### 2. Test a Specific Notebook

1. Click on any notebook (e.g., `00_setup_and_introduction.ipynb`)
2. Click **"Kernel"** → **"Restart & Run All"**
3. Wait for all cells to execute
4. Check for any errors (red text or exceptions)

### 3. Expected Behavior

✅ **Good Signs**:
- All cells execute successfully
- Code examples produce expected output
- No error messages (except in error handling examples)
- Numbers appear next to executed cells: `[1]`, `[2]`, etc.

❌ **Problems to Look For**:
- Red error messages (Exception, TypeError, etc.)
- Cells that never finish executing
- Missing `In [#]` or `Out[#]` indicators
- Warnings about missing modules

---

## 🔧 Troubleshooting

### Problem: ModuleNotFoundError

**Symptom**: `ModuleNotFoundError: No module named 'xyz'`

**Solution**:
```bash
pip install xyz
```

Common missing modules:
```bash
pip install jupyter notebook ipykernel ipywidgets
```

### Problem: Jupyter Won't Start

**Solution**:
```bash
# Try upgrading jupyter
pip install --upgrade jupyter

# Or reinstall
pip uninstall jupyter
pip install jupyter
```

### Problem: Kernel Keeps Dying

**Possible Causes**:
1. Memory issues (too many notebooks open)
2. Python version compatibility
3. Corrupted environment

**Solutions**:
```bash
# Restart Jupyter
# Close other notebooks
# Try in a fresh virtual environment

python -m venv test_env
test_env\Scripts\activate  # Windows
source test_env/bin/activate  # Mac/Linux
pip install jupyter
```

### Problem: Cannot Import Sample Files

**Symptom**: `FileNotFoundError` when running file handling examples

**Solution**: Make sure you're running notebooks from the `notebooks/` directory:
```bash
cd projects/python-fundamentals/notebooks
jupyter notebook
```

The notebooks use relative paths like `../data/sample_files/sample.txt`

### Problem: Encoding Errors (Windows)

**Symptom**: `UnicodeEncodeError` or garbled text

**Solution**: Set environment variable before starting Jupyter:
```bash
# Windows Command Prompt
set PYTHONIOENCODING=utf-8
jupyter notebook

# Windows PowerShell
$env:PYTHONIOENCODING="utf-8"
jupyter notebook
```

---

## 📊 What Gets Tested

### Syntax Validation
- ✅ Valid JSON structure
- ✅ Required notebook fields (cells, metadata)
- ✅ Cell type validation
- ✅ No corrupted data

### Execution Testing (with --execute flag)
- ✅ All code cells run without errors
- ✅ Imports work correctly
- ✅ File paths are correct
- ✅ Examples produce expected output

### Code Quality Checks
- ✅ Clear comments and documentation
- ✅ Consistent code style
- ✅ Working examples
- ✅ Exercise templates

---

## 🎯 Testing Checklist

Before sharing or using these notebooks, verify:

- [ ] All notebooks open in Jupyter without errors
- [ ] Module 00 (Setup) runs completely
- [ ] Sample data files exist in `data/sample_files/`
- [ ] File paths work correctly
- [ ] No broken imports
- [ ] Exercise cells have TODO comments
- [ ] Solutions are in `docs/exercise_solutions.md`
- [ ] README.md instructions are accurate

---

## 🐛 Reporting Issues

If you find any problems:

1. **Note the module number and cell number**
   - Example: "Module 05, Cell 12 throws TypeError"

2. **Copy the error message**
   - Include the full stack trace

3. **Check your environment**
   - Python version: `python --version`
   - Jupyter version: `jupyter --version`
   - Operating system

4. **Try in a clean environment**
   - Create a new virtual environment
   - Install only required packages
   - Test again

---

## 📈 Performance Benchmarks

Approximate execution times on standard hardware:

| Module | Execution Time | Notes |
|--------|---------------|-------|
| 00 | < 5 seconds | Simple print statements |
| 01 | < 5 seconds | Variable operations |
| 02 | < 5 seconds | Calculations |
| 03 | < 10 seconds | Loops and iterations |
| 04 | < 5 seconds | Function definitions |
| 05 | < 10 seconds | Data structure operations |
| 06 | < 10 seconds | File I/O operations |
| 07 | < 5 seconds | Exception handling |
| 08 | < 15 seconds | Module imports and tests |
| 09 | < 5 seconds | Class definitions |
| 10 | N/A | Template only |

**Total for all modules**: ~1-2 minutes

---

## ✨ Continuous Testing

### Before Each Session

Quick check:
```bash
python scripts/validate_notebooks.py
```

### After Making Changes

Full test:
```bash
python scripts/validate_notebooks.py --execute
```

### Weekly Maintenance

1. Update all packages:
   ```bash
   pip install --upgrade jupyter notebook ipykernel
   ```

2. Run full validation:
   ```bash
   python scripts/validate_notebooks.py --execute
   ```

3. Check for deprecated features or warnings

---

## 🎓 For Educators

If you're using these notebooks for teaching:

### Pre-Class Checklist
- [ ] Run validation script
- [ ] Test on target Python version
- [ ] Verify all examples work
- [ ] Check exercise difficulty
- [ ] Review solutions document

### During Class
- Monitor for common student issues
- Note which cells cause confusion
- Collect feedback on difficulty

### Post-Class
- Update notebooks based on feedback
- Fix any issues found
- Re-run validation

---

## 📝 Version History

### v1.0.0 (2025-01-14)
- Initial release
- 11 complete modules
- 244 code examples
- All tests passing

---

## 🆘 Getting Help

If you encounter issues:

1. **Check this testing guide first**
2. **Review the README.md**
3. **Look at exercise solutions**: `docs/exercise_solutions.md`
4. **Search for similar issues** online
5. **Ask in Python communities**:
   - [r/learnpython](https://reddit.com/r/learnpython)
   - [Python Discord](https://pythondiscord.com/)
   - [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

---

**Last Updated**: 2025-01-14
**Tested With**: Python 3.13.5, Jupyter 7.4.7

---
skill_name: quality-checker
description: Code formatting, style enforcement, and quality standards for educational notebooks
version: 1.0.0
author: Educational Notebook System
tags: [quality, formatting, linting, code-style, best-practices]
activation_keywords: [check quality, format code, lint code, code style, quality standards]
dependencies: [black, flake8, isort, nbqa]
---

# Quality Checker Skill

## Purpose

Enforces code quality, formatting standards, and best practices in educational Jupyter notebooks through automated checking and formatting tools.

## When to Use This Skill

Activate when you need to:
- Format code in notebooks to PEP 8 standards
- Check code style and catch common errors
- Organize imports correctly
- Enforce educational code standards
- Prepare notebooks for publication
- Ensure consistent code quality across projects

## Quality Tools

### 1. Black - Code Formatting

**Purpose**: Automatic code formatting (the uncompromising formatter)

**Usage**:
```bash
# Format Python files
black script.py

# Format notebooks (requires nbqa)
nbqa black notebook.ipynb

# Check without modifying
black --check notebook.ipynb

# Format all notebooks in directory
nbqa black notebooks/
```

**Educational Configuration**:
- Line length: 88 characters (Black default, relaxed from strict 79)
- Allows longer lines for clarity in teaching code

### 2. Flake8 - Linting

**Purpose**: Style guide enforcement and error detection

**Usage**:
```bash
# Check single notebook
nbqa flake8 notebook.ipynb

# Check all notebooks
nbqa flake8 notebooks/

# With specific rules
flake8 --max-line-length=100 --ignore=E501,W503 notebook.py
```

**Educational Rules** (in `.flake8`):
```ini
[flake8]
max-line-length = 100
extend-ignore =
    E501,  # Line too long (acceptable for teaching)
    W503,  # Line break before binary operator (clearer for beginners)
    E402,  # Module level import not at top (demos often need context first)
exclude =
    .git,
    __pycache__,
    .ipynb_checkpoints,
    venv,
per-file-ignores =
    notebooks/*:F401  # Allow unused imports in demo notebooks
```

### 3. isort - Import Organization

**Purpose**: Automatically organize and format imports

**Usage**:
```bash
# Sort imports in notebook
nbqa isort notebook.ipynb

# Check without modifying
nbqa isort --check notebook.ipynb

# Sort all notebooks
nbqa isort notebooks/
```

**Import Order** (automatic):
1. Standard library imports
2. Third-party library imports
3. Local application imports

### 4. nbqa - Apply Tools to Notebooks

**Purpose**: Wrapper to run quality tools on Jupyter notebooks

**Usage**:
```bash
# Format with black
nbqa black notebook.ipynb

# Lint with flake8
nbqa flake8 notebook.ipynb

# Sort imports
nbqa isort notebook.ipynb

# Run multiple tools
nbqa black notebook.ipynb && nbqa isort notebook.ipynb && nbqa flake8 notebook.ipynb
```

## Educational Code Standards

### Variable Naming

**Good Examples**:
```python
# Descriptive and clear
customer_purchase_history = load_data('customers.csv')
average_order_value = calculate_mean(purchase_amounts)
high_value_customers = filter_by_threshold(customers, threshold=1000)

# Using conventional abbreviations
df = pd.read_csv('data.csv')  # 'df' is universally understood for DataFrame
fig, ax = plt.subplots()      # Standard matplotlib convention
```

**Bad Examples**:
```python
# Too cryptic
cph = load_data('customers.csv')  # What is 'cph'?
aov = calc_mean(pa)               # Too many abbreviations

# Too generic
data2 = data1.copy()  # What makes it 'data2'?
temp = filter(stuff)  # Meaningless names
```

### Comment Quality

**Good Comments** (explain WHY):
```python
# Use log transformation to handle right-skewed distribution
# This stabilizes variance and makes data more normal
log_sales = np.log1p(sales_data['amount'])

# StandardScaler over MinMaxScaler: preserves outlier information
# Critical for detecting anomalous transactions
scaler = StandardScaler()
```

**Bad Comments** (state the obvious):
```python
# Create a variable
x = 5

# Loop through the data
for item in data:
    process(item)
```

### Code Organization

**Well-Organized Cell**:
```python
# 1. Load data
sales_data = pd.read_csv('data/sales.csv')

# 2. Validate loading
print(f"Loaded {len(sales_data)} records")
assert len(sales_data) > 0, "No data loaded"

# 3. Display sample
sales_data.head()
```

**Poorly-Organized Cell**:
```python
sales_data = pd.read_csv('data/sales.csv')
x = sales_data['amount'].mean()
print("Average:", x)
y = sales_data[sales_data['status'] == 'active']
# Too many unrelated operations in one cell
```

## Quality Checklist

### Code Quality (Target: ≥85%)
- [ ] Variable names are descriptive
- [ ] Comments explain WHY, not WHAT
- [ ] No magic numbers (use named constants)
- [ ] Proper error handling
- [ ] Functions have docstrings
- [ ] Code formatted with Black
- [ ] Imports organized with isort
- [ ] No flake8 warnings (except approved exceptions)

### Educational Value (Target: ≥80%)
- [ ] Code complexity appropriate for level
- [ ] Demonstrates best practices
- [ ] Avoids clever but confusing patterns
- [ ] Clear learning progression
- [ ] Good examples to learn from

## Common Issues and Fixes

### Issue: Long Lines

**Problem**:
```python
# Line too long
result = data[(data['category'] == 'electronics') & (data['price'] > 100) & (data['status'] == 'active')]
```

**Fix**:
```python
# Break into logical chunks
is_electronics = data['category'] == 'electronics'
is_expensive = data['price'] > 100
is_active = data['status'] == 'active'

result = data[is_electronics & is_expensive & is_active]
```

### Issue: Disorganized Imports

**Problem**:
```python
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import numpy as np
import os
```

**Fix** (isort automatically fixes):
```python
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

### Issue: Unclear Variable Names

**Problem**:
```python
df2 = df1[df1['x'] > 100]
df3 = df2.groupby('y').mean()
```

**Fix**:
```python
high_value_sales = all_sales[all_sales['amount'] > 100]
average_by_category = high_value_sales.groupby('category').mean()
```

## Automation with Pre-commit

Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
      - id: black-jupyter

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: ["--config=.flake8"]

  - repo: https://github.com/nbQA-dev/nbQA
    rev: 1.7.1
    hooks:
      - id: nbqa-black
      - id: nbqa-isort
      - id: nbqa-flake8
```

Install and run:
```bash
# Install pre-commit
pip install pre-commit

# Install git hooks
pre-commit install

# Run on all files
pre-commit run --all-files
```

## Using This Skill

### Quick Quality Check
```bash
# Format code
nbqa black notebook.ipynb

# Organize imports
nbqa isort notebook.ipynb

# Check style
nbqa flake8 notebook.ipynb
```

### Full Quality Pass
```bash
# Run all tools in sequence
nbqa black notebooks/ && \
nbqa isort notebooks/ && \
nbqa flake8 notebooks/
```

### Quality Report
```bash
# Check what would change (without modifying)
nbqa black --check notebooks/
nbqa isort --check notebooks/
nbqa flake8 notebooks/ > quality_report.txt
```

## Success Criteria

Quality-checked notebook:
- ✅ Code formatted consistently (Black)
- ✅ Imports organized correctly (isort)
- ✅ No style violations (flake8 with educational exceptions)
- ✅ Descriptive variable names
- ✅ Meaningful comments
- ✅ Appropriate code complexity for level
- ✅ Ready for learners to study and emulate

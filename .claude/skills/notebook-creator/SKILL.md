---
skill_name: notebook-creator
description: Creates educational Jupyter notebooks with proper structure, progressive scaffolding, and pedagogical best practices
version: 1.0.0
author: Educational Notebook System
tags: [education, jupyter, notebooks, pedagogy, scaffolding]
activation_keywords: [create notebook, jupyter notebook, educational content, learning module, teaching material]
dependencies: [jupyter, pandas, numpy, matplotlib]
---

# Notebook Creator Skill

## Purpose

This skill provides comprehensive guidelines, templates, and patterns for creating high-quality educational Jupyter notebooks that follow proven pedagogical principles and technical best practices.

## When to Use This Skill

Activate this skill when you need to:
- Create new educational Jupyter notebooks from scratch
- Restructure existing notebooks to follow best practices
- Design learning progressions and exercise sequences
- Ensure notebooks follow consistent structural standards
- Implement progressive scaffolding patterns
- Create notebook templates for specific difficulty levels

## Structural Standards

### Notebook Organization

Every educational notebook should follow this structure:

1. **Title Cell** (Markdown)
   - Clear, descriptive title
   - Module number if part of sequence

2. **Metadata Cell** (Markdown)
   - Difficulty level (⭐/⭐⭐/⭐⭐⭐)
   - Estimated completion time
   - Prerequisites with links
   - Learning objectives

3. **Setup Section**
   - Import statements
   - Configuration (matplotlib inline, random seeds)
   - Helper function definitions

4. **Content Sections**
   - Concept introduction (markdown)
   - Code demonstration
   - Explanation of results
   - Repeat for each concept

5. **Exercise Section**
   - Progressive exercises (3+ per major concept)
   - Clear instructions and success criteria
   - Solution validation cells

6. **Summary Section**
   - Key concepts recap
   - What's next
   - Additional resources

### Cell Length Limits

- **Code cells**: Maximum 15 lines for readability
- **Markdown cells**: 50-200 lines for explanatory text
- Break longer operations into multiple cells with intermediate outputs

### File Naming Convention

```
NN_descriptive_topic_name.ipynb

Examples:
00_setup_introduction.ipynb
01_data_loading_basics.ipynb
02_filtering_and_selection.ipynb
10_final_project.ipynb
```

## Progressive Scaffolding Patterns

### Beginner Level (⭐): "Shift-Enter" Demonstration Mode

Provide complete, working code with extensive explanation:

```markdown
## Loading Data

Let's load our sales data using pandas. Pandas is a powerful library for working
with tabular data (think of it like Excel, but with code!).

```python
# Import the pandas library and give it the short name 'pd'
# This is standard practice - everyone uses 'pd' for pandas
import pandas as pd

# Load the CSV file from our data folder
# CSV = "Comma Separated Values" - a simple data format
sales_data = pd.read_csv('data/sample/sales.csv')

# Let's see what we loaded!
print(f"Loaded {len(sales_data)} rows of sales data")
print(f"Columns: {list(sales_data.columns)}")

# Display the first few rows to get a sense of the data
sales_data.head()
```

Notice how we:
1. Imported pandas with a short name for convenience
2. Loaded the data from a CSV file
3. Checked what we loaded before proceeding
4. Displayed the first rows to verify the data structure

This is a best practice workflow you should follow whenever loading data!
```

**Characteristics**:
- Nearly every line has a comment
- Explains WHY, not just WHAT
- Shows intermediate results
- Uses encouraging language
- Breaks operations into smallest steps

### Intermediate Level (⭐⭐): "Fill-in-the-Blanks" Mode

Provide structure with student completion:

```markdown
## Exercise: Filter High-Value Sales

You've learned about boolean indexing. Now apply it to find high-value sales.

**Your task**: Complete the code below to find all sales over $1000.

```python
# TODO: Create a boolean mask for sales over $1000
# Hint: Use the 'amount' column and the > operator
high_value_mask = sales_data[___] ___ ___

# TODO: Apply the mask to filter the data
high_value_sales = sales_data[___]

# Check your work
print(f"Found {len(high_value_sales)} high-value sales")
assert len(high_value_sales) > 0, "Check your filter condition"
```

**Expected output**: Around 150 high-value sales in the dataset

**Solution**:
```python
high_value_mask = sales_data['amount'] > 1000
high_value_sales = sales_data[high_value_mask]
```
```

**Characteristics**:
- Clear TODO markers
- Hints about approach
- Validation cells
- Solutions available (in separate file or later section)
- Assumes basic concept understanding

### Advanced Level (⭐⭐⭐): "Now-You-Try" Mode

Provide problem statement with minimal scaffolding:

```markdown
## Challenge: Optimize Query Performance

**Problem**: The current data filtering approach using pandas boolean indexing works
well for our sample dataset (10K rows), but production data has 10M+ rows.

**Your task**: Implement an optimized filtering strategy that:
1. Handles datasets too large for memory
2. Achieves <2 second query time for typical filters
3. Supports multiple filter conditions efficiently

**Constraints**:
- Data is stored in SQLite database (see `data/production.db`)
- Cannot load entire dataset into memory
- Must support these filter operations: >, <, ==, BETWEEN, IN

**Approach considerations**:
- SQL queries with appropriate indexes?
- Chunked processing with pandas?
- Dask or Vaex for out-of-core computing?
- Query optimization vs. data structure optimization?

**Deliverable**:
- Implementation with performance benchmarks
- Comparison of approaches tried
- Justification of final choice

**Evaluation**: Performance on provided test queries in `tests/query_benchmark.py`
```

**Characteristics**:
- Real-world problem framing
- Multiple valid approaches
- Requires design decisions
- No step-by-step guidance
- Focus on methodology and trade-offs

## Content Patterns

### Concept Introduction Template

```markdown
## {Concept Name}

### What is it?
{Clear, simple definition}

### Why do we need it?
{Practical motivation - what problem does it solve?}

### How does it work?
{Explanation with visual aid if possible}

### Example: {Concrete scenario}
{Code demonstration with real data}

### Common Mistakes
{Pitfalls to avoid with examples}

### Practice
{Exercise applying the concept}
```

### Code Demonstration Pattern

```python
# 1. Show the problem/motivation
# 2. Demonstrate the solution
# 3. Explain what happened
# 4. Show the results
```

Example:
```python
# Problem: Our dates are stored as strings, not datetime objects
print(type(sales_data['date'][0]))  # Shows: <class 'str'>
print(sales_data['date'].head())

# Solution: Convert to datetime
sales_data['date'] = pd.to_datetime(sales_data['date'])

# Verify the conversion worked
print(type(sales_data['date'][0]))  # Now shows: <class 'Timestamp'>

# Result: Now we can do date operations!
sales_data['month'] = sales_data['date'].dt.month
sales_data['year'] = sales_data['date'].dt.year
sales_data[['date', 'month', 'year']].head()
```

### Exercise Design Pattern

**Structure**:
1. **Title**: Clear, specific task description
2. **Objective**: What skill is being practiced
3. **Task**: Step-by-step instructions
4. **Starter Code**: Template to complete
5. **Expected Output**: What success looks like
6. **Hints**: Helpful guidance without giving away answer
7. **Validation**: Assert statements or checks
8. **Solution**: Complete answer (in student vs. instructor versions)

**Difficulty Progression**:
- Exercise 1: Apply exactly what was just demonstrated
- Exercise 2: Combine concept with previous learning
- Exercise 3: Extension requiring slight creativity

## Quality Standards

### Markdown-to-Code Ratio

Maintain **minimum 30% markdown content** (measured by character count).

Calculate:
```python
markdown_chars = sum(len(''.join(cell['source']))
                    for cell in notebook['cells']
                    if cell['cell_type'] == 'markdown')
code_chars = sum(len(''.join(cell['source']))
                for cell in notebook['cells']
                if cell['cell_type'] == 'code')
ratio = markdown_chars / (markdown_chars + code_chars)
# ratio should be >= 0.30
```

### Exercise Requirements

- **Minimum**: 3 exercises per major concept
- **Coverage**: Each learning objective has associated practice
- **Validation**: Every exercise includes success criteria or assertion checks
- **Progression**: Exercises increase in difficulty

### Execution Requirements

- **"Restart and Run All" test**: Must pass without errors
- **No hidden state**: Cells must execute top-to-bottom in sequence
- **Reproducibility**: Random seeds set, outputs deterministic
- **Reasonable runtime**: Complete execution under 5 minutes (unless noted)

## Templates

Templates are provided in the `templates/` directory:

- `beginner_template.ipynb`: Verbose, extensively commented starter
- `intermediate_template.ipynb`: Balanced explanation and practice
- `advanced_template.ipynb`: Challenge-based, minimal scaffolding
- `exercise_template.md`: Standard exercise format
- `metadata_template.md`: Learning objectives and prerequisites

Load templates with:
```python
import shutil
shutil.copy('.claude/skills/notebook-creator/templates/beginner_template.ipynb',
            'notebooks/new_notebook.ipynb')
```

## Data Handling Best Practices

### File Paths
- **Always use relative paths**: `data/sample/file.csv`
- **Never use absolute paths**: ❌ `C:/Users/Name/project/data/file.csv`
- **Verify existence before loading**:
  ```python
  from pathlib import Path
  data_file = Path('data/sample/sales.csv')
  if not data_file.exists():
      raise FileNotFoundError(f"Data file not found: {data_file}")
  ```

### Data Organization
```
project/
├── data/
│   ├── raw/           # Original, immutable data
│   ├── processed/     # Cleaned, ready for analysis
│   ├── sample/        # Small datasets for examples (< 10 MB)
│   └── external/      # Third-party data with README attribution
```

### Data Loading Pattern
```python
# 1. Load
data = pd.read_csv('data/sample/sales.csv')

# 2. Validate
print(f"Loaded {len(data)} rows, {len(data.columns)} columns")
print(f"Columns: {list(data.columns)}")
assert len(data) > 0, "Data file is empty!"

# 3. Display
data.head()

# 4. Check types
data.dtypes
```

## Common Mistakes to Avoid

### ❌ Don't Do This

```python
# Unexplained magic numbers
data[data['age'] > 18]

# No intermediate outputs
result = data.groupby('category')['amount'].sum().sort_values(ascending=False)

# Meaningless variable names
df2 = df1[df1['status'] == 'active']
df3 = df2.groupby('type').mean()

# Assuming code is self-explanatory (it rarely is for learners)
x = np.log1p(y)
```

### ✅ Do This Instead

```python
# Explain the threshold
ADULT_AGE_THRESHOLD = 18  # Legal adult age
adults = data[data['age'] > ADULT_AGE_THRESHOLD]

# Show intermediate steps
category_totals = data.groupby('category')['amount'].sum()
sorted_totals = category_totals.sort_values(ascending=False)
print("Top categories by sales:")
sorted_totals.head()

# Use descriptive names
active_customers = all_customers[all_customers['status'] == 'active']
average_by_type = active_customers.groupby('customer_type').mean()

# Explain transformations
# Apply log transformation to handle right-skewed distribution
# Adding 1 before log prevents issues with zero values
log_transformed_amounts = np.log1p(sales_amounts)
```

## Reproducibility Checklist

- [ ] Random seeds set at notebook start (`np.random.seed(42)`)
- [ ] All required libraries imported in setup section
- [ ] Data files referenced with relative paths
- [ ] No interactive widgets that block execution
- [ ] No user input required (`input()` calls)
- [ ] All cells execute in order without error
- [ ] Outputs are deterministic (or non-determinism documented)
- [ ] Environment dependencies documented in requirements.txt

## Accessibility Considerations

- [ ] Proper heading hierarchy (H1 → H2 → H3, no skipping)
- [ ] Descriptive link text (not "click here")
- [ ] Alt text for images (though minimal in educational notebooks)
- [ ] Color-blind friendly visualizations (use colorblind-safe palettes)
- [ ] Code can be understood without seeing plots (describe key insights)

## Using This Skill

When this skill is activated, you have access to:

1. **Structural templates** in `templates/` directory
2. **Best practice patterns** documented above
3. **Quality checklists** for validation
4. **Example notebooks** showing proper implementation

Follow the patterns, maintain the standards, and create notebooks that learners love to work through!

## Success Metrics

A well-created notebook:
- ✅ Executes top-to-bottom without errors
- ✅ Maintains ≥30% markdown ratio
- ✅ Includes 3+ exercises per concept
- ✅ Has clear learning objectives and prerequisites
- ✅ Uses descriptive variable names throughout
- ✅ Explains WHY, not just WHAT
- ✅ Increases difficulty progressively
- ✅ Provides validation for exercises
- ✅ Runs in <5 minutes (or documents longer runtime)
- ✅ Receives positive learner feedback

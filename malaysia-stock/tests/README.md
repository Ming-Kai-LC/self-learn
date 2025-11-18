# Malaysia Stock Project - Testing Framework

This directory contains testing and validation tools for the Malaysian Stock Technical Analysis educational notebooks.

## Overview

The testing framework validates that notebooks meet educational quality standards:
- ✅ Proper structure (metadata, learning objectives)
- ✅ Sufficient explanatory content (≥30% markdown ratio)
- ✅ Adequate practice exercises (≥3 per notebook)
- ✅ Executable without errors (optional validation)

## Quick Start

### Basic Validation

Test all notebooks for structure and content quality:

```bash
python test_notebooks.py
```

### Test Specific Notebook

Test a single notebook:

```bash
python test_notebooks.py --notebook 00
python test_notebooks.py --notebook 05
```

### Full Execution Test

Validate that notebooks actually run without errors:

```bash
python test_notebooks.py --execute
```

**⚠️ Warning**: Execution tests require:
- All dependencies installed (`pip install -r requirements.txt`)
- Active internet connection (for yfinance data downloads)
- May take 5-10 minutes to complete

## Quality Standards

### Minimum Requirements

Each notebook must have:

| Metric | Minimum | Recommended | Notes |
|--------|---------|-------------|-------|
| **Markdown Ratio** | 30% | 40%+ | Explanatory content vs code |
| **Exercise Count** | 3 | 4+ | Practice exercises |
| **Learning Objectives** | Required | - | Clear, measurable goals |
| **Metadata** | Required | - | Difficulty, time, prerequisites |

### Current Project Status

As of last validation:

```
Total Notebooks: 11
✅ Passed: 11
❌ Failed: 0

Average Markdown Ratio: 41.0%
Average Exercise Count: 4.3
```

All notebooks meet or exceed quality standards! 🎉

## Testing Tools

### `test_notebooks.py`

Main validation script with these capabilities:

**Quality Checks**:
- Markdown content ratio
- Exercise count
- Learning objectives presence
- Metadata completeness (difficulty, time, prerequisites)
- Cell counts (code vs markdown)

**Usage Options**:
```bash
# Test all notebooks
python test_notebooks.py

# Test specific notebook
python test_notebooks.py --notebook 03

# Execute notebooks (full validation)
python test_notebooks.py --execute

# Quiet mode (less verbose)
python test_notebooks.py --verbose=False
```

**Exit Codes**:
- `0`: All tests passed
- `1`: One or more tests failed

## Test Output Explained

### Sample Output

```
✅ PASS 00_setup_introduction
======================================================================
  Markdown Ratio: 60.1%
  Exercise Count: 4
  Total Cells: 28 (Code: 13, Markdown: 15)
  Learning Objectives: Yes
  Metadata Complete: Yes
```

### Status Indicators

- ✅ **PASS**: Notebook meets all minimum requirements
- ❌ **FAIL**: Notebook missing required elements
- ⚠️  **Warnings**: Below recommended thresholds (not failures)

### Common Warnings

```
⚠️  Warnings:
   • Markdown ratio 27.3% is below recommended 30%
```

This is informational - the notebook still passes but could use more explanatory content.

## Adding New Tests

To add custom validation rules, modify `test_notebooks.py`:

```python
def validate_notebook(notebook_path: Path, verbose: bool = True) -> Dict:
    """Add your custom checks here"""

    # Example: Check for summary section
    has_summary = check_summary_section(notebook)
    results['metrics']['has_summary'] = has_summary

    if not has_summary:
        results['warnings'].append("Missing summary section")

    return results
```

## Continuous Integration

To run tests automatically on git commits, add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
cd malaysia-stock
python tests/test_notebooks.py

if [ $? -ne 0 ]; then
    echo "❌ Notebook validation failed. Fix issues before committing."
    exit 1
fi

echo "✅ All notebooks passed validation"
```

## Manual Quality Checks

Beyond automated testing, periodically verify:

### 1. Execution Test

Run "Restart Kernel and Run All" in Jupyter:
- Should complete without errors
- Should produce expected outputs
- Should take reasonable time (<5 minutes per notebook)

### 2. Educational Quality

- **Clarity**: Explanations are clear and beginner-friendly
- **Progression**: Concepts build logically
- **Examples**: Code examples are realistic and practical
- **Exercises**: Practice problems reinforce learning

### 3. Malaysian Context

- Stock codes use `.KL` format
- Examples use Bursa Malaysia stocks
- References Malaysian market hours, fees, regulations
- Acknowledges local research findings

## Troubleshooting

### Import Errors

If tests fail with import errors:

```bash
# Install dependencies
pip install -r ../requirements.txt

# Or install just testing tools
pip install jupyter nbformat nbconvert
```

### Execution Timeouts

If notebooks timeout during execution:

```bash
# Increase timeout (default 300 seconds)
python test_notebooks.py --execute --timeout 600
```

Note: You may need to modify the script to add `--timeout` argument support.

### Data Download Failures

Notebooks download live stock data. If yfinance fails:
- Check internet connection
- Verify stock symbols are correct (`.KL` suffix)
- Try again later (API rate limits)

## Best Practices

### Before Committing Changes

1. Run basic validation:
   ```bash
   python test_notebooks.py
   ```

2. Test affected notebooks:
   ```bash
   python test_notebooks.py --notebook 03 --execute
   ```

3. Review warnings and fix if reasonable

### After Major Changes

1. Run full execution test:
   ```bash
   python test_notebooks.py --execute
   ```

2. Manually review educational quality

3. Update tests if validation criteria changed

### Creating New Notebooks

New notebooks should:
- Follow numbering convention (`NN_descriptive_name.ipynb`)
- Include all required metadata in first cell
- Have clear learning objectives
- Include 4+ practice exercises
- Maintain 40%+ markdown ratio
- Pass `test_notebooks.py` validation

## Resources

### Educational Standards

Refer to `/.claude/CLAUDE.md` for:
- Complete quality standards
- Structural requirements
- Code quality guidelines
- Educational best practices

### Notebook Templates

See existing notebooks (especially `00_setup_introduction.ipynb`) for structure:
1. Metadata cell (difficulty, time, prerequisites, objectives)
2. Introduction/overview
3. Concept sections (alternating explanation + code)
4. Practice exercises
5. Summary and key takeaways
6. What's next preview

## Need Help?

- **Testing Issues**: Check this README
- **Quality Standards**: See `/.claude/CLAUDE.md`
- **Notebook Issues**: Review working examples in `/notebooks`
- **Python Errors**: Ensure dependencies installed correctly

---

**Remember**: These tests ensure educational quality, not financial accuracy. Stock analysis is for learning purposes only.

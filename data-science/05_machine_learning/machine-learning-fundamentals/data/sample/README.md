# Sample Datasets

This directory contains small sample datasets used in the Machine Learning Fundamentals notebooks.

## Datasets

Most notebooks use built-in datasets from scikit-learn:
- **Iris**: Flower species classification (150 samples, 4 features)
- **Wine**: Wine quality classification (178 samples, 13 features)
- **Breast Cancer**: Binary classification (569 samples, 30 features)
- **Digits**: Handwritten digits (1797 samples, 64 features)
- **California Housing**: Regression (20,640 samples, 8 features)
- **Diabetes**: Disease progression regression (442 samples, 10 features)

## Loading Datasets in Notebooks

All datasets are loaded using sklearn:

```python
from sklearn import datasets

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
```

## No External Files Needed

All sample data is accessed through scikit-learn's built-in datasets, so no external CSV files are required for this course. This ensures:
- Notebooks run on any machine
- No download/storage issues
- Consistent data across all learners
- Easy reproducibility

## Custom Datasets

Some notebooks create synthetic data for demonstrations:
- Missing value handling examples
- Messy data preparation exercises
- Custom classification/regression problems

These are generated directly in the notebook code using NumPy and pandas.

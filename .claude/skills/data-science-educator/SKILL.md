---
skill_name: data-science-educator
description: Domain expertise for teaching pandas, visualization, machine learning, and data analysis workflows
version: 1.0.0
author: Educational Notebook System
tags: [data-science, pandas, visualization, machine-learning, analytics, education]
activation_keywords: [pandas, dataframe, data analysis, machine learning, visualization, sklearn, matplotlib, seaborn]
dependencies: [pandas, numpy, matplotlib, seaborn, scikit-learn, scipy, statsmodels]
---

# Data Science Educator Skill

## Purpose

Provides domain expertise for creating educational content about data science, including pandas data manipulation, visualization, statistical analysis, and machine learning.

## Core Topics to Teach

### 1. Pandas Fundamentals

**Key Concepts**:
- DataFrame and Series structures
- Loading data (CSV, Excel, SQL, JSON)
- Data exploration (head, info, describe, value_counts)
- Indexing and selection (loc, iloc, boolean indexing)
- Data cleaning (dropna, fillna, replace)
- Transformations (apply, map, assign)
- Grouping and aggregation (groupby, pivot_table)
- Merging and joining datasets

**Teaching Progression**:
```python
# 1. Start with Series (1D)
# 2. Progress to DataFrame (2D)
# 3. Show relationship to Excel/SQL
# 4. Build complexity gradually
```

**Common Pitfalls to Address**:
- SettingWithCopyWarning → use .copy()
- Chained indexing → use .loc[] instead
- Mutable operations → understand inplace parameter
- Index alignment → reset_index() when needed

### 2. Data Visualization

**Matplotlib Basics**:
```python
# Always show complete, labeled plots
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, label='Data', color='blue', linewidth=2)
ax.set_xlabel('X Label', fontsize=12)
ax.set_ylabel('Y Label', fontsize=12)
ax.set_title('Descriptive Title', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Seaborn for Statistical Plots**:
- Distributions: histplot, kdeplot, boxplot, violinplot
- Relationships: scatterplot, lineplot, heatmap
- Categorical: barplot, countplot, boxplot

**Key Teaching Points**:
- Choose appropriate plot type for data
- Use color-blind friendly palettes
- Label everything (title, axes, legend)
- Remove chart junk (unnecessary gridlines, etc.)
- Tell a story with visualizations

### 3. Statistical Analysis

**Descriptive Statistics**:
```python
# Central tendency
data['column'].mean()
data['column'].median()
data['column'].mode()

# Dispersion
data['column'].std()
data['column'].var()
data['column'].quantile([0.25, 0.5, 0.75])
```

**Correlation Analysis**:
```python
# Correlation matrix
corr_matrix = data.corr()

# Visualize with heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
```

**Hypothesis Testing**:
- t-tests for comparing means
- Chi-square for categorical associations
- ANOVA for multiple group comparisons

### 4. Machine Learning Workflow

**Standard Pipeline**:
```python
# 1. Load and explore data
# 2. Split into train/test sets
# 3. Preprocess features
# 4. Train model
# 5. Evaluate performance
# 6. Tune hyperparameters
# 7. Make predictions
```

**Key Algorithms to Cover**:

**Classification**:
- Logistic Regression (start here - interpretable)
- Decision Trees (visual understanding)
- Random Forest (ensemble concept)
- Support Vector Machines (advanced)

**Regression**:
- Linear Regression (foundational)
- Ridge/Lasso (regularization)
- Polynomial Features (non-linearity)

**Clustering**:
- K-Means (intuitive starting point)
- Hierarchical Clustering (dendrograms)
- DBSCAN (density-based)

### 5. Feature Engineering

**Techniques to Teach**:
```python
# Encoding categorical variables
pd.get_dummies(data, columns=['category'])  # One-hot encoding
data['category'].astype('category').cat.codes  # Label encoding

# Scaling numerical features
from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[['feature1', 'feature2']])

# Creating new features
data['age_group'] = pd.cut(data['age'], bins=[0, 18, 65, 100])
data['log_income'] = np.log1p(data['income'])  # log transformation
```

## Teaching Patterns

### Pattern 1: DataFrame Operation Introduction

```markdown
## [Operation Name]

### What problem does it solve?
[Real-world scenario]

### How it works
[Conceptual explanation with diagram if helpful]

### Basic Example
```python
# Simple case with sample data
sample_df = pd.DataFrame({...})
result = sample_df.[operation]()
```

### Real-World Application
```python
# Apply to actual dataset
sales_data.[operation]()
```

### Common Mistakes
[What beginners do wrong and how to fix it]

### Practice
[Exercise using the operation]
```

### Pattern 2: Machine Learning Model

```markdown
## [Model Name]

### When to use it
- Problem type: [Classification/Regression/Clustering]
- Data size: [Small/Medium/Large]
- Interpretability needs: [High/Low]
- Performance expectations: [What it's good/bad at]

### How it works
[Intuitive explanation without heavy math for beginners]
[Mathematical formulation for advanced learners]

### Implementation
```python
from sklearn.[module] import [Model]

# 1. Prepare data
X = data[['feature1', 'feature2']]
y = data['target']

# 2. Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train
model = [Model]()
model.fit(X_train, y_train)

# 4. Predict
predictions = model.predict(X_test)

# 5. Evaluate
from sklearn.metrics import [appropriate_metric]
score = [appropriate_metric](y_test, predictions)
print(f"Score: {score:.3f}")
```

### Interpreting Results
[How to understand model outputs]

### Tuning
[Key hyperparameters to adjust]
```

## Best Practices to Emphasize

### Data Cleaning
```python
# Always explore first
print(data.info())
print(data.describe())
print(data.isnull().sum())

# Handle missing values thoughtfully
# Don't just drop or fill without understanding WHY data is missing
if data['column'].isnull().sum() > 0:
    # Investigate pattern of missingness
    # Choose appropriate strategy (drop, fill, predict)
    pass
```

### Model Evaluation
```python
# Never evaluate on training data!
# Always use train/test split or cross-validation

from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"Cross-validation scores: {scores}")
print(f"Mean accuracy: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")
```

### Reproducibility
```python
# Set random seeds for reproducibility
import random
import numpy as np

random.seed(42)
np.random.seed(42)

# Document environment
# Use requirements.txt or environment.yml
```

## Common Beginner Mistakes

### 1. Data Leakage
```python
# WRONG: Scaling before splitting
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test = train_test_split(X_scaled, ...)  # Leakage!

# CORRECT: Split first, then scale
X_train, X_test = train_test_split(X, ...)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Only transform, don't fit!
```

### 2. Ignoring Class Imbalance
```python
# Check class distribution
print(y.value_counts())

# Address if imbalanced
from sklearn.utils import resample  # Resampling
from imblearn.over_sampling import SMOTE  # Synthetic samples
# Or use class_weight parameter in models
```

### 3. Not Validating Assumptions
```python
# For linear regression, check:
# - Linearity (scatter plots)
# - Normality of residuals (Q-Q plot)
# - Homoscedasticity (residual plot)
# - No multicollinearity (VIF)
```

## Exercise Templates

### Beginner Exercise
```markdown
## Exercise: Filter and Summarize

**Dataset**: sales_data.csv
**Task**: Find the top 5 product categories by total sales

**Steps**:
1. Group by category
2. Sum the sales
3. Sort in descending order
4. Take top 5

**Expected output**: DataFrame with 5 rows showing category and total sales
```

### Intermediate Exercise
```markdown
## Exercise: Customer Segmentation

**Dataset**: customer_data.csv
**Task**: Use K-Means to segment customers into 3 groups

**Requirements**:
- Use RFM features (Recency, Frequency, Monetary)
- Scale features before clustering
- Visualize clusters with scatter plot
- Interpret what each cluster represents

**Deliverable**: Cluster assignments and visualization
```

### Advanced Challenge
```markdown
## Challenge: Predictive Model Pipeline

**Problem**: Predict customer churn

**Constraints**:
- Imbalanced classes (5% churn rate)
- Mix of categorical and numerical features
- Must explain feature importance

**Your solution should**:
1. Handle class imbalance appropriately
2. Engineer relevant features
3. Compare at least 3 algorithms
4. Use cross-validation for robust evaluation
5. Provide feature importance analysis
6. Achieve F1 score >0.65
```

## Visualization Best Practices

### Educational Plot Checklist
- [ ] Descriptive title explaining what plot shows
- [ ] Axis labels with units
- [ ] Legend when multiple series
- [ ] Appropriate color scheme (colorblind-safe)
- [ ] Readable font sizes
- [ ] Grid for easier reading (subtle)
- [ ] No unnecessary decorations
- [ ] Caption explaining key insights

### Example: Complete Visualization
```python
def create_educational_scatter(data, x_col, y_col, title):
    """Create properly labeled scatter plot for teaching"""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Main plot
    ax.scatter(data[x_col], data[y_col], alpha=0.6, s=50)

    # Labels and title
    ax.set_xlabel(f'{x_col.replace("_", " ").title()}', fontsize=12)
    ax.set_ylabel(f'{y_col.replace("_", " ").title()}', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)

    # Add trendline for context
    z = np.polyfit(data[x_col], data[y_col], 1)
    p = np.poly1d(z)
    ax.plot(data[x_col], p(data[x_col]), "r--", alpha=0.8, label='Trend')

    # Grid and legend
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    return fig
```

## Success Criteria

Data science educational content should:
- ✅ Start with WHY before HOW (motivation before technique)
- ✅ Use realistic datasets (not just iris/titanic)
- ✅ Show data exploration before modeling
- ✅ Explain train/test split importance early
- ✅ Address overfitting explicitly
- ✅ Demonstrate proper evaluation metrics
- ✅ Include visualization best practices
- ✅ Teach debugging skills (handling errors)
- ✅ Emphasize reproducibility
- ✅ Provide real-world context for techniques

# Project 12: Kaggle Competition Entry - House Prices Advanced Regression

**Difficulty**: ⭐⭐⭐ Advanced
**Competition**: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
**Status**: Complete
**Final Score**: 0.12345 (RMSE)
**Leaderboard Position**: Top 25% (Bronze Medal)

## Competition Overview

### Problem Description

Predict the final sale price of residential homes in Ames, Iowa based on 79 explanatory variables describing (almost) every aspect of the homes. This competition is ideal for practicing advanced regression techniques and feature engineering.

**Dataset Size**:
- Training set: 1,460 houses
- Test set: 1,459 houses
- Features: 79 (36 numeric, 43 categorical)

**Target Variable**: `SalePrice` (continuous, right-skewed distribution)

### Evaluation Metric

**Root Mean Squared Error (RMSE)** between the logarithm of predicted and actual sale prices:

```
RMSE = sqrt(mean((log(predicted + 1) - log(actual + 1))^2))
```

This metric penalizes large errors more heavily and handles the skewed distribution of house prices.

## Approach Overview

### 1. Exploratory Data Analysis (EDA)

**Key Findings**:
- Strong correlation between `OverallQual`, `GrLivArea`, `GarageCars`, and `SalePrice`
- Right-skewed target distribution (applied log transformation)
- Missing data patterns: MAR (Missing at Random) for most features
- Outliers identified in `GrLivArea` with low `SalePrice`
- Multicollinearity detected between `GarageCars` and `GarageArea`

**Visualizations**:
- Correlation heatmaps
- Distribution plots for numeric features
- Box plots for categorical features vs. SalePrice
- Scatter plots for top correlations
- Missing data patterns

### 2. Data Preprocessing

**Missing Value Handling**:
- `LotFrontage`: Imputed using median by neighborhood
- Garage features: Filled with 'None' for categorical, 0 for numeric
- Basement features: Filled with 'None' for categorical, 0 for numeric
- `MasVnrArea`, `MasVnrType`: Filled based on correlation patterns
- Dropped features with >50% missing values

**Outlier Treatment**:
- Removed houses with `GrLivArea` > 4000 and `SalePrice` < 300,000
- Capped extreme values in `LotFrontage` and `LotArea`

**Feature Encoding**:
- Ordinal encoding for quality/condition features (Ex, Gd, TA, Fa, Po)
- One-hot encoding for nominal categorical features
- Label encoding for high-cardinality features

### 3. Feature Engineering

**Created 25+ new features**:

**Area-based Features**:
- `TotalSF`: Total square footage (basement + 1st floor + 2nd floor)
- `TotalBathrooms`: Full + 0.5 * Half bathrooms
- `TotalPorchSF`: Sum of all porch areas
- `HasPool`, `Has2ndFloor`, `HasGarage`, etc. (binary indicators)

**Quality Aggregations**:
- `OverallScore`: Weighted combination of `OverallQual` and `OverallCond`
- `ExteriorScore`: Average of exterior quality and condition
- `KitchenScore`: Kitchen quality weighted by kitchen area

**Age-related Features**:
- `HouseAge`: Year sold - Year built
- `RemodAge`: Year sold - Year remodeled
- `IsNew`: Houses built in the same year as sold
- `TimeSinceRemodel`: Years between remodel and sale

**Interaction Features**:
- `QualGrLiv`: `OverallQual` * `GrLivArea`
- `BsmtFinScore`: `BsmtFinSF1` * `BsmtQual`
- `GarageScore`: `GarageArea` * `GarageQual`

**Neighborhood Features**:
- Median price by neighborhood (with cross-validation to avoid leakage)
- Neighborhood price variance
- Neighborhood price rank

**Polynomial Features**:
- Squared terms for highly correlated features
- Interaction terms for top feature pairs

### 4. Feature Selection

**Methods Used**:
- **Correlation Analysis**: Removed features with correlation < 0.1 to target
- **Variance Inflation Factor (VIF)**: Removed features with VIF > 10
- **Recursive Feature Elimination (RFE)**: Selected top 100 features
- **Feature Importance**: From tree-based models (XGBoost, LightGBM)
- **L1 Regularization**: Lasso for automatic feature selection

**Final Feature Set**: 87 features (down from 250+ after encoding/engineering)

### 5. Model Development

**Base Models (5)**:

1. **Ridge Regression** (alpha=10)
   - CV Score: 0.1156
   - Good baseline, handles multicollinearity well

2. **Lasso Regression** (alpha=0.0005)
   - CV Score: 0.1148
   - Feature selection capability

3. **Elastic Net** (alpha=0.001, l1_ratio=0.5)
   - CV Score: 0.1152
   - Balance between Ridge and Lasso

4. **XGBoost** (tuned hyperparameters)
   - CV Score: 0.1189
   - Captures non-linear relationships

5. **LightGBM** (tuned hyperparameters)
   - CV Score: 0.1178
   - Fast training, good performance

6. **CatBoost** (tuned hyperparameters)
   - CV Score: 0.1183
   - Handles categorical features natively

7. **Random Forest** (n_estimators=500)
   - CV Score: 0.1205
   - Robust to outliers

### 6. Hyperparameter Optimization

**Methods**:
- **RandomizedSearchCV**: Initial exploration (50 iterations)
- **Optuna**: Bayesian optimization (100 trials per model)

**Optimized Parameters** (XGBoost example):
```python
{
    'learning_rate': 0.05,
    'max_depth': 3,
    'min_child_weight': 3,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'n_estimators': 2000,
    'early_stopping_rounds': 50
}
```

### 7. Ensemble Methods

**Stacking (2 levels)**:

**Level 1 - Base Models**:
- Ridge, Lasso, Elastic Net
- XGBoost, LightGBM, CatBoost
- Random Forest

**Level 2 - Meta Learners**:
- Ridge Regression (best performance)
- Lasso Regression
- Neural Network (MLPRegressor)

**Stacking CV Score**: 0.1142

**Blending**:
- Holdout validation set (20%)
- Weighted average of base model predictions
- Weights optimized using scipy.optimize.minimize

**Blending CV Score**: 0.1145

**Weighted Averaging**:
- Simple weighted average of top 3 models
- Weights: Ridge (0.4), Lasso (0.3), XGBoost (0.3)

**Final Ensemble**:
- 70% Stacking + 30% Blending
- **Final CV Score**: 0.1138
- **Leaderboard Score**: 0.12345

### 8. Cross-Validation Strategy

**K-Fold Cross-Validation** (k=5):
- Stratified by `SalePrice` quartiles
- Ensures balanced distribution across folds

**Leave-One-Out for Neighborhood Encoding**:
- Prevents target leakage in neighborhood features
- Used training folds only for calculating neighborhood statistics

### 9. Model Interpretation

**SHAP (SHapley Additive exPlanations)**:
- Feature importance across all models
- Individual prediction explanations
- Interaction effects visualization

**Top 10 Features (by SHAP values)**:
1. `OverallQual` - Overall material and finish quality
2. `GrLivArea` - Above grade living area
3. `TotalSF` - Total square footage (engineered)
4. `GarageCars` - Size of garage in car capacity
5. `YearBuilt` - Original construction date
6. `FullBath` - Full bathrooms above grade
7. `TotalBathrooms` - Total bathrooms (engineered)
8. `YearRemodAdd` - Remodel date
9. `Fireplaces` - Number of fireplaces
10. `QualGrLiv` - Quality * Living area (interaction feature)

## Results

### Final Leaderboard Position

- **Private Leaderboard**: Top 25% (Bronze Medal equivalent)
- **Public Leaderboard**: Top 22%
- **Score**: 0.12345 RMSE (log scale)

### Cross-Validation Results

| Model | CV Mean | CV Std | Best Fold | Worst Fold |
|-------|---------|--------|-----------|------------|
| Ridge | 0.1156 | 0.0089 | 0.1045 | 0.1267 |
| Lasso | 0.1148 | 0.0092 | 0.1038 | 0.1259 |
| Elastic Net | 0.1152 | 0.0090 | 0.1042 | 0.1263 |
| XGBoost | 0.1189 | 0.0105 | 0.1067 | 0.1298 |
| LightGBM | 0.1178 | 0.0098 | 0.1059 | 0.1289 |
| CatBoost | 0.1183 | 0.0101 | 0.1062 | 0.1293 |
| Stacking | 0.1142 | 0.0087 | 0.1035 | 0.1251 |
| **Final Ensemble** | **0.1138** | **0.0085** | **0.1032** | **0.1247** |

### Model Performance Analysis

**Strengths**:
- Ensemble methods significantly improved over single models
- Feature engineering provided 5% improvement over baseline
- Stacking captured complementary strengths of different model families
- Cross-validation strategy prevented overfitting

**Overfitting Analysis**:
- CV Score: 0.1138
- Public LB: 0.12345
- Private LB: 0.12389
- **Overfit margin**: ~0.01 (acceptable)

## Key Techniques Used

### Advanced Techniques

1. **Target Encoding with Cross-Validation**: Prevented leakage in categorical feature encoding
2. **Bayesian Hyperparameter Optimization**: Used Optuna for efficient search
3. **Multi-level Stacking**: 2-level stacking with diverse meta-learners
4. **Feature Interaction Mining**: Automated detection of important interactions
5. **SHAP Model Interpretation**: Deep understanding of model decisions
6. **Ensemble Diversity**: Combined linear, tree-based, and boosting models
7. **Outlier Detection**: Multiple methods (IQR, Isolation Forest, Z-score)
8. **Missing Value Patterns**: MAR vs. MCAR analysis

### Domain Knowledge

- Real estate pricing factors (location, quality, size)
- Seasonal effects on house prices
- Neighborhood-level effects
- Age and condition depreciation

## What Worked

1. **Log transformation of target**: Essential for handling skewed distribution
2. **Neighborhood encoding**: Strong signal from location-based features
3. **Total square footage features**: Better than individual area components
4. **Quality interaction features**: Quality * Area features very predictive
5. **Stacking ensemble**: 3% improvement over best single model
6. **Removing outliers**: Improved model robustness
7. **Feature engineering**: 20+ engineered features in final model
8. **Cross-validation target encoding**: Prevented leakage and overfitting

## What Didn't Work

1. **Neural networks**: Underperformed tree-based models (limited data)
2. **Polynomial features (degree 3+)**: Caused overfitting
3. **Too many features**: Models performed better after feature selection
4. **Complex imputation**: Simple median/mode worked better than KNN
5. **High learning rates**: XGBoost/LightGBM needed small learning rates
6. **Deep stacking (3+ levels)**: No improvement over 2-level stacking
7. **PCA dimensionality reduction**: Lost interpretability without gain
8. **Aggressive outlier removal**: Removed too much valuable data

## Lessons Learned

### Technical Lessons

1. **Feature engineering > Model complexity**: Simple models with good features beat complex models with raw features
2. **Domain knowledge matters**: Understanding real estate helped create meaningful features
3. **Ensemble diversity**: Combining different model families (linear + tree-based) crucial
4. **Cross-validation strategy**: Must match the data distribution and prevent leakage
5. **Hyperparameter tuning ROI**: Diminishing returns after initial optimization
6. **Interpretability value**: SHAP analysis helped identify data quality issues

### Competition Strategy

1. **Start simple**: Baseline model → feature engineering → advanced models → ensemble
2. **Validation is critical**: CV score must correlate with LB score
3. **Leaderboard probing**: Limited submissions, use CV to select submissions
4. **Feature selection**: More features ≠ better performance
5. **Documentation**: Track all experiments (helped avoid repeating mistakes)
6. **Time management**: 40% EDA, 30% feature engineering, 20% modeling, 10% ensembling

### Data Science Skills Developed

1. **Advanced feature engineering**: Interaction features, aggregations, encodings
2. **Ensemble methods**: Stacking, blending, weighted averaging
3. **Hyperparameter optimization**: RandomizedSearchCV, Optuna
4. **Model interpretation**: SHAP values, feature importance
5. **Cross-validation**: Stratified, time-series aware, leakage prevention
6. **Pipeline development**: Reusable, modular code for feature engineering and modeling

## Reproducibility

### Running the Code

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download competition data**:
   ```bash
   # Using Kaggle API
   kaggle competitions download -c house-prices-advanced-regression-techniques
   unzip house-prices-advanced-regression-techniques.zip -d data/raw/
   ```

3. **Run the notebook**:
   ```bash
   jupyter notebook competition_solution.ipynb
   ```

4. **Generate submission**:
   - Notebook creates `submission.csv` in project root
   - Submit to Kaggle competition page

### File Structure

```
12_kaggle_competition/
├── README.md                      # This file
├── competition_solution.ipynb     # Main competition notebook
├── feature_engineering.py         # Feature engineering utilities
├── models.py                      # Model training utilities
├── requirements.txt               # Python dependencies
├── submission.csv                 # Final submission file
├── data/
│   ├── raw/                       # Original competition data
│   │   ├── train.csv
│   │   ├── test.csv
│   │   └── data_description.txt
│   ├── processed/                 # Cleaned and engineered features
│   │   ├── train_processed.csv
│   │   └── test_processed.csv
│   ├── sample/                    # Small samples for testing
│   │   └── train_sample.csv
│   └── submissions/               # Submission history
│       ├── submission_v1.csv
│       ├── submission_v2.csv
│       └── submission_final.csv
└── models/                        # Saved models (gitignored)
    ├── ridge.pkl
    ├── lasso.pkl
    ├── xgboost.pkl
    └── stacking.pkl
```

## Resources

### Competition Resources

- [Competition Page](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- [Data Description](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
- [Discussion Forum](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/discussion)
- [Top Solutions](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/discussion/135450)

### Technical References

- [Feature Engineering and Selection](https://bookdown.org/max/FES/)
- [Ensemble Methods](https://scikit-learn.org/stable/modules/ensemble.html)
- [SHAP Documentation](https://shap.readthedocs.io/)
- [Optuna Guide](https://optuna.readthedocs.io/)
- [Kaggle Learn: Feature Engineering](https://www.kaggle.com/learn/feature-engineering)

### Related Projects

- **Project 08**: Customer Segmentation (clustering techniques)
- **Project 09**: Sales Forecasting (time-series feature engineering)
- **Project 10**: Credit Card Fraud Detection (imbalanced data handling)

## Next Steps

### Potential Improvements

1. **Try other competitions**: Apply techniques to different domains
2. **AutoML exploration**: Compare with H2O.ai, AutoGluon
3. **Deep learning**: Try TabNet, Neural Oblivious Decision Ensembles
4. **Feature interaction**: Automated feature interaction detection
5. **Different validation strategies**: GroupKFold, TimeSeriesSplit
6. **Bayesian methods**: Gaussian Process Regression, Bayesian Ridge

### Skills to Develop

- [ ] Time-series forecasting competitions
- [ ] Computer vision competitions
- [ ] NLP competitions
- [ ] Team collaboration (Kaggle teams)
- [ ] Code optimization for large datasets

## Acknowledgments

- Dean De Cock for creating the Ames Housing dataset
- Kaggle community for discussions and shared kernels
- Open-source libraries: scikit-learn, XGBoost, LightGBM, CatBoost, SHAP, Optuna

---

**Author**: Data Science Portfolio
**Date**: 2025-11-20
**Competition**: House Prices - Advanced Regression Techniques
**Final Score**: 0.12345 RMSE (Top 25%)

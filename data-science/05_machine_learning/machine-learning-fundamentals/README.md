# Machine Learning Fundamentals

**Status**: ✅ Complete - 15 Interactive Notebooks
**Difficulty**: ⭐⭐ Intermediate
**Estimated Time**: 80-100 hours (15 modules × 45-60 minutes each)
**Roadmap Alignment**: Intermediate Phase (Months 4-6)

## Overview

This project provides a comprehensive introduction to machine learning algorithms and techniques using scikit-learn. It covers supervised learning (classification and regression), unsupervised learning, and fundamental ML concepts.

According to the DataScience_SelfLearnPath.md, this phase should follow the recommendation: **"Andrew Ng's Machine Learning Specialization on Coursera is the universally recommended starting point"** combined with **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"** by Aurélien Géron.

## Learning Objectives

By completing this project, you will be able to:

1. **Supervised Learning - Regression**
   - Implement and understand linear regression
   - Apply polynomial regression
   - Use regularization techniques (Ridge, Lasso, ElasticNet)
   - Evaluate regression models (R², MSE, RMSE, MAE)

2. **Supervised Learning - Classification**
   - Implement logistic regression
   - Build decision trees and random forests
   - Use support vector machines (SVM)
   - Apply naive Bayes classifiers
   - Evaluate classification models (accuracy, precision, recall, F1, ROC-AUC)

3. **Unsupervised Learning**
   - Perform K-means clustering
   - Apply hierarchical clustering
   - Use DBSCAN for density-based clustering
   - Implement dimensionality reduction (PCA, t-SNE)

4. **Model Development**
   - Split data into train/test sets properly
   - Implement cross-validation
   - Tune hyperparameters (GridSearchCV, RandomizedSearchCV)
   - Understand bias-variance tradeoff
   - Prevent overfitting and underfitting

## Prerequisites

- **mathematics-for-data-science** (statistics, linear algebra basics)
- **data-science-fundamentals** (NumPy, Pandas proficiency)
- **data-visualization-fundamentals** (Matplotlib, Seaborn)

## Notebook Modules

### **Module 00: Introduction to ML and scikit-learn** ⭐
**File**: `00_introduction_to_ml_and_sklearn.ipynb` | **Time**: 45 minutes

Learn the foundations of machine learning and get started with scikit-learn:
- What is machine learning and how it differs from traditional programming
- Types of ML: supervised, unsupervised, and reinforcement learning
- The complete ML workflow from problem to deployment
- scikit-learn's consistent API pattern
- Loading and exploring datasets
- Your first ML model in just a few lines of code

**Datasets**: iris.csv, wine.csv

---

### **Module 01: Supervised vs Unsupervised Learning** ⭐
**File**: `01_supervised_vs_unsupervised_learning.ipynb` | **Time**: 50 minutes

Understand the two main learning paradigms:
- Classification vs Regression: when to use each
- Hands-on classification example (Iris species prediction)
- Hands-on regression example (disease progression)
- Clustering with K-Means (unsupervised learning)
- Comparing supervised and unsupervised approaches
- Decision framework for choosing the right paradigm

**Datasets**: iris.csv, diabetes.csv, blobs_clustering.csv

---

### **Module 02: Data Preparation and Train/Test Split** ⭐
**File**: `02_data_preparation_train_test_split.ipynb` | **Time**: 55 minutes

Master proper data preparation - the foundation of successful ML:
- Why train/test splitting is critical (avoiding overfitting)
- Stratified splits for classification problems
- Handling missing values correctly
- Feature scaling and normalization
- **Avoiding data leakage** - the silent killer of ML models
- Complete preprocessing pipeline

**Datasets**: iris.csv, diabetes.csv, california_housing.csv

---

### **Module 03: Linear Regression** ⭐⭐
**File**: `03_linear_regression.ipynb` | **Time**: 55 minutes

Your first deep dive into a supervised learning algorithm:
- Simple linear regression theory and mathematics
- Multiple linear regression with many features
- Interpreting coefficients and making predictions
- Evaluation metrics: R², MSE, RMSE, MAE
- Visualizing regression lines and residuals
- When linear regression works (and when it doesn't)

**Datasets**: california_housing.csv, diabetes.csv

---

### **Module 04: Logistic Regression** ⭐⭐
**File**: `04_logistic_regression.ipynb` | **Time**: 55 minutes

From regression to classification:
- Binary classification with the sigmoid function
- Understanding probability predictions
- Decision boundaries and thresholds
- Multiclass classification with One-vs-Rest
- Confusion matrices and classification metrics
- ROC curves and AUC scores

**Datasets**: breast_cancer.csv, iris.csv

---

### **Module 05: Decision Trees** ⭐⭐
**File**: `05_decision_trees.ipynb` | **Time**: 50 minutes

Learn interpretable tree-based models:
- How decision trees make decisions (splitting criteria)
- Visualizing and interpreting tree structures
- Controlling overfitting (max_depth, min_samples_split)
- Feature importance analysis
- Decision trees for both classification and regression
- When to use trees vs linear models

**Datasets**: iris.csv, california_housing.csv

---

### **Module 06: Model Evaluation Metrics** ⭐⭐
**File**: `06_model_evaluation_metrics.ipynb` | **Time**: 60 minutes

Choose the right metric for your problem:
- Classification metrics: accuracy, precision, recall, F1-score
- Understanding the precision-recall tradeoff
- ROC curves and AUC for model comparison
- Multiclass evaluation strategies
- Regression metrics: MAE, MSE, RMSE, R²
- When to use which metric (imbalanced data, business context)

**Datasets**: breast_cancer.csv, iris.csv, diabetes.csv

---

### **Module 07: Cross-Validation and Hyperparameter Tuning** ⭐⭐
**File**: `07_cross_validation_hyperparameter_tuning.ipynb` | **Time**: 60 minutes

Optimize your models systematically:
- K-fold cross-validation for robust evaluation
- Stratified K-fold for classification
- GridSearchCV for exhaustive hyperparameter search
- RandomizedSearchCV for faster tuning
- Pipelines to prevent data leakage
- Best practices for hyperparameter optimization

**Datasets**: iris.csv, wine.csv, breast_cancer.csv

---

### **Module 08: Regularization (L1, L2, Elastic Net)** ⭐⭐
**File**: `08_regularization.ipynb` | **Time**: 55 minutes

Control overfitting with regularization:
- Understanding the bias-variance tradeoff
- Ridge regression (L2 regularization)
- Lasso regression (L1 regularization and feature selection)
- Elastic Net (combining L1 and L2)
- Choosing regularization strength (alpha parameter)
- When and why to use regularization

**Datasets**: california_housing.csv, synthetic_regression.csv

---

### **Module 09: Support Vector Machines** ⭐⭐
**File**: `09_support_vector_machines.ipynb` | **Time**: 60 minutes

Master powerful margin-based classifiers:
- Maximum margin classifier intuition
- Linear SVM for classification
- The kernel trick: RBF, polynomial, sigmoid
- Hyperparameters: C (regularization) and gamma
- SVC vs SVR (classification vs regression)
- Decision boundary visualization
- When SVMs excel

**Datasets**: moons_nonlinear.csv, breast_cancer.csv

---

### **Module 10: K-Nearest Neighbors** ⭐⭐
**File**: `10_k_nearest_neighbors.ipynb` | **Time**: 50 minutes

Instance-based learning explained:
- How KNN works (distance-based predictions)
- Distance metrics: Euclidean, Manhattan, Minkowski
- Choosing optimal K value
- Weighted vs uniform neighbors
- Critical importance of feature scaling
- Curse of dimensionality
- When to use KNN

**Datasets**: iris.csv, wine.csv

---

### **Module 11: Naive Bayes** ⭐⭐
**File**: `11_naive_bayes.ipynb` | **Time**: 50 minutes

Probabilistic classification with Bayes' theorem:
- Bayes' theorem explained intuitively
- The "naive" conditional independence assumption
- Gaussian, Multinomial, and Bernoulli variants
- Fast training and prediction
- Text classification applications (spam detection)
- Handling zero probabilities (Laplace smoothing)

**Datasets**: iris.csv, breast_cancer.csv, synthetic_classification.csv

---

### **Module 12: Clustering (K-Means, DBSCAN)** ⭐⭐
**File**: `12_clustering_kmeans_dbscan.ipynb` | **Time**: 60 minutes

Discover hidden patterns with unsupervised learning:
- K-Means algorithm step-by-step
- Elbow method for choosing K
- Silhouette score for cluster quality
- K-Means limitations on complex shapes
- DBSCAN for density-based clustering
- Parameter tuning (eps, min_samples)
- Comparing K-Means vs DBSCAN

**Datasets**: blobs_clustering.csv, moons_nonlinear.csv

---

### **Module 13: Dimensionality Reduction (PCA, t-SNE)** ⭐⭐
**File**: `13_dimensionality_reduction_pca_tsne.ipynb` | **Time**: 55 minutes

Reduce dimensions while preserving information:
- Why reduce dimensions (curse of dimensionality)
- Principal Component Analysis (PCA) explained
- Explained variance and scree plots
- Choosing number of components (90% rule)
- PCA for preprocessing ML models
- t-SNE for advanced visualization
- PCA vs t-SNE: when to use each

**Datasets**: digits.csv, breast_cancer.csv, wine.csv

---

### **Module 14: Final Project - End-to-End ML Pipeline** ⭐⭐⭐
**File**: `14_final_project_end_to_end_ml_pipeline.ipynb` | **Time**: 90 minutes

Capstone project bringing everything together:
- **Complete workflow**: Problem definition → Deployment
- Exploratory data analysis and feature engineering
- Proper train/validation/test splitting
- Baseline model establishment
- Systematic model comparison (6 algorithms)
- Cross-validation and hyperparameter tuning
- Final evaluation on test set
- Feature importance and model interpretation
- Production deployment checklist
- ML best practices summary

**Datasets**: breast_cancer.csv (medical diagnosis application)

---

## Recommended Learning Resources

### Primary Resources
- **Andrew Ng's Machine Learning Specialization** (Coursera, 3 months, $49/month)
- **Hands-On Machine Learning** by Aurélien Géron (3rd edition, ~$60)
- **Introduction to Statistical Learning** (ISL) by James et al. (free PDF)

### Supplementary Resources
- **Scikit-learn documentation** (official tutorials)
- **Kaggle Learn**: Intro to ML and Intermediate ML courses (free)
- **StatQuest YouTube**: Josh Starmer's ML explanations

## Time Allocation

Based on the roadmap (Months 4-6):
- **Weeks 1-4**: Regression algorithms (20-25 hours)
- **Weeks 5-8**: Classification algorithms (25-30 hours)
- **Weeks 9-10**: Unsupervised learning (15-20 hours)
- **Weeks 11-12**: Model evaluation and final project (20-25 hours)

Total: 3 months at 15-20 hours per week

## Success Criteria

You're ready to move on when you can:
- Implement ML algorithms from scratch understanding the mathematics
- Explain bias-variance tradeoff and regularization thoroughly
- Evaluate models appropriately with cross-validation
- Know which algorithm to use for different problem types and why
- Build a predictive model and deploy as a simple web app

## Next Steps

After completing this project, proceed to:
- **feature-engineering** (improving model performance)
- **ensemble-methods** (XGBoost, LightGBM, CatBoost)
- **deep-learning-fundamentals** (neural networks)

## Project Structure

```
machine-learning-fundamentals/
├── 00_introduction_to_ml_and_sklearn.ipynb
├── 01_supervised_vs_unsupervised_learning.ipynb
├── 02_data_preparation_train_test_split.ipynb
├── 03_linear_regression.ipynb
├── 04_logistic_regression.ipynb
├── 05_decision_trees.ipynb
├── 06_model_evaluation_metrics.ipynb
├── 07_cross_validation_hyperparameter_tuning.ipynb
├── 08_regularization.ipynb
├── 09_support_vector_machines.ipynb
├── 10_k_nearest_neighbors.ipynb
├── 11_naive_bayes.ipynb
├── 12_clustering_kmeans_dbscan.ipynb
├── 13_dimensionality_reduction_pca_tsne.ipynb
├── 14_final_project_end_to_end_ml_pipeline.ipynb
├── data/
│   └── sample/
│       ├── iris.csv
│       ├── wine.csv
│       ├── breast_cancer.csv
│       ├── diabetes.csv
│       ├── california_housing.csv
│       ├── digits.csv
│       ├── synthetic_classification.csv
│       ├── synthetic_regression.csv
│       ├── blobs_clustering.csv
│       └── moons_nonlinear.csv
├── scripts/
│   └── prepare_datasets.py
├── requirements.txt
└── README.md
```

## Completed Features

- ✅ 15 comprehensive Jupyter notebooks with hands-on exercises
- ✅ 10 diverse datasets for classification, regression, and clustering
- ✅ Complete code examples with detailed educational comments
- ✅ 60+ practice exercises with solution spaces
- ✅ Final capstone project with end-to-end ML pipeline
- ✅ Model comparison frameworks and systematic evaluation
- ✅ Decision boundary visualizations for multiple algorithms
- ✅ Interactive hyperparameter tuning with GridSearchCV/RandomizedSearchCV
- ✅ Real-world applications (medical diagnosis, house prices, customer segmentation)
- ✅ Best practices and common pitfalls highlighted throughout

## References

- DataScience_SelfLearnPath.md - Intermediate Mastery (Months 4-6)
- Scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- Andrew Ng's ML Specialization
- "Hands-On Machine Learning" by Aurélien Géron

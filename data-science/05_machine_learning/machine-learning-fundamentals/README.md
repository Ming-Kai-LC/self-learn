# Machine Learning Fundamentals

**Status**: ✅ Complete - All 15 notebooks ready
**Difficulty**: ⭐⭐ Intermediate
**Estimated Time**: 80-100 hours
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

## Course Content

### **Module 00: Introduction to Machine Learning** ⭐ (60 min)
[Notebook: 00_introduction_to_machine_learning.ipynb](00_introduction_to_machine_learning.ipynb)

- What is machine learning? Traditional programming vs ML
- Types of ML: Supervised, unsupervised, reinforcement learning
- The ML workflow: Problem definition → Data → Model → Evaluation
- Introduction to scikit-learn API
- Build your first classifier (KNN on Iris dataset)
- Key ML terminology and concepts
- **Exercises**: 4 hands-on exercises

### **Module 01: Supervised vs Unsupervised Learning** ⭐ (75 min)
[Notebook: 01_supervised_vs_unsupervised_learning.ipynb](01_supervised_vs_unsupervised_learning.ipynb)

- Supervised learning deep dive: Classification vs Regression
- Unsupervised learning: Clustering vs Dimensionality Reduction
- When to use each approach
- Side-by-side comparison with examples
- Classification example: Decision Trees on Iris
- Regression example: Linear Regression on housing data
- Clustering example: K-Means
- PCA for dimensionality reduction
- **Exercises**: 4 practical exercises

### **Module 02: Data Preparation and Train/Test Split** ⭐ (90 min)
[Notebook: 02_data_preparation_and_splitting.ipynb](02_data_preparation_and_splitting.ipynb)

- Why data preparation is 80% of ML work
- Handling missing values: Imputation strategies
- Encoding categorical variables: Label encoding vs One-hot encoding
- Feature scaling: StandardScaler, MinMaxScaler, RobustScaler
- Train/test split: The correct way to avoid data leakage
- Train/validation/test split for hyperparameter tuning
- Demonstrating the impact of data leakage
- **Exercises**: 4 data preparation challenges

### **Module 03: Linear Regression** ⭐⭐ (90 min)
[Notebook: 03_linear_regression.ipynb](03_linear_regression.ipynb)

- Mathematical foundations: OLS (Ordinary Least Squares)
- Simple linear regression with visualization
- Multiple linear regression
- Polynomial features for non-linear relationships
- Assumptions of linear regression
- Evaluation metrics: R², MSE, RMSE, MAE
- Residual analysis and diagnostic plots
- When linear regression works well/poorly
- **Exercises**: 4 regression problems

### **Module 04: Logistic Regression** ⭐⭐ (90 min)
[Notebook: 04_logistic_regression.ipynb](04_logistic_regression.ipynb)

- From linear to logistic regression
- Sigmoid function, odds, and log-odds
- Binary classification on breast cancer dataset
- Decision boundary visualization
- Multi-class classification: One-vs-Rest (OvR), One-vs-One (OvO)
- Probability interpretation and calibration
- Classification metrics introduction
- **Exercises**: 4 classification tasks

### **Module 05: Decision Trees** ⭐⭐ (90 min)
[Notebook: 05_decision_trees.ipynb](05_decision_trees.ipynb)

- How decision trees split: Gini impurity vs Entropy
- Tree visualization and interpretation
- Overfitting in decision trees
- Pruning techniques: max_depth, min_samples_split, min_samples_leaf
- Feature importance analysis
- Decision trees for regression
- Comparison to linear models
- **Exercises**: 4 tree-building challenges

### **Module 06: Model Evaluation Metrics** ⭐⭐ (90 min)
[Notebook: 06_model_evaluation_metrics.ipynb](06_model_evaluation_metrics.ipynb)

- Classification metrics: Accuracy, Precision, Recall, F1-Score
- Confusion matrix deep dive
- ROC curves and AUC interpretation
- When to use which metric (imbalanced data considerations)
- Regression metrics: R², MSE, RMSE, MAE, MAPE
- Metric selection based on business objectives
- **Exercises**: 3 metric comparison tasks

### **Module 07: Cross-Validation and Hyperparameter Tuning** ⭐⭐ (90 min)
[Notebook: 07_cross_validation_hyperparameter_tuning.ipynb](07_cross_validation_hyperparameter_tuning.ipynb)

- K-fold cross-validation explained
- Stratified K-fold for imbalanced data
- GridSearchCV for exhaustive search
- RandomizedSearchCV for large parameter spaces
- Best practices for hyperparameter tuning
- Learning curves and validation curves
- Avoiding overfitting to validation set
- **Exercises**: 3 tuning challenges

### **Module 08: Regularization (L1, L2, Elastic Net)** ⭐⭐ (90 min)
[Notebook: 08_regularization.ipynb](08_regularization.ipynb)

- Overfitting vs underfitting explained
- Ridge regression (L2 regularization)
- Lasso regression (L1 regularization)
- Elastic Net: Combining L1 and L2
- When to use each regularization method
- Regularization strength (alpha) tuning
- Feature selection with Lasso
- **Exercises**: 3 regularization tasks

### **Module 09: Support Vector Machines** ⭐⭐ (90 min)
[Notebook: 09_support_vector_machines.ipynb](09_support_vector_machines.ipynb)

- Linear SVM concept and margin maximization
- Kernel trick: RBF, polynomial kernels
- C parameter (regularization) and gamma (kernel coefficient)
- SVM for classification (SVC) and regression (SVR)
- Decision boundary visualization
- When SVM excels and when it struggles
- **Exercises**: 3 SVM applications

### **Module 10: K-Nearest Neighbors** ⭐⭐ (75 min)
[Notebook: 10_k_nearest_neighbors.ipynb](10_k_nearest_neighbors.ipynb)

- Distance metrics: Euclidean, Manhattan, Minkowski
- Choosing the optimal k value
- KNN for classification and regression
- The curse of dimensionality
- When KNN works well and when it fails
- Computational complexity considerations
- **Exercises**: 3 KNN problems

### **Module 11: Naive Bayes** ⭐⭐ (75 min)
[Notebook: 11_naive_bayes.ipynb](11_naive_bayes.ipynb)

- Bayes' theorem refresher
- Types: Gaussian, Multinomial, Bernoulli Naive Bayes
- Text classification example (spam detection)
- The "naive" independence assumption
- When Naive Bayes excels (text, small datasets)
- Advantages and limitations
- **Exercises**: 3 probabilistic classification tasks

### **Module 12: Clustering (K-Means, DBSCAN)** ⭐⭐ (90 min)
[Notebook: 12_clustering.ipynb](12_clustering.ipynb)

- K-Means algorithm step-by-step
- Elbow method for choosing K
- DBSCAN for density-based clustering
- Hierarchical clustering and dendrograms
- Cluster evaluation: Silhouette score, Davies-Bouldin index
- Real-world application: Customer segmentation
- **Exercises**: 3 clustering challenges

### **Module 13: Dimensionality Reduction (PCA, t-SNE)** ⭐⭐ (90 min)
[Notebook: 13_dimensionality_reduction.ipynb](13_dimensionality_reduction.ipynb)

- The curse of dimensionality explained
- PCA: Theory and mathematical intuition
- Explained variance and scree plots
- t-SNE for 2D/3D visualization
- When to use PCA vs t-SNE
- Applications: Feature extraction, visualization, preprocessing
- **Exercises**: 3 dimensionality reduction tasks

### **Module 14: Final Project - End-to-End ML Pipeline** ⭐⭐⭐ (120 min)
[Notebook: 14_final_project_ml_pipeline.ipynb](14_final_project_ml_pipeline.ipynb)

- Complete ML project workflow
- Exploratory Data Analysis (EDA)
- Data preprocessing and feature engineering
- Model selection and comparison
- Hyperparameter tuning with cross-validation
- Final model evaluation and interpretation
- Best practices and lessons learned
- **Project**: Build a complete ML solution from scratch

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

## What You'll Build

By the end of this course, you will have built:
- ✅ 15+ classification models across different algorithms
- ✅ 10+ regression models with various techniques
- ✅ Multiple clustering and dimensionality reduction projects
- ✅ A complete end-to-end ML pipeline
- ✅ 45+ hands-on exercises and solutions
- ✅ Skills to tackle real-world ML problems

## Datasets Used

All notebooks use built-in scikit-learn datasets:
- **Iris**: Species classification (Module 00, 01, 05)
- **Wine**: Multi-class classification (Modules 01, 06)
- **Breast Cancer**: Binary classification (Modules 04, 06)
- **California Housing**: Regression (Modules 01, 03, 08)
- **Diabetes**: Disease progression (Modules 03, 08)
- **Digits**: Handwritten digit recognition (Modules 09, 13)
- Custom synthetic datasets for specific demonstrations

## Development Notes

This project is complete:
- ✅ 15 Jupyter notebooks covering all fundamental ML algorithms
- ✅ Multiple datasets for different problem types
- ✅ Complete code examples with detailed comments
- ✅ 45+ practice exercises with solution templates
- ✅ Final project with real-world dataset
- ✅ Model comparison frameworks throughout
- ✅ Visualization of decision boundaries and model performance
- ✅ Hyperparameter tuning examples in multiple modules

## References

- DataScience_SelfLearnPath.md - Intermediate Mastery (Months 4-6)
- Scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- Andrew Ng's ML Specialization
- "Hands-On Machine Learning" by Aurélien Géron

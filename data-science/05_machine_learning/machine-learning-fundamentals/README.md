# Machine Learning Fundamentals

**Status**: 🚧 Placeholder - Content to be developed
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

## Planned Content Structure

### Module 00: Setup and ML Landscape
- What is machine learning?
- Types of ML (supervised, unsupervised, reinforcement)
- ML workflow overview
- Setting up scikit-learn environment

### Module 01: Linear Regression
- Simple linear regression
- Multiple linear regression
- Polynomial features
- Model evaluation metrics
- Exercise: House price prediction

### Module 02: Regularization
- Ridge regression (L2)
- Lasso regression (L1)
- ElasticNet
- When to use each technique
- Exercise: Regularization on high-dimensional data

### Module 03: Logistic Regression
- Binary classification
- Decision boundaries
- Multiclass classification (OvR, OvO)
- Model evaluation metrics
- Exercise: Customer churn prediction

### Module 04: Decision Trees and Random Forests
- Decision tree algorithm
- Tree visualization and interpretation
- Random forest ensemble
- Feature importance
- Exercise: Loan approval prediction

### Module 05: Support Vector Machines
- Linear SVM
- Kernel trick and non-linear SVM
- SVM for classification and regression
- Hyperparameter tuning
- Exercise: Image classification (digits)

### Module 06: Unsupervised Learning
- K-means clustering
- Hierarchical clustering
- DBSCAN
- Cluster evaluation metrics
- Exercise: Customer segmentation

### Module 07: Dimensionality Reduction
- Principal Component Analysis (PCA)
- t-SNE visualization
- Applications in preprocessing
- Exercise: Visualizing high-dimensional data

### Module 08: Model Selection and Evaluation
- Train/test splits and cross-validation
- Hyperparameter tuning strategies
- Model comparison and selection
- Learning curves
- Exercise: Complete ML pipeline

### Module 09: Final Project
- End-to-end ML project
- Data preprocessing
- Model selection and tuning
- Evaluation and interpretation
- Project: Kaggle-style competition dataset

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

## Development Notes

This project needs:
- [ ] 10 Jupyter notebooks covering all modules
- [ ] Multiple datasets for different problem types
- [ ] Complete code examples with detailed comments
- [ ] Practice exercises with solutions
- [ ] Final project with real-world dataset
- [ ] Model comparison framework
- [ ] Visualization of decision boundaries
- [ ] Interactive hyperparameter tuning examples

## References

- DataScience_SelfLearnPath.md - Intermediate Mastery (Months 4-6)
- Scikit-learn user guide: https://scikit-learn.org/stable/user_guide.html
- Andrew Ng's ML Specialization
- "Hands-On Machine Learning" by Aurélien Géron

"""
Prepare sample datasets for Machine Learning Fundamentals notebooks.

This script downloads datasets from scikit-learn and saves them as CSV files
in the data/sample/ directory for use in educational notebooks.
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Create output directory
output_dir = Path(__file__).parent.parent / "data" / "sample"
output_dir.mkdir(parents=True, exist_ok=True)

print("Preparing sample datasets for ML Fundamentals notebooks...")
print(f"Output directory: {output_dir}")

# 1. Iris Dataset (classification - multiclass)
print("\n1. Loading Iris dataset...")
iris = datasets.load_iris()
iris_df = pd.DataFrame(
    data=iris.data,
    columns=iris.feature_names
)
iris_df['species'] = iris.target
iris_df['species_name'] = iris_df['species'].map({
    0: 'setosa', 1: 'versicolor', 2: 'virginica'
})
iris_df.to_csv(output_dir / "iris.csv", index=False)
print(f"   Saved: iris.csv ({len(iris_df)} rows, {len(iris_df.columns)} columns)")

# 2. Wine Dataset (classification - multiclass)
print("\n2. Loading Wine dataset...")
wine = datasets.load_wine()
wine_df = pd.DataFrame(
    data=wine.data,
    columns=wine.feature_names
)
wine_df['target'] = wine.target
wine_df.to_csv(output_dir / "wine.csv", index=False)
print(f"   Saved: wine.csv ({len(wine_df)} rows, {len(wine_df.columns)} columns)")

# 3. Breast Cancer Dataset (classification - binary)
print("\n3. Loading Breast Cancer dataset...")
cancer = datasets.load_breast_cancer()
cancer_df = pd.DataFrame(
    data=cancer.data,
    columns=cancer.feature_names
)
cancer_df['target'] = cancer.target
cancer_df['diagnosis'] = cancer_df['target'].map({0: 'malignant', 1: 'benign'})
cancer_df.to_csv(output_dir / "breast_cancer.csv", index=False)
print(f"   Saved: breast_cancer.csv ({len(cancer_df)} rows, {len(cancer_df.columns)} columns)")

# 4. Diabetes Dataset (regression)
print("\n4. Loading Diabetes dataset...")
diabetes = datasets.load_diabetes()
diabetes_df = pd.DataFrame(
    data=diabetes.data,
    columns=diabetes.feature_names
)
diabetes_df['progression'] = diabetes.target
diabetes_df.to_csv(output_dir / "diabetes.csv", index=False)
print(f"   Saved: diabetes.csv ({len(diabetes_df)} rows, {len(diabetes_df.columns)} columns)")

# 5. Create a synthetic housing dataset (avoid network dependency)
print("\n5. Creating synthetic housing dataset...")
np.random.seed(42)
n_samples = 2000

# Create realistic housing features
housing_data = {
    'MedInc': np.random.uniform(0.5, 15, n_samples),  # Median income
    'HouseAge': np.random.uniform(1, 52, n_samples),  # House age
    'AveRooms': np.random.uniform(2, 10, n_samples),  # Average rooms
    'AveBedrms': np.random.uniform(1, 5, n_samples),  # Average bedrooms
    'Population': np.random.uniform(100, 5000, n_samples),  # Population
    'AveOccup': np.random.uniform(1, 6, n_samples),  # Average occupancy
    'Latitude': np.random.uniform(32, 42, n_samples),  # Latitude
    'Longitude': np.random.uniform(-124, -114, n_samples),  # Longitude
}

housing_df = pd.DataFrame(housing_data)

# Create target with realistic relationship
housing_df['median_house_value'] = (
    housing_df['MedInc'] * 40000 +
    housing_df['AveRooms'] * 10000 -
    housing_df['HouseAge'] * 500 +
    np.random.normal(0, 50000, n_samples)
)

housing_df.to_csv(output_dir / "california_housing.csv", index=False)
print(f"   Saved: california_housing.csv ({len(housing_df)} rows, {len(housing_df.columns)} columns)")

# 6. Digits Dataset (image classification - for visualization)
print("\n6. Loading Digits dataset...")
digits = datasets.load_digits()
# Save images and labels
digits_df = pd.DataFrame(
    data=digits.data,
    columns=[f'pixel_{i}' for i in range(64)]
)
digits_df['digit'] = digits.target
# Sample to reduce size
digits_sample = digits_df.sample(n=500, random_state=42)
digits_sample.to_csv(output_dir / "digits.csv", index=False)
print(f"   Saved: digits.csv ({len(digits_sample)} rows, {len(digits_sample.columns)} columns)")

# 7. Make Classification Dataset (synthetic for teaching)
print("\n7. Creating synthetic classification dataset...")
X_class, y_class = datasets.make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    n_classes=2,
    random_state=42
)
synthetic_class_df = pd.DataFrame(
    data=X_class,
    columns=[f'feature_{i+1}' for i in range(20)]
)
synthetic_class_df['target'] = y_class
synthetic_class_df.to_csv(output_dir / "synthetic_classification.csv", index=False)
print(f"   Saved: synthetic_classification.csv ({len(synthetic_class_df)} rows, {len(synthetic_class_df.columns)} columns)")

# 8. Make Regression Dataset (synthetic for teaching)
print("\n8. Creating synthetic regression dataset...")
X_reg, y_reg = datasets.make_regression(
    n_samples=1000,
    n_features=10,
    n_informative=8,
    noise=15.0,
    random_state=42
)
synthetic_reg_df = pd.DataFrame(
    data=X_reg,
    columns=[f'feature_{i+1}' for i in range(10)]
)
synthetic_reg_df['target'] = y_reg
synthetic_reg_df.to_csv(output_dir / "synthetic_regression.csv", index=False)
print(f"   Saved: synthetic_regression.csv ({len(synthetic_reg_df)} rows, {len(synthetic_reg_df.columns)} columns)")

# 9. Make Blobs Dataset (clustering)
print("\n9. Creating blobs dataset for clustering...")
X_blobs, y_blobs = datasets.make_blobs(
    n_samples=800,
    centers=4,
    n_features=2,
    cluster_std=1.0,
    random_state=42
)
blobs_df = pd.DataFrame(
    data=X_blobs,
    columns=['feature_1', 'feature_2']
)
blobs_df['true_cluster'] = y_blobs
blobs_df.to_csv(output_dir / "blobs_clustering.csv", index=False)
print(f"   Saved: blobs_clustering.csv ({len(blobs_df)} rows, {len(blobs_df.columns)} columns)")

# 10. Make Moons Dataset (non-linear classification)
print("\n10. Creating moons dataset for non-linear classification...")
X_moons, y_moons = datasets.make_moons(
    n_samples=500,
    noise=0.1,
    random_state=42
)
moons_df = pd.DataFrame(
    data=X_moons,
    columns=['feature_1', 'feature_2']
)
moons_df['target'] = y_moons
moons_df.to_csv(output_dir / "moons_nonlinear.csv", index=False)
print(f"   Saved: moons_nonlinear.csv ({len(moons_df)} rows, {len(moons_df.columns)} columns)")

print("\n" + "="*60)
print("✓ All datasets prepared successfully!")
print(f"✓ Location: {output_dir}")
print("="*60)

# Print summary
print("\nDataset Summary:")
print("-" * 60)
print("Classification Datasets:")
print("  - iris.csv (multiclass, 4 features)")
print("  - wine.csv (multiclass, 13 features)")
print("  - breast_cancer.csv (binary, 30 features)")
print("  - synthetic_classification.csv (binary, 20 features)")
print("  - moons_nonlinear.csv (binary, 2 features, non-linear)")
print("\nRegression Datasets:")
print("  - diabetes.csv (10 features)")
print("  - california_housing.csv (8 features, sampled)")
print("  - synthetic_regression.csv (10 features)")
print("\nClustering/Unsupervised:")
print("  - blobs_clustering.csv (2D, 4 clusters)")
print("\nImage Classification:")
print("  - digits.csv (8x8 pixel images, 10 classes)")
print("-" * 60)

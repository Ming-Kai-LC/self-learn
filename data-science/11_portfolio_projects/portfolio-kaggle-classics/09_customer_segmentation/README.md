# Project 09: Customer Segmentation

**Difficulty**: ⭐⭐ Intermediate
**Estimated Time**: 4-5 hours
**Domain**: Marketing Analytics, Unsupervised Learning

## Problem Statement

Customer segmentation is a critical task in marketing analytics that involves dividing a customer base into distinct groups that share similar characteristics. This project focuses on segmenting customers to enable:

- **Targeted Marketing**: Create personalized campaigns for different customer groups
- **Resource Optimization**: Allocate marketing budgets more effectively
- **Customer Retention**: Identify high-value customers and at-risk segments
- **Product Development**: Understand needs of different customer types

The goal is to discover 4-6 meaningful customer segments that can drive actionable business strategies.

## Dataset

This project uses one of the following popular datasets from Kaggle:

1. **Online Retail Dataset** (Recommended)
   - Source: UCI Machine Learning Repository / Kaggle
   - Contains: 500K+ transactions from UK-based online retailer (2010-2011)
   - Features: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country
   - Size: ~20MB
   - [Kaggle Link](https://www.kaggle.com/datasets/vijayuv/onlineretail)

2. **Mall Customer Dataset** (Alternative)
   - Source: Kaggle
   - Contains: 200 customer records from mall
   - Features: CustomerID, Gender, Age, Annual Income, Spending Score
   - Size: Small (~5KB)
   - [Kaggle Link](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

**Note**: Download the dataset from Kaggle and place it in the `data/` directory (not included in repo due to size).

## Methodology

### 1. RFM Analysis

**RFM** is a proven technique for customer segmentation based on:
- **Recency (R)**: How recently did the customer make a purchase?
- **Frequency (F)**: How often do they purchase?
- **Monetary (M)**: How much do they spend?

RFM scores are calculated and used as features for clustering.

### 2. Clustering Methods

Multiple clustering algorithms are explored and compared:

#### K-Means Clustering
- **Type**: Partitioning-based
- **Pros**: Fast, scalable, works well with spherical clusters
- **Cons**: Requires predefined K, sensitive to outliers
- **Use Case**: General-purpose segmentation

#### DBSCAN (Density-Based Spatial Clustering)
- **Type**: Density-based
- **Pros**: Finds arbitrarily shaped clusters, identifies outliers
- **Cons**: Sensitive to parameters (eps, min_samples)
- **Use Case**: Identifying core customer groups and outliers

#### Hierarchical Clustering
- **Type**: Agglomerative (bottom-up)
- **Pros**: Creates dendrogram for visual analysis, no need to specify K upfront
- **Cons**: Computationally expensive for large datasets
- **Use Case**: Understanding cluster hierarchy and relationships

#### Gaussian Mixture Models (GMM)
- **Type**: Probabilistic
- **Pros**: Soft clustering (probability of belonging to each cluster), flexible cluster shapes
- **Cons**: Can overfit, sensitive to initialization
- **Use Case**: When cluster boundaries are fuzzy

### 3. Determining Optimal K

- **Elbow Method**: Plot within-cluster sum of squares (WCSS) vs. K
- **Silhouette Analysis**: Measure how similar objects are to their own cluster vs. other clusters
- **Business Constraints**: Consider practical limits (e.g., marketing team can handle 4-6 segments)

### 4. Dimensionality Reduction for Visualization

High-dimensional customer data is visualized using:

- **PCA (Principal Component Analysis)**: Linear dimensionality reduction preserving variance
- **t-SNE (t-Distributed Stochastic Neighbor Embedding)**: Non-linear reduction preserving local structure

These techniques reduce features to 2D for visualization while maintaining cluster separation.

## Tech Stack

- **Data Manipulation**: pandas, numpy
- **Machine Learning**: scikit-learn
- **Statistical Analysis**: scipy
- **Visualization**: matplotlib, seaborn
- **Environment**: Jupyter Notebook

## Project Structure

```
09_customer_segmentation/
├── README.md                          # This file
├── customer_segmentation.ipynb        # Main analysis notebook
├── requirements.txt                   # Python dependencies
└── data/                              # Data directory (not in repo)
    └── online_retail.csv              # Download from Kaggle
```

## Expected Outcomes

### 4-6 Distinct Customer Segments

Example segments (will vary based on actual data):

1. **Champions**: High RFM scores - Best customers, recent and frequent buyers with high spend
2. **Loyal Customers**: High frequency, moderate recency and monetary
3. **Big Spenders**: High monetary, lower frequency
4. **At-Risk**: High monetary but low recency - Were valuable, now inactive
5. **Lost Customers**: Low recency, frequency, and monetary - Need reactivation campaigns
6. **New Customers**: Recent but low frequency/monetary - Potential for growth

### Business Insights

Each segment will be profiled with:
- **Size**: Number of customers and % of total
- **Characteristics**: Average RFM scores, demographics
- **Value**: Total and average revenue contribution
- **Behavior Patterns**: Purchase frequency, product preferences

### Marketing Recommendations

Actionable strategies for each segment:
- **Retention tactics** for at-risk customers
- **Upselling opportunities** for big spenders
- **Loyalty programs** for champions
- **Win-back campaigns** for lost customers

## Learning Objectives

By completing this project, you will:

1. Understand and implement RFM analysis for customer behavior
2. Apply multiple clustering algorithms and compare their results
3. Use elbow method and silhouette analysis to determine optimal clusters
4. Visualize high-dimensional data using PCA and t-SNE
5. Profile and interpret customer segments
6. Translate analytical findings into business recommendations
7. Evaluate clustering quality using multiple metrics

## Prerequisites

- Understanding of unsupervised learning concepts
- Familiarity with pandas for data manipulation
- Basic knowledge of scikit-learn
- Understanding of distance metrics and clustering fundamentals

## Getting Started

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download Dataset**:
   - Go to [Online Retail Dataset on Kaggle](https://www.kaggle.com/datasets/vijayuv/onlineretail)
   - Download `online_retail.csv`
   - Create `data/` directory and place the file there

3. **Run Notebook**:
   ```bash
   jupyter notebook customer_segmentation.ipynb
   ```

4. **Follow Along**:
   - Execute cells sequentially
   - Complete exercises to reinforce learning
   - Experiment with different parameters

## Key Concepts Covered

- **RFM Analysis**: Customer value metrics
- **Feature Engineering**: Creating customer-level aggregations
- **Clustering Algorithms**: K-Means, DBSCAN, Hierarchical, GMM
- **Cluster Validation**: Elbow method, silhouette score, Davies-Bouldin index
- **Dimensionality Reduction**: PCA and t-SNE
- **Data Preprocessing**: Scaling, handling missing values
- **Business Analytics**: Translating clusters to actionable insights

## Extensions and Next Steps

- **Predictive Modeling**: Build classifier to assign new customers to segments
- **Time Series Analysis**: Track how customers move between segments over time
- **Advanced Features**: Include product categories, browsing behavior
- **A/B Testing**: Test different marketing strategies per segment
- **Customer Lifetime Value (CLV)**: Calculate and predict CLV per segment

## References

- [Customer Segmentation using K-Means](https://www.scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)
- [RFM Analysis for Customer Segmentation](https://www.putler.com/rfm-analysis/)
- [Comparing Clustering Algorithms](https://scikit-learn.org/stable/modules/clustering.html)
- [t-SNE Visualization](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

## Author Notes

This project demonstrates the complete workflow of customer segmentation from raw transaction data to actionable business recommendations. The techniques learned here are directly applicable to real-world marketing analytics and customer relationship management.

**Difficulty Justification**: ⭐⭐ Intermediate
- Requires understanding of multiple clustering algorithms
- Involves feature engineering and RFM calculations
- Needs interpretation of business context
- More complex than basic supervised learning projects

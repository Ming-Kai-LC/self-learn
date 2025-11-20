# Project 07: Movie Recommendation System (⭐⭐ Intermediate)

## Problem Statement

Build a collaborative filtering recommendation engine that suggests movies to users based on their historical ratings and preferences. The system should handle sparse rating matrices and provide personalized recommendations using various collaborative filtering techniques.

## Dataset

**MovieLens Dataset** (100K or 1M version)
- **Source**: [MovieLens by GroupLens](https://grouplens.org/datasets/movielens/)
- **Size**:
  - 100K: ~100,000 ratings from 943 users on 1,682 movies
  - 1M: ~1,000,000 ratings from 6,040 users on 3,706 movies
- **Features**:
  - User ID, Movie ID, Rating (1-5 stars), Timestamp
  - Movie metadata: Title, genres
  - User demographics: Age, gender, occupation

## Approaches

This project implements and compares multiple recommendation techniques:

1. **User-Based Collaborative Filtering**
   - Find similar users based on rating patterns
   - Recommend items liked by similar users
   - Uses cosine similarity or Pearson correlation

2. **Item-Based Collaborative Filtering**
   - Find similar items based on user ratings
   - Recommend items similar to what user has liked
   - More stable than user-based for sparse data

3. **Matrix Factorization (SVD)**
   - Singular Value Decomposition for dimensionality reduction
   - Learns latent factors for users and items
   - Handles sparsity better than memory-based methods

4. **SVD++ (Advanced Matrix Factorization)**
   - Extension of SVD with implicit feedback
   - Incorporates both explicit ratings and implicit signals
   - Generally achieves better accuracy

5. **Hybrid Approach**
   - Combines multiple methods for improved performance
   - Weighted average or switching strategies
   - Balances accuracy and coverage

## Evaluation Metrics

- **RMSE** (Root Mean Squared Error): Measures prediction accuracy for ratings
- **MAE** (Mean Absolute Error): Average absolute difference between predicted and actual ratings
- **Precision@K**: Proportion of recommended items that are relevant (top K recommendations)
- **Recall@K**: Proportion of relevant items that are recommended (top K recommendations)
- **Coverage**: Percentage of items that can be recommended

## Tech Stack

- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Machine Learning**: scikit-learn, scipy
- **Recommendation Systems**: scikit-surprise (specialized library for recommendation algorithms)
- **Development**: Jupyter notebook

## Expected Performance

- **Target RMSE**: < 0.90
- **Typical Results**:
  - User-based CF: RMSE ~0.95-1.00
  - Item-based CF: RMSE ~0.92-0.98
  - SVD: RMSE ~0.87-0.92
  - SVD++: RMSE ~0.86-0.90
  - Hybrid: RMSE ~0.85-0.88

## Demo Features

The notebook includes a function to get top-N recommendations for any user:

```python
def get_recommendations(user_id, n=10, model='svd'):
    """
    Get top-N movie recommendations for a user

    Parameters:
    - user_id: ID of the user
    - n: Number of recommendations to return
    - model: Model to use ('user_cf', 'item_cf', 'svd', 'svdpp', 'hybrid')

    Returns:
    - DataFrame with movie titles, predicted ratings, and genres
    """
    # Implementation in notebook
    pass
```

## Key Insights

1. **Sparsity Challenge**: Rating matrices are typically 95%+ sparse, requiring sophisticated techniques
2. **Cold Start Problem**: Difficult to recommend for new users/items with no ratings
3. **Scalability**: Memory-based methods (user/item CF) struggle with large datasets
4. **Model-Based Advantage**: Matrix factorization scales better and handles sparsity well
5. **Hybrid Benefits**: Combining approaches improves both accuracy and coverage

## Learning Objectives

By completing this project, you will:
- Understand collaborative filtering principles (user-based vs item-based)
- Implement memory-based and model-based recommendation systems
- Handle sparse matrices and similarity computations
- Apply matrix factorization techniques (SVD, SVD++)
- Evaluate recommendation systems with appropriate metrics
- Address cold start and scalability challenges
- Build a production-ready recommendation function

## Project Structure

```
07_movie_recommendations/
├── README.md                        # This file
├── movie_recommendations.ipynb      # Main analysis notebook
├── requirements.txt                 # Python dependencies
└── data/                           # Dataset directory (download separately)
    ├── ml-100k/                    # MovieLens 100K dataset
    └── ml-1m/                      # MovieLens 1M dataset (optional)
```

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Download dataset**:
   - Visit [MovieLens](https://grouplens.org/datasets/movielens/)
   - Download MovieLens 100K or 1M dataset
   - Extract to `data/ml-100k/` or `data/ml-1m/`

3. **Run notebook**:
   ```bash
   jupyter notebook movie_recommendations.ipynb
   ```

## Next Steps

After completing this project, consider:
- **Content-Based Filtering**: Use movie metadata (genres, actors, directors)
- **Deep Learning**: Neural collaborative filtering with embeddings
- **Context-Aware**: Incorporate temporal dynamics and user context
- **Explainability**: Generate explanations for recommendations
- **Production**: Deploy as REST API with Flask/FastAPI

## References

- [Surprise Documentation](http://surpriselib.com/)
- [MovieLens Dataset](https://grouplens.org/datasets/movielens/)
- [Collaborative Filtering Tutorial](https://realpython.com/build-recommendation-engine-collaborative-filtering/)
- Research Paper: [Matrix Factorization Techniques for Recommender Systems](https://datajobs.com/data-science-repo/Recommender-Systems-[Netflix].pdf)

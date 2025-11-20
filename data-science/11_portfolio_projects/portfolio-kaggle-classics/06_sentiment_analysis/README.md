# Project 06: Sentiment Analysis System (⭐⭐ Intermediate)

## Problem Statement

Build a Natural Language Processing (NLP) sentiment classifier to automatically determine whether movie reviews are positive or negative. This project demonstrates end-to-end machine learning pipeline development, from text preprocessing to model deployment.

**Business Value**: Sentiment analysis is crucial for:
- Product review monitoring
- Social media sentiment tracking
- Customer feedback analysis
- Brand reputation management
- Market research and consumer insights

## Dataset

**IMDB Movie Reviews Dataset**
- **Size**: 50,000 movie reviews
- **Split**: 25,000 training, 25,000 testing
- **Classes**: Binary (Positive/Negative)
- **Balance**: 50% positive, 50% negative
- **Source**: [Stanford AI Lab - IMDB Dataset](http://ai.stanford.edu/~amaas/data/sentiment/)

**Note**: This project includes instructions to download the dataset. Due to size constraints, the dataset is not included in the repository.

## Approach

### 1. Data Exploration
- Word clouds for positive/negative reviews
- Review length distribution analysis
- Word frequency analysis
- Class balance verification

### 2. Text Preprocessing Pipeline
- Lowercasing and normalization
- HTML tag removal
- Punctuation and special character handling
- Stopword removal (NLTK)
- Stemming (Porter Stemmer) and Lemmatization (WordNet)
- Text cleaning and tokenization

### 3. Feature Engineering
- **TF-IDF (Term Frequency-Inverse Document Frequency)**
  - Unigrams and bigrams
  - Max features: 5,000-10,000

- **Word2Vec Embeddings**
  - Pre-trained vectors (Google News 300d) or custom training
  - Document embeddings via averaging

### 4. Models Implemented

| Model | Type | Key Features |
|-------|------|--------------|
| **Naive Bayes** | Traditional ML | Fast, probabilistic, baseline |
| **Logistic Regression** | Traditional ML | Interpretable, regularization |
| **Random Forest** | Ensemble | Handles non-linearity, feature importance |
| **LSTM Neural Network** | Deep Learning | Captures sequential patterns, state-of-the-art |

### 5. Evaluation Metrics
- Accuracy
- Precision, Recall, F1-Score
- Confusion Matrix
- ROC-AUC Curve
- Classification Report

### 6. Model Interpretability
- Feature importance analysis
- Most influential words per class
- Misclassification error analysis
- Example predictions with explanations

## Tech Stack

### Core Libraries
- **pandas** (1.5+): Data manipulation
- **numpy** (1.23+): Numerical operations
- **matplotlib** (3.7+): Visualization
- **seaborn** (0.12+): Statistical visualizations

### NLP & Machine Learning
- **nltk** (3.8+): Text preprocessing, tokenization, stopwords
- **scikit-learn** (1.3+): TF-IDF, traditional ML models, evaluation
- **tensorflow** (2.13+) or **pytorch** (2.0+): Deep learning (LSTM)
- **gensim** (4.3+): Word2Vec embeddings (optional)

### Visualization
- **wordcloud** (1.9+): Word cloud generation

### Deployment
- **fastapi** (0.100+): REST API framework
- **uvicorn** (0.23+): ASGI server
- **pydantic** (2.0+): Data validation

## Expected Results

| Model | Accuracy | F1-Score | Training Time |
|-------|----------|----------|---------------|
| Naive Bayes | 83-85% | 0.83-0.85 | < 1 min |
| Logistic Regression | 87-89% | 0.87-0.89 | 2-5 min |
| Random Forest | 84-86% | 0.84-0.86 | 5-10 min |
| LSTM | 88-90% | 0.88-0.90 | 15-30 min |

**Best Model**: LSTM typically achieves the highest accuracy (88-90%) but requires more computational resources.

**Production Recommendation**: Logistic Regression offers best balance of performance (87-89%) and inference speed.

## Project Structure

```
06_sentiment_analysis/
├── README.md                    # This file
├── sentiment_analysis.ipynb     # Main analysis notebook
├── requirements.txt             # Python dependencies
├── api.py                       # FastAPI deployment (optional)
├── models/                      # Saved model files (gitignored)
│   ├── best_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── label_encoder.pkl
└── data/                        # Dataset directory (gitignored)
    ├── train/
    │   ├── pos/
    │   └── neg/
    └── test/
        ├── pos/
        └── neg/
```

## Installation

### 1. Clone Repository

```bash
cd data-science/11_portfolio_projects/portfolio-kaggle-classics/06_sentiment_analysis
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')
```

### 5. Download Dataset

**Option A: Manual Download**
1. Visit [Stanford IMDB Dataset](http://ai.stanford.edu/~amaas/data/sentiment/)
2. Download `aclImdb_v1.tar.gz`
3. Extract to `data/` directory

**Option B: Command Line**
```bash
# Download dataset
wget http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz

# Extract
tar -xzf aclImdb_v1.tar.gz -C data/

# Clean up
rm aclImdb_v1.tar.gz
```

## Usage

### Running the Notebook

```bash
# Start Jupyter
jupyter notebook sentiment_analysis.ipynb
```

**Workflow**:
1. Run all cells: `Cell > Run All`
2. Explore data visualizations
3. Review model performance metrics
4. Analyze misclassified examples
5. Export best model for deployment

### Deploying the API

```bash
# Start FastAPI server
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

**API Endpoints**:

```bash
# Health check
curl http://localhost:8000/

# Predict sentiment
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie was absolutely amazing! Best film of the year."}'

# Expected response:
# {
#   "text": "This movie was absolutely amazing! Best film of the year.",
#   "sentiment": "positive",
#   "confidence": 0.95,
#   "model": "logistic_regression"
# }
```

**Interactive Documentation**: Visit `http://localhost:8000/docs` for Swagger UI

## Key Learnings

### Technical Skills
1. **Text Preprocessing**: Complete NLP pipeline from raw text to clean tokens
2. **Feature Engineering**: TF-IDF and Word2Vec for text representation
3. **Model Comparison**: Evaluating traditional ML vs deep learning approaches
4. **Error Analysis**: Understanding model failures and limitations
5. **API Development**: Deploying ML models as production-ready services

### Best Practices
- Always validate data loading with assertions
- Use train/test split from source (avoid data leakage)
- Set random seeds for reproducibility
- Balance model complexity vs interpretability
- Document preprocessing steps for deployment consistency

### Common Pitfalls Avoided
- ✅ Removing HTML tags and special characters
- ✅ Handling class imbalance (dataset is balanced)
- ✅ Preventing data leakage (fit vectorizer on train only)
- ✅ Testing on truly unseen data
- ✅ Saving preprocessing artifacts with model

## Extensions and Improvements

### Beginner Enhancements
- [ ] Add simple word count features
- [ ] Visualize most common positive/negative words
- [ ] Test on custom movie reviews

### Intermediate Enhancements
- [ ] Experiment with different n-gram ranges
- [ ] Try ensemble methods (voting, stacking)
- [ ] Add cross-validation for robust evaluation
- [ ] Implement GridSearchCV for hyperparameter tuning

### Advanced Enhancements
- [ ] Use BERT or transformer models (Hugging Face)
- [ ] Multi-class sentiment (positive, neutral, negative)
- [ ] Aspect-based sentiment analysis
- [ ] Real-time streaming sentiment analysis
- [ ] Deploy to cloud (AWS Lambda, GCP Cloud Run)
- [ ] A/B testing different models in production

## Resources

### Datasets
- [IMDB Movie Reviews](http://ai.stanford.edu/~amaas/data/sentiment/)
- [Twitter Sentiment140](http://help.sentiment140.com/for-students)
- [Amazon Product Reviews](https://nijianmo.github.io/amazon/index.html)

### Tutorials
- [NLTK Book](https://www.nltk.org/book/)
- [Scikit-learn Text Classification](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)
- [TensorFlow Text Classification](https://www.tensorflow.org/tutorials/keras/text_classification)

### Papers
- [Maas et al., 2011 - Learning Word Vectors for Sentiment Analysis](http://ai.stanford.edu/~amaas/papers/wvSent_acl2011.pdf)
- [Kim, 2014 - Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882)

## License

This project is for educational purposes. The IMDB dataset has its own license terms.

## Author

Created as part of the Data Science Portfolio Project series.

**Difficulty**: ⭐⭐ Intermediate
**Estimated Time**: 6-8 hours
**Prerequisites**:
- Python programming
- Pandas and NumPy basics
- Basic machine learning concepts
- Understanding of classification metrics

---

**Next Project**: [Project 07 - Credit Card Fraud Detection](../07_credit_card_fraud/)

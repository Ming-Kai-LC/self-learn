"""
FastAPI Sentiment Analysis API

Provides REST endpoints for real-time sentiment prediction on movie reviews.

Usage:
    uvicorn api:app --reload --host 0.0.0.0 --port 8000

Endpoints:
    GET  /                  - Health check and API info
    POST /predict          - Predict sentiment for a single review
    POST /predict/batch    - Predict sentiment for multiple reviews
    GET  /model/info       - Get model information and statistics
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List, Dict, Any, Optional
import pickle
import re
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup
import numpy as np

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="Real-time sentiment analysis for movie reviews using machine learning",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Global variables for model and preprocessing tools
model = None
vectorizer = None
preprocessing_config = None
stop_words = None
lemmatizer = None

# Model metadata
MODEL_INFO = {
    "model_type": "Logistic Regression",
    "training_accuracy": 0.88,
    "features": "TF-IDF (unigrams + bigrams)",
    "vocabulary_size": 10000,
    "trained_on": "IMDB Movie Reviews Dataset (50,000 reviews)"
}


class ReviewRequest(BaseModel):
    """Request model for single review prediction"""
    text: str = Field(
        ...,
        min_length=10,
        max_length=10000,
        description="Movie review text to analyze",
        example="This movie was absolutely fantastic! The acting was superb."
    )

    @validator('text')
    def validate_text(cls, v):
        if not v.strip():
            raise ValueError("Review text cannot be empty")
        return v


class BatchReviewRequest(BaseModel):
    """Request model for batch prediction"""
    reviews: List[str] = Field(
        ...,
        min_items=1,
        max_items=100,
        description="List of movie reviews to analyze (max 100)",
        example=[
            "Great movie! Highly recommended.",
            "Terrible waste of time. Very disappointed."
        ]
    )

    @validator('reviews')
    def validate_reviews(cls, v):
        if any(not text.strip() for text in v):
            raise ValueError("Reviews cannot be empty")
        return v


class SentimentResponse(BaseModel):
    """Response model for sentiment prediction"""
    text: str = Field(..., description="Original review text")
    sentiment: str = Field(..., description="Predicted sentiment (positive/negative)")
    confidence: float = Field(..., description="Prediction confidence (0-1)")
    probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution over classes"
    )


class BatchSentimentResponse(BaseModel):
    """Response model for batch predictions"""
    results: List[SentimentResponse]
    count: int = Field(..., description="Number of reviews processed")
    summary: Dict[str, int] = Field(
        ...,
        description="Summary statistics (positive/negative counts)"
    )


def load_models():
    """
    Load trained model and preprocessing artifacts from disk.

    This function is called on app startup to load all necessary components.
    """
    global model, vectorizer, preprocessing_config, stop_words, lemmatizer

    models_dir = Path("models")

    # Check if models directory exists
    if not models_dir.exists():
        raise FileNotFoundError(
            f"Models directory not found: {models_dir}\n"
            "Please train the model first by running the Jupyter notebook."
        )

    # Load Logistic Regression model
    model_path = models_dir / "logistic_regression_model.pkl"
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")

    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print(f"✓ Loaded model from {model_path}")

    # Load TF-IDF vectorizer
    vectorizer_path = models_dir / "tfidf_vectorizer.pkl"
    if not vectorizer_path.exists():
        raise FileNotFoundError(f"Vectorizer file not found: {vectorizer_path}")

    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)
    print(f"✓ Loaded vectorizer from {vectorizer_path}")

    # Load preprocessing config
    config_path = models_dir / "preprocessing_config.pkl"
    if config_path.exists():
        with open(config_path, 'rb') as f:
            preprocessing_config = pickle.load(f)
        print(f"✓ Loaded preprocessing config from {config_path}")
    else:
        # Default config
        preprocessing_config = {
            'use_stemming': False,
            'use_lemmatization': True,
            'remove_stopwords': True
        }

    # Initialize NLTK components
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading NLTK stopwords...")
        nltk.download('stopwords', quiet=True)

    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("Downloading NLTK punkt...")
        nltk.download('punkt', quiet=True)

    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        print("Downloading NLTK wordnet...")
        nltk.download('wordnet', quiet=True)
        nltk.download('omw-1.4', quiet=True)

    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    print("✓ All models and preprocessing tools loaded successfully")


def preprocess_text(text: str) -> str:
    """
    Preprocess text using the same pipeline as training.

    Steps:
    1. Remove HTML tags
    2. Convert to lowercase
    3. Remove URLs
    4. Remove special characters and numbers
    5. Tokenization
    6. Remove stopwords
    7. Lemmatization

    Args:
        text: Raw review text

    Returns:
        Cleaned and preprocessed text
    """
    # Remove HTML tags
    text = BeautifulSoup(text, 'html.parser').get_text()

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', ' ', text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    if preprocessing_config.get('remove_stopwords', True):
        tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    if preprocessing_config.get('use_lemmatization', True):
        tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join tokens back into string
    cleaned_text = ' '.join(tokens)

    return cleaned_text


def predict_sentiment(text: str) -> Dict[str, Any]:
    """
    Predict sentiment for a single review.

    Args:
        text: Raw review text

    Returns:
        Dictionary with sentiment, confidence, and probabilities
    """
    # Preprocess text
    cleaned = preprocess_text(text)

    # Handle empty text after preprocessing
    if not cleaned.strip():
        return {
            'text': text,
            'sentiment': 'neutral',
            'confidence': 0.5,
            'probabilities': {'negative': 0.5, 'positive': 0.5}
        }

    # Vectorize
    features = vectorizer.transform([cleaned])

    # Predict
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]

    sentiment = 'positive' if prediction == 1 else 'negative'
    confidence = probabilities[prediction]

    return {
        'text': text,
        'sentiment': sentiment,
        'confidence': float(confidence),
        'probabilities': {
            'negative': float(probabilities[0]),
            'positive': float(probabilities[1])
        }
    }


@app.on_event("startup")
async def startup_event():
    """
    Load models when the API starts.
    """
    try:
        load_models()
    except Exception as e:
        print(f"ERROR: Failed to load models: {e}")
        print("API will not function properly until models are loaded.")


@app.get("/", tags=["Info"])
async def root():
    """
    Health check endpoint - returns API status and basic info.
    """
    return {
        "status": "online",
        "message": "Sentiment Analysis API is running",
        "version": "1.0.0",
        "endpoints": {
            "predict": "POST /predict - Predict sentiment for a single review",
            "batch_predict": "POST /predict/batch - Predict sentiment for multiple reviews",
            "model_info": "GET /model/info - Get model information",
            "docs": "GET /docs - Interactive API documentation",
        }
    }


@app.post("/predict", response_model=SentimentResponse, tags=["Prediction"])
async def predict(request: ReviewRequest):
    """
    Predict sentiment for a single movie review.

    **Request Body:**
    - `text`: Review text (10-10,000 characters)

    **Response:**
    - `text`: Original review text
    - `sentiment`: Predicted sentiment (positive/negative)
    - `confidence`: Prediction confidence (0-1)
    - `probabilities`: Probability distribution over classes

    **Example:**
    ```json
    {
        "text": "This movie was absolutely fantastic! Best film of the year."
    }
    ```
    """
    if model is None or vectorizer is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please ensure models are trained and available."
        )

    try:
        result = predict_sentiment(request.text)
        return SentimentResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


@app.post("/predict/batch", response_model=BatchSentimentResponse, tags=["Prediction"])
async def predict_batch(request: BatchReviewRequest):
    """
    Predict sentiment for multiple movie reviews (batch processing).

    **Request Body:**
    - `reviews`: List of review texts (1-100 reviews)

    **Response:**
    - `results`: List of individual predictions
    - `count`: Number of reviews processed
    - `summary`: Summary statistics (positive/negative counts)

    **Example:**
    ```json
    {
        "reviews": [
            "Great movie! Highly recommended.",
            "Terrible waste of time. Very disappointed."
        ]
    }
    ```
    """
    if model is None or vectorizer is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please ensure models are trained and available."
        )

    try:
        # Predict for all reviews
        results = [predict_sentiment(text) for text in request.reviews]

        # Calculate summary statistics
        positive_count = sum(1 for r in results if r['sentiment'] == 'positive')
        negative_count = sum(1 for r in results if r['sentiment'] == 'negative')

        return BatchSentimentResponse(
            results=[SentimentResponse(**r) for r in results],
            count=len(results),
            summary={
                "positive": positive_count,
                "negative": negative_count
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch prediction failed: {str(e)}")


@app.get("/model/info", tags=["Info"])
async def model_info():
    """
    Get information about the loaded model.

    **Response:**
    - Model type and architecture
    - Training accuracy
    - Feature engineering details
    - Dataset information
    """
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please ensure models are trained and available."
        )

    # Get vocabulary size from vectorizer
    vocab_size = len(vectorizer.get_feature_names_out()) if vectorizer else 0

    return {
        **MODEL_INFO,
        "vocabulary_size": vocab_size,
        "preprocessing": preprocessing_config,
        "model_loaded": model is not None,
        "vectorizer_loaded": vectorizer is not None
    }


# Health check for monitoring
@app.get("/health", tags=["Info"])
async def health_check():
    """
    Health check endpoint for monitoring systems.
    """
    is_healthy = model is not None and vectorizer is not None

    return {
        "status": "healthy" if is_healthy else "unhealthy",
        "model_loaded": model is not None,
        "vectorizer_loaded": vectorizer is not None
    }


if __name__ == "__main__":
    import uvicorn

    # Run the API
    print("Starting Sentiment Analysis API...")
    print("Visit http://localhost:8000/docs for interactive documentation")

    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

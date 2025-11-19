"""
FastAPI Application for ML Model Serving
Used in Module 04: Creating ML APIs with FastAPI

This is a production-ready example of serving ML models via REST API.

Run with: uvicorn fastapi_app:app --reload
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
import joblib
import numpy as np
from typing import List, Dict, Any
import logging
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import Response
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Prometheus metrics
PREDICTION_COUNTER = Counter('predictions_total', 'Total number of predictions made')
PREDICTION_LATENCY = Histogram('prediction_latency_seconds', 'Prediction latency in seconds')
ERROR_COUNTER = Counter('prediction_errors_total', 'Total number of prediction errors')

# Initialize FastAPI app
app = FastAPI(
    title="ML Model Serving API",
    description="Production-ready API for serving machine learning models",
    version="1.0.0",
)

# Global model variable
model = None


# Request schema
class PredictionRequest(BaseModel):
    """Schema for prediction requests"""
    features: List[float] = Field(..., min_items=20, max_items=20)

    @validator('features')
    def validate_features(cls, v):
        """Validate that features are valid numbers"""
        if not all(isinstance(x, (int, float)) for x in v):
            raise ValueError('All features must be numeric')
        if any(np.isnan(x) or np.isinf(x) for x in v):
            raise ValueError('Features cannot contain NaN or infinite values')
        return v

    class Config:
        schema_extra = {
            "example": {
                "features": [0.5] * 20
            }
        }


# Response schema
class PredictionResponse(BaseModel):
    """Schema for prediction responses"""
    prediction: int = Field(..., ge=0, le=1)
    probability: float = Field(..., ge=0.0, le=1.0)
    model_version: str
    prediction_time_ms: float


class HealthResponse(BaseModel):
    """Schema for health check responses"""
    status: str
    model_loaded: bool
    version: str


@app.on_event("startup")
async def load_model():
    """Load model on application startup"""
    global model
    try:
        # In production, load from model registry or cloud storage
        # model = joblib.load('models/model.pkl')
        # For this example, we'll use a dummy model
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        # Fit with dummy data
        X_dummy = np.random.randn(100, 20)
        y_dummy = np.random.randint(0, 2, 100)
        model.fit(X_dummy, y_dummy)

        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        raise


@app.get("/", tags=["General"])
async def root():
    """Root endpoint"""
    return {
        "message": "ML Model Serving API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "metrics": "/metrics",
            "docs": "/docs"
        }
    }


@app.get("/health", response_model=HealthResponse, tags=["General"])
async def health_check():
    """Health check endpoint for load balancers and monitoring"""
    return HealthResponse(
        status="healthy" if model is not None else "unhealthy",
        model_loaded=model is not None,
        version="1.0.0"
    )


@app.post("/predict", response_model=PredictionResponse, tags=["Predictions"])
async def predict(request: PredictionRequest):
    """
    Make a prediction using the loaded model

    - **features**: List of 20 numeric features
    - Returns prediction (0 or 1), probability, and metadata
    """
    if model is None:
        ERROR_COUNTER.inc()
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model not loaded"
        )

    try:
        # Track prediction count
        PREDICTION_COUNTER.inc()

        # Time the prediction
        start_time = time.time()

        # Prepare input
        features_array = np.array(request.features).reshape(1, -1)

        # Make prediction
        with PREDICTION_LATENCY.time():
            prediction = int(model.predict(features_array)[0])
            probability = float(model.predict_proba(features_array)[0][1])

        prediction_time_ms = (time.time() - start_time) * 1000

        logger.info(f"Prediction made: {prediction} (probability: {probability:.4f})")

        return PredictionResponse(
            prediction=prediction,
            probability=probability,
            model_version="1.0.0",
            prediction_time_ms=prediction_time_ms
        )

    except Exception as e:
        ERROR_COUNTER.inc()
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Prediction failed: {str(e)}"
        )


@app.get("/metrics", tags=["Monitoring"])
async def metrics():
    """Prometheus metrics endpoint"""
    return Response(content=generate_latest(), media_type="text/plain")


@app.post("/batch-predict", tags=["Predictions"])
async def batch_predict(requests: List[PredictionRequest]):
    """
    Make batch predictions for multiple samples

    Useful for batch inference scenarios
    """
    if model is None:
        ERROR_COUNTER.inc()
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model not loaded"
        )

    if len(requests) > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Batch size exceeds maximum of 100"
        )

    try:
        results = []
        for req in requests:
            features_array = np.array(req.features).reshape(1, -1)
            prediction = int(model.predict(features_array)[0])
            probability = float(model.predict_proba(features_array)[0][1])

            results.append({
                "prediction": prediction,
                "probability": probability
            })

        PREDICTION_COUNTER.inc(len(requests))
        logger.info(f"Batch prediction completed for {len(requests)} samples")

        return {"predictions": results, "count": len(results)}

    except Exception as e:
        ERROR_COUNTER.inc()
        logger.error(f"Batch prediction failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Batch prediction failed: {str(e)}"
        )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    ERROR_COUNTER.inc()
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

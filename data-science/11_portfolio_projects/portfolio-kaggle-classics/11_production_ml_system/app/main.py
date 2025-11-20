"""
FastAPI ML Production System
Endpoints: /predict, /health, /metrics
Features: Model versioning, caching, logging, monitoring
"""

import os
import json
import hashlib
import uuid
from datetime import datetime
from typing import Dict, Optional

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
import redis

from app.model import get_model, MLModel
from app.database import init_db, get_db, PredictionLog
from app.monitoring import (
    metrics_endpoint,
    predictions_total,
    prediction_latency,
    prediction_distribution,
    prediction_mean,
    prediction_std,
    prediction_errors,
    cache_hits,
    cache_misses
)

# Initialize FastAPI app
app = FastAPI(
    title="Production ML System",
    description="End-to-end ML system with monitoring, caching, and logging",
    version="1.0.0"
)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    """
    Initialize database and load model on application startup
    """
    init_db()
    # Preload model
    get_model()
    print("✓ Application started successfully")


# Redis connection (with fallback if Redis is not available)
def get_redis_client():
    """
    Get Redis client for caching
    Returns None if Redis is not available
    """
    try:
        redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
        client = redis.from_url(redis_url, decode_responses=True)
        # Test connection
        client.ping()
        return client
    except Exception as e:
        print(f"Warning: Redis not available: {e}")
        return None


redis_client = get_redis_client()


# Pydantic models for request/response validation
class PredictionRequest(BaseModel):
    """
    Request body for prediction endpoint
    Features should be a dictionary of feature_name: value
    """
    features: Dict[str, float] = Field(
        ...,
        description="Dictionary of feature names and values",
        example={
            "feature_1": 0.5,
            "feature_2": 1.2,
            "feature_3": -0.3
        }
    )
    use_cache: bool = Field(
        True,
        description="Whether to use cached predictions if available"
    )


class PredictionResponse(BaseModel):
    """
    Response from prediction endpoint
    """
    request_id: str
    prediction: float
    probability: Optional[float] = None
    model_version: str
    latency_ms: float
    cached: bool = False
    timestamp: str


class HealthResponse(BaseModel):
    """
    Response from health check endpoint
    """
    status: str
    model_version: str
    database_connected: bool
    redis_connected: bool
    timestamp: str


def log_prediction_background(
    db: Session,
    request_id: str,
    model_version: str,
    features: Dict,
    prediction: float,
    probability: Optional[float],
    latency_ms: float
):
    """
    Background task to log prediction to database
    Runs asynchronously to not block the response
    """
    try:
        log_entry = PredictionLog(
            request_id=request_id,
            timestamp=datetime.utcnow(),
            model_version=model_version,
            input_features=features,
            prediction=prediction,
            prediction_proba=probability,
            latency_ms=latency_ms
        )
        db.add(log_entry)
        db.commit()
    except Exception as e:
        print(f"Error logging prediction: {e}")
        db.rollback()


def get_cache_key(features: Dict) -> str:
    """
    Generate cache key from features
    Uses hash of sorted features to ensure consistency
    """
    features_str = json.dumps(features, sort_keys=True)
    return f"prediction:{hashlib.md5(features_str.encode()).hexdigest()}"


@app.post("/predict", response_model=PredictionResponse)
async def predict(
    request: PredictionRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Make prediction using the loaded model

    Features:
    - Caching with Redis for repeated requests
    - Automatic logging to PostgreSQL
    - Prometheus metrics collection
    - Model versioning

    Args:
        request: Prediction request with features
        background_tasks: FastAPI background tasks
        db: Database session

    Returns:
        PredictionResponse with prediction and metadata
    """
    request_id = str(uuid.uuid4())
    model = get_model()
    cached = False
    prediction = None
    probability = None
    latency_ms = 0

    try:
        # Check cache first
        if request.use_cache and redis_client:
            cache_key = get_cache_key(request.features)
            cached_result = redis_client.get(cache_key)

            if cached_result:
                cache_hits.inc()
                cached = True
                result = json.loads(cached_result)
                prediction = result["prediction"]
                probability = result.get("probability")
                latency_ms = 0.0  # Cache hit is essentially instant
            else:
                cache_misses.inc()

        # Make prediction if not cached
        if not cached:
            prediction, probability, latency_ms = model.predict(request.features)

            # Cache the result if Redis is available
            if redis_client:
                cache_key = get_cache_key(request.features)
                cache_value = json.dumps({
                    "prediction": prediction,
                    "probability": probability
                })
                # Cache for 1 hour
                redis_client.setex(cache_key, 3600, cache_value)

        # Update Prometheus metrics
        predictions_total.labels(model_version=model.version).inc()
        prediction_latency.observe(latency_ms / 1000)
        prediction_distribution.observe(prediction)

        # Update drift metrics
        drift_metrics = model.get_drift_metrics()
        prediction_mean.labels(model_version=model.version).set(drift_metrics["mean"])
        prediction_std.labels(model_version=model.version).set(drift_metrics["std"])

        # Log to database (background task)
        background_tasks.add_task(
            log_prediction_background,
            db=db,
            request_id=request_id,
            model_version=model.version,
            features=request.features,
            prediction=prediction,
            probability=probability,
            latency_ms=latency_ms
        )

        return PredictionResponse(
            request_id=request_id,
            prediction=prediction,
            probability=probability,
            model_version=model.version,
            latency_ms=latency_ms,
            cached=cached,
            timestamp=datetime.utcnow().isoformat()
        )

    except Exception as e:
        prediction_errors.labels(error_type=type(e).__name__).inc()
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.get("/health", response_model=HealthResponse)
async def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint

    Returns system status including:
    - Model version
    - Database connectivity
    - Redis connectivity
    """
    model = get_model()

    # Check database
    db_connected = True
    try:
        db.execute("SELECT 1")
    except Exception:
        db_connected = False

    # Check Redis
    redis_connected = False
    if redis_client:
        try:
            redis_client.ping()
            redis_connected = True
        except Exception:
            pass

    return HealthResponse(
        status="healthy" if db_connected else "degraded",
        model_version=model.version,
        database_connected=db_connected,
        redis_connected=redis_connected,
        timestamp=datetime.utcnow().isoformat()
    )


@app.get("/metrics")
async def metrics():
    """
    Prometheus metrics endpoint
    Returns metrics in Prometheus format for scraping
    """
    return metrics_endpoint()


@app.get("/model/info")
async def model_info():
    """
    Get information about the loaded model

    Returns:
        Model metadata including version, features, drift metrics
    """
    model = get_model()
    drift_metrics = model.get_drift_metrics()

    return {
        "version": model.version,
        "model_path": str(model.model_path),
        "feature_names": model.feature_names,
        "feature_count": len(model.feature_names) if model.feature_names else None,
        "drift_metrics": drift_metrics
    }


@app.post("/model/reload")
async def reload_model():
    """
    Reload model from disk
    Useful for deploying new model versions without restarting the service
    """
    try:
        model = get_model()
        model.reload_model()
        return {"status": "success", "message": "Model reloaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reloading model: {str(e)}")


@app.get("/")
async def root():
    """
    Root endpoint with API information
    """
    return {
        "name": "Production ML System",
        "version": "1.0.0",
        "endpoints": {
            "/predict": "Make predictions",
            "/health": "Health check",
            "/metrics": "Prometheus metrics",
            "/model/info": "Model information",
            "/model/reload": "Reload model",
            "/docs": "API documentation (Swagger UI)"
        }
    }

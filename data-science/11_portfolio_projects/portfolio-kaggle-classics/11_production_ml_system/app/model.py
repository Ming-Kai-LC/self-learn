"""
ML Model loading and prediction logic
Supports model versioning with MLflow
"""

import os
import joblib
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import time

# For model drift tracking
from collections import deque


class MLModel:
    """
    Wrapper class for ML model with versioning support
    """

    def __init__(self, model_path: str = "models/model.pkl", version: str = "v1.0"):
        """
        Initialize model from disk

        Args:
            model_path: Path to serialized model file
            version: Model version identifier
        """
        self.model_path = Path(model_path)
        self.version = version
        self.model = None
        self.feature_names = None

        # For tracking predictions (model drift detection)
        self.recent_predictions = deque(maxlen=1000)

        self.load_model()

    def load_model(self):
        """
        Load model from disk
        Raises FileNotFoundError if model doesn't exist
        """
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model file not found: {self.model_path}\n"
                f"Please train a model first using notebooks/model_training.ipynb"
            )

        self.model = joblib.load(self.model_path)
        print(f"✓ Model loaded successfully from {self.model_path}")
        print(f"  Version: {self.version}")

        # Try to get feature names if available
        if hasattr(self.model, 'feature_names_in_'):
            self.feature_names = self.model.feature_names_in_.tolist()
            print(f"  Features: {len(self.feature_names)}")

    def predict(self, features: Dict[str, float]) -> Tuple[float, Optional[float], float]:
        """
        Make prediction from input features

        Args:
            features: Dictionary of feature name -> value

        Returns:
            Tuple of (prediction, probability, latency_ms)
        """
        start_time = time.time()

        # Convert features dict to array in correct order
        if self.feature_names:
            feature_array = np.array([
                [features.get(name, 0.0) for name in self.feature_names]
            ])
        else:
            # If no feature names, assume features dict has correct order
            feature_array = np.array([list(features.values())])

        # Make prediction
        prediction = self.model.predict(feature_array)[0]

        # Get probability if available (for classifiers)
        probability = None
        if hasattr(self.model, 'predict_proba'):
            proba = self.model.predict_proba(feature_array)[0]
            probability = float(proba[1]) if len(proba) > 1 else float(proba[0])

        # Calculate latency
        latency_ms = (time.time() - start_time) * 1000

        # Track prediction for drift monitoring
        self.recent_predictions.append(float(prediction))

        return float(prediction), probability, latency_ms

    def get_drift_metrics(self) -> Dict[str, float]:
        """
        Calculate metrics for model drift detection

        Returns:
            Dictionary with mean, std of recent predictions
        """
        if not self.recent_predictions:
            return {"mean": 0.0, "std": 0.0, "count": 0}

        predictions_array = np.array(self.recent_predictions)
        return {
            "mean": float(np.mean(predictions_array)),
            "std": float(np.std(predictions_array)),
            "count": len(self.recent_predictions)
        }

    def reload_model(self):
        """
        Reload model from disk (useful for model updates)
        """
        print(f"Reloading model from {self.model_path}...")
        self.load_model()


# Global model instance
_model_instance: Optional[MLModel] = None


def get_model() -> MLModel:
    """
    Get or create global model instance (singleton pattern)
    Ensures only one model is loaded in memory
    """
    global _model_instance

    if _model_instance is None:
        model_path = os.getenv("MODEL_PATH", "models/model.pkl")
        model_version = os.getenv("MODEL_VERSION", "v1.0")
        _model_instance = MLModel(model_path, model_version)

    return _model_instance

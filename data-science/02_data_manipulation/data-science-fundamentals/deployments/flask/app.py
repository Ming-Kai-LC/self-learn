"""
Flask API Template for ML Model Deployment
Module 22: Model Deployment

This template shows how to deploy a machine learning model as a REST API.
"""

import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load your trained model (replace with your model path)
# model = joblib.load('../../models/your_model.pkl')


@app.route("/")
def home():
    """Home endpoint with API information."""
    return jsonify(
        {
            "message": "ML Model API",
            "version": "1.0",
            "endpoints": {
                "/predict": "POST - Make predictions",
                "/health": "GET - Check API health",
            },
        }
    )


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "model_loaded": True})


@app.route("/predict", methods=["POST"])
def predict():
    """
    Make predictions using the trained model.

    Expected JSON input:
    {
        "features": [feature1, feature2, feature3, ...]
    }

    Returns:
    {
        "prediction": prediction_value,
        "probability": probability_value (if classifier)
    }
    """
    try:
        # Get data from request
        data = request.get_json()

        if "features" not in data:
            return jsonify({"error": "No features provided"}), 400

        # Extract features
        features = np.array(data["features"]).reshape(1, -1)

        # Make prediction
        # prediction = model.predict(features)
        # For demonstration, returning dummy prediction
        prediction = [1]

        # If classifier, get probabilities
        # probabilities = model.predict_proba(features)

        response = {
            "prediction": int(prediction[0]),
            "status": "success",
            # 'probability': float(probabilities[0][1])  # For binary classification
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/batch_predict", methods=["POST"])
def batch_predict():
    """
    Make predictions for multiple samples.

    Expected JSON input:
    {
        "features": [[f1, f2, f3], [f1, f2, f3], ...]
    }
    """
    try:
        data = request.get_json()

        if "features" not in data:
            return jsonify({"error": "No features provided"}), 400

        features = np.array(data["features"])

        # Make predictions
        # predictions = model.predict(features)
        # For demonstration
        predictions = [1] * len(features)

        response = {
            "predictions": [int(p) for p in predictions],
            "count": len(predictions),
            "status": "success",
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting Flask ML API...")
    print("API running at http://localhost:5000")
    print("\nAvailable endpoints:")
    print("  GET  /          - API information")
    print("  GET  /health    - Health check")
    print("  POST /predict   - Single prediction")
    print("  POST /batch_predict - Batch predictions")

    app.run(debug=True, host="0.0.0.0", port=5000)

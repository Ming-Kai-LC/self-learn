"""
Model Inference Script for SageMaker Endpoint

This script provides the Flask app for serving predictions
via SageMaker endpoints.
"""

import json
import os
from pathlib import Path

import joblib
import numpy as np
from flask import Flask, request, jsonify

from preprocess import TextPreprocessor


class SentimentPredictor:
    """Sentiment prediction handler"""

    def __init__(self, model_path="/opt/ml/model"):
        """
        Initialize predictor

        Args:
            model_path: Path to model artifacts directory
        """
        self.model_path = Path(model_path)
        self.model = None
        self.vectorizer = None
        self.preprocessor = None
        self.loaded = False

    def load_model(self):
        """Load model artifacts from disk"""
        if self.loaded:
            return

        print(f"Loading model from {self.model_path}")

        try:
            # Load model
            model_file = self.model_path / "model.pkl"
            self.model = joblib.load(model_file)
            print(f"Loaded model from {model_file}")

            # Load vectorizer
            vectorizer_file = self.model_path / "vectorizer.pkl"
            self.vectorizer = joblib.load(vectorizer_file)
            print(f"Loaded vectorizer from {vectorizer_file}")

            # Load preprocessor
            preprocessor_file = self.model_path / "preprocessor.pkl"
            self.preprocessor = joblib.load(preprocessor_file)
            print(f"Loaded preprocessor from {preprocessor_file}")

            self.loaded = True
            print("Model loaded successfully!")

        except Exception as e:
            print(f"Error loading model: {e}")
            raise

    def predict(self, text):
        """
        Make prediction on input text

        Args:
            text: Input text to classify

        Returns:
            Dictionary with prediction and confidence
        """
        # Ensure model is loaded
        if not self.loaded:
            self.load_model()

        # Preprocess text
        processed_text = self.preprocessor.preprocess(text)

        # Vectorize
        X = self.vectorizer.transform([processed_text])

        # Predict
        prediction = self.model.predict(X)[0]
        probabilities = self.model.predict_proba(X)[0]

        # Get confidence (probability of predicted class)
        confidence = float(probabilities[prediction])

        # Map prediction to label
        label = "positive" if prediction == 1 else "negative"

        result = {
            "prediction": label,
            "confidence": confidence,
            "probabilities": {
                "negative": float(probabilities[0]),
                "positive": float(probabilities[1]),
            },
        }

        return result

    def predict_batch(self, texts):
        """
        Make predictions on batch of texts

        Args:
            texts: List of input texts

        Returns:
            List of prediction dictionaries
        """
        # Ensure model is loaded
        if not self.loaded:
            self.load_model()

        # Preprocess texts
        processed_texts = [self.preprocessor.preprocess(text) for text in texts]

        # Vectorize
        X = self.vectorizer.transform(processed_texts)

        # Predict
        predictions = self.model.predict(X)
        probabilities = self.model.predict_proba(X)

        # Format results
        results = []
        for i, pred in enumerate(predictions):
            label = "positive" if pred == 1 else "negative"
            confidence = float(probabilities[i][pred])

            result = {
                "prediction": label,
                "confidence": confidence,
                "probabilities": {
                    "negative": float(probabilities[i][0]),
                    "positive": float(probabilities[i][1]),
                },
            }
            results.append(result)

        return results


# ==================== Flask App for SageMaker ====================

# Initialize Flask app
app = Flask(__name__)

# Initialize predictor
predictor = SentimentPredictor()


@app.route("/ping", methods=["GET"])
def ping():
    """
    Health check endpoint

    SageMaker uses this to verify the container is ready
    """
    try:
        # Try to load model if not already loaded
        if not predictor.loaded:
            predictor.load_model()

        status = 200
        response = {"status": "healthy"}
    except Exception as e:
        status = 500
        response = {"status": "unhealthy", "error": str(e)}

    return jsonify(response), status


@app.route("/invocations", methods=["POST"])
def invoke():
    """
    Prediction endpoint

    SageMaker sends prediction requests here
    """
    try:
        # Parse request
        content_type = request.content_type

        if content_type == "application/json":
            data = request.get_json()

            # Handle single text or batch
            if isinstance(data, dict):
                if "text" in data:
                    # Single prediction
                    text = data["text"]
                    result = predictor.predict(text)
                elif "texts" in data:
                    # Batch prediction
                    texts = data["texts"]
                    result = predictor.predict_batch(texts)
                else:
                    return jsonify({"error": "Missing 'text' or 'texts' field"}), 400
            elif isinstance(data, str):
                # Single text as string
                result = predictor.predict(data)
            else:
                return jsonify({"error": "Invalid input format"}), 400

            return jsonify(result), 200

        elif content_type == "text/plain":
            # Plain text input
            text = request.data.decode("utf-8")
            result = predictor.predict(text)
            return jsonify(result), 200

        else:
            return (
                jsonify({"error": f"Unsupported content type: {content_type}"}),
                415,
            )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def root():
    """Root endpoint with API info"""
    info = {
        "name": "Sentiment Analysis API",
        "version": "1.0.0",
        "endpoints": {
            "/ping": "Health check",
            "/invocations": "Make predictions (POST)",
        },
        "example": {
            "url": "/invocations",
            "method": "POST",
            "content_type": "application/json",
            "body": {"text": "This product is amazing!"},
        },
    }
    return jsonify(info), 200


# ==================== CLI for Local Testing ====================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sentiment analysis inference")

    parser.add_argument(
        "--text",
        type=str,
        help="Text to classify",
    )
    parser.add_argument(
        "--model-path",
        type=str,
        default="models/local",
        help="Path to model artifacts",
    )
    parser.add_argument(
        "--endpoint",
        type=str,
        help="SageMaker endpoint name (for testing deployed model)",
    )
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Start Flask server for local testing",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port for Flask server",
    )

    args = parser.parse_args()

    if args.serve:
        # Start Flask server
        print(f"Starting server on port {args.port}")
        app.run(host="0.0.0.0", port=args.port, debug=False)

    elif args.endpoint:
        # Test SageMaker endpoint
        import boto3

        runtime_client = boto3.client("sagemaker-runtime")

        payload = json.dumps({"text": args.text})

        response = runtime_client.invoke_endpoint(
            EndpointName=args.endpoint,
            ContentType="application/json",
            Body=payload,
        )

        result = json.loads(response["Body"].read().decode())
        print(json.dumps(result, indent=2))

    elif args.text:
        # Local prediction
        predictor = SentimentPredictor(model_path=args.model_path)
        result = predictor.predict(args.text)
        print(json.dumps(result, indent=2))

    else:
        parser.print_help()

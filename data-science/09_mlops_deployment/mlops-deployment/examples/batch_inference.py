"""
Batch Inference Script
Used in Module 06: Model Serving Patterns

This script demonstrates batch inference for processing large datasets.

Usage:
    python batch_inference.py --input data.csv --output predictions.csv
"""

import argparse
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
import logging
from tqdm import tqdm
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_model(model_path: str):
    """Load the trained model"""
    logger.info(f"Loading model from {model_path}")
    try:
        model = joblib.load(model_path)
        logger.info("Model loaded successfully")
        return model
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        raise


def load_data(input_path: str) -> pd.DataFrame:
    """Load input data"""
    logger.info(f"Loading data from {input_path}")
    try:
        data = pd.read_csv(input_path)
        logger.info(f"Loaded {len(data)} rows")
        return data
    except Exception as e:
        logger.error(f"Failed to load data: {str(e)}")
        raise


def preprocess_data(data: pd.DataFrame) -> np.ndarray:
    """Preprocess data for inference"""
    # Add your preprocessing logic here
    # This is a placeholder - adjust based on your model requirements
    feature_cols = [col for col in data.columns if col.startswith('feature_')]

    if not feature_cols:
        raise ValueError("No feature columns found in data")

    X = data[feature_cols].values

    # Handle missing values
    if np.isnan(X).any():
        logger.warning("Found missing values, filling with 0")
        X = np.nan_to_num(X, nan=0.0)

    return X


def batch_predict(model, X: np.ndarray, batch_size: int = 1000):
    """
    Make predictions in batches to manage memory

    Args:
        model: Trained model
        X: Input features
        batch_size: Number of samples per batch

    Returns:
        predictions: Array of predictions
        probabilities: Array of probabilities
    """
    n_samples = X.shape[0]
    n_batches = (n_samples + batch_size - 1) // batch_size

    predictions = []
    probabilities = []

    logger.info(f"Processing {n_samples} samples in {n_batches} batches")

    for i in tqdm(range(n_batches), desc="Predicting"):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, n_samples)

        X_batch = X[start_idx:end_idx]

        # Make predictions
        batch_preds = model.predict(X_batch)
        batch_probs = model.predict_proba(X_batch)[:, 1]

        predictions.extend(batch_preds)
        probabilities.extend(batch_probs)

    return np.array(predictions), np.array(probabilities)


def save_predictions(
    data: pd.DataFrame,
    predictions: np.ndarray,
    probabilities: np.ndarray,
    output_path: str
):
    """Save predictions to CSV"""
    logger.info(f"Saving predictions to {output_path}")

    # Create output dataframe
    output_df = data.copy()
    output_df['prediction'] = predictions
    output_df['probability'] = probabilities

    # Save to CSV
    output_df.to_csv(output_path, index=False)
    logger.info(f"Saved {len(output_df)} predictions")

    # Log summary statistics
    logger.info(f"Prediction summary:")
    logger.info(f"  Class 0: {(predictions == 0).sum()} ({(predictions == 0).mean()*100:.1f}%)")
    logger.info(f"  Class 1: {(predictions == 1).sum()} ({(predictions == 1).mean()*100:.1f}%)")
    logger.info(f"  Average probability: {probabilities.mean():.4f}")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='Batch inference script')
    parser.add_argument('--input', type=str, required=True, help='Input CSV file')
    parser.add_argument('--output', type=str, required=True, help='Output CSV file')
    parser.add_argument('--model', type=str, default='models/model.pkl', help='Model file path')
    parser.add_argument('--batch-size', type=int, default=1000, help='Batch size for inference')

    args = parser.parse_args()

    # Validate inputs
    if not Path(args.input).exists():
        raise FileNotFoundError(f"Input file not found: {args.input}")

    if not Path(args.model).exists():
        raise FileNotFoundError(f"Model file not found: {args.model}")

    # Execute pipeline
    start_time = time.time()

    # Load model and data
    model = load_model(args.model)
    data = load_data(args.input)

    # Preprocess
    X = preprocess_data(data)

    # Predict
    predictions, probabilities = batch_predict(model, X, args.batch_size)

    # Save results
    save_predictions(data, predictions, probabilities, args.output)

    # Report timing
    elapsed_time = time.time() - start_time
    samples_per_second = len(data) / elapsed_time

    logger.info(f"Batch inference completed in {elapsed_time:.2f} seconds")
    logger.info(f"Throughput: {samples_per_second:.0f} samples/second")


if __name__ == "__main__":
    main()

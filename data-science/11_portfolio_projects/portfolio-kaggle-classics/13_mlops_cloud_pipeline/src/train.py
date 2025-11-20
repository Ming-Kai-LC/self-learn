"""
Model Training Script for Sentiment Analysis

This script can be run locally or on AWS SageMaker.
It trains a sentiment analysis model and saves artifacts.
"""

import argparse
import os
import pickle
import sys
from pathlib import Path

import boto3
import joblib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split

from preprocess import TextPreprocessor


class SentimentModelTrainer:
    """Train and save sentiment analysis model"""

    def __init__(self, max_features=5000, random_state=42):
        """
        Initialize trainer

        Args:
            max_features: Maximum number of features for TF-IDF
            random_state: Random seed for reproducibility
        """
        self.max_features = max_features
        self.random_state = random_state
        self.preprocessor = TextPreprocessor()
        self.vectorizer = None
        self.model = None

    def load_data(self, data_path):
        """
        Load training data from CSV or S3

        Args:
            data_path: Local path or S3 URI to CSV file

        Returns:
            DataFrame with text and label columns
        """
        print(f"Loading data from {data_path}")

        if data_path.startswith("s3://"):
            # Load from S3
            s3_client = boto3.client("s3")
            bucket, key = data_path.replace("s3://", "").split("/", 1)

            obj = s3_client.get_object(Bucket=bucket, Key=key)
            data = pd.read_csv(obj["Body"])
        else:
            # Load from local file
            data = pd.read_csv(data_path)

        print(f"Loaded {len(data)} samples")
        return data

    def prepare_data(self, data, text_column="text", label_column="label"):
        """
        Prepare data for training

        Args:
            data: DataFrame with text and labels
            text_column: Name of text column
            label_column: Name of label column

        Returns:
            X_train, X_val, y_train, y_val
        """
        print("Preprocessing text data...")

        # Extract features and labels
        texts = data[text_column].values
        labels = data[label_column].values

        # Preprocess texts
        processed_texts = [self.preprocessor.preprocess(text) for text in texts]

        # Split into train and validation
        X_train, X_val, y_train, y_val = train_test_split(
            processed_texts,
            labels,
            test_size=0.2,
            random_state=self.random_state,
            stratify=labels,
        )

        print(f"Training samples: {len(X_train)}")
        print(f"Validation samples: {len(X_val)}")

        return X_train, X_val, y_train, y_val

    def train(self, X_train, y_train):
        """
        Train the sentiment model

        Args:
            X_train: Training texts
            y_train: Training labels

        Returns:
            Trained model
        """
        print("Vectorizing text with TF-IDF...")

        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(
            max_features=self.max_features,
            ngram_range=(1, 2),
            min_df=2,
            max_df=0.95,
        )

        # Transform training data
        X_train_tfidf = self.vectorizer.fit_transform(X_train)

        print(f"Feature matrix shape: {X_train_tfidf.shape}")
        print("Training Logistic Regression model...")

        # Train model
        self.model = LogisticRegression(
            C=1.0,
            max_iter=1000,
            random_state=self.random_state,
            n_jobs=-1,
            solver="lbfgs",
        )

        self.model.fit(X_train_tfidf, y_train)

        print("Training complete!")
        return self.model

    def evaluate(self, X_val, y_val):
        """
        Evaluate model on validation set

        Args:
            X_val: Validation texts
            y_val: Validation labels

        Returns:
            Dictionary of evaluation metrics
        """
        print("Evaluating model...")

        # Transform validation data
        X_val_tfidf = self.vectorizer.transform(X_val)

        # Make predictions
        y_pred = self.model.predict(X_val_tfidf)

        # Calculate metrics
        accuracy = accuracy_score(y_val, y_pred)
        f1 = f1_score(y_val, y_pred, average="weighted")

        print(f"\nValidation Accuracy: {accuracy:.4f}")
        print(f"Validation F1 Score: {f1:.4f}")
        print("\nClassification Report:")
        print(classification_report(y_val, y_pred))

        metrics = {
            "accuracy": accuracy,
            "f1_score": f1,
        }

        return metrics

    def save_model(self, output_path):
        """
        Save model artifacts

        Args:
            output_path: Directory to save model files
        """
        print(f"Saving model to {output_path}")

        # Create output directory
        output_dir = Path(output_path)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save vectorizer
        vectorizer_path = output_dir / "vectorizer.pkl"
        joblib.dump(self.vectorizer, vectorizer_path)
        print(f"Saved vectorizer to {vectorizer_path}")

        # Save model
        model_path = output_dir / "model.pkl"
        joblib.dump(self.model, model_path)
        print(f"Saved model to {model_path}")

        # Save preprocessor
        preprocessor_path = output_dir / "preprocessor.pkl"
        joblib.dump(self.preprocessor, preprocessor_path)
        print(f"Saved preprocessor to {preprocessor_path}")

    def upload_to_s3(self, local_path, s3_path):
        """
        Upload model artifacts to S3

        Args:
            local_path: Local directory with model files
            s3_path: S3 URI for upload destination
        """
        print(f"Uploading model to {s3_path}")

        s3_client = boto3.client("s3")
        bucket, prefix = s3_path.replace("s3://", "").split("/", 1)

        local_dir = Path(local_path)

        for file_path in local_dir.glob("*.pkl"):
            key = f"{prefix}/{file_path.name}"
            s3_client.upload_file(str(file_path), bucket, key)
            print(f"Uploaded {file_path.name} to s3://{bucket}/{key}")


def main():
    """Main training function"""
    parser = argparse.ArgumentParser(description="Train sentiment analysis model")

    parser.add_argument(
        "--data-path",
        type=str,
        default="data/train.csv",
        help="Path to training data (local or S3)",
    )
    parser.add_argument(
        "--output-path",
        type=str,
        default="models/local",
        help="Path to save model artifacts",
    )
    parser.add_argument(
        "--max-features",
        type=int,
        default=5000,
        help="Maximum features for TF-IDF",
    )
    parser.add_argument(
        "--cloud",
        action="store_true",
        help="Running on SageMaker (upload to S3)",
    )
    parser.add_argument(
        "--s3-output",
        type=str,
        help="S3 path for model artifacts (for cloud training)",
    )
    parser.add_argument(
        "--local",
        action="store_true",
        help="Run with minimal data for testing",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=100,
        help="Sample size for local testing",
    )

    args = parser.parse_args()

    # Use SageMaker paths if running on SageMaker
    if "SM_CHANNEL_TRAINING" in os.environ:
        args.data_path = f"{os.environ['SM_CHANNEL_TRAINING']}/train.csv"
        args.output_path = os.environ.get("SM_MODEL_DIR", "/opt/ml/model")
        args.cloud = True

    # Initialize trainer
    trainer = SentimentModelTrainer(
        max_features=args.max_features,
        random_state=42,
    )

    # Load data
    data = trainer.load_data(args.data_path)

    # Sample data for local testing
    if args.local and len(data) > args.sample_size:
        print(f"Sampling {args.sample_size} rows for local testing")
        data = data.sample(n=args.sample_size, random_state=42)

    # Prepare data
    X_train, X_val, y_train, y_val = trainer.prepare_data(data)

    # Train model
    trainer.train(X_train, y_train)

    # Evaluate model
    metrics = trainer.evaluate(X_val, y_val)

    # Save model
    trainer.save_model(args.output_path)

    # Upload to S3 if running in cloud
    if args.cloud and args.s3_output:
        trainer.upload_to_s3(args.output_path, args.s3_output)

    print("\nTraining complete!")
    print(f"Final metrics: {metrics}")


if __name__ == "__main__":
    main()

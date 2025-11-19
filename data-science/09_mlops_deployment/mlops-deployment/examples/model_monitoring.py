"""
Model Monitoring Script
Used in Module 07: Model Monitoring and Logging

This script demonstrates how to monitor model performance in production.

Usage:
    python model_monitoring.py --predictions predictions.csv --ground-truth labels.csv
"""

import argparse
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_predictions(predictions_path: str) -> pd.DataFrame:
    """Load predictions from CSV"""
    logger.info(f"Loading predictions from {predictions_path}")
    df = pd.read_csv(predictions_path)

    required_cols = ['prediction', 'probability']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"Predictions file must contain columns: {required_cols}")

    return df


def load_ground_truth(ground_truth_path: str) -> pd.DataFrame:
    """Load ground truth labels"""
    logger.info(f"Loading ground truth from {ground_truth_path}")
    df = pd.read_csv(ground_truth_path)

    if 'label' not in df.columns:
        raise ValueError("Ground truth file must contain 'label' column")

    return df


def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray, y_prob: np.ndarray) -> dict:
    """Calculate comprehensive performance metrics"""
    logger.info("Calculating performance metrics")

    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, zero_division=0),
        'recall': recall_score(y_true, y_pred, zero_division=0),
        'f1_score': f1_score(y_true, y_pred, zero_division=0),
        'roc_auc': roc_auc_score(y_true, y_prob) if len(np.unique(y_true)) > 1 else 0,
        'timestamp': datetime.now().isoformat()
    }

    # Add confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    metrics['confusion_matrix'] = {
        'true_negative': int(cm[0, 0]),
        'false_positive': int(cm[0, 1]),
        'false_negative': int(cm[1, 0]),
        'true_positive': int(cm[1, 1])
    }

    return metrics


def check_performance_degradation(metrics: dict, baseline: dict) -> dict:
    """Check if performance has degraded compared to baseline"""
    logger.info("Checking for performance degradation")

    degradation_threshold = 0.05  # 5% degradation triggers alert

    alerts = []

    for metric in ['accuracy', 'precision', 'recall', 'f1_score', 'roc_auc']:
        if metric in baseline:
            current = metrics[metric]
            baseline_value = baseline[metric]
            degradation = baseline_value - current

            if degradation > degradation_threshold:
                alerts.append({
                    'metric': metric,
                    'baseline': baseline_value,
                    'current': current,
                    'degradation': degradation,
                    'severity': 'HIGH' if degradation > 0.1 else 'MEDIUM'
                })
                logger.warning(
                    f"Performance degradation detected: {metric} "
                    f"decreased from {baseline_value:.4f} to {current:.4f}"
                )

    return {
        'has_degradation': len(alerts) > 0,
        'alerts': alerts
    }


def plot_metrics_comparison(current_metrics: dict, baseline_metrics: dict, output_path: str):
    """Plot comparison between current and baseline metrics"""
    logger.info("Generating metrics comparison plot")

    metrics_to_plot = ['accuracy', 'precision', 'recall', 'f1_score', 'roc_auc']

    current_values = [current_metrics.get(m, 0) for m in metrics_to_plot]
    baseline_values = [baseline_metrics.get(m, 0) for m in metrics_to_plot]

    x = np.arange(len(metrics_to_plot))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))

    bars1 = ax.bar(x - width/2, baseline_values, width, label='Baseline', alpha=0.8)
    bars2 = ax.bar(x + width/2, current_values, width, label='Current', alpha=0.8)

    # Color bars based on performance
    for i, (baseline, current) in enumerate(zip(baseline_values, current_values)):
        if current < baseline - 0.05:
            bars2[i].set_color('red')
        elif current > baseline + 0.05:
            bars2[i].set_color('green')

    ax.set_xlabel('Metric', fontweight='bold')
    ax.set_ylabel('Score', fontweight='bold')
    ax.set_title('Model Performance: Current vs Baseline', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([m.replace('_', ' ').title() for m in metrics_to_plot])
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(0, 1.1)

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.3f}',
                   ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    logger.info(f"Saved metrics comparison plot to {output_path}")
    plt.close()


def plot_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray, output_path: str):
    """Plot confusion matrix"""
    logger.info("Generating confusion matrix plot")

    cm = confusion_matrix(y_true, y_pred)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_xlabel('Predicted', fontweight='bold')
    ax.set_ylabel('Actual', fontweight='bold')
    ax.set_title('Confusion Matrix', fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    logger.info(f"Saved confusion matrix plot to {output_path}")
    plt.close()


def save_monitoring_report(metrics: dict, degradation: dict, output_path: str):
    """Save monitoring report as JSON"""
    logger.info(f"Saving monitoring report to {output_path}")

    report = {
        'timestamp': datetime.now().isoformat(),
        'metrics': metrics,
        'degradation_check': degradation,
        'status': 'ALERT' if degradation['has_degradation'] else 'OK'
    }

    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)

    logger.info("Monitoring report saved")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='Model monitoring script')
    parser.add_argument('--predictions', type=str, required=True, help='Predictions CSV file')
    parser.add_argument('--ground-truth', type=str, required=True, help='Ground truth CSV file')
    parser.add_argument('--baseline', type=str, help='Baseline metrics JSON file')
    parser.add_argument('--output-dir', type=str, default='reports', help='Output directory')

    args = parser.parse_args()

    # Load data
    predictions_df = load_predictions(args.predictions)
    ground_truth_df = load_ground_truth(args.ground_truth)

    # Merge predictions with ground truth
    if 'id' in predictions_df.columns and 'id' in ground_truth_df.columns:
        merged = predictions_df.merge(ground_truth_df, on='id')
    else:
        # Assume same order
        merged = predictions_df.copy()
        merged['label'] = ground_truth_df['label'].values

    y_true = merged['label'].values
    y_pred = merged['prediction'].values
    y_prob = merged['probability'].values

    # Calculate metrics
    metrics = calculate_metrics(y_true, y_pred, y_prob)

    logger.info("Current Performance Metrics:")
    logger.info(f"  Accuracy:  {metrics['accuracy']:.4f}")
    logger.info(f"  Precision: {metrics['precision']:.4f}")
    logger.info(f"  Recall:    {metrics['recall']:.4f}")
    logger.info(f"  F1 Score:  {metrics['f1_score']:.4f}")
    logger.info(f"  ROC AUC:   {metrics['roc_auc']:.4f}")

    # Check for degradation if baseline provided
    degradation = {'has_degradation': False, 'alerts': []}
    baseline_metrics = {}

    if args.baseline:
        with open(args.baseline, 'r') as f:
            baseline_metrics = json.load(f)
        degradation = check_performance_degradation(metrics, baseline_metrics)

    # Create output directory
    import os
    os.makedirs(args.output_dir, exist_ok=True)

    # Generate plots
    plot_confusion_matrix(y_true, y_pred, f"{args.output_dir}/confusion_matrix.png")

    if baseline_metrics:
        plot_metrics_comparison(
            metrics, baseline_metrics,
            f"{args.output_dir}/metrics_comparison.png"
        )

    # Save report
    save_monitoring_report(metrics, degradation, f"{args.output_dir}/monitoring_report.json")

    # Exit with error code if degradation detected
    if degradation['has_degradation']:
        logger.error("Performance degradation detected! Review the monitoring report.")
        exit(1)
    else:
        logger.info("All performance metrics within acceptable range.")
        exit(0)


if __name__ == "__main__":
    main()

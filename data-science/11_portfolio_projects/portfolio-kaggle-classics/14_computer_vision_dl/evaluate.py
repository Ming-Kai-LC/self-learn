"""
Evaluation Utilities for Deep Learning Computer Vision Models

This script provides:
1. Model evaluation metrics (accuracy, precision, recall, F1)
2. Confusion matrix visualization
3. Per-class performance analysis
4. Error analysis (misclassified examples)
5. GradCAM visualization for model interpretability
6. Inference time benchmarking

Usage:
    python evaluate.py --model models/efficientnet_best.h5
    python evaluate.py --model models/baseline_cnn.h5 --gradcam --num_examples 10
"""

import argparse
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_recall_fscore_support,
)
from tensorflow import keras

try:
    from tf_keras_vis.gradcam import Gradcam
    from tf_keras_vis.utils.scores import CategoricalScore
    GRADCAM_AVAILABLE = True
except ImportError:
    print("Warning: tf-keras-vis not installed. GradCAM will not be available.")
    print("Install with: pip install tf-keras-vis")
    GRADCAM_AVAILABLE = False


# CIFAR-10 class names
CLASS_NAMES = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]


def load_cifar10_test_data():
    """
    Load CIFAR-10 test dataset.

    Returns:
        x_test, y_test (normalized images and labels)
    """
    print("Loading CIFAR-10 test data...")
    (_, _), (x_test, y_test) = keras.datasets.cifar10.load_data()

    x_test = x_test.astype('float32') / 255.0
    y_test = y_test.flatten()  # Convert from (N, 1) to (N,)

    print(f"Test data shape: {x_test.shape}")
    print(f"Test labels shape: {y_test.shape}")

    return x_test, y_test


def evaluate_model(model, x_test, y_test):
    """
    Evaluate model and compute comprehensive metrics.

    Args:
        model: Trained Keras model
        x_test: Test images
        y_test: Test labels (integer format)

    Returns:
        Dictionary of evaluation metrics
    """
    print("\n" + "="*60)
    print("Model Evaluation")
    print("="*60)

    # Get predictions
    print("Making predictions...")
    y_pred_probs = model.predict(x_test, verbose=1)
    y_pred = np.argmax(y_pred_probs, axis=1)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average='weighted'
    )

    # Top-3 accuracy
    top3_pred = np.argsort(y_pred_probs, axis=1)[:, -3:]
    top3_accuracy = np.mean([y_test[i] in top3_pred[i] for i in range(len(y_test))])

    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'top3_accuracy': top3_accuracy,
        'y_pred': y_pred,
        'y_pred_probs': y_pred_probs
    }

    # Print summary
    print(f"\nAccuracy:       {accuracy:.4f}")
    print(f"Precision:      {precision:.4f}")
    print(f"Recall:         {recall:.4f}")
    print(f"F1 Score:       {f1:.4f}")
    print(f"Top-3 Accuracy: {top3_accuracy:.4f}")
    print("="*60)

    return metrics


def plot_confusion_matrix(y_true, y_pred, save_path='results/confusion_matrix.png'):
    """
    Plot and save confusion matrix.

    Args:
        y_true: True labels
        y_pred: Predicted labels
        save_path: Path to save the plot
    """
    print("\nGenerating confusion matrix...")

    # Create directory if needed
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)

    # Normalize confusion matrix
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    # Plot
    plt.figure(figsize=(12, 10))
    sns.heatmap(
        cm_normalized,
        annot=True,
        fmt='.2f',
        cmap='Blues',
        xticklabels=CLASS_NAMES,
        yticklabels=CLASS_NAMES,
        cbar_kws={'label': 'Normalized Count'}
    )
    plt.title('Confusion Matrix (Normalized)', fontsize=16, pad=20)
    plt.ylabel('True Label', fontsize=12)
    plt.xlabel('Predicted Label', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Confusion matrix saved to: {save_path}")
    plt.close()


def print_classification_report(y_true, y_pred):
    """
    Print detailed classification report.

    Args:
        y_true: True labels
        y_pred: Predicted labels
    """
    print("\n" + "="*60)
    print("Per-Class Performance")
    print("="*60)
    print(classification_report(
        y_true, y_pred,
        target_names=CLASS_NAMES,
        digits=4
    ))
    print("="*60)


def analyze_errors(x_test, y_test, y_pred, num_examples=10, save_path='results/error_analysis.png'):
    """
    Visualize misclassified examples.

    Args:
        x_test: Test images
        y_test: True labels
        y_pred: Predicted labels
        num_examples: Number of examples to show
        save_path: Path to save the plot
    """
    print(f"\nAnalyzing misclassified examples...")

    # Find misclassified indices
    misclassified_idx = np.where(y_test != y_pred)[0]

    if len(misclassified_idx) == 0:
        print("No misclassifications found!")
        return

    # Randomly sample examples
    num_examples = min(num_examples, len(misclassified_idx))
    sample_idx = np.random.choice(misclassified_idx, num_examples, replace=False)

    # Create directory if needed
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)

    # Plot
    fig, axes = plt.subplots(2, 5, figsize=(15, 6))
    axes = axes.flatten()

    for i, idx in enumerate(sample_idx):
        ax = axes[i]
        ax.imshow(x_test[idx])
        true_label = CLASS_NAMES[y_test[idx]]
        pred_label = CLASS_NAMES[y_pred[idx]]
        ax.set_title(f'True: {true_label}\nPred: {pred_label}', fontsize=10)
        ax.axis('off')

    plt.suptitle('Misclassified Examples', fontsize=16, y=1.02)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Error analysis saved to: {save_path}")
    plt.close()


def visualize_gradcam(model, x_test, y_test, num_examples=5, save_path='results/gradcam_examples.png'):
    """
    Visualize GradCAM heatmaps for model interpretability.

    Args:
        model: Trained Keras model
        x_test: Test images
        y_test: True labels
        num_examples: Number of examples to visualize
        save_path: Path to save the plot
    """
    if not GRADCAM_AVAILABLE:
        print("GradCAM not available. Skipping...")
        return

    print(f"\nGenerating GradCAM visualizations...")

    # Select random examples
    sample_idx = np.random.choice(len(x_test), num_examples, replace=False)
    sample_images = x_test[sample_idx]
    sample_labels = y_test[sample_idx]

    # Create GradCAM object
    # Find the last convolutional layer
    last_conv_layer = None
    for layer in reversed(model.layers):
        if 'conv' in layer.name.lower():
            last_conv_layer = layer.name
            break

    if last_conv_layer is None:
        print("No convolutional layer found. Cannot generate GradCAM.")
        return

    print(f"Using layer for GradCAM: {last_conv_layer}")

    try:
        # Create GradCAM
        gradcam = Gradcam(
            model,
            model_modifier=None,
            clone=True
        )

        # Generate heatmaps
        score = CategoricalScore(sample_labels)
        heatmaps = gradcam(
            score,
            sample_images,
            penultimate_layer=last_conv_layer
        )

        # Create directory if needed
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)

        # Plot
        fig, axes = plt.subplots(num_examples, 3, figsize=(12, num_examples * 3))

        for i in range(num_examples):
            # Original image
            axes[i, 0].imshow(sample_images[i])
            axes[i, 0].set_title(f'Original\n{CLASS_NAMES[sample_labels[i]]}')
            axes[i, 0].axis('off')

            # Heatmap
            axes[i, 1].imshow(heatmaps[i], cmap='jet')
            axes[i, 1].set_title('GradCAM Heatmap')
            axes[i, 1].axis('off')

            # Overlay
            axes[i, 2].imshow(sample_images[i])
            axes[i, 2].imshow(heatmaps[i], cmap='jet', alpha=0.5)
            axes[i, 2].set_title('Overlay')
            axes[i, 2].axis('off')

        plt.suptitle('GradCAM Visualization - Model Attention', fontsize=16, y=0.995)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"GradCAM visualizations saved to: {save_path}")
        plt.close()

    except Exception as e:
        print(f"Error generating GradCAM: {e}")


def benchmark_inference_time(model, x_test, num_samples=1000, num_runs=10):
    """
    Benchmark model inference time.

    Args:
        model: Trained model
        x_test: Test images
        num_samples: Number of samples to use
        num_runs: Number of runs for averaging

    Returns:
        Dictionary with timing statistics
    """
    print("\n" + "="*60)
    print("Inference Time Benchmarking")
    print("="*60)

    # Select samples
    sample_data = x_test[:num_samples]

    # Warmup
    _ = model.predict(sample_data[:10], verbose=0)

    # Benchmark
    times = []
    for i in range(num_runs):
        start_time = time.time()
        _ = model.predict(sample_data, verbose=0)
        elapsed = time.time() - start_time
        times.append(elapsed)

    avg_time = np.mean(times)
    std_time = np.std(times)
    per_image = (avg_time / num_samples) * 1000  # Convert to ms

    print(f"Samples: {num_samples}")
    print(f"Runs: {num_runs}")
    print(f"Average time: {avg_time:.4f} s")
    print(f"Std dev: {std_time:.4f} s")
    print(f"Per image: {per_image:.2f} ms")
    print(f"Throughput: {num_samples/avg_time:.1f} images/sec")
    print("="*60)

    return {
        'avg_time_s': avg_time,
        'std_time_s': std_time,
        'per_image_ms': per_image,
        'throughput': num_samples / avg_time
    }


def main():
    """Main evaluation function."""
    parser = argparse.ArgumentParser(
        description='Evaluate deep learning computer vision models'
    )

    parser.add_argument(
        '--model',
        type=str,
        required=True,
        help='Path to trained model (.h5 file)'
    )
    parser.add_argument(
        '--gradcam',
        action='store_true',
        help='Generate GradCAM visualizations'
    )
    parser.add_argument(
        '--num_examples',
        type=int,
        default=5,
        help='Number of examples for GradCAM and error analysis'
    )
    parser.add_argument(
        '--benchmark',
        action='store_true',
        help='Run inference time benchmarking'
    )

    args = parser.parse_args()

    # Load model
    print(f"Loading model from: {args.model}")
    model = keras.models.load_model(args.model)
    print("Model loaded successfully!")

    # Load test data
    x_test, y_test = load_cifar10_test_data()

    # Evaluate model
    metrics = evaluate_model(model, x_test, y_test)

    # Generate visualizations
    plot_confusion_matrix(y_test, metrics['y_pred'])
    print_classification_report(y_test, metrics['y_pred'])
    analyze_errors(x_test, y_test, metrics['y_pred'], num_examples=args.num_examples)

    # GradCAM visualization
    if args.gradcam:
        visualize_gradcam(model, x_test, y_test, num_examples=args.num_examples)

    # Benchmark inference time
    if args.benchmark:
        benchmark_inference_time(model, x_test)

    print("\nEvaluation completed successfully!")


if __name__ == '__main__':
    main()

"""
CNN Architecture Visualizer

This script provides utilities to visualize CNN architectures,
including layer dimensions, parameter counts, and feature maps.

Usage:
    from scripts.visualize_architecture import visualize_model, plot_feature_maps

    model = YourCNN()
    visualize_model(model, input_size=(1, 1, 28, 28))
"""

from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn


def count_parameters(model: nn.Module) -> dict:
    """
    Count total and trainable parameters in a model

    Args:
        model: PyTorch model

    Returns:
        Dictionary with parameter counts
    """
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

    return {
        "total": total_params,
        "trainable": trainable_params,
        "non_trainable": total_params - trainable_params,
    }


def get_model_size_mb(model: nn.Module) -> float:
    """
    Estimate model size in megabytes

    Args:
        model: PyTorch model

    Returns:
        Model size in MB
    """
    param_size = 0
    for param in model.parameters():
        param_size += param.nelement() * param.element_size()

    buffer_size = 0
    for buffer in model.buffers():
        buffer_size += buffer.nelement() * buffer.element_size()

    size_mb = (param_size + buffer_size) / 1024**2
    return size_mb


def visualize_model(model: nn.Module, input_size: Tuple[int, ...], device: str = "cpu"):
    """
    Print a detailed summary of the model architecture

    Args:
        model: PyTorch model
        input_size: Input tensor size (batch_size, channels, height, width)
        device: Device to run the model on ('cpu' or 'cuda')
    """
    model = model.to(device)
    model.eval()

    print("=" * 80)
    print(f"{'Model Architecture Summary':^80}")
    print("=" * 80)

    # Create a dummy input
    x = torch.randn(*input_size).to(device)

    # Track layer outputs
    layer_outputs = []
    layer_names = []
    layer_params = []

    def hook_fn(module, input, output):
        layer_outputs.append(output.shape)
        layer_names.append(module.__class__.__name__)
        layer_params.append(sum(p.numel() for p in module.parameters()))

    # Register hooks
    hooks = []
    for layer in model.modules():
        if not isinstance(layer, nn.Sequential) and layer != model:
            hooks.append(layer.register_forward_hook(hook_fn))

    # Forward pass
    with torch.no_grad():
        output = model(x)

    # Remove hooks
    for hook in hooks:
        hook.remove()

    # Print layer-by-layer information
    print(f"\n{'Layer':<25} {'Output Shape':<25} {'Parameters':<15}")
    print("-" * 80)

    total_params = 0
    for name, shape, params in zip(layer_names, layer_outputs, layer_params):
        print(f"{name:<25} {str(tuple(shape)):<25} {params:>12,}")
        total_params += params

    print("-" * 80)

    # Model statistics
    param_info = count_parameters(model)
    model_size = get_model_size_mb(model)

    print(f"\nTotal parameters: {param_info['total']:,}")
    print(f"Trainable parameters: {param_info['trainable']:,}")
    print(f"Non-trainable parameters: {param_info['non_trainable']:,}")
    print(f"Model size: {model_size:.2f} MB")
    print(f"Input size: {input_size}")
    print(f"Output size: {tuple(output.shape)}")

    print("=" * 80)


def plot_feature_maps(
    feature_maps: torch.Tensor,
    num_maps: int = 16,
    title: str = "Feature Maps",
    figsize: Tuple[int, int] = (15, 8),
):
    """
    Visualize feature maps from a convolutional layer

    Args:
        feature_maps: Feature maps tensor (batch, channels, height, width)
        num_maps: Number of feature maps to display
        title: Plot title
        figsize: Figure size
    """
    # Get the first image in batch
    if feature_maps.dim() == 4:
        feature_maps = feature_maps[0]  # (channels, height, width)

    # Detach and move to CPU
    feature_maps = feature_maps.detach().cpu()

    # Limit the number of feature maps
    num_maps = min(num_maps, feature_maps.shape[0])

    # Calculate grid size
    n_cols = 4
    n_rows = (num_maps + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    fig.suptitle(title, fontsize=16, fontweight="bold")

    # Flatten axes for easy iteration
    axes = axes.flatten() if num_maps > 1 else [axes]

    for idx in range(len(axes)):
        ax = axes[idx]

        if idx < num_maps:
            # Plot feature map
            img = feature_maps[idx].numpy()
            im = ax.imshow(img, cmap="viridis")
            ax.set_title(f"Filter {idx+1}")
            ax.axis("off")
            plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        else:
            # Hide extra subplots
            ax.axis("off")

    plt.tight_layout()
    plt.show()


def plot_filters(
    model: nn.Module,
    layer_name: str = None,
    num_filters: int = 16,
    figsize: Tuple[int, int] = (15, 8),
):
    """
    Visualize the learned filters from a convolutional layer

    Args:
        model: PyTorch model
        layer_name: Name of the layer to visualize (if None, uses first conv layer)
        num_filters: Number of filters to display
        figsize: Figure size
    """
    # Find the first convolutional layer if layer_name is None
    conv_layer = None

    if layer_name is None:
        for module in model.modules():
            if isinstance(module, nn.Conv2d):
                conv_layer = module
                break
    else:
        conv_layer = dict(model.named_modules())[layer_name]

    if conv_layer is None:
        print("No convolutional layer found!")
        return

    # Get the weights
    filters = conv_layer.weight.data.cpu()

    # Normalize filters to [0, 1] for visualization
    filters = (filters - filters.min()) / (filters.max() - filters.min())

    # Limit number of filters
    num_filters = min(num_filters, filters.shape[0])

    # Calculate grid size
    n_cols = 4
    n_rows = (num_filters + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    fig.suptitle(
        f"Learned Filters - {conv_layer.__class__.__name__}", fontsize=16, fontweight="bold"
    )

    axes = axes.flatten() if num_filters > 1 else [axes]

    for idx in range(len(axes)):
        ax = axes[idx]

        if idx < num_filters:
            # Get filter
            filt = filters[idx]

            # If filter has multiple input channels, show the first one
            if filt.shape[0] > 1:
                filt = filt[0]
            else:
                filt = filt.squeeze()

            # Plot filter
            ax.imshow(filt.numpy(), cmap="gray")
            ax.set_title(f"Filter {idx+1}")
            ax.axis("off")
        else:
            ax.axis("off")

    plt.tight_layout()
    plt.show()


def plot_training_history(history: dict, figsize: Tuple[int, int] = (15, 5)):
    """
    Plot training history (loss and accuracy)

    Args:
        history: Dictionary containing 'train_loss', 'val_loss', 'train_acc', 'val_acc'
        figsize: Figure size
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

    # Plot loss
    if "train_loss" in history:
        ax1.plot(history["train_loss"], label="Train Loss", marker="o")
    if "val_loss" in history:
        ax1.plot(history["val_loss"], label="Validation Loss", marker="o")
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Loss")
    ax1.set_title("Training and Validation Loss")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot accuracy
    if "train_acc" in history:
        ax2.plot(history["train_acc"], label="Train Accuracy", marker="o")
    if "val_acc" in history:
        ax2.plot(history["val_acc"], label="Validation Accuracy", marker="o")
    ax2.set_xlabel("Epoch")
    ax2.set_ylabel("Accuracy (%)")
    ax2.set_title("Training and Validation Accuracy")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def visualize_predictions(
    images: torch.Tensor,
    predictions: List,
    true_labels: List,
    class_names: List[str] = None,
    num_images: int = 10,
    figsize: Tuple[int, int] = (15, 8),
):
    """
    Visualize model predictions alongside ground truth

    Args:
        images: Batch of images
        predictions: Predicted class indices
        true_labels: Ground truth class indices
        class_names: List of class names
        num_images: Number of images to display
        figsize: Figure size
    """
    num_images = min(num_images, len(images))

    n_cols = 5
    n_rows = (num_images + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    axes = axes.flatten() if num_images > 1 else [axes]

    for idx in range(len(axes)):
        ax = axes[idx]

        if idx < num_images:
            # Get image
            img = images[idx].cpu()

            # Convert to numpy and transpose if needed
            if img.shape[0] in [1, 3]:  # (C, H, W) -> (H, W, C)
                img = img.permute(1, 2, 0)

            # Normalize to [0, 1] if needed
            img = img.numpy()
            img = (img - img.min()) / (img.max() - img.min() + 1e-8)

            # Plot image
            if img.shape[-1] == 1:
                ax.imshow(img.squeeze(), cmap="gray")
            else:
                ax.imshow(img)

            # Create title
            pred_label = predictions[idx]
            true_label = true_labels[idx]

            if class_names:
                pred_name = class_names[pred_label]
                true_name = class_names[true_label]
                title = f"Pred: {pred_name}\nTrue: {true_name}"
            else:
                title = f"Pred: {pred_label}\nTrue: {true_label}"

            # Color code: green if correct, red if wrong
            color = "green" if pred_label == true_label else "red"
            ax.set_title(title, color=color, fontsize=10)
            ax.axis("off")
        else:
            ax.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("CNN Architecture Visualizer")
    print("Import this module in your notebooks to visualize models!")
    print("\nExample usage:")
    print("  from scripts.visualize_architecture import visualize_model")
    print("  visualize_model(model, input_size=(1, 1, 28, 28))")

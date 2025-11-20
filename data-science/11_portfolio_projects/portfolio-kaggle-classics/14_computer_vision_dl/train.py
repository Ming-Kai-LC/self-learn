"""
Training Script for Deep Learning Computer Vision Models

This script provides command-line interface for training:
- Baseline CNN models
- Transfer learning models (ResNet, EfficientNet, MobileNet)
- Fine-tuning with learning rate scheduling
- Data augmentation and regularization

Usage:
    python train.py --model baseline --epochs 50 --batch_size 64
    python train.py --model efficientnet --freeze_base --epochs 30
    python train.py --model efficientnet --unfreeze_layers 50 --epochs 20
"""

import argparse
import os
from datetime import datetime
from pathlib import Path

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau,
    TensorBoard,
    LearningRateScheduler,
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from model import (
    build_baseline_cnn,
    build_deeper_cnn,
    build_transfer_learning_model,
    unfreeze_model,
    compile_model,
    print_model_info,
)


def load_cifar10_data():
    """
    Load and preprocess CIFAR-10 dataset.

    Returns:
        Tuple of (x_train, y_train), (x_val, y_val), (x_test, y_test)
    """
    print("Loading CIFAR-10 dataset...")
    (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

    # Split training data into train and validation (90/10 split)
    val_size = int(0.1 * len(x_train))
    x_val = x_train[-val_size:]
    y_val = y_train[-val_size:]
    x_train = x_train[:-val_size]
    y_train = y_train[:-val_size]

    # Convert to float32 and normalize to [0, 1]
    x_train = x_train.astype('float32') / 255.0
    x_val = x_val.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0

    # Convert labels to categorical (one-hot encoding)
    num_classes = 10
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_val = keras.utils.to_categorical(y_val, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    print(f"Train shape: {x_train.shape}, {y_train.shape}")
    print(f"Validation shape: {x_val.shape}, {y_val.shape}")
    print(f"Test shape: {x_test.shape}, {y_test.shape}")

    return (x_train, y_train), (x_val, y_val), (x_test, y_test)


def create_data_augmentation():
    """
    Create ImageDataGenerator for data augmentation.

    Returns:
        ImageDataGenerator with augmentation settings
    """
    return ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True,
        zoom_range=0.1,
        fill_mode='nearest'
    )


def create_callbacks(model_name, patience=10, reduce_lr_patience=5):
    """
    Create training callbacks.

    Args:
        model_name: Name of the model for file saving
        patience: Patience for early stopping
        reduce_lr_patience: Patience for learning rate reduction

    Returns:
        List of callbacks
    """
    # Create directories if they don't exist
    Path('models').mkdir(exist_ok=True)
    Path('logs').mkdir(exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    model_path = f'models/{model_name}_{timestamp}.h5'
    log_dir = f'logs/{model_name}_{timestamp}'

    callbacks = [
        # Save best model
        ModelCheckpoint(
            model_path,
            monitor='val_accuracy',
            save_best_only=True,
            mode='max',
            verbose=1
        ),

        # Early stopping
        EarlyStopping(
            monitor='val_loss',
            patience=patience,
            restore_best_weights=True,
            verbose=1
        ),

        # Reduce learning rate on plateau
        ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=reduce_lr_patience,
            min_lr=1e-7,
            verbose=1
        ),

        # TensorBoard logging
        TensorBoard(
            log_dir=log_dir,
            histogram_freq=1,
            write_graph=True
        )
    ]

    print(f"Model will be saved to: {model_path}")
    print(f"TensorBoard logs: {log_dir}")
    print(f"Run: tensorboard --logdir=logs")

    return callbacks


def cosine_decay_with_warmup(epoch, total_epochs=50, warmup_epochs=5,
                              max_lr=1e-3, min_lr=1e-6):
    """
    Cosine learning rate decay with warmup.

    Args:
        epoch: Current epoch
        total_epochs: Total training epochs
        warmup_epochs: Number of warmup epochs
        max_lr: Maximum learning rate
        min_lr: Minimum learning rate

    Returns:
        Learning rate for current epoch
    """
    if epoch < warmup_epochs:
        # Linear warmup
        return max_lr * (epoch + 1) / warmup_epochs
    else:
        # Cosine decay
        progress = (epoch - warmup_epochs) / (total_epochs - warmup_epochs)
        return min_lr + (max_lr - min_lr) * 0.5 * (1 + np.cos(np.pi * progress))


def train_model(
    model,
    x_train,
    y_train,
    x_val,
    y_val,
    model_name,
    epochs=50,
    batch_size=64,
    use_augmentation=True,
    use_cosine_decay=False
):
    """
    Train the model.

    Args:
        model: Keras model to train
        x_train, y_train: Training data
        x_val, y_val: Validation data
        model_name: Name for saving
        epochs: Number of training epochs
        batch_size: Batch size
        use_augmentation: Whether to use data augmentation
        use_cosine_decay: Whether to use cosine learning rate decay

    Returns:
        Training history
    """
    print(f"\nStarting training: {model_name}")
    print(f"Epochs: {epochs}, Batch size: {batch_size}")
    print(f"Augmentation: {use_augmentation}, Cosine decay: {use_cosine_decay}")

    # Create callbacks
    callbacks = create_callbacks(model_name, patience=10)

    # Add cosine decay scheduler if requested
    if use_cosine_decay:
        lr_scheduler = LearningRateScheduler(
            lambda epoch: cosine_decay_with_warmup(epoch, total_epochs=epochs)
        )
        callbacks.append(lr_scheduler)

    # Train with or without augmentation
    if use_augmentation:
        datagen = create_data_augmentation()
        history = model.fit(
            datagen.flow(x_train, y_train, batch_size=batch_size),
            steps_per_epoch=len(x_train) // batch_size,
            epochs=epochs,
            validation_data=(x_val, y_val),
            callbacks=callbacks,
            verbose=1
        )
    else:
        history = model.fit(
            x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_data=(x_val, y_val),
            callbacks=callbacks,
            verbose=1
        )

    return history


def main():
    """Main training function."""
    parser = argparse.ArgumentParser(
        description='Train deep learning computer vision models'
    )

    # Model selection
    parser.add_argument(
        '--model',
        type=str,
        default='baseline',
        choices=['baseline', 'deeper', 'resnet50', 'efficientnet', 'mobilenet'],
        help='Model architecture to train'
    )

    # Training parameters
    parser.add_argument('--epochs', type=int, default=50, help='Number of epochs')
    parser.add_argument('--batch_size', type=int, default=64, help='Batch size')
    parser.add_argument('--learning_rate', type=float, default=1e-3, help='Learning rate')
    parser.add_argument('--dropout', type=float, default=0.3, help='Dropout rate')

    # Transfer learning options
    parser.add_argument(
        '--freeze_base',
        action='store_true',
        help='Freeze base model (transfer learning)'
    )
    parser.add_argument(
        '--unfreeze_layers',
        type=int,
        default=0,
        help='Number of layers to unfreeze for fine-tuning'
    )

    # Augmentation and scheduling
    parser.add_argument(
        '--no_augmentation',
        action='store_true',
        help='Disable data augmentation'
    )
    parser.add_argument(
        '--cosine_decay',
        action='store_true',
        help='Use cosine learning rate decay with warmup'
    )

    # Other options
    parser.add_argument(
        '--label_smoothing',
        type=float,
        default=0.1,
        help='Label smoothing factor'
    )

    args = parser.parse_args()

    # Set random seeds for reproducibility
    np.random.seed(42)
    tf.random.set_seed(42)

    # Load data
    (x_train, y_train), (x_val, y_val), (x_test, y_test) = load_cifar10_data()

    # Build model
    print(f"\nBuilding model: {args.model}")
    if args.model == 'baseline':
        model = build_baseline_cnn(dropout_rate=args.dropout)
    elif args.model == 'deeper':
        model = build_deeper_cnn(dropout_rate=args.dropout)
    elif args.model in ['resnet50', 'efficientnet', 'mobilenet']:
        model = build_transfer_learning_model(
            base_model_name=args.model,
            freeze_base=args.freeze_base,
            dropout_rate=args.dropout
        )
    else:
        raise ValueError(f"Unknown model: {args.model}")

    # Unfreeze layers if specified
    if args.unfreeze_layers > 0:
        print(f"\nUnfreezing top {args.unfreeze_layers} layers...")
        model = unfreeze_model(model, args.unfreeze_layers)

    # Print model information
    print_model_info(model)

    # Compile model
    model = compile_model(
        model,
        learning_rate=args.learning_rate,
        label_smoothing=args.label_smoothing
    )

    # Train model
    history = train_model(
        model,
        x_train, y_train,
        x_val, y_val,
        model_name=args.model,
        epochs=args.epochs,
        batch_size=args.batch_size,
        use_augmentation=not args.no_augmentation,
        use_cosine_decay=args.cosine_decay
    )

    # Final evaluation on test set
    print("\n" + "="*60)
    print("Final Evaluation on Test Set")
    print("="*60)
    test_results = model.evaluate(x_test, y_test, verbose=0)
    print(f"Test Loss: {test_results[0]:.4f}")
    print(f"Test Accuracy: {test_results[1]:.4f}")
    print(f"Test Top-3 Accuracy: {test_results[2]:.4f}")
    print("="*60)

    print("\nTraining completed successfully!")


if __name__ == '__main__':
    main()

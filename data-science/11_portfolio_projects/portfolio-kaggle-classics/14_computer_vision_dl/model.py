"""
Model Architecture Definitions for Deep Learning Computer Vision

This module contains:
1. Baseline CNN architecture from scratch
2. Transfer learning model builders (ResNet, EfficientNet, MobileNet)
3. Model compilation utilities
4. Custom layers and blocks
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.applications import (
    ResNet50,
    EfficientNetB0,
    MobileNetV2,
)


def build_baseline_cnn(input_shape=(32, 32, 3), num_classes=10, dropout_rate=0.3):
    """
    Build a baseline CNN architecture from scratch.

    Architecture:
    - 3 Convolutional blocks (Conv → BatchNorm → ReLU → MaxPool → Dropout)
    - Global Average Pooling
    - Dense classification head

    Args:
        input_shape: Input image shape (height, width, channels)
        num_classes: Number of output classes
        dropout_rate: Dropout rate for regularization

    Returns:
        Compiled Keras model
    """
    model = models.Sequential(name='baseline_cnn')

    # Input layer
    model.add(layers.Input(shape=input_shape))

    # Block 1: 32 filters
    model.add(layers.Conv2D(32, (3, 3), padding='same', name='conv1'))
    model.add(layers.BatchNormalization(name='bn1'))
    model.add(layers.Activation('relu', name='relu1'))
    model.add(layers.MaxPooling2D((2, 2), name='pool1'))
    model.add(layers.Dropout(dropout_rate, name='dropout1'))

    # Block 2: 64 filters
    model.add(layers.Conv2D(64, (3, 3), padding='same', name='conv2'))
    model.add(layers.BatchNormalization(name='bn2'))
    model.add(layers.Activation('relu', name='relu2'))
    model.add(layers.MaxPooling2D((2, 2), name='pool2'))
    model.add(layers.Dropout(dropout_rate, name='dropout2'))

    # Block 3: 128 filters
    model.add(layers.Conv2D(128, (3, 3), padding='same', name='conv3'))
    model.add(layers.BatchNormalization(name='bn3'))
    model.add(layers.Activation('relu', name='relu3'))
    model.add(layers.MaxPooling2D((2, 2), name='pool3'))
    model.add(layers.Dropout(dropout_rate, name='dropout3'))

    # Global Average Pooling (better than Flatten for generalization)
    model.add(layers.GlobalAveragePooling2D(name='gap'))

    # Dense classification head
    model.add(layers.Dense(256, activation='relu', name='fc1'))
    model.add(layers.Dropout(dropout_rate, name='dropout_fc'))
    model.add(layers.Dense(num_classes, activation='softmax', name='predictions'))

    return model


def build_deeper_cnn(input_shape=(32, 32, 3), num_classes=10, dropout_rate=0.4):
    """
    Build a deeper CNN with 5 convolutional blocks.

    This is a more complex baseline for comparison.

    Args:
        input_shape: Input image shape
        num_classes: Number of output classes
        dropout_rate: Dropout rate

    Returns:
        Compiled Keras model
    """
    model = models.Sequential(name='deeper_cnn')

    model.add(layers.Input(shape=input_shape))

    # Block 1
    model.add(layers.Conv2D(32, (3, 3), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.Conv2D(32, (3, 3), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Dropout(dropout_rate))

    # Block 2
    model.add(layers.Conv2D(64, (3, 3), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.Conv2D(64, (3, 3), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Dropout(dropout_rate))

    # Block 3
    model.add(layers.Conv2D(128, (3, 3), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Dropout(dropout_rate))

    # Classification head
    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dropout(dropout_rate))
    model.add(layers.Dense(num_classes, activation='softmax'))

    return model


def build_transfer_learning_model(
    base_model_name='efficientnet',
    input_shape=(32, 32, 3),
    num_classes=10,
    freeze_base=True,
    dropout_rate=0.3
):
    """
    Build a transfer learning model using pre-trained weights.

    Args:
        base_model_name: Name of base model ('resnet50', 'efficientnet', 'mobilenet')
        input_shape: Input image shape
        num_classes: Number of output classes
        freeze_base: Whether to freeze base model layers
        dropout_rate: Dropout rate in classification head

    Returns:
        Compiled Keras model
    """
    # Select base model
    base_model_map = {
        'resnet50': ResNet50,
        'efficientnet': EfficientNetB0,
        'mobilenet': MobileNetV2,
    }

    if base_model_name.lower() not in base_model_map:
        raise ValueError(
            f"Unknown model: {base_model_name}. "
            f"Choose from {list(base_model_map.keys())}"
        )

    BaseModel = base_model_map[base_model_name.lower()]

    # Load pre-trained base model (without top classification layer)
    base_model = BaseModel(
        include_top=False,
        weights='imagenet',
        input_shape=input_shape,
        pooling='avg'  # Global average pooling
    )

    # Freeze base model if specified
    base_model.trainable = not freeze_base

    # Build model with custom classification head
    inputs = layers.Input(shape=input_shape)

    # Preprocessing (normalize to ImageNet statistics)
    x = inputs
    if base_model_name.lower() == 'resnet50':
        x = tf.keras.applications.resnet50.preprocess_input(x)
    elif base_model_name.lower() == 'efficientnet':
        x = tf.keras.applications.efficientnet.preprocess_input(x)
    elif base_model_name.lower() == 'mobilenet':
        x = tf.keras.applications.mobilenet_v2.preprocess_input(x)

    # Base model
    x = base_model(x, training=False)  # Set to False for frozen base

    # Classification head
    x = layers.Dropout(dropout_rate)(x)
    x = layers.Dense(256, activation='relu', name='fc1')(x)
    x = layers.Dropout(dropout_rate)(x)
    outputs = layers.Dense(num_classes, activation='softmax', name='predictions')(x)

    model = models.Model(inputs, outputs, name=f'{base_model_name}_transfer')

    return model


def unfreeze_model(model, num_layers_to_unfreeze=50):
    """
    Unfreeze the top layers of a pre-trained model for fine-tuning.

    Args:
        model: Keras model with frozen base
        num_layers_to_unfreeze: Number of top layers to unfreeze

    Returns:
        Model with unfrozen layers
    """
    # Unfreeze the base model
    base_model = None
    for layer in model.layers:
        if isinstance(layer, keras.Model):
            base_model = layer
            break

    if base_model is None:
        print("No base model found. Model might already be unfrozen.")
        return model

    # Set base model to trainable
    base_model.trainable = True

    # Freeze all layers except the top ones
    total_layers = len(base_model.layers)
    freeze_until = max(0, total_layers - num_layers_to_unfreeze)

    for i, layer in enumerate(base_model.layers):
        if i < freeze_until:
            layer.trainable = False
        else:
            layer.trainable = True

    print(f"Unfroze top {num_layers_to_unfreeze} layers of base model")
    print(f"Total layers: {total_layers}, Frozen: {freeze_until}, Trainable: {num_layers_to_unfreeze}")

    return model


def compile_model(model, learning_rate=1e-3, label_smoothing=0.1):
    """
    Compile model with optimizer, loss, and metrics.

    Args:
        model: Keras model to compile
        learning_rate: Learning rate for optimizer
        label_smoothing: Label smoothing factor (0.0 to 0.2)

    Returns:
        Compiled model
    """
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)

    loss = keras.losses.CategoricalCrossentropy(
        label_smoothing=label_smoothing
    )

    metrics = [
        'accuracy',
        keras.metrics.TopKCategoricalAccuracy(k=3, name='top3_accuracy'),
        keras.metrics.Precision(name='precision'),
        keras.metrics.Recall(name='recall')
    ]

    model.compile(
        optimizer=optimizer,
        loss=loss,
        metrics=metrics
    )

    return model


def get_model_summary(model):
    """
    Get comprehensive model summary including parameter count and size.

    Args:
        model: Keras model

    Returns:
        Dictionary with model statistics
    """
    trainable_params = sum([tf.size(w).numpy() for w in model.trainable_weights])
    non_trainable_params = sum([tf.size(w).numpy() for w in model.non_trainable_weights])
    total_params = trainable_params + non_trainable_params

    # Estimate model size (4 bytes per float32 parameter)
    model_size_mb = (total_params * 4) / (1024 ** 2)

    return {
        'total_params': total_params,
        'trainable_params': trainable_params,
        'non_trainable_params': non_trainable_params,
        'model_size_mb': model_size_mb,
        'layers': len(model.layers)
    }


def print_model_info(model):
    """
    Print detailed model information.

    Args:
        model: Keras model
    """
    print(f"\n{'='*60}")
    print(f"Model: {model.name}")
    print(f"{'='*60}")

    model.summary()

    stats = get_model_summary(model)
    print(f"\n{'='*60}")
    print("Model Statistics:")
    print(f"{'='*60}")
    print(f"Total Parameters:        {stats['total_params']:,}")
    print(f"Trainable Parameters:    {stats['trainable_params']:,}")
    print(f"Non-trainable Parameters: {stats['non_trainable_params']:,}")
    print(f"Estimated Size:          {stats['model_size_mb']:.2f} MB")
    print(f"Number of Layers:        {stats['layers']}")
    print(f"{'='*60}\n")


# Example usage
if __name__ == "__main__":
    print("Building baseline CNN...")
    baseline = build_baseline_cnn()
    print_model_info(baseline)

    print("\nBuilding ResNet50 transfer learning model...")
    resnet = build_transfer_learning_model('resnet50')
    print_model_info(resnet)

    print("\nBuilding EfficientNetB0 transfer learning model...")
    efficientnet = build_transfer_learning_model('efficientnet')
    print_model_info(efficientnet)

    print("\nBuilding MobileNetV2 transfer learning model...")
    mobilenet = build_transfer_learning_model('mobilenet')
    print_model_info(mobilenet)

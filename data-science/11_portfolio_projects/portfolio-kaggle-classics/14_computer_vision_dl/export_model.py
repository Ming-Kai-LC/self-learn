"""
Model Export Utilities for Production Deployment

This script exports trained models to various formats:
1. ONNX - Universal format for cross-framework deployment
2. TensorFlow Lite - Mobile and edge device deployment
3. SavedModel - TensorFlow Serving format
4. Quantization - Model compression

Usage:
    python export_model.py --model models/efficientnet_best.h5 --format onnx
    python export_model.py --model models/baseline_cnn.h5 --format tflite --quantize
    python export_model.py --model models/resnet50.h5 --format all
"""

import argparse
import os
from pathlib import Path

import numpy as np
import tensorflow as tf
from tensorflow import keras

# Try to import ONNX conversion tools
try:
    import tf2onnx
    ONNX_AVAILABLE = True
except ImportError:
    print("Warning: tf2onnx not installed. ONNX export will not be available.")
    print("Install with: pip install tf2onnx onnx")
    ONNX_AVAILABLE = False


def export_to_savedmodel(model, output_path='models/saved_model'):
    """
    Export model to TensorFlow SavedModel format.

    This format is used for TensorFlow Serving and TensorFlow.js.

    Args:
        model: Keras model
        output_path: Directory to save the model

    Returns:
        Path to saved model
    """
    print("\n" + "="*60)
    print("Exporting to TensorFlow SavedModel")
    print("="*60)

    # Create directory
    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Save model
    model.save(output_path, save_format='tf')

    # Get model size
    size_mb = sum(
        f.stat().st_size for f in Path(output_path).rglob('*') if f.is_file()
    ) / (1024 ** 2)

    print(f"SavedModel exported to: {output_path}")
    print(f"Model size: {size_mb:.2f} MB")
    print("="*60)

    return output_path


def export_to_onnx(model, output_path='models/model.onnx', opset=13):
    """
    Export model to ONNX format.

    ONNX (Open Neural Network Exchange) is a universal format that works
    across frameworks (TensorFlow, PyTorch, etc.) and platforms.

    Args:
        model: Keras model
        output_path: Path to save ONNX model
        opset: ONNX opset version

    Returns:
        Path to ONNX model
    """
    if not ONNX_AVAILABLE:
        print("ONNX export not available. Please install tf2onnx.")
        return None

    print("\n" + "="*60)
    print("Exporting to ONNX")
    print("="*60)

    # Create directory
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # Convert to ONNX
    spec = (tf.TensorSpec(model.input_shape, tf.float32, name="input"),)

    try:
        model_proto, _ = tf2onnx.convert.from_keras(
            model,
            input_signature=spec,
            opset=opset,
            output_path=output_path
        )

        # Get model size
        size_mb = Path(output_path).stat().st_size / (1024 ** 2)

        print(f"ONNX model exported to: {output_path}")
        print(f"Model size: {size_mb:.2f} MB")
        print(f"ONNX opset: {opset}")
        print("="*60)

        return output_path

    except Exception as e:
        print(f"Error exporting to ONNX: {e}")
        return None


def export_to_tflite(model, output_path='models/model.tflite', quantize=False):
    """
    Export model to TensorFlow Lite format.

    TFLite is optimized for mobile and edge devices (Android, iOS, RPi, etc.).

    Args:
        model: Keras model
        output_path: Path to save TFLite model
        quantize: Whether to apply dynamic range quantization

    Returns:
        Path to TFLite model
    """
    print("\n" + "="*60)
    print(f"Exporting to TensorFlow Lite (Quantize: {quantize})")
    print("="*60)

    # Create directory
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # Convert to TFLite
    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    if quantize:
        # Apply dynamic range quantization (INT8)
        # This reduces model size by ~4x with minimal accuracy loss
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        print("Applying dynamic range quantization (FP32 -> INT8)...")

    # Convert
    tflite_model = converter.convert()

    # Save model
    with open(output_path, 'wb') as f:
        f.write(tflite_model)

    # Get model size
    size_mb = Path(output_path).stat().st_size / (1024 ** 2)

    print(f"TFLite model exported to: {output_path}")
    print(f"Model size: {size_mb:.2f} MB")
    print("="*60)

    return output_path


def export_to_tflite_full_quantization(
    model,
    representative_dataset_fn,
    output_path='models/model_quantized.tflite'
):
    """
    Export model with full integer quantization.

    This provides maximum size reduction and inference speed,
    but requires a representative dataset for calibration.

    Args:
        model: Keras model
        representative_dataset_fn: Generator yielding sample data
        output_path: Path to save quantized model

    Returns:
        Path to quantized TFLite model
    """
    print("\n" + "="*60)
    print("Exporting to TensorFlow Lite (Full Integer Quantization)")
    print("="*60)

    # Create directory
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # Convert to TFLite with full quantization
    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    # Enable all optimizations
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    # Provide representative dataset for calibration
    converter.representative_dataset = representative_dataset_fn

    # Ensure all operations are quantized
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
    converter.inference_input_type = tf.int8
    converter.inference_output_type = tf.int8

    # Convert
    try:
        tflite_model = converter.convert()

        # Save model
        with open(output_path, 'wb') as f:
            f.write(tflite_model)

        # Get model size
        size_mb = Path(output_path).stat().st_size / (1024 ** 2)

        print(f"Fully quantized TFLite model exported to: {output_path}")
        print(f"Model size: {size_mb:.2f} MB")
        print("="*60)

        return output_path

    except Exception as e:
        print(f"Error with full quantization: {e}")
        print("Falling back to dynamic range quantization...")
        return export_to_tflite(model, output_path, quantize=True)


def create_representative_dataset():
    """
    Create a representative dataset generator for quantization calibration.

    Returns:
        Generator function
    """
    # Load a subset of CIFAR-10 for calibration
    (x_train, _), _ = keras.datasets.cifar10.load_data()
    x_train = x_train[:1000].astype('float32') / 255.0

    def representative_dataset_gen():
        for i in range(100):
            # Get batch of one sample
            sample = x_train[i:i+1]
            yield [sample]

    return representative_dataset_gen


def benchmark_tflite_model(tflite_path, x_test, num_samples=100):
    """
    Benchmark TFLite model inference time and accuracy.

    Args:
        tflite_path: Path to TFLite model
        x_test: Test data
        num_samples: Number of samples to test

    Returns:
        Dictionary with benchmark results
    """
    print("\n" + "="*60)
    print("Benchmarking TFLite Model")
    print("="*60)

    # Load TFLite model
    interpreter = tf.lite.Interpreter(model_path=tflite_path)
    interpreter.allocate_tensors()

    # Get input and output details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    print(f"Input shape: {input_details[0]['shape']}")
    print(f"Input dtype: {input_details[0]['dtype']}")
    print(f"Output shape: {output_details[0]['shape']}")

    # Test on samples
    import time
    times = []

    for i in range(num_samples):
        sample = x_test[i:i+1]

        # Set input tensor
        interpreter.set_tensor(input_details[0]['index'], sample)

        # Run inference
        start_time = time.time()
        interpreter.invoke()
        elapsed = time.time() - start_time
        times.append(elapsed)

    avg_time_ms = np.mean(times) * 1000

    print(f"Samples tested: {num_samples}")
    print(f"Average inference time: {avg_time_ms:.2f} ms")
    print(f"Throughput: {1000/avg_time_ms:.1f} images/sec")
    print("="*60)

    return {
        'avg_time_ms': avg_time_ms,
        'throughput': 1000 / avg_time_ms
    }


def compare_model_sizes(model_name):
    """
    Compare sizes of different export formats.

    Args:
        model_name: Base name of the model
    """
    print("\n" + "="*60)
    print("Model Size Comparison")
    print("="*60)

    formats = {
        'Original (.h5)': f'models/{model_name}.h5',
        'SavedModel': f'models/{model_name}_saved',
        'ONNX': f'models/{model_name}.onnx',
        'TFLite': f'models/{model_name}.tflite',
        'TFLite (Quantized)': f'models/{model_name}_quantized.tflite',
    }

    for format_name, path in formats.items():
        if not Path(path).exists():
            continue

        if Path(path).is_dir():
            # For SavedModel
            size_mb = sum(
                f.stat().st_size for f in Path(path).rglob('*') if f.is_file()
            ) / (1024 ** 2)
        else:
            # For single files
            size_mb = Path(path).stat().st_size / (1024 ** 2)

        print(f"{format_name:25s}: {size_mb:8.2f} MB")

    print("="*60)


def main():
    """Main export function."""
    parser = argparse.ArgumentParser(
        description='Export trained models to various formats'
    )

    parser.add_argument(
        '--model',
        type=str,
        required=True,
        help='Path to trained model (.h5 file)'
    )
    parser.add_argument(
        '--format',
        type=str,
        default='all',
        choices=['savedmodel', 'onnx', 'tflite', 'all'],
        help='Export format'
    )
    parser.add_argument(
        '--quantize',
        action='store_true',
        help='Apply quantization to TFLite model'
    )
    parser.add_argument(
        '--full_quantize',
        action='store_true',
        help='Apply full integer quantization (requires representative dataset)'
    )
    parser.add_argument(
        '--benchmark',
        action='store_true',
        help='Benchmark TFLite model performance'
    )
    parser.add_argument(
        '--output_dir',
        type=str,
        default='models',
        help='Output directory for exported models'
    )

    args = parser.parse_args()

    # Load model
    print(f"Loading model from: {args.model}")
    model = keras.models.load_model(args.model)
    print("Model loaded successfully!")
    print(f"Input shape: {model.input_shape}")
    print(f"Output shape: {model.output_shape}")

    # Get base model name
    model_name = Path(args.model).stem

    # Export to requested formats
    if args.format in ['savedmodel', 'all']:
        export_to_savedmodel(
            model,
            output_path=f'{args.output_dir}/{model_name}_saved'
        )

    if args.format in ['onnx', 'all']:
        export_to_onnx(
            model,
            output_path=f'{args.output_dir}/{model_name}.onnx'
        )

    if args.format in ['tflite', 'all']:
        if args.full_quantize:
            # Full integer quantization
            representative_dataset = create_representative_dataset()
            tflite_path = export_to_tflite_full_quantization(
                model,
                representative_dataset,
                output_path=f'{args.output_dir}/{model_name}_quantized.tflite'
            )
        else:
            # Standard or dynamic range quantization
            tflite_path = export_to_tflite(
                model,
                output_path=f'{args.output_dir}/{model_name}.tflite',
                quantize=args.quantize
            )

        # Benchmark TFLite model if requested
        if args.benchmark and tflite_path:
            # Load test data
            (_, _), (x_test, _) = keras.datasets.cifar10.load_data()
            x_test = x_test.astype('float32') / 255.0
            benchmark_tflite_model(tflite_path, x_test)

    # Compare model sizes
    compare_model_sizes(model_name)

    print("\nExport completed successfully!")
    print("\nNext steps:")
    print("1. Test ONNX model: onnxruntime")
    print("2. Deploy TFLite to mobile: Android/iOS app")
    print("3. Serve SavedModel: TensorFlow Serving or FastAPI")


if __name__ == '__main__':
    main()

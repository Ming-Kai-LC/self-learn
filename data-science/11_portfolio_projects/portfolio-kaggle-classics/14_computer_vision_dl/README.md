# Project 14: Deep Learning Computer Vision

**Difficulty**: ⭐⭐⭐ Advanced
**Estimated Time**: 8-12 hours
**Status**: Portfolio Project

## Problem Statement

Build a robust deep learning image classification system using modern computer vision techniques. This project demonstrates proficiency in:
- Convolutional Neural Networks (CNNs) from scratch
- Transfer learning with state-of-the-art pre-trained models
- Data augmentation strategies
- Model optimization (pruning, quantization)
- Model interpretability (GradCAM)
- Production deployment (ONNX, TensorFlow Lite)

## Dataset

**Primary**: CIFAR-10 (60,000 32x32 color images in 10 classes)
- Training: 50,000 images
- Test: 10,000 images
- Classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

**Alternative**: Fashion-MNIST or custom dataset

## Approach

### 1. Data Exploration & Preprocessing
- Dataset visualization and class distribution analysis
- Data normalization and standardization
- Train/validation/test split (80/10/10)

### 2. Data Augmentation
- Random rotation (±15 degrees)
- Horizontal flip
- Random zoom (10-20%)
- Color jitter (brightness, contrast, saturation)
- Cutout/random erasing
- Mixup (advanced technique)

### 3. Baseline Model
- Custom CNN architecture from scratch
- Architecture: Conv → BatchNorm → ReLU → MaxPool → Dropout
- 3-5 convolutional blocks
- Global Average Pooling
- Dense classification head

### 4. Transfer Learning
Pre-trained models (ImageNet weights):
- **ResNet50**: Deep residual network, 25M parameters
- **EfficientNetB0**: Compound scaling, 5M parameters
- **MobileNetV2**: Mobile-optimized, 3.5M parameters

Fine-tuning strategies:
- Freeze base layers, train classifier only (Phase 1)
- Unfreeze top layers, fine-tune with low LR (Phase 2)
- Progressive unfreezing (optional)

### 5. Training Optimization
- **Loss**: Categorical cross-entropy with label smoothing
- **Optimizer**: Adam with learning rate scheduling
- **Learning Rate Schedule**:
  - Warmup: Linear increase for first 5 epochs
  - Decay: Cosine annealing or ReduceLROnPlateau
- **Regularization**:
  - L2 weight decay
  - Dropout (0.3-0.5)
  - Early stopping (patience=10)
- **Batch Size**: 32-64 (depending on GPU memory)
- **Epochs**: 50-100 with early stopping

### 6. Model Evaluation
- Accuracy, Precision, Recall, F1-score
- Confusion matrix heatmap
- Per-class performance analysis
- Error analysis (misclassified examples)
- Model comparison table:
  - Test accuracy
  - Number of parameters
  - Inference time (CPU/GPU)
  - Model size (MB)

### 7. Model Interpretability
- **GradCAM** (Gradient-weighted Class Activation Mapping)
  - Visualize which regions of images the model focuses on
  - Identify potential biases or spurious correlations
  - Validate model is learning relevant features

### 8. Model Optimization
- **Pruning**: Remove low-magnitude weights (10-30% sparsity)
- **Quantization**: Convert FP32 → INT8 (4x size reduction)
- **Knowledge Distillation**: Train smaller model using larger model's outputs (optional)
- Compare optimized vs. original:
  - Accuracy drop (should be <2%)
  - Size reduction (target: 4-10x)
  - Speed improvement (target: 2-4x)

### 9. Model Export & Deployment
- **ONNX**: Universal model format for cross-framework deployment
- **TensorFlow Lite**: Mobile and edge device deployment
- **TensorFlow Serving**: Production REST API serving
- Benchmarking on different platforms (CPU, mobile)

## Technical Stack

### Core Frameworks
- **TensorFlow 2.x** (primary) or **PyTorch 1.10+**
- Keras (high-level API)

### Computer Vision
- OpenCV (image preprocessing)
- Albumentations (advanced augmentation)
- PIL/Pillow (image I/O)

### Visualization & Analysis
- Matplotlib, Seaborn (plots)
- TensorBoard (training monitoring)
- Plotly (interactive visualizations)

### Model Tools
- ONNX (model export)
- TensorFlow Lite (mobile deployment)
- tf-keras-vis (GradCAM)

### Utilities
- NumPy (numerical operations)
- Pandas (data management)
- scikit-learn (metrics)
- tqdm (progress bars)

## Expected Results

### Performance Targets
- **Baseline CNN**: 70-75% test accuracy
- **Transfer Learning (ResNet50)**: 85-90% test accuracy
- **Transfer Learning (EfficientNetB0)**: 90-93% test accuracy
- **Fine-tuned Best Model**: **>90% test accuracy**

### Model Comparison Example

| Model | Test Acc | Params | Size (MB) | Inference (ms) |
|-------|----------|--------|-----------|----------------|
| Baseline CNN | 72.5% | 2.1M | 8.3 | 12 |
| ResNet50 | 88.3% | 25.6M | 98.0 | 45 |
| EfficientNetB0 | 91.7% | 5.3M | 21.0 | 28 |
| MobileNetV2 | 89.2% | 3.5M | 14.0 | 18 |
| EfficientNet (Pruned) | 90.8% | 5.3M | 5.2 | 22 |
| EfficientNet (Quantized) | 91.2% | 5.3M | 5.5 | 15 |

### Deliverables
1. ✅ Fully documented Jupyter notebook
2. ✅ Modular Python scripts (train, evaluate, export)
3. ✅ Trained model weights
4. ✅ ONNX and TFLite exported models
5. ✅ Performance comparison report
6. ✅ GradCAM visualizations
7. ✅ Deployment-ready code

## Project Structure

```
14_computer_vision_dl/
├── README.md                    # This file
├── computer_vision_dl.ipynb     # Main notebook
├── requirements.txt             # Dependencies
├── model.py                     # Model architectures
├── train.py                     # Training script
├── evaluate.py                  # Evaluation utilities
├── export_model.py              # ONNX/TFLite export
├── data/                        # Data directory (gitignored)
│   ├── cifar-10/               # CIFAR-10 dataset
│   └── processed/              # Augmented samples
├── models/                      # Saved models (gitignored)
│   ├── baseline_cnn.h5
│   ├── resnet50_finetuned.h5
│   ├── efficientnet_best.h5
│   ├── model_optimized.onnx
│   └── model_quantized.tflite
├── results/                     # Results and visualizations
│   ├── confusion_matrix.png
│   ├── gradcam_examples.png
│   ├── training_history.png
│   └── model_comparison.csv
└── notebooks/                   # Experimental notebooks
    └── exploration.ipynb
```

## Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download Dataset
```python
# CIFAR-10 auto-downloads via TensorFlow/PyTorch
from tensorflow.keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
```

### 3. Run the Notebook
```bash
jupyter notebook computer_vision_dl.ipynb
```

### 4. Train Models (Script)
```bash
# Train baseline CNN
python train.py --model baseline --epochs 50 --batch_size 64

# Train with transfer learning
python train.py --model efficientnet --epochs 30 --batch_size 32 --freeze_base

# Fine-tune
python train.py --model efficientnet --epochs 20 --batch_size 16 --unfreeze_layers 50
```

### 5. Evaluate Models
```bash
python evaluate.py --model models/efficientnet_best.h5 --gradcam
```

### 6. Export Model
```bash
python export_model.py --model models/efficientnet_best.h5 --format onnx
python export_model.py --model models/efficientnet_best.h5 --format tflite --quantize
```

## Key Learning Outcomes

By completing this project, you will:

1. ✅ Understand CNN architecture design principles
2. ✅ Master transfer learning and fine-tuning strategies
3. ✅ Implement advanced data augmentation techniques
4. ✅ Apply learning rate scheduling and regularization
5. ✅ Conduct comprehensive model evaluation and comparison
6. ✅ Interpret model predictions using GradCAM
7. ✅ Optimize models for production (pruning, quantization)
8. ✅ Export models to deployment formats (ONNX, TFLite)
9. ✅ Build end-to-end computer vision pipelines
10. ✅ Demonstrate industry-ready deep learning skills

## Next Steps & Extensions

### Beginner Extensions
- Try different datasets (Fashion-MNIST, Cats vs Dogs)
- Experiment with different augmentation strategies
- Visualize feature maps from intermediate layers

### Intermediate Extensions
- Implement custom data loaders for large datasets
- Add test-time augmentation (TTA)
- Create ensemble models (voting/averaging)
- Deploy as REST API using FastAPI

### Advanced Extensions
- Object detection (YOLO, Faster R-CNN)
- Semantic segmentation (U-Net, DeepLab)
- Multi-label classification
- Self-supervised learning (SimCLR, MoCo)
- Neural Architecture Search (NAS)
- Deploy to edge devices (Raspberry Pi, Jetson Nano)

## Resources

### Courses & Tutorials
- [Stanford CS231n: CNNs for Visual Recognition](http://cs231n.stanford.edu/)
- [Fast.ai Practical Deep Learning](https://course.fast.ai/)
- [TensorFlow Image Classification Tutorial](https://www.tensorflow.org/tutorials/images/classification)

### Papers
- ResNet: "Deep Residual Learning for Image Recognition" (He et al., 2015)
- EfficientNet: "Rethinking Model Scaling for CNNs" (Tan & Le, 2019)
- MobileNet: "Efficient CNNs for Mobile Vision" (Howard et al., 2017)
- GradCAM: "Visual Explanations from Deep Networks" (Selvaraju et al., 2017)

### Tools & Libraries
- [TensorFlow Model Optimization](https://www.tensorflow.org/model_optimization)
- [ONNX Runtime](https://onnxruntime.ai/)
- [Albumentations Documentation](https://albumentations.ai/)
- [TensorBoard Guide](https://www.tensorflow.org/tensorboard)

## Portfolio Highlights

**What makes this project stand out?**

1. **Comprehensive Comparison**: Not just one model, but systematic comparison of multiple approaches
2. **Production-Ready**: Includes optimization and deployment, not just training
3. **Interpretability**: GradCAM shows you understand model explainability
4. **Best Practices**: Data augmentation, learning rate scheduling, proper evaluation
5. **Modular Code**: Reusable scripts, not just notebook code
6. **Documentation**: Clear explanations of methodology and trade-offs

**Interview Talking Points:**
- "I implemented transfer learning with three different architectures and compared their trade-offs"
- "I reduced model size by 75% through quantization with only 0.5% accuracy loss"
- "I used GradCAM to verify the model learned relevant features, not spurious correlations"
- "I exported the model to ONNX for cross-platform deployment"

---

**Author**: Generated for Data Science Portfolio
**Date**: 2025-11-20
**License**: MIT

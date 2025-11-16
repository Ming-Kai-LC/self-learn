"""
Verify that all notebooks are ready to run

This script checks that:
1. All notebooks exist
2. All notebooks are valid JSON
3. Required packages are installed
4. Datasets are available
"""

import json
import sys
from pathlib import Path


def check_notebook_exists(notebook_path):
    """Check if notebook exists and is valid JSON"""
    if not notebook_path.exists():
        return False, f"File not found: {notebook_path}"

    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = json.load(f)
        return True, "OK"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    except Exception as e:
        return False, f"Error: {e}"


def main():
    print("=" * 60)
    print("CNN Learning Project - Notebook Verification")
    print("=" * 60)

    # Get notebooks directory
    script_dir = Path(__file__).parent
    notebooks_dir = script_dir.parent / "notebooks"

    # List of expected notebooks
    notebooks = [
        "00_setup_and_introduction.ipynb",
        "01_neural_network_fundamentals.ipynb",
        "02_introduction_to_cnn.ipynb",
        "03_building_your_first_cnn.ipynb",
        "04_training_and_optimization.ipynb",
        "05_cnn_architectures.ipynb",
        "06_transfer_learning.ipynb",
        "07_image_classification_project.ipynb",
        "08_intro_to_object_detection.ipynb",
        "09_intro_to_image_segmentation.ipynb",
        "10_final_projects_and_next_steps.ipynb",
    ]

    print("\nChecking notebooks...")
    print("-" * 60)

    all_ok = True
    for nb_name in notebooks:
        nb_path = notebooks_dir / nb_name
        success, message = check_notebook_exists(nb_path)

        status = "[OK]" if success else "[ERROR]"
        print(f"{status} {nb_name}: {message}")

        if not success:
            all_ok = False

    print("-" * 60)

    # Check packages
    print("\nChecking required packages...")
    print("-" * 60)

    packages_ok = True
    try:
        import torch

        print(f"[OK] PyTorch {torch.__version__}")
    except ImportError:
        print("[ERROR] PyTorch not installed")
        packages_ok = False

    try:
        import torchvision

        print(f"[OK] TorchVision {torchvision.__version__}")
    except ImportError:
        print("[ERROR] TorchVision not installed")
        packages_ok = False

    try:
        import numpy

        print(f"[OK] NumPy {numpy.__version__}")
    except ImportError:
        print("[ERROR] NumPy not installed")
        packages_ok = False

    try:
        import matplotlib

        print(f"[OK] Matplotlib {matplotlib.__version__}")
    except ImportError:
        print("[ERROR] Matplotlib not installed")
        packages_ok = False

    print("-" * 60)

    # Check datasets
    print("\nChecking datasets...")
    print("-" * 60)

    data_dir = script_dir.parent / "data" / "datasets"
    mnist_dir = data_dir / "MNIST"
    cifar_dir = data_dir / "cifar-10-batches-py"

    datasets_ok = True
    if mnist_dir.exists():
        print("[OK] MNIST dataset found")
    else:
        print("[WARNING] MNIST dataset not found (will auto-download when needed)")
        datasets_ok = False

    if cifar_dir.exists():
        print("[OK] CIFAR-10 dataset found")
    else:
        print("[WARNING] CIFAR-10 dataset not found (will auto-download when needed)")
        datasets_ok = False

    print("-" * 60)

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)

    if all_ok and packages_ok:
        print("[OK] All notebooks are valid and ready to run!")
        if not datasets_ok:
            print("[INFO] Datasets will auto-download on first use")
        print("\nTo start learning:")
        print("  1. cd notebooks")
        print("  2. jupyter notebook")
        print("  3. Open 00_setup_and_introduction.ipynb")
        return 0
    else:
        if not all_ok:
            print("[ERROR] Some notebooks have issues")
        if not packages_ok:
            print("[ERROR] Some required packages are missing")
            print("\nInstall missing packages with:")
            print("  pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())

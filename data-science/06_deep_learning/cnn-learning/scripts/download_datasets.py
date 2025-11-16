"""
Dataset Downloader for CNN Learning Project

This script helps download common datasets used throughout the course:
- MNIST (handwritten digits)
- CIFAR-10 (small images in 10 categories)
- Sample images for testing

Usage:
    python download_datasets.py --all
    python download_datasets.py --mnist
    python download_datasets.py --cifar10
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import torch
    import torchvision
    import torchvision.transforms as transforms
    from torchvision.datasets import CIFAR10, MNIST
except ImportError:
    print("Error: PyTorch and torchvision are required.")
    print("Please install them with: pip install torch torchvision")
    sys.exit(1)


def get_data_dir():
    """Get the data directory path relative to script location"""
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data" / "datasets"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def download_mnist():
    """Download MNIST dataset"""
    print("\n" + "=" * 60)
    print("Downloading MNIST Dataset")
    print("=" * 60)
    print("MNIST contains 70,000 handwritten digit images (0-9)")
    print("Training set: 60,000 images")
    print("Test set: 10,000 images")
    print("Image size: 28x28 pixels, grayscale")
    print()

    data_dir = get_data_dir()

    try:
        # Download training set
        print("Downloading training set...")
        train_dataset = MNIST(
            root=str(data_dir), train=True, download=True, transform=transforms.ToTensor()
        )
        print(f"[OK] Training set downloaded: {len(train_dataset)} images")

        # Download test set
        print("Downloading test set...")
        test_dataset = MNIST(
            root=str(data_dir), train=False, download=True, transform=transforms.ToTensor()
        )
        print(f"[OK] Test set downloaded: {len(test_dataset)} images")

        print(f"\n[OK] MNIST dataset successfully downloaded to: {data_dir}")
        print(f"Total disk space used: ~15 MB")

        return True

    except Exception as e:
        print(f"\n[ERROR] Error downloading MNIST: {e}")
        return False


def download_cifar10():
    """Download CIFAR-10 dataset"""
    print("\n" + "=" * 60)
    print("Downloading CIFAR-10 Dataset")
    print("=" * 60)
    print("CIFAR-10 contains 60,000 color images in 10 classes")
    print("Classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck")
    print("Training set: 50,000 images")
    print("Test set: 10,000 images")
    print("Image size: 32x32 pixels, RGB color")
    print()

    data_dir = get_data_dir()

    try:
        # Download training set
        print("Downloading training set... (this may take a few minutes)")
        train_dataset = CIFAR10(
            root=str(data_dir), train=True, download=True, transform=transforms.ToTensor()
        )
        print(f"[OK] Training set downloaded: {len(train_dataset)} images")

        # Download test set
        print("Downloading test set...")
        test_dataset = CIFAR10(
            root=str(data_dir), train=False, download=True, transform=transforms.ToTensor()
        )
        print(f"[OK] Test set downloaded: {len(test_dataset)} images")

        print(f"\n[OK] CIFAR-10 dataset successfully downloaded to: {data_dir}")
        print(f"Total disk space used: ~170 MB")

        return True

    except Exception as e:
        print(f"\n[ERROR] Error downloading CIFAR-10: {e}")
        return False


def download_sample_images():
    """Download sample images for testing"""
    print("\n" + "=" * 60)
    print("Downloading Sample Images")
    print("=" * 60)
    print("Downloading a few sample images for testing and demonstrations...")
    print()

    sample_dir = get_data_dir().parent / "sample_images"
    sample_dir.mkdir(parents=True, exist_ok=True)

    try:
        import io
        import urllib.request

        from PIL import Image

        # Sample images (free to use)
        sample_urls = {
            "cat.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/481px-Cat03.jpg",
            "dog.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Golden_retriever_eating_pigs_foot.jpg/640px-Golden_retriever_eating_pigs_foot.jpg",
        }

        for filename, url in sample_urls.items():
            filepath = sample_dir / filename
            if filepath.exists():
                print(f"[OK] {filename} already exists, skipping...")
                continue

            try:
                print(f"Downloading {filename}...")
                response = urllib.request.urlopen(url, timeout=10)
                img_data = response.read()
                img = Image.open(io.BytesIO(img_data))
                img.save(filepath)
                print(f"[OK] {filename} downloaded successfully")
            except Exception as e:
                print(f"[WARNING] Could not download {filename}: {e}")

        print(f"\n[OK] Sample images saved to: {sample_dir}")
        return True

    except Exception as e:
        print(f"\n[ERROR] Error downloading sample images: {e}")
        print("Don't worry! You can use your own images instead.")
        return False


def check_existing_datasets():
    """Check which datasets are already downloaded"""
    data_dir = get_data_dir()

    print("\n" + "=" * 60)
    print("Checking Existing Datasets")
    print("=" * 60)

    # Check MNIST
    mnist_dir = data_dir / "MNIST"
    if mnist_dir.exists():
        print("[OK] MNIST dataset found")
    else:
        print("[NOT FOUND] MNIST dataset not found")

    # Check CIFAR-10
    cifar_dir = data_dir / "cifar-10-batches-py"
    if cifar_dir.exists():
        print("[OK] CIFAR-10 dataset found")
    else:
        print("[NOT FOUND] CIFAR-10 dataset not found")

    # Check sample images
    sample_dir = data_dir.parent / "sample_images"
    if sample_dir.exists() and list(sample_dir.glob("*.jpg")):
        print(f"[OK] Sample images found: {len(list(sample_dir.glob('*.jpg')))} images")
    else:
        print("[NOT FOUND] Sample images not found")

    print("=" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Download datasets for CNN Learning Project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python download_datasets.py --all          Download all datasets
  python download_datasets.py --mnist        Download only MNIST
  python download_datasets.py --cifar10      Download only CIFAR-10
  python download_datasets.py --samples      Download only sample images
  python download_datasets.py --check        Check existing datasets
        """,
    )

    parser.add_argument("--all", action="store_true", help="Download all datasets")
    parser.add_argument("--mnist", action="store_true", help="Download MNIST dataset")
    parser.add_argument("--cifar10", action="store_true", help="Download CIFAR-10 dataset")
    parser.add_argument("--samples", action="store_true", help="Download sample images")
    parser.add_argument("--check", action="store_true", help="Check existing datasets")

    args = parser.parse_args()

    # If no arguments, show help
    if not any([args.all, args.mnist, args.cifar10, args.samples, args.check]):
        parser.print_help()
        print("\nTip: Use --all to download everything you need for the course!")
        return

    print("\n" + "=" * 60)
    print("CNN Learning Project - Dataset Downloader")
    print("=" * 60)

    # Check existing datasets if requested
    if args.check:
        check_existing_datasets()
        return

    success_count = 0
    total_count = 0

    # Download requested datasets
    if args.all or args.mnist:
        total_count += 1
        if download_mnist():
            success_count += 1

    if args.all or args.cifar10:
        total_count += 1
        if download_cifar10():
            success_count += 1

    if args.all or args.samples:
        total_count += 1
        if download_sample_images():
            success_count += 1

    # Summary
    print("\n" + "=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successfully downloaded: {success_count}/{total_count} datasets")

    if success_count == total_count:
        print("\n[OK] All datasets downloaded successfully!")
        print("You're ready to start learning!")
    elif success_count > 0:
        print("\n[WARNING] Some downloads failed, but you can continue with what's available.")
    else:
        print("\n[ERROR] No datasets were downloaded. Please check your internet connection.")

    print("\nYou can check downloaded datasets anytime with:")
    print("  python download_datasets.py --check")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

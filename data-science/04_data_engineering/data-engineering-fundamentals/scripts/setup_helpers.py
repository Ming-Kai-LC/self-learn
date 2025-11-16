"""
Setup Helper Functions for Data Engineering Fundamentals

This module provides utility functions to help with environment setup,
validation, and common tasks throughout the learning modules.
"""

import subprocess
import sys
from pathlib import Path


def check_python_version(min_version=(3, 8)):
    """
    Check if Python version meets minimum requirements

    Args:
        min_version: Tuple of (major, minor) version numbers

    Returns:
        bool: True if version is sufficient, False otherwise
    """
    current_version = sys.version_info[:2]

    if current_version >= min_version:
        print(
            f"[OK] Python {current_version[0]}.{current_version[1]} detected (minimum {min_version[0]}.{min_version[1]} required)"
        )
        return True
    else:
        print(
            f"[FAIL] Python {current_version[0]}.{current_version[1]} detected (minimum {min_version[0]}.{min_version[1]} required)"
        )
        print(f"       Please upgrade Python to continue")
        return False


def check_package_installed(package_name):
    """
    Check if a Python package is installed

    Args:
        package_name: Name of the package to check

    Returns:
        bool: True if installed, False otherwise
    """
    try:
        __import__(package_name)
        print(f"[OK] {package_name} is installed")
        return True
    except ImportError:
        print(f"[MISSING] {package_name} is not installed")
        return False


def check_all_requirements():
    """
    Check if all required packages are installed

    Returns:
        dict: Dictionary with package names as keys and installation status as values
    """
    required_packages = [
        "pandas",
        "numpy",
        "sqlalchemy",
        "requests",
        "pyspark",
        "jupyter",
        "matplotlib",
        "pyarrow",
    ]

    results = {}
    print("Checking required packages...")
    print("=" * 60)

    for package in required_packages:
        results[package] = check_package_installed(package)

    print("=" * 60)

    installed = sum(results.values())
    total = len(results)

    print(f"\nSummary: {installed}/{total} packages installed")

    if installed < total:
        print("\nTo install missing packages, run:")
        print("  pip install -r requirements.txt")

    return results


def create_directory_structure(base_path="."):
    """
    Create the recommended directory structure for data engineering projects

    Args:
        base_path: Base directory path (default is current directory)

    Returns:
        bool: True if successful, False otherwise
    """
    base = Path(base_path)

    directories = [
        base / "data" / "raw",
        base / "data" / "processed",
        base / "data" / "interim",
        base / "notebooks" / "outputs",
        base / "scripts",
        base / "logs",
        base / "configs",
    ]

    print("Creating directory structure...")
    print("=" * 60)

    try:
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"[CREATED] {directory}")

            # Create .gitkeep file to preserve empty directories in git
            gitkeep = directory / ".gitkeep"
            if not gitkeep.exists() and not any(directory.iterdir()):
                gitkeep.touch()

        print("=" * 60)
        print("[SUCCESS] Directory structure created successfully")
        return True

    except Exception as e:
        print(f"[ERROR] Error creating directories: {e}")
        return False


def verify_environment():
    """
    Comprehensive environment verification

    Returns:
        dict: Dictionary with verification results
    """
    print("\n" + "=" * 60)
    print("DATA ENGINEERING ENVIRONMENT VERIFICATION")
    print("=" * 60)
    print()

    results = {}

    # Check Python version
    print("[1/3] Checking Python version...")
    results["python_version"] = check_python_version()
    print()

    # Check packages
    print("[2/3] Checking installed packages...")
    results["packages"] = check_all_requirements()
    print()

    # Check directory structure
    print("[3/3] Checking directory structure...")
    data_dir = Path("data")
    notebooks_dir = Path("notebooks")

    results["directories"] = {"data": data_dir.exists(), "notebooks": notebooks_dir.exists()}

    if data_dir.exists():
        print(f"[OK] data/ directory exists")
    else:
        print(f"[MISSING] data/ directory not found")

    if notebooks_dir.exists():
        print(f"[OK] notebooks/ directory exists")
    else:
        print(f"[MISSING] notebooks/ directory not found")

    print()
    print("=" * 60)
    print("VERIFICATION COMPLETE")
    print("=" * 60)

    return results


def install_requirements(requirements_file="requirements.txt"):
    """
    Install packages from requirements.txt

    Args:
        requirements_file: Path to requirements.txt file

    Returns:
        bool: True if successful, False otherwise
    """
    requirements_path = Path(requirements_file)

    if not requirements_path.exists():
        print(f"[ERROR] {requirements_file} not found")
        return False

    print(f"Installing packages from {requirements_file}...")
    print("This may take a few minutes...")
    print("=" * 60)

    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements_path)]
        )
        print("=" * 60)
        print("[SUCCESS] All packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print("=" * 60)
        print(f"[ERROR] Installation failed: {e}")
        return False


def get_sample_data_path(filename):
    """
    Get the path to a sample data file

    Args:
        filename: Name of the data file

    Returns:
        Path: Path object pointing to the data file
    """
    return Path("data") / "raw" / filename


def main():
    """
    Main function to run environment setup and verification
    """
    import argparse

    parser = argparse.ArgumentParser(description="Data Engineering Fundamentals - Setup Helper")
    parser.add_argument("--verify", action="store_true", help="Verify environment setup")
    parser.add_argument("--install", action="store_true", help="Install required packages")
    parser.add_argument("--create-dirs", action="store_true", help="Create directory structure")

    args = parser.parse_args()

    if args.install:
        install_requirements()

    if args.create_dirs:
        create_directory_structure()

    if args.verify or not any([args.install, args.create_dirs]):
        verify_environment()


if __name__ == "__main__":
    main()

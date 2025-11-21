#!/usr/bin/env python3
"""
Django Fundamentals - Notebook Validation Script

This script validates all Jupyter notebooks in the project to ensure they:
1. Are valid JSON
2. Have the expected structure
3. Contain proper metadata
4. Follow naming conventions

Usage:
    python scripts/validate_notebooks.py
"""

import json
import sys
from pathlib import Path


def validate_notebook_structure(notebook_path):
    """Validate that a notebook has the expected structure."""
    errors = []

    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Invalid JSON: {e}"]
    except Exception as e:
        return [f"Error reading file: {e}"]

    # Check required top-level keys
    required_keys = ["cells", "metadata", "nbformat", "nbformat_minor"]
    for key in required_keys:
        if key not in nb:
            errors.append(f"Missing required key: {key}")

    # Check cells structure
    if "cells" in nb:
        if not isinstance(nb["cells"], list):
            errors.append("'cells' must be a list")
        elif len(nb["cells"]) == 0:
            errors.append("Notebook has no cells")
        else:
            # Check first cell is markdown with title
            first_cell = nb["cells"][0]
            if first_cell.get("cell_type") != "markdown":
                errors.append("First cell should be markdown (title cell)")
            else:
                source = first_cell.get("source", [])
                if isinstance(source, list):
                    source = "".join(source)
                if not source.strip().startswith("#"):
                    errors.append("First cell should start with a title (# heading)")

    # Check metadata
    if "metadata" in nb:
        if "kernelspec" not in nb["metadata"]:
            errors.append("Missing kernelspec in metadata")

    return errors


def validate_naming_convention(notebook_path):
    """Validate notebook naming convention."""
    errors = []
    filename = notebook_path.name

    # Check format: NN_name.ipynb
    if not filename.endswith(".ipynb"):
        errors.append("Notebook must have .ipynb extension")
    else:
        name_part = filename[:-6]  # Remove .ipynb

        # Check if it starts with two digits and underscore
        if len(name_part) < 3:
            errors.append("Filename too short")
        elif not name_part[:2].isdigit():
            errors.append("Filename should start with two digits (e.g., 00_)")
        elif name_part[2] != "_":
            errors.append("Digits should be followed by underscore (e.g., 00_)")
        else:
            # Check that rest is lowercase with underscores
            rest = name_part[3:]
            if rest != rest.lower():
                errors.append("Filename should be lowercase after the number")
            if " " in rest:
                errors.append("Filename should use underscores, not spaces")

    return errors


def get_notebook_title(notebook_path):
    """Extract the title from the first markdown cell."""
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        if nb.get("cells") and len(nb["cells"]) > 0:
            first_cell = nb["cells"][0]
            if first_cell.get("cell_type") == "markdown":
                source = first_cell.get("source", [])
                if isinstance(source, list):
                    source = "".join(source)

                # Extract first line
                first_line = source.split("\n")[0].strip()
                # Remove markdown heading symbols
                title = first_line.lstrip("#").strip()
                return title
    except Exception:
        pass

    return None


def validate_all_notebooks(notebooks_dir):
    """Validate all notebooks in the directory."""
    notebooks_dir = Path(notebooks_dir)

    if not notebooks_dir.exists():
        print(f"Error: Directory not found: {notebooks_dir}")
        return False

    # Get all notebook files
    notebooks = sorted(notebooks_dir.glob("*.ipynb"))

    if not notebooks:
        print(f"No notebooks found in {notebooks_dir}")
        return False

    print("=" * 70)
    print("Django Fundamentals - Notebook Validation")
    print("=" * 70)
    print(f"\nFound {len(notebooks)} notebook(s)\n")

    all_valid = True

    for notebook_path in notebooks:
        print(f"\n📓 {notebook_path.name}")
        print("-" * 70)

        # Get title
        title = get_notebook_title(notebook_path)
        if title:
            print(f"   Title: {title}")

        # Validate naming
        naming_errors = validate_naming_convention(notebook_path)

        # Validate structure
        structure_errors = validate_notebook_structure(notebook_path)

        # Combine errors
        all_errors = naming_errors + structure_errors

        if all_errors:
            all_valid = False
            print("   ❌ FAILED")
            for error in all_errors:
                print(f"      - {error}")
        else:
            print("   ✅ VALID")

    print("\n" + "=" * 70)
    if all_valid:
        print("✅ All notebooks are valid!")
        print("=" * 70)
        return True
    else:
        print("❌ Some notebooks have validation errors")
        print("=" * 70)
        return False


def main():
    """Main function."""
    # Get project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    notebooks_dir = project_root / "notebooks"

    print(f"Project root: {project_root}")
    print(f"Notebooks directory: {notebooks_dir}\n")

    # Validate all notebooks
    success = validate_all_notebooks(notebooks_dir)

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

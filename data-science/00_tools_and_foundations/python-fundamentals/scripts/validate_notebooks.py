"""
Notebook Validation Script
Tests all Jupyter notebooks to ensure they can run without errors.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")


class NotebookValidator:
    def __init__(self, notebooks_dir):
        self.notebooks_dir = Path(notebooks_dir)
        self.results = {"total": 0, "passed": 0, "failed": 0, "skipped": 0, "errors": []}

    def get_all_notebooks(self):
        """Find all .ipynb files in the notebooks directory"""
        notebooks = sorted(self.notebooks_dir.glob("*.ipynb"))
        # Filter out checkpoints
        notebooks = [nb for nb in notebooks if ".ipynb_checkpoints" not in str(nb)]
        return notebooks

    def check_notebook_syntax(self, notebook_path):
        """Check if notebook has valid JSON structure"""
        try:
            with open(notebook_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Check required fields
            if "cells" not in data:
                return False, "Missing 'cells' field"
            if "metadata" not in data:
                return False, "Missing 'metadata' field"

            return True, "Valid structure"
        except json.JSONDecodeError as e:
            return False, f"JSON decode error: {e}"
        except Exception as e:
            return False, f"Error reading file: {e}"

    def validate_notebook(self, notebook_path, execute=False):
        """Validate a single notebook"""
        print(f"\n{'='*60}")
        print(f"Testing: {notebook_path.name}")
        print("=" * 60)

        # Check syntax
        is_valid, message = self.check_notebook_syntax(notebook_path)
        if not is_valid:
            print(f"❌ Syntax Error: {message}")
            return False, message

        print(f"✅ Syntax: Valid JSON structure")

        # Count cells
        with open(notebook_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        code_cells = sum(1 for cell in data["cells"] if cell["cell_type"] == "code")
        markdown_cells = sum(1 for cell in data["cells"] if cell["cell_type"] == "markdown")

        print(f"📊 Statistics:")
        print(f"   - Code cells: {code_cells}")
        print(f"   - Markdown cells: {markdown_cells}")
        print(f"   - Total cells: {len(data['cells'])}")

        # Optional: Execute notebook
        if execute:
            print(f"\n🔄 Executing notebook...")
            try:
                result = subprocess.run(
                    [
                        "jupyter",
                        "nbconvert",
                        "--to",
                        "notebook",
                        "--execute",
                        "--ExecutePreprocessor.timeout=60",
                        "--output",
                        f"{notebook_path.stem}_tested.ipynb",
                        str(notebook_path),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=120,
                )

                if result.returncode == 0:
                    print(f"✅ Execution: Success")
                    # Clean up tested file
                    tested_file = notebook_path.parent / f"{notebook_path.stem}_tested.ipynb"
                    if tested_file.exists():
                        tested_file.unlink()
                    return True, "Execution successful"
                else:
                    print(f"❌ Execution Error:")
                    print(result.stderr[:500])  # Print first 500 chars of error
                    return False, f"Execution failed: {result.stderr[:200]}"

            except subprocess.TimeoutExpired:
                print(f"⏱️  Timeout: Execution took too long")
                return False, "Execution timeout"
            except Exception as e:
                print(f"❌ Execution Error: {e}")
                return False, f"Execution error: {str(e)}"

        return True, "Validation successful"

    def run_validation(self, execute=False, skip_modules=None):
        """Run validation on all notebooks"""
        skip_modules = skip_modules or []
        notebooks = self.get_all_notebooks()

        print("\n" + "=" * 60)
        print("PYTHON FUNDAMENTALS - NOTEBOOK VALIDATION")
        print("=" * 60)
        print(f"Found {len(notebooks)} notebooks to validate")

        if skip_modules:
            print(f"Skipping modules: {', '.join(skip_modules)}")

        for notebook in notebooks:
            self.results["total"] += 1

            # Check if should skip
            if any(skip in notebook.name for skip in skip_modules):
                print(f"\n⏭️  Skipping: {notebook.name}")
                self.results["skipped"] += 1
                continue

            # Validate
            success, message = self.validate_notebook(notebook, execute=execute)

            if success:
                self.results["passed"] += 1
                print(f"✅ Status: PASSED")
            else:
                self.results["failed"] += 1
                self.results["errors"].append({"notebook": notebook.name, "error": message})
                print(f"❌ Status: FAILED")

        # Print summary
        self.print_summary()

    def print_summary(self):
        """Print validation summary"""
        print("\n" + "=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Total notebooks: {self.results['total']}")
        print(f"✅ Passed: {self.results['passed']}")
        print(f"❌ Failed: {self.results['failed']}")
        print(f"⏭️  Skipped: {self.results['skipped']}")

        if self.results["failed"] > 0:
            print("\n❌ FAILED NOTEBOOKS:")
            for error in self.results["errors"]:
                print(f"\n  - {error['notebook']}")
                print(f"    Error: {error['error']}")

        print("\n" + "=" * 60)

        if self.results["failed"] == 0 and self.results["passed"] > 0:
            print("🎉 ALL TESTS PASSED!")
        elif self.results["failed"] > 0:
            print("⚠️  SOME TESTS FAILED - Please review errors above")

        print("=" * 60 + "\n")


def main():
    """Main function"""
    import argparse

    parser = argparse.ArgumentParser(description="Validate Python Fundamentals notebooks")
    parser.add_argument(
        "--execute", action="store_true", help="Execute notebooks (slower but more thorough)"
    )
    parser.add_argument(
        "--skip", nargs="+", default=[], help="Module numbers to skip (e.g., --skip 10)"
    )

    args = parser.parse_args()

    # Get notebooks directory
    script_dir = Path(__file__).parent
    notebooks_dir = script_dir.parent / "notebooks"

    if not notebooks_dir.exists():
        print(f"❌ Error: Notebooks directory not found: {notebooks_dir}")
        sys.exit(1)

    # Run validation
    validator = NotebookValidator(notebooks_dir)

    skip_modules = [f"{num:02d}_" for num in map(int, args.skip)] if args.skip else []

    validator.run_validation(execute=args.execute, skip_modules=skip_modules)

    # Exit with appropriate code
    sys.exit(0 if validator.results["failed"] == 0 else 1)


if __name__ == "__main__":
    main()

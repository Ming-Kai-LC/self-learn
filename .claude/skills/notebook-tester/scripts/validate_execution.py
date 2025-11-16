#!/usr/bin/env python
"""
Basic notebook execution validator.
Returns exit code 0 for success, 1 for failure.
"""
import json
import subprocess
import sys
from pathlib import Path


def validate_notebook(notebook_path, timeout=600):
    """Execute notebook and check for errors"""
    output_path = Path(notebook_path).with_suffix(".tested.ipynb")

    # Execute notebook
    cmd = [
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        str(notebook_path),
        "--output",
        str(output_path),
        f"--ExecutePreprocessor.timeout={timeout}",
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ PASS: {notebook_path}")

        # Check for errors in output cells
        with open(output_path, "r", encoding="utf-8") as f:
            nb = json.load(f)

        errors = []
        for i, cell in enumerate(nb["cells"]):
            if cell["cell_type"] == "code":
                for output in cell.get("outputs", []):
                    if output.get("output_type") == "error":
                        errors.append(
                            {
                                "cell": i,
                                "error": output.get("ename"),
                                "message": output.get("evalue"),
                            }
                        )

        if errors:
            print(f"⚠️  Errors found in outputs:")
            for err in errors:
                print(f"  Cell {err['cell']}: {err['error']} - {err['message']}")
            return False

        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ FAIL: {notebook_path}")
        print(f"Error: {e.stderr}")
        return False


if __name__ == "__main__":
    # Set UTF-8 encoding for Windows console
    if sys.platform == "win32":
        import io

        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    if len(sys.argv) < 2:
        print("Usage: python validate_execution.py <notebook.ipynb> [timeout_seconds]")
        sys.exit(1)

    notebook = sys.argv[1]
    timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 600

    success = validate_notebook(notebook, timeout)
    sys.exit(0 if success else 1)

#!/usr/bin/env python
"""
Calculate educational quality metrics for notebooks.
"""
import json
import sys
from pathlib import Path


def calculate_metrics(notebook_path):
    """Calculate notebook quality metrics"""
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    cells = nb["cells"]
    markdown_cells = [c for c in cells if c["cell_type"] == "markdown"]
    code_cells = [c for c in cells if c["cell_type"] == "code"]

    # Calculate character counts
    markdown_chars = sum(len("".join(c["source"])) for c in markdown_cells)
    code_chars = sum(len("".join(c["source"])) for c in code_cells)

    total_chars = markdown_chars + code_chars
    markdown_ratio = markdown_chars / total_chars if total_chars > 0 else 0

    # Count exercises
    exercise_keywords = ["exercise", "task", "todo", "try it", "your turn", "practice"]
    exercises = sum(
        1
        for c in markdown_cells
        if any(keyword in "".join(c["source"]).lower() for keyword in exercise_keywords)
    )

    # Check for learning objectives
    has_objectives = any(
        "learning objective" in "".join(c["source"]).lower() for c in markdown_cells
    )

    # Check for prerequisites
    has_prerequisites = any("prerequisite" in "".join(c["source"]).lower() for c in markdown_cells)

    # Calculate average cell length
    avg_cell_length = total_chars / len(cells) if cells else 0

    metrics = {
        "total_cells": len(cells),
        "markdown_cells": len(markdown_cells),
        "code_cells": len(code_cells),
        "markdown_ratio": round(markdown_ratio, 3),
        "exercises_count": exercises,
        "has_learning_objectives": has_objectives,
        "has_prerequisites": has_prerequisites,
        "avg_cell_length": round(avg_cell_length, 1),
    }

    return metrics


def check_quality_gates(metrics):
    """Check if metrics meet minimum standards"""
    issues = []

    if metrics["markdown_ratio"] < 0.30:
        issues.append(f"Markdown ratio {metrics['markdown_ratio']:.1%} below 30% target")

    if metrics["exercises_count"] < 3:
        issues.append(f"Only {metrics['exercises_count']} exercises found (target: ≥3)")

    if not metrics["has_learning_objectives"]:
        issues.append("Learning objectives not found")

    if not metrics["has_prerequisites"]:
        issues.append("Prerequisites not documented")

    return issues


if __name__ == "__main__":
    # Set UTF-8 encoding for Windows console
    if sys.platform == "win32":
        import io

        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    if len(sys.argv) < 2:
        print("Usage: python calculate_quality.py <notebook.ipynb>")
        sys.exit(1)

    notebook = sys.argv[1]
    metrics = calculate_metrics(notebook)

    print(f"\n[Quality Metrics] {Path(notebook).name}")
    print("=" * 50)
    print(f"Total cells: {metrics['total_cells']}")
    print(f"Markdown cells: {metrics['markdown_cells']}")
    print(f"Code cells: {metrics['code_cells']}")
    print(f"Markdown ratio: {metrics['markdown_ratio']:.1%} (target: >=30%)")
    print(f"Exercises: {metrics['exercises_count']} (target: >=3)")
    print(f"Learning objectives: {'[YES]' if metrics['has_learning_objectives'] else '[NO]'}")
    print(f"Prerequisites: {'[YES]' if metrics['has_prerequisites'] else '[NO]'}")
    print(f"Avg cell length: {metrics['avg_cell_length']:.0f} chars")

    issues = check_quality_gates(metrics)
    if issues:
        print(f"\n[WARNING] Quality Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
    else:
        print(f"\n[PASS] All quality gates passed!")
        sys.exit(0)

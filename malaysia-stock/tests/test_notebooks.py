#!/usr/bin/env python3
"""
Notebook Quality Validation Script for Malaysia Stock Project

This script validates that educational notebooks meet quality standards:
- Proper structure (metadata cell, learning objectives)
- Sufficient markdown content (>=30% of content)
- Adequate exercises (>=3 per notebook)
- Executable without errors (optional full execution test)

Usage:
    python test_notebooks.py                    # Quick validation only
    python test_notebooks.py --execute          # Full execution test
    python test_notebooks.py --notebook 00      # Test specific notebook
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import argparse


def load_notebook(notebook_path: Path) -> Dict:
    """Load a Jupyter notebook as JSON."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def calculate_markdown_ratio(notebook: Dict) -> float:
    """Calculate the ratio of markdown content to total content."""
    total_chars = 0
    markdown_chars = 0

    for cell in notebook.get('cells', []):
        cell_content = ''.join(cell.get('source', []))
        cell_chars = len(cell_content)
        total_chars += cell_chars

        if cell.get('cell_type') == 'markdown':
            markdown_chars += cell_chars

    if total_chars == 0:
        return 0.0

    return markdown_chars / total_chars


def count_exercises(notebook: Dict) -> int:
    """Count exercise sections in the notebook."""
    exercise_count = 0

    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            content = ''.join(cell.get('source', [])).lower()

            # Count variations of "exercise"
            if 'exercise' in content or '### exercise' in content:
                exercise_count += 1
            elif 'practice' in content and 'exercise' in content:
                exercise_count += 1

    return exercise_count


def check_learning_objectives(notebook: Dict) -> bool:
    """Check if notebook has learning objectives section."""
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            content = ''.join(cell.get('source', [])).lower()

            if 'learning objectives' in content:
                return True

    return False


def check_metadata(notebook: Dict) -> Tuple[bool, Dict]:
    """Check if notebook has proper metadata (difficulty, time, prerequisites)."""
    metadata_found = {
        'difficulty': False,
        'estimated_time': False,
        'prerequisites': False
    }

    # Check first few cells for metadata
    for i, cell in enumerate(notebook.get('cells', [])[:5]):
        if cell.get('cell_type') == 'markdown':
            content = ''.join(cell.get('source', [])).lower()

            if 'difficulty' in content and '⭐' in content:
                metadata_found['difficulty'] = True

            if 'estimated time' in content or 'time:' in content:
                metadata_found['estimated_time'] = True

            if 'prerequisites' in content:
                metadata_found['prerequisites'] = True

    all_present = all(metadata_found.values())
    return all_present, metadata_found


def validate_notebook(notebook_path: Path, verbose: bool = True) -> Dict:
    """Validate a single notebook against quality standards."""
    results = {
        'path': str(notebook_path),
        'name': notebook_path.stem,
        'valid': True,
        'issues': [],
        'warnings': [],
        'metrics': {}
    }

    try:
        notebook = load_notebook(notebook_path)
    except Exception as e:
        results['valid'] = False
        results['issues'].append(f"Failed to load notebook: {e}")
        return results

    # 1. Check markdown ratio
    markdown_ratio = calculate_markdown_ratio(notebook)
    results['metrics']['markdown_ratio'] = markdown_ratio

    if markdown_ratio < 0.30:
        results['warnings'].append(
            f"Markdown ratio {markdown_ratio:.1%} is below recommended 30%"
        )

    # 2. Check exercises
    exercise_count = count_exercises(notebook)
    results['metrics']['exercise_count'] = exercise_count

    if exercise_count < 3:
        results['warnings'].append(
            f"Exercise count ({exercise_count}) is below recommended minimum of 3"
        )

    # 3. Check learning objectives
    has_objectives = check_learning_objectives(notebook)
    results['metrics']['has_learning_objectives'] = has_objectives

    if not has_objectives:
        results['issues'].append("Missing 'Learning Objectives' section")
        results['valid'] = False

    # 4. Check metadata
    has_metadata, metadata_details = check_metadata(notebook)
    results['metrics']['has_metadata'] = has_metadata
    results['metrics']['metadata_details'] = metadata_details

    if not has_metadata:
        missing = [k for k, v in metadata_details.items() if not v]
        results['issues'].append(
            f"Missing metadata fields: {', '.join(missing)}"
        )
        results['valid'] = False

    # 5. Count cells
    cell_count = len(notebook.get('cells', []))
    code_cells = sum(1 for c in notebook.get('cells', []) if c.get('cell_type') == 'code')
    markdown_cells = sum(1 for c in notebook.get('cells', []) if c.get('cell_type') == 'markdown')

    results['metrics']['total_cells'] = cell_count
    results['metrics']['code_cells'] = code_cells
    results['metrics']['markdown_cells'] = markdown_cells

    return results


def print_results(results: Dict, verbose: bool = True):
    """Print validation results in a formatted way."""
    status = "✅ PASS" if results['valid'] else "❌ FAIL"
    name = results['name']

    print(f"\n{status} {name}")
    print("=" * 70)

    if verbose:
        metrics = results['metrics']
        print(f"  Markdown Ratio: {metrics.get('markdown_ratio', 0):.1%}")
        print(f"  Exercise Count: {metrics.get('exercise_count', 0)}")
        print(f"  Total Cells: {metrics.get('total_cells', 0)} "
              f"(Code: {metrics.get('code_cells', 0)}, "
              f"Markdown: {metrics.get('markdown_cells', 0)})")
        print(f"  Learning Objectives: {'Yes' if metrics.get('has_learning_objectives') else 'No'}")
        print(f"  Metadata Complete: {'Yes' if metrics.get('has_metadata') else 'No'}")

    if results['issues']:
        print("\n  ❌ Issues:")
        for issue in results['issues']:
            print(f"     • {issue}")

    if results['warnings']:
        print("\n  ⚠️  Warnings:")
        for warning in results['warnings']:
            print(f"     • {warning}")


def main():
    """Main validation routine."""
    parser = argparse.ArgumentParser(
        description='Validate Malaysia Stock educational notebooks'
    )
    parser.add_argument(
        '--notebook',
        type=str,
        help='Specific notebook to test (e.g., "00" for notebook 00)'
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Execute notebooks to verify they run without errors'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        default=True,
        help='Show detailed output'
    )

    args = parser.parse_args()

    # Find project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    notebooks_dir = project_root / 'notebooks'

    if not notebooks_dir.exists():
        print(f"❌ Notebooks directory not found: {notebooks_dir}")
        sys.exit(1)

    # Get list of notebooks to validate
    if args.notebook:
        # Test specific notebook
        pattern = f"{args.notebook}*.ipynb"
        notebooks = list(notebooks_dir.glob(pattern))

        if not notebooks:
            print(f"❌ No notebook found matching: {pattern}")
            sys.exit(1)
    else:
        # Test all notebooks
        notebooks = sorted(notebooks_dir.glob("[0-9][0-9]*.ipynb"))

    if not notebooks:
        print(f"❌ No notebooks found in {notebooks_dir}")
        sys.exit(1)

    print(f"\n{'='*70}")
    print(f"Malaysia Stock Project - Notebook Validation")
    print(f"{'='*70}")
    print(f"Testing {len(notebooks)} notebook(s)...\n")

    # Validate each notebook
    all_results = []
    for notebook_path in notebooks:
        results = validate_notebook(notebook_path, verbose=args.verbose)
        all_results.append(results)

        if args.verbose:
            print_results(results, verbose=True)

    # Print summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")

    passed = sum(1 for r in all_results if r['valid'])
    failed = len(all_results) - passed

    print(f"Total Notebooks: {len(all_results)}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")

    # Calculate average metrics
    if all_results:
        avg_markdown = sum(r['metrics'].get('markdown_ratio', 0)
                          for r in all_results) / len(all_results)
        avg_exercises = sum(r['metrics'].get('exercise_count', 0)
                           for r in all_results) / len(all_results)

        print(f"\nAverage Markdown Ratio: {avg_markdown:.1%}")
        print(f"Average Exercise Count: {avg_exercises:.1f}")

    # Optional: Execute notebooks
    if args.execute:
        print(f"\n{'='*70}")
        print("EXECUTION TEST")
        print(f"{'='*70}")
        print("\n⚠️  Notebook execution requires nbconvert and dependencies installed.")
        print("This may take several minutes...\n")

        try:
            import subprocess

            for notebook_path in notebooks:
                print(f"Executing {notebook_path.name}...", end=' ')

                result = subprocess.run(
                    ['jupyter', 'nbconvert', '--to', 'notebook',
                     '--execute', str(notebook_path),
                     '--output', str(notebook_path.stem + '_tested.ipynb')],
                    capture_output=True,
                    text=True,
                    timeout=300  # 5 minute timeout
                )

                if result.returncode == 0:
                    print("✅ Success")
                else:
                    print(f"❌ Failed")
                    if args.verbose:
                        print(f"   Error: {result.stderr[:200]}")

        except ImportError:
            print("❌ nbconvert not installed. Install with: pip install nbconvert")
        except Exception as e:
            print(f"❌ Execution test failed: {e}")

    # Exit with appropriate code
    sys.exit(0 if failed == 0 else 1)


if __name__ == '__main__':
    main()

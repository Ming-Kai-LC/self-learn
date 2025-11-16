#!/usr/bin/env python3
"""
Fix emoji characters in all notebooks for Windows compatibility
"""

import json
from pathlib import Path

# Emoji replacements
EMOJI_REPLACEMENTS = {
    "✅": "[OK]",
    "❌": "[FAIL]",
    "⚠️": "[WARNING]",
    "📊": "[DATA]",
    "🎉": "[SUCCESS]",
    "📁": "[FOLDER]",
    "📚": "[MODULES]",
    "✨": "[FEATURE]",
    "🛠️": "[TOOLS]",
    "🚀": "[DEPLOY]",
    "🔧": "[FIX]",
    "💡": "[TIP]",
    "⚡": "[FAST]",
    "🐍": "[PYTHON]",
    "📈": "[CHART]",
    "🤖": "[BOT]",
}


def fix_notebook_emojis(notebook_path):
    """Remove emojis from a notebook file"""
    print(f"Processing: {notebook_path.name}")

    # Read notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    changes_made = 0

    # Process each cell
    for cell in notebook.get("cells", []):
        if "source" in cell:
            # Process source (can be string or list)
            if isinstance(cell["source"], list):
                new_source = []
                for line in cell["source"]:
                    new_line = line
                    for emoji, replacement in EMOJI_REPLACEMENTS.items():
                        if emoji in new_line:
                            new_line = new_line.replace(emoji, replacement)
                            changes_made += 1
                    new_source.append(new_line)
                cell["source"] = new_source
            elif isinstance(cell["source"], str):
                new_source = cell["source"]
                for emoji, replacement in EMOJI_REPLACEMENTS.items():
                    if emoji in new_source:
                        new_source = new_source.replace(emoji, replacement)
                        changes_made += 1
                cell["source"] = new_source

        # Process outputs if present
        if "outputs" in cell:
            for output in cell["outputs"]:
                if "text" in output:
                    if isinstance(output["text"], list):
                        new_text = []
                        for line in output["text"]:
                            new_line = line
                            for emoji, replacement in EMOJI_REPLACEMENTS.items():
                                if emoji in new_line:
                                    new_line = new_line.replace(emoji, replacement)
                                    changes_made += 1
                            new_text.append(new_line)
                        output["text"] = new_text

    # Write back
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)

    print(f"  - Made {changes_made} emoji replacements")
    return changes_made


def main():
    notebooks_dir = Path(__file__).parent.parent / "notebooks"

    print("=" * 60)
    print("FIXING EMOJI CHARACTERS IN NOTEBOOKS")
    print("=" * 60)
    print()

    total_changes = 0
    notebooks_processed = 0

    # Process all .ipynb files
    for notebook_file in sorted(notebooks_dir.glob("*.ipynb")):
        # Skip test outputs
        if "_tested" in notebook_file.name:
            continue

        changes = fix_notebook_emojis(notebook_file)
        total_changes += changes
        notebooks_processed += 1

    print()
    print("=" * 60)
    print(f"COMPLETE: Fixed {total_changes} emojis in {notebooks_processed} notebooks")
    print("=" * 60)


if __name__ == "__main__":
    main()

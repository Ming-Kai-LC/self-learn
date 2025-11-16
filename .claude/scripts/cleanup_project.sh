#!/bin/bash
# Cleanup script for project structure
# Usage: ./cleanup_project.sh <project-name>
# Example: ./cleanup_project.sh projects/my-project

set -e  # Exit on error

PROJECT_DIR="$1"

if [ -z "$PROJECT_DIR" ]; then
    echo "Usage: $0 <project-directory>"
    echo "Example: $0 projects/my-project"
    exit 1
fi

if [ ! -d "$PROJECT_DIR" ]; then
    echo "Error: Directory '$PROJECT_DIR' does not exist"
    exit 1
fi

echo "Cleaning up project: $PROJECT_DIR"
echo "=================================="

cd "$PROJECT_DIR" || exit 1

# Create standard directories
echo "Creating standard directory structure..."
mkdir -p scripts docs/development data/{raw,processed,sample}

# Move generator scripts from root to scripts/
echo "Moving generator/helper scripts to scripts/..."
find . -maxdepth 1 -name "*.py" -exec mv {} scripts/ \; 2>/dev/null || true
find notebooks -maxdepth 1 -name "*.py" -exec mv {} scripts/ \; 2>/dev/null || true

# Clean temporary files
echo "Removing temporary files..."
rm -f nul *_tested.ipynb *_executed.ipynb *_backup*.ipynb 2>/dev/null || true
find notebooks -name "*_tested.ipynb" -delete 2>/dev/null || true
find notebooks -name "*_executed.ipynb" -delete 2>/dev/null || true
find notebooks -name "nul" -delete 2>/dev/null || true

# Move process docs to development folder
echo "Organizing documentation..."
mv *TESTING*.md *SUMMARY*.md *FIXES*.md *QUALITY*.md *PRODUCTION*.md docs/development/ 2>/dev/null || true

# Move media files from notebooks to data
echo "Organizing media files..."
mkdir -p data/sample_media
find notebooks -maxdepth 1 \( -name "*.jpg" -o -name "*.png" -o -name "*.mp4" -o -name "*.avi" \) -exec mv {} data/sample_media/ \; 2>/dev/null || true

# Remove empty directories
echo "Removing empty directories..."
find . -type d -empty -delete 2>/dev/null || true

echo "=================================="
echo "Cleanup complete for $PROJECT_DIR"
echo ""
echo "Summary:"
echo "  - Standard directories created: scripts/, docs/, data/{raw,processed,sample}"
echo "  - Temporary files removed: *_tested.ipynb, nul, etc."
echo "  - Scripts organized in scripts/ directory"
echo "  - Process documentation moved to docs/development/"
echo "  - Media files moved to data/sample_media/"

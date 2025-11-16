# Scripts Directory

This directory contains utility scripts and helper tools used in the project.

## Scripts

### extract_pdf_content.py
**Purpose**: Safely extract text content from the Practical Handbook PDF

**Usage**:
```bash
cd scripts
python extract_pdf_content.py
```

**What it does**:
- Checks PDF file size and page count for safety
- Extracts text from all 113 pages of the handbook
- Creates `handbook_extracted_text.txt` with full content
- Creates `handbook_structure.txt` with chapter/section analysis
- Prevents crashes from large PDF files using chunked extraction

**Requirements**:
- PyMuPDF (fitz)
- pypdf

**Output Location**: `../source_materials/`

## Future Scripts (To Be Added)

### image_utils.py
Utility functions for:
- Displaying multiple images in a grid
- Comparing before/after images
- Saving processed images with timestamps
- Resizing images while maintaining aspect ratio

### video_utils.py
Utility functions for:
- Converting video to frames
- Converting frames to video
- Extracting video information

### filter_utils.py
Collection of:
- Custom kernels for filtering
- Filter application helpers
- Comparison functions

## Adding New Scripts

When creating new utility scripts:
1. Add clear docstrings explaining purpose
2. Include usage examples in comments
3. Update this README with script description
4. Make scripts runnable from command line if applicable

## Running Scripts

All scripts should be run from the project root or scripts directory:

```bash
# From project root:
python scripts/script_name.py

# From scripts directory:
cd scripts
python script_name.py
```

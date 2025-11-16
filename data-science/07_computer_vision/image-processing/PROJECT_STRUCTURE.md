# Image Processing Project - Directory Structure

## Visual Overview

```
image-processing/
│
├── README.md                                    # 📖 Main project guide & learning path
├── PROJECT_STRUCTURE.md                         # 📋 This file - directory organization
│
├── notebooks/                                   # 📓 All Jupyter notebooks
│   ├── README.md                               # Guide to notebooks organization
│   ├── 00_setup_and_introduction.ipynb         # ✅ Notebook 0: Setup & intro
│   ├── 01_getting_started_opencv.ipynb         # ✅ Notebook 1: Getting started
│   ├── 02_image_basics_roi.ipynb              # ⏳ To be created
│   ├── 03_image_processing_fundamentals.ipynb # ⏳ To be created
│   ├── 04_image_transformations.ipynb         # ⏳ To be created
│   ├── 05_morphological_operations.ipynb      # ⏳ To be created
│   ├── 06_image_segmentation.ipynb            # ⏳ To be created
│   ├── 07_feature_detection.ipynb             # ⏳ To be created
│   ├── 08_feature_matching.ipynb              # ⏳ To be created
│   ├── 09_hand_gesture_recognition.ipynb      # ⏳ To be created
│   │
│   └── outputs/                                # 🖼️ Generated files from notebooks
│       ├── notebook_00/                        # Outputs from notebook 00 (none yet)
│       └── notebook_01/                        # Outputs from notebook 01
│           ├── sample_image.jpg               # Test gradient image
│           ├── saved_image.jpg                # Saved copy of sample
│           ├── my_house.jpg                   # House drawing example
│           └── sample_video.mp4               # 3-second animation
│
├── sample_images/                              # 🏞️ Sample images for practice
│   └── README.md                              # Guide for adding/using images
│   # Add your test images here!
│   # Examples: landscape.jpg, face.png, text_doc.jpg
│
├── scripts/                                    # 🔧 Utility scripts
│   ├── README.md                              # Script documentation
│   └── extract_pdf_content.py                 # PDF text extraction tool
│   # Future: image_utils.py, video_utils.py, filter_utils.py
│
├── source_materials/                           # 📚 Original handbook & extracted content
│   ├── README.md                              # Content mapping guide
│   ├── Practical-Handbook.pdf                 # Original handbook (113 pages, 17.62 MB)
│   ├── handbook_extracted_text.txt            # Extracted text (131K chars)
│   └── handbook_structure.txt                 # Chapter/section analysis
│
└── docs/                                       # 📄 Project documentation
    ├── README.md                              # Documentation overview
    ├── FUTURE_DEVELOPMENT.md                  # Roadmap for notebooks 02-09
    └── TESTING_RESULTS.md                     # Testing logs & bug fixes
```

---

## Directory Purposes

### 📁 Root Level
- **README.md**: Start here! Main guide with installation, learning path, and resources
- **PROJECT_STRUCTURE.md**: This file - shows how everything is organized

### 📓 notebooks/
**Purpose**: All learning notebooks in sequential order

**What's here**:
- Jupyter notebooks numbered 00-09
- Each builds on previous concepts
- Start with 00, progress to 01, then 02, etc.

**Outputs subdirectory**: Files generated when running notebooks
- Organized by notebook number (notebook_00, notebook_01, etc.)
- Keep working directory clean
- Easy to identify which notebook created which files

**How to use**:
```bash
cd notebooks
jupyter notebook
# Open 00_setup_and_introduction.ipynb first
```

---

### 🏞️ sample_images/
**Purpose**: Reusable test images for practice across all notebooks

**What to put here**:
- Photos for testing (landscapes, faces, objects)
- Text documents for OCR practice
- Noisy images for denoising
- Binary images for morphology
- Complex scenes for segmentation

**How to reference in notebooks**:
```python
img = cv.imread('../sample_images/your_image.jpg')
```

**Current status**: Empty - add your own images!

---

### 🔧 scripts/
**Purpose**: Utility scripts and helper tools

**Current scripts**:
- `extract_pdf_content.py`: Extract text from PDF handbook

**Future scripts** (to be added):
- `image_utils.py`: Image display and comparison helpers
- `video_utils.py`: Video conversion tools
- `filter_utils.py`: Custom kernels and filters

**How to run**:
```bash
cd scripts
python extract_pdf_content.py
```

---

### 📚 source_materials/
**Purpose**: Original handbook and extracted reference content

**Files**:
- **Practical-Handbook.pdf**: Original 113-page handbook from university
- **handbook_extracted_text.txt**: Searchable text from PDF
- **handbook_structure.txt**: Chapter/section analysis

**Usage**: Reference when creating new notebooks
- Check original handbook for accuracy
- Search extracted text for specific content
- Map handbook sections to notebooks

---

### 📄 docs/
**Purpose**: Development documentation and testing results

**Files**:
- **FUTURE_DEVELOPMENT.md**:
  - Complete roadmap for notebooks 02-09
  - Detailed content plans
  - Time estimates (47-65 hours total)

- **TESTING_RESULTS.md**:
  - Testing logs for completed notebooks
  - Bug fixes documented
  - Library versions verified

**Use when**:
- Creating new notebooks → check FUTURE_DEVELOPMENT.md
- Testing notebooks → update TESTING_RESULTS.md
- Planning development → estimate time from roadmap

---

## File Naming Conventions

### Notebooks
- Format: `##_descriptive_name.ipynb`
- Example: `01_getting_started_opencv.ipynb`
- Always two-digit numbers (00, 01, 02, etc.)

### Generated Files
- Saved in: `notebooks/outputs/notebook_##/`
- Use descriptive names: `sample_image.jpg`, not `img1.jpg`

### Sample Images
- Lowercase with underscores: `landscape_mountain.jpg`
- Descriptive: `noisy_photo.jpg`, `text_document.png`

### Scripts
- Lowercase with underscores: `extract_pdf_content.py`
- Descriptive function names

---

## Quick Navigation

| I want to... | Go to... |
|-------------|----------|
| Start learning | `notebooks/00_setup_and_introduction.ipynb` |
| See what's planned | `docs/FUTURE_DEVELOPMENT.md` |
| Check test results | `docs/TESTING_RESULTS.md` |
| Add sample images | `sample_images/` |
| Run utility scripts | `scripts/` |
| Reference handbook | `source_materials/Practical-Handbook.pdf` |
| Understand organization | This file! |

---

## File Count Summary

| Category | Files | Status |
|----------|-------|--------|
| **Notebooks** | 2 of 9 | ✅ 00, 01 complete |
| **Documentation** | 7 files | ✅ Complete |
| **Scripts** | 1 | ✅ Working |
| **Source Materials** | 3 files | ✅ Extracted |
| **Sample Images** | 0 | ⏳ Add your own |
| **Generated Outputs** | 4 files | ✅ From notebook 01 |

---

## Workflow

### For Learners:
1. Read main `README.md`
2. Navigate to `notebooks/`
3. Open and run notebooks in order (00 → 01 → 02 → ...)
4. Add your own images to `sample_images/`
5. Experiment and practice!

### For Developers:
1. Check `docs/FUTURE_DEVELOPMENT.md` for next notebook to create
2. Reference `source_materials/` for content
3. Create notebook in `notebooks/`
4. Test thoroughly
5. Update `docs/TESTING_RESULTS.md`
6. Update main `README.md` learning path

---

## Maintenance

### Keep Organized:
- ✅ Generated files go in `notebooks/outputs/notebook_##/`
- ✅ Documentation stays in `docs/`
- ✅ Reusable images in `sample_images/`
- ✅ Scripts in `scripts/`

### Don't Clutter Root:
- ❌ Don't save test images to root
- ❌ Don't create notebooks in root
- ❌ Don't scatter generated files
- ✅ Use designated directories!

---

**Last Updated**: 2025-11-13
**Organization Status**: ✅ Fully Organized
**Total Files**: 20+ files across 6 directories

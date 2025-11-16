# Image Processing with OpenCV - Learning Path for Beginners

Welcome to the **Image Processing with OpenCV** learning series! This comprehensive guide will take you from absolute beginner to proficient in image processing using Python and OpenCV.

## About This Project

This learning series is based on the **BMDS2133 Image Processing Practical Handbook** and has been restructured into beginner-friendly Jupyter notebooks. Whether you're new to programming or new to image processing, these notebooks will guide you step by step.

## 📁 Project Organization

This project is well-organized for easy navigation:

- **`notebooks/`** - All Jupyter notebooks (start here!)
  - `00_setup_and_introduction.ipynb` ✅
  - `01_getting_started_opencv.ipynb` ✅
  - `02_image_basics_roi.ipynb` ✅
  - `03_image_processing_fundamentals.ipynb` ✅
  - `04_image_transformations.ipynb` ✅
  - `05_morphological_operations.ipynb` ✅
  - `06_image_segmentation.ipynb` ✅
  - `07_feature_detection.ipynb` ✅
  - `08_feature_matching.ipynb` ✅
  - `09_hand_gesture_recognition.ipynb` ✅
  - `outputs/` - Generated files organized by notebook

- **`sample_images/`** - Reusable test images for practice
- **`scripts/`** - Utility scripts (PDF extraction, helpers)
- **`source_materials/`** - Original handbook and extracted content
- **`docs/`** - Development roadmap and testing results

📋 **See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for complete directory guide**

## Who Is This For?

- **Complete beginners** to Python and image processing
- Anyone interested in computer vision
- Students learning OpenCV
- Developers wanting to add image processing skills
- Hobbyists interested in photo manipulation and analysis

## What You'll Learn

By completing this series, you'll be able to:
- Load, display, and manipulate images
- Process video feeds from files and webcams
- Apply filters and transformations to images
- Detect features like edges, corners, and shapes
- Recognize objects and patterns
- Build real-world image processing applications

---

## Prerequisites

### Required Knowledge
- **None!** This series is designed for complete beginners
- Basic computer skills (using a web browser, installing software)
- Willingness to learn and experiment

### Required Software
- **Python 3.x** (3.8 or higher recommended)
- **Jupyter Notebook** (included with Anaconda)
- See `00_setup_and_introduction.ipynb` for detailed installation instructions

---

## Learning Path

Follow these notebooks in order for the best learning experience:

### 📘 Module 0: Setup and Introduction
**Notebook:** `00_setup_and_introduction.ipynb`

**What you'll learn:**
- What is image processing and why it matters
- What is OpenCV and what can it do
- How to install Python, Jupyter, and required libraries
- Understanding digital images (pixels, colors, dimensions)
- Your first image processing code
- Jupyter Notebook basics

**Time:** ~1 hour
**Difficulty:** Beginner

---

### 📘 Module 1: Getting Started with OpenCV
**Notebook:** `01_getting_started_opencv.ipynb`

**What you'll learn:**
- The "Tiga Sekawan" (3 companions) for images
- The "Empat Sekawan" (4 companions) for videos
- Loading and displaying images
- Saving images to files
- Reading video from files and webcam
- Converting to grayscale for faster processing
- Drawing shapes (lines, rectangles, circles, ellipses, polygons)
- Adding text to images
- Understanding BGR vs RGB color format

**Projects:**
- Create your own logo using drawing functions
- Build a simple house drawing
- Create animated videos

**Time:** ~2-3 hours
**Difficulty:** Beginner

---

### 📘 Module 2: Image Basics and Region of Interest
**Notebook:** `02_image_basics_roi.ipynb`

**What you'll learn:**
- Access and modify individual pixels
- Understand image properties (shape, size, dtype)
- Work with Region of Interest (ROI)
- Apply Region of Non-Interest (RONI) masking
- Split and merge color channels (R, G, B)
- Add borders and padding to images
- Perform image arithmetic operations

**Projects:**
- Face blurring for privacy
- Channel swapping for artistic effects
- Simple watermark creation
- Photo frame borders

**Real-World Applications:**
- Privacy protection (face/license plate blurring)
- Photo editing (selective adjustments)
- Medical imaging (tissue region analysis)
- Creative effects (channel manipulation)

**Time:** ~2-3 hours
**Difficulty:** Beginner to Intermediate

---

### 📘 Module 3: Image Processing Fundamentals
**Notebook:** `03_image_processing_fundamentals.ipynb`

**What you'll learn:**
- Color space conversions (BGR, RGB, HSV, LAB, Grayscale)
- HSV-based object tracking by color
- **Image thresholding** (simple, adaptive, Otsu's)
- **Smoothing and filtering**:
  - Averaging filter
  - Gaussian blurring
  - Median filtering
  - Bilateral filtering (edge-preserving)
- **Histogram equalization** (standard and CLAHE)
- **Image denoising** techniques (Non-Local Means)

**Projects:**
- Build a color-based object tracker
- Compare different thresholding methods
- Create an advanced denoising tool

**Real-World Applications:**
- Color-based object detection in robotics
- Noise reduction in low-light photography
- Medical image enhancement
- Document scanning and processing

**Time:** ~3-4 hours
**Difficulty:** Intermediate

---

### 📘 Module 4: Image Transformations
**Notebook:** `04_image_transformations.ipynb`

**What you'll learn:**
- **Geometric transformations**:
  - Scaling (resizing) with interpolation methods
  - Translation (shifting images)
  - Rotation around any point
  - Perspective transformation for document scanning
- Understanding interpolation (NEAREST, LINEAR, CUBIC, LANCZOS4, AREA)
- **Digital watermarking** with LSB (Least Significant Bit) method
- **PSNR** (Peak Signal-to-Noise Ratio) for quality measurement

**Projects:**
- Photo resizer for social media platforms
- Document scanner with perspective correction
- Simple watermarking system
- 360° rotation animation

**Real-World Applications:**
- Photo editing and resizing for web/social media
- Document scanning apps (perspective correction)
- Digital watermarking for copyright protection
- Image alignment for panoramas

**Time:** ~3-4 hours
**Difficulty:** Intermediate

---

### 📘 Module 5: Morphological Operations
**Topics Covered (from Handbook):**
- What are morphological operations?
- **Basic operations**:
  - Dilation (expanding)
  - Erosion (shrinking)
  - Opening (remove noise)
  - Closing (fill holes)
- **Advanced operations**:
  - Morphological gradient
  - Top Hat
  - Black Hat
- Building interactive morphology tools

**Real-World Applications:**
- Removing noise from binary images
- Separating connected objects
- Detecting boundaries
- Fingerprint processing

**Time:** ~2-3 hours
**Difficulty:** Intermediate

---

### 📘 Module 6: Image Segmentation
**Topics Covered (from Handbook):**
- What is image segmentation?
- **Thresholding approaches**:
  - Supervised thresholding
  - Unsupervised thresholding
- **Watershed algorithm**
  - Understanding the watershed concept
  - Marker-based watershed
  - Separating overlapping objects

**Real-World Applications:**
- Cell counting in microscopy
- Separating objects in images
- Medical image analysis
- Automated quality control

**Time:** ~2-3 hours
**Difficulty:** Intermediate to Advanced

---

### 📘 Module 7: Feature Detection and Description
**Topics Covered (from Handbook):**
- What are features?
- **Corner detection**:
  - Harris Corner Detector
  - Shi-Tomasi Corner Detector
  - Good Features to Track
- **Advanced feature detection**:
  - **SIFT** (Scale-Invariant Feature Transform)
  - **FAST** Algorithm
  - **ORB** (Oriented FAST and Rotated BRIEF)

**Real-World Applications:**
- Object recognition
- Image stitching (panoramas)
- 3D reconstruction
- Augmented reality

**Time:** ~3-4 hours
**Difficulty:** Advanced

---

### 📘 Module 8: Feature Matching
**Topics Covered (from Handbook):**
- What is feature matching?
- **Brute-Force (BF) Matcher**
- **FLANN-based Matcher**
- **Feature Matching + Homography**
  - Finding objects in scenes
  - Image alignment
  - Object detection

**Real-World Applications:**
- Object recognition and tracking
- Image registration
- Panorama stitching
- Augmented reality applications

**Time:** ~2-3 hours
**Difficulty:** Advanced

---

### 📘 Bonus Module: Hand Gesture Recognition
**Topics Covered (from Handbook):**
- Introduction to **MediaPipe**
- Hand landmark detection
- Gesture recognition
- **Real-time gesture control**
- Volume control with hand gestures

**Real-World Applications:**
- Touchless interfaces
- Sign language recognition
- Virtual reality controls
- Accessibility tools

**Time:** ~2-3 hours
**Difficulty:** Intermediate

---

## Project Structure

```
image-processing/
├── README.md                               # This file - start here!
├── PROJECT_STRUCTURE.md                    # Detailed directory guide
│
├── notebooks/                              # 📓 All learning notebooks
│   ├── 00_setup_and_introduction.ipynb    # ✅ Setup & intro
│   ├── 01_getting_started_opencv.ipynb    # ✅ Getting started
│   ├── 02_image_basics_roi.ipynb          # ✅ Image basics & ROI
│   ├── 03_image_processing_fundamentals.ipynb # ✅ Processing fundamentals
│   ├── 04_image_transformations.ipynb     # ✅ Image transformations
│   ├── 05_morphological_operations.ipynb  # ✅ Morphological operations
│   ├── 06_image_segmentation.ipynb        # ✅ Image segmentation
│   ├── 07_feature_detection.ipynb         # ✅ Feature detection
│   ├── 08_feature_matching.ipynb          # ✅ Feature matching
│   ├── 09_hand_gesture_recognition.ipynb  # ✅ Hand gesture recognition
│   └── outputs/                           # Generated files organized by notebook
│       ├── notebook_00/
│       └── notebook_01/
│           ├── sample_image.jpg
│           ├── saved_image.jpg
│           ├── my_house.jpg
│           └── sample_video.mp4
│
├── sample_images/                          # 🏞️ Test images for practice
│   └── README.md                          # (Add your own images here!)
│
├── scripts/                                # 🔧 Utility scripts
│   ├── extract_pdf_content.py             # PDF extraction tool
│   └── README.md                          # Script documentation
│
├── source_materials/                       # 📚 Original handbook
│   ├── Practical-Handbook.pdf             # 113-page handbook
│   ├── handbook_extracted_text.txt        # Extracted text
│   ├── handbook_structure.txt             # Structure analysis
│   └── README.md                          # Content mapping
│
└── docs/                                   # 📄 Documentation
    ├── FUTURE_DEVELOPMENT.md              # Roadmap for notebooks 02-09
    ├── TESTING_RESULTS.md                 # Testing logs
    └── README.md                          # Documentation guide
```

📋 **See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed explanations**

---

## Installation

### Option 1: Quick Start with Anaconda (Recommended)

1. **Install Anaconda**:
   - Download from [https://www.anaconda.com/download](https://www.anaconda.com/download)
   - Install following the wizard

2. **Open Anaconda Prompt** and run:
   ```bash
   # Navigate to project directory
   cd path/to/image-processing

   # Install required packages
   pip install opencv-python numpy matplotlib Pillow scikit-image

   # Navigate to notebooks directory
   cd image-processing/notebooks

   # Launch Jupyter Notebook
   jupyter notebook
   ```

3. **Open `00_setup_and_introduction.ipynb`** in Jupyter and start learning!

### Option 2: Using pip and Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\\Scripts\\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Navigate to notebooks directory
cd notebooks

# Launch Jupyter Notebook
jupyter notebook
```

### Required Libraries

```
opencv-python>=4.8.0
numpy>=1.24.0
matplotlib>=3.7.0
Pillow>=10.0.0
scikit-image>=0.21.0
jupyter>=1.0.0
notebook>=7.0.0
```

---

## How to Use This Learning Series

### For Self-Study

1. **Start from Module 0** and work through sequentially
2. **Read the theory** in markdown cells carefully
3. **Run every code cell** (Shift + Enter) and observe outputs
4. **Complete all exercises** - learning by doing is key!
5. **Experiment!** Change parameters and see what happens
6. **Don't skip** - each module builds on previous ones

### For Classroom Use

**Instructors**: Feel free to use these notebooks for teaching. Each module includes:
- Clear learning objectives
- Theory explanations for beginners
- Hands-on code examples
- Practice exercises
- Real-world applications

**Suggested pace**:
- 1-2 modules per week
- Mix theory with hands-on practice
- Encourage experimentation
- Assign exercises as homework

---

## Tips for Success

### For Beginners

1. **Don't rush** - take time to understand each concept
2. **Practice daily** - even 30 minutes makes a difference
3. **Break things!** - errors are learning opportunities
4. **Ask questions** - use comments or discussion forums
5. **Build projects** - apply what you learn to real problems

### Common Pitfalls to Avoid

- **Skipping the setup** - proper installation prevents frustration
- **Not running code cells** - reading ≠ learning, you must practice
- **Ignoring errors** - read error messages, they teach you
- **Jumping ahead** - foundational knowledge is crucial
- **Not experimenting** - change values, try new ideas!

---

## Troubleshooting

### Installation Issues

**Problem**: `ModuleNotFoundError: No module named 'cv2'`
**Solution**: Run `pip install opencv-python`

**Problem**: Import errors with numpy
**Solution**: Update numpy with `pip install --upgrade numpy`

**Problem**: Jupyter doesn't start
**Solution**: Try `jupyter notebook` in terminal, or reinstall: `pip install --upgrade jupyter notebook`

### Code Issues

**Problem**: Images don't display
**Solution**: Make sure matplotlib is imported and use `%matplotlib inline`

**Problem**: BGR vs RGB colors look wrong
**Solution**: Always convert with `cv.cvtColor(img, cv.COLOR_BGR2RGB)` before displaying with matplotlib

**Problem**: Video/webcam doesn't work
**Solution**: Check camera permissions, try different camera index (0, 1, 2...)

---

## Additional Resources

### Official Documentation
- **OpenCV Documentation**: [https://docs.opencv.org/](https://docs.opencv.org/)
- **OpenCV-Python Tutorials**: [https://docs.opencv.org/master/d6/d00/tutorial_py_root.html](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- **NumPy Documentation**: [https://numpy.org/doc/](https://numpy.org/doc/)

### Learning Resources
- **OpenCV Course** (free): [https://opencv.org/courses/](https://opencv.org/courses/)
- **PyImageSearch**: Excellent tutorials and courses
- **YouTube**: Search for "OpenCV Python tutorial"

### Communities
- **OpenCV Forum**: [https://forum.opencv.org/](https://forum.opencv.org/)
- **Stack Overflow**: Tag `opencv` or `python-opencv`
- **Reddit**: r/computervision, r/opencv

---

## Real-World Project Ideas

Once you complete the modules, try these projects:

### Beginner Projects
1. **Photo Editor**: Apply filters, adjust brightness/contrast
2. **Color Palette Extractor**: Find dominant colors in images
3. **Simple Object Counter**: Count objects by color
4. **Barcode/QR Code Reader**: Detect and decode barcodes

### Intermediate Projects
5. **Document Scanner**: Perspective correction and enhancement
6. **Face Detection App**: Detect and blur faces for privacy
7. **Panorama Stitcher**: Combine multiple photos
8. **Motion Detection**: Security camera with movement alerts

### Advanced Projects
9. **License Plate Recognition**: OCR for vehicle plates
10. **Hand Gesture Controller**: Control apps with hand gestures
11. **Object Tracking**: Track objects in videos
12. **Augmented Reality**: Overlay virtual objects on real scenes

---

## Contributing

Found an error or have a suggestion?

- Check the source material (Practical-Handbook.pdf)
- Test your changes thoroughly
- Share improvements with the community

---

## Acknowledgments

This learning series is based on the **BMDS2133 Image Processing Practical Handbook** from the Faculty of Computing and Information Technology (FOCS), Tunku Abdul Rahman University of Management and Technology.

**OpenCV** was started at Intel in 1999 by Gary Bradsky. Special thanks to:
- The OpenCV development team
- The Python and NumPy communities
- All contributors to open-source computer vision tools

---

## License

The notebooks and code in this series are provided for educational purposes. OpenCV is released under the Apache 2 License.

---

## Get Started Now!

Ready to begin your image processing journey?

1. Navigate to `notebooks/` directory
2. Open `00_setup_and_introduction.ipynb`
3. Follow the installation instructions
4. Start learning!

**Remember**: The best way to learn is by doing. Run the code, experiment, make mistakes, and learn from them.

**Happy Learning!** 🎉📸🔬

---

## Quick Reference

### Essential OpenCV Functions

```python
# Loading and displaying images
img = cv.imread('image.jpg')           # Load image
cv.imshow('window', img)                # Display image (use plt.imshow in notebooks)
cv.imwrite('output.jpg', img)           # Save image

# Color conversions
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Drawing functions
cv.line(img, pt1, pt2, color, thickness)
cv.rectangle(img, pt1, pt2, color, thickness)
cv.circle(img, center, radius, color, thickness)
cv.putText(img, text, position, font, scale, color, thickness)

# Video capture
cap = cv.VideoCapture(0)                # 0 for webcam, or filename
ret, frame = cap.read()                 # Read frame
cap.release()                           # Release capture
```

### Common Color Codes (BGR format)
```python
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
```

---

**Version**: 1.0
**Last Updated**: 2025-11-14
**Status**: 9 of 9 notebooks completed (100% complete) ✅

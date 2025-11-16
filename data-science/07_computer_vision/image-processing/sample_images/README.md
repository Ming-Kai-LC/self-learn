# Sample Images Directory

This directory is for storing sample images that can be used across multiple notebooks for practice and examples.

## Purpose

- Provide consistent test images for all notebooks
- Allow students to practice with various image types
- Include images with different properties (size, color, complexity)

## Recommended Images to Add

### Basic Shapes
- Simple geometric shapes (circles, squares, triangles)
- Single-color backgrounds
- High-contrast images for thresholding practice

### Natural Images
- Landscape photos
- People/faces (for detection practice)
- Objects on plain backgrounds
- Complex scenes

### Special Purpose
- Noisy images (for denoising practice)
- Text documents (for OCR practice)
- Binary images (for morphology practice)
- Overlapping objects (for segmentation practice)

## Usage in Notebooks

Reference images from notebooks using relative paths:
```python
img = cv.imread('../sample_images/your_image.jpg')
```

## Sources for Free Images

- **Unsplash**: https://unsplash.com (free high-quality photos)
- **Pixabay**: https://pixabay.com (free images and videos)
- **OpenCV Samples**: https://github.com/opencv/opencv/tree/master/samples/data
- **Create your own**: Use notebooks to generate test images

## Current Status

📁 **Empty** - Add your own images or download from sources above

## File Naming Convention

Use descriptive names:
- `landscape_mountain.jpg`
- `face_portrait.jpg`
- `text_document_scan.png`
- `noisy_photo.jpg`
- `binary_shapes.png`

Keep names lowercase with underscores for consistency.

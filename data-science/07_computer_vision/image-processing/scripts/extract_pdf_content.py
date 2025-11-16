"""
PDF Content Extraction Script
Safely extracts text from the Practical-Handbook.pdf for analysis
"""

import os

import fitz  # PyMuPDF


def check_pdf_safety(pdf_path, max_pages=50, max_mb=15):
    """Check if PDF can be safely processed."""
    # Check file size
    size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"File size: {size_mb:.2f}MB")

    # Check page count
    try:
        doc = fitz.open(pdf_path)
        page_count = len(doc)
        doc.close()
        print(f"Page count: {page_count}")

        return {
            "size_mb": size_mb,
            "page_count": page_count,
            "safe_direct_read": size_mb <= max_mb and page_count <= max_pages,
        }
    except Exception as e:
        print(f"Error checking PDF: {e}")
        return None


def extract_text_with_pages(pdf_path, output_path):
    """Extract all text from PDF with page markers."""
    print(f"Extracting text from: {pdf_path}")

    doc = fitz.open(pdf_path)
    full_text = []

    # Extract text page by page
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()

        # Add page marker
        full_text.append(f"\n{'='*80}\n")
        full_text.append(f"PAGE {page_num + 1}\n")
        full_text.append(f"{'='*80}\n\n")
        full_text.append(text)

        # Progress indicator
        if (page_num + 1) % 10 == 0:
            print(f"Processed {page_num + 1}/{len(doc)} pages...")

    doc.close()

    # Save to file
    full_text_content = "".join(full_text)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text_content)

    print(f"\nExtraction complete!")
    print(f"Total characters: {len(full_text_content):,}")
    print(f"Saved to: {output_path}")

    return full_text_content


def analyze_structure(text):
    """Analyze the extracted text to identify chapters and sections."""
    lines = text.split("\n")

    # Look for chapter headings (usually uppercase or contain "Chapter")
    chapters = []
    sections = []

    for i, line in enumerate(lines):
        line_stripped = line.strip()

        # Skip empty lines
        if not line_stripped:
            continue

        # Identify potential chapter headings
        if (
            "chapter" in line_stripped.lower()
            or "CHAPTER" in line
            or (line_stripped.isupper() and len(line_stripped) > 5 and len(line_stripped) < 100)
        ):
            chapters.append((i, line_stripped))

        # Identify numbered sections (e.g., "1.1", "2.3")
        if len(line_stripped) > 0 and line_stripped[0].isdigit() and "." in line_stripped[:10]:
            sections.append((i, line_stripped))

    return {
        "chapters": chapters[:50],  # First 50 potential chapters
        "sections": sections[:100],  # First 100 potential sections
    }


def main():
    # Paths
    pdf_path = "Practical-Handbook.pdf"
    output_text_path = "handbook_extracted_text.txt"
    analysis_output = "handbook_structure.txt"

    # Check PDF safety
    print("Checking PDF file...")
    safety_info = check_pdf_safety(pdf_path)

    if not safety_info:
        print("Error: Could not check PDF file")
        return

    print(f"\nSafety assessment:")
    print(f"  Safe for direct read: {safety_info['safe_direct_read']}")
    print(f"  Using chunked extraction method...\n")

    # Extract text
    text_content = extract_text_with_pages(pdf_path, output_text_path)

    # Analyze structure
    print("\nAnalyzing document structure...")
    structure = analyze_structure(text_content)

    # Save structure analysis
    with open(analysis_output, "w", encoding="utf-8") as f:
        f.write("DOCUMENT STRUCTURE ANALYSIS\n")
        f.write("=" * 80 + "\n\n")

        f.write("POTENTIAL CHAPTERS:\n")
        f.write("-" * 80 + "\n")
        for line_num, heading in structure["chapters"]:
            f.write(f"Line {line_num}: {heading}\n")

        f.write("\n\nPOTENTIAL SECTIONS:\n")
        f.write("-" * 80 + "\n")
        for line_num, section in structure["sections"]:
            f.write(f"Line {line_num}: {section}\n")

    print(f"Structure analysis saved to: {analysis_output}")
    print(f"\nFound {len(structure['chapters'])} potential chapters")
    print(f"Found {len(structure['sections'])} potential sections")

    print("\n" + "=" * 80)
    print("NEXT STEPS:")
    print("1. Review 'handbook_extracted_text.txt' for content")
    print("2. Review 'handbook_structure.txt' for topics")
    print("3. Use this information to plan notebook topics")
    print("=" * 80)


if __name__ == "__main__":
    main()

import easyocr

# Initialize OCR reader once
reader = easyocr.Reader(['en'])

def extract_text(image_path):
    """
    Extract text from an image using EasyOCR.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Extracted text.
    """
    result = reader.readtext(image_path, detail=0)
    text = " ".join(result)

    return text


if __name__ == "__main__":
    image_path = "sample.jpg"

    try:
        text = extract_text(image_path)

        print("\nExtracted Text:\n")
        print(text)

    except Exception as e:
        print(f"Error: {e}")

import pytesseract
from PIL import Image


def extract_text(image_path):
    image = Image.open(image_path)

    image = image.resize((image.width * 3, image.height * 3))

    image = image.convert("L")

    text = pytesseract.image_to_string(image, config="--psm 6")

    return text

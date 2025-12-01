# #proper working terminal

# from PIL import Image
# import pytesseract
# from pathlib import Path

# def extract_text_from_image(image_path):
#     """
#     Extract text from an image using pytesseract (OCR).
#     Supports both English and Spanish languages.
#     Args:
#         image_path (str or Path): Path to the image file.
#     Returns:
#         str: Extracted text from the image.
#     """
#     image_path = Path(image_path)  # Ensure the path is a Path object
#     if not image_path.exists():
#         raise FileNotFoundError(f"Image file not found: {image_path}")

#     try:
#         # Open the image file
#         img = Image.open(image_path)

#         # Perform OCR using pytesseract
#         text = pytesseract.image_to_string(img, lang="eng+spa")
#         return text
#     except Exception as e:
#         print(f"Error processing image {image_path}: {e}")
#         return None















#streamlit working
from PIL import Image
import pytesseract
from io import BytesIO

def extract_text_from_image(image_bytes):
    """
    Extract text from an image using pytesseract (OCR).
    Supports both English and Spanish languages.
    Args:
        image_bytes (BytesIO): In-memory byte stream of the image file.
    Returns:
        str: Extracted text from the image.
    """
    try:
        # Open the image file from BytesIO
        img = Image.open(image_bytes)

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(img, lang="eng+spa")
        return text
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

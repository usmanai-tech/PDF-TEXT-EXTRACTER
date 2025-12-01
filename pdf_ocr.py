# #proper working terminal

# import platform
# from tempfile import TemporaryDirectory
# from pathlib import Path
# import pytesseract
# from pdf2image import convert_from_path
# from PIL import Image

# def extract_text_from_pdf(pdf_path):
#     """Extract text from a PDF file."""
#     image_file_list = []

#     # Path for output text file
#     out_directory = Path("output")
#     out_directory.mkdir(exist_ok=True)
#     text_file = out_directory / Path(f"extracted_text.txt")

#     try:
#         with TemporaryDirectory() as tempdir:
#             print(f"Temporary directory created: {tempdir}")

#             # Part 1: Convert PDF pages to images
#             if platform.system() == "Windows":
#                 print(f"Converting PDF to images using Poppler...")
#                 pdf_pages = convert_from_path(pdf_path, 500, poppler_path=r"C:\poppler\Library\bin")
#             else:
#                 print(f"Converting PDF to images without Poppler...")
#                 pdf_pages = convert_from_path(pdf_path, 500)

#             print(f"Converted PDF to {len(pdf_pages)} pages.")

#             # Save images
#             for page_enumeration, page in enumerate(pdf_pages, start=1):
#                 filename = f"{tempdir}/page_{page_enumeration:03}.jpg"
#                 page.save(filename, "JPEG")
#                 image_file_list.append(filename)

#             # Part 2: Extract text from the images
#             with open(text_file, "w", encoding="utf-8") as output_file:
#                 for image_file in image_file_list:
#                     # Extract text using pytesseract
#                     text = pytesseract.image_to_string(Image.open(image_file))

#                     # Check if text is valid and not empty
#                     if text:
#                         text = text.replace("-\n", "")  # Remove hyphenation at line breaks
#                         output_file.write(text)
#                     else:
#                         print(f"Warning: No text extracted from {image_file}. Skipping.")

#             print(f"Text extraction complete. Output saved to {text_file}")
#     except Exception as e:
#         print(f"Error during PDF OCR extraction: {e}")
#         raise





















# #streamlit working code
# import platform
# from tempfile import TemporaryDirectory
# from io import BytesIO
# import pytesseract
# from pdf2image import convert_from_path
# from PIL import Image

# def extract_text_from_pdf(pdf_bytes):
#     """Extract text from a PDF file (from memory)."""
#     image_file_list = []

#     # Use a temporary file to store the PDF content
#     with TemporaryDirectory() as tempdir:
#         try:
#             # Write PDF bytes to a temporary file
#             with open(f"{tempdir}/temp.pdf", "wb") as f:
#                 f.write(pdf_bytes.read())

#             # Convert PDF pages to images
#             if platform.system() == "Windows":
#                 pdf_pages = convert_from_path(f"{tempdir}/temp.pdf", 500, poppler_path=r"C:\poppler\Library\bin")
#             else:
#                 pdf_pages = convert_from_path(f"{tempdir}/temp.pdf", 500)

#             # Extract text from images
#             for page_enumeration, page in enumerate(pdf_pages, start=1):
#                 image_file = f"{tempdir}/page_{page_enumeration:03}.jpg"
#                 page.save(image_file, "JPEG")
#                 image_file_list.append(image_file)

#             text = ""
#             for image_file in image_file_list:
#                 text += pytesseract.image_to_string(Image.open(image_file))

#             return text

#         except Exception as e:
#             print(f"Error during PDF OCR extraction: {e}")
#             return None


















#poppler with project directory
import platform
import os
from tempfile import TemporaryDirectory
from io import BytesIO
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def extract_text_from_pdf(pdf_bytes):
    """Extract text from a PDF file (from memory)."""
    image_file_list = []

    # Define Poppler path based on the project directory
    poppler_path = os.path.join(os.getcwd(), "models", "poppler", "Library", "bin")

    # Use a temporary directory to store the PDF content and images
    with TemporaryDirectory() as tempdir:
        try:
            # Write PDF bytes to a temporary file
            pdf_path = os.path.join(tempdir, "temp.pdf")
            with open(pdf_path, "wb") as f:
                f.write(pdf_bytes.read())

            # Convert PDF pages to images
            if platform.system() == "Windows":
                pdf_pages = convert_from_path(pdf_path, 500, poppler_path=poppler_path)
            else:
                pdf_pages = convert_from_path(pdf_path, 500)

            # Extract text from images
            text = ""
            for page_enumeration, page in enumerate(pdf_pages, start=1):
                image_file = os.path.join(tempdir, f"page_{page_enumeration:03}.jpg")
                page.save(image_file, "JPEG")
                text += pytesseract.image_to_string(Image.open(image_file))

            return text

        except Exception as e:
            print(f"Error during PDF OCR extraction: {e}")
            return None




























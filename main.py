# # main.py

# import os
# from pathlib import Path
# from PIL import Image
# import pytesseract
# from text_preprocessing import preprocess_text

# def extract_text_from_image(image_path):
#     """Extract text from an image using Tesseract OCR."""
#     img = Image.open(image_path)
#     text = pytesseract.image_to_string(img, lang='eng+spa')  # Use both English and Spanish
#     return text

# def extract_text_from_pdf(pdf_path):
#     """Extract text from a PDF using Tesseract OCR (after converting it to images)."""
#     from pdf2image import convert_from_path
#     pdf_pages = convert_from_path(pdf_path, 500)
#     text = ""
#     for page in pdf_pages:
#         text += pytesseract.image_to_string(page, lang='eng+spa')
#     return text

# def main():
#     # Define the input and output directories
#     input_pdf_path = Path("input_samples\VM_Migration.pdf")
#     input_image_path = Path("input_samples/image_sample2.jpg")
#     output_text_path = Path("output/processed_text.txt")

#     # Extract text from PDF
#     if input_pdf_path.exists():
#         print("Extracting text from PDF...")
#         pdf_text = extract_text_from_pdf(input_pdf_path)
#         print(f"Extracted text from PDF (first 1000 chars):\n{pdf_text[:1000]}")
#         processed_pdf_text = preprocess_text(pdf_text, source_type="pdf_ocr")
#         if processed_pdf_text:
#             with open(output_text_path, "w") as file:
#                 file.write(processed_pdf_text)
#             print(f"Processed PDF text saved to {output_text_path}")
#         else:
#             print("Error processing PDF text.")
    
#     # Extract text from Image
#     if input_image_path.exists():
#         print("\nExtracting text from Image...")
#         image_text = extract_text_from_image(input_image_path)
#         print(f"Extracted text from Image (first 1000 chars):\n{image_text[:1000]}")
#         processed_image_text = preprocess_text(image_text, source_type="image_ocr")
#         if processed_image_text:
#             with open(output_text_path, "w") as file:
#                 file.write(processed_image_text)
#             print(f"Processed image text saved to {output_text_path}")
#         else:
#             print("Error processing image text.")

# if __name__ == "__main__":
#     main()










# # working main.py

# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import extract_text_from_pdf
# from text_preprocessing import preprocess_text

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check the file type and call the appropriate OCR function
#     if file_path.suffix.lower() in [".pdf"]:
#         print("PDF file detected. Extracting text from PDF...")
#         raw_text = extract_text_from_pdf(file_path)
#         source_type = "pdf_ocr"
#     elif file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         raw_text = extract_text_from_image(file_path)
#         source_type = "image_ocr"
#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")
#         return

#     if raw_text is None:
#         print("Error: Text extraction failed. Please check the input file.")
#         return

#     # Preprocess the extracted text
#     print("Preprocessing the extracted text...")
#     processed_text = preprocess_text(raw_text, source_type=source_type)

#     if processed_text:
#         # Save the processed text to an output file
#         output_dir = Path("output")
#         output_dir.mkdir(exist_ok=True)  # Create the output directory if it doesn't exist
#         output_text_path = output_dir / "processed_text.txt"

#         with open(output_text_path, "w", encoding="utf-8") as file:
#             file.write(processed_text)
#         print(f"Processed text saved to: {output_text_path}")
#     else:
#         print("Error: Preprocessing failed.")

# if __name__ == "__main__":
#     main()












# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import extract_text_from_pdf
# from text_preprocessing import preprocess_text
# import info_extraction  # Import the info_extraction module

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check the file type and call the appropriate OCR function
#     if file_path.suffix.lower() in [".pdf"]:
#         print("PDF file detected. Extracting text from PDF...")
#         raw_text = extract_text_from_pdf(file_path)
#         source_type = "pdf_ocr"
#     elif file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         raw_text = extract_text_from_image(file_path)
#         source_type = "image_ocr"
#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")
#         return

#     if raw_text is None:
#         print("Error: Text extraction failed. Please check the input file.")
#         return

#     # Preprocess the extracted text
#     print("Preprocessing the extracted text...")
#     processed_text = preprocess_text(raw_text, source_type=source_type)

#     if processed_text:
#         # Save the processed text to an output file
#         output_dir = Path("output")
#         output_dir.mkdir(exist_ok=True)  # Create the output directory if it doesn't exist
#         output_text_path = output_dir / "processed_text.txt"

#         with open(output_text_path, "w", encoding="utf-8") as file:
#             file.write(processed_text)
#         print(f"Processed text saved to: {output_text_path}")
        
#         # Trigger info extraction on the processed text
#         print("Triggering info extraction from processed text...")
#         info_extraction.extract_information(output_text_path)  # Call the extraction function
#     else:
#         print("Error: Preprocessing failed.")

# if __name__ == "__main__":
#     main()

















# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import main as pdf_ocr_main

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check if the input is an image or a PDF
#     if file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         try:
#             # Extract text from the image
#             raw_text = extract_text_from_image(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"{file_path.stem}_extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from image saved to: {output_text_path}")

#         except Exception as e:
#             print(f"Error during image text extraction: {e}")
    
#     elif file_path.suffix.lower() == ".pdf":
#         print("PDF file detected. Extracting text from PDF...")
#         try:
#             # Call the PDF OCR function
#             pdf_ocr_main(file_path)
#         except Exception as e:
#             print(f"Error during PDF OCR extraction: {e}")

#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")

# if __name__ == "__main__":
#     main()

















# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import main as pdf_ocr_main

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check if the input is an image or a PDF
#     if file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         try:
#             # Extract text from the image
#             raw_text = extract_text_from_image(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"{file_path.stem}_extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from image saved to: {output_text_path}")

#         except Exception as e:
#             print(f"Error during image text extraction: {e}")
    
#     elif file_path.suffix.lower() == ".pdf":
#         print("PDF file detected. Extracting text from PDF...")
#         try:
#             # Call the PDF OCR function but without passing arguments
#             pdf_ocr_main()

#         except Exception as e:
#             print(f"Error during PDF OCR extraction: {e}")

#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")

# if __name__ == "__main__":
#     main()













# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import extract_text_from_pdf

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check if the input is an image or a PDF
#     if file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         try:
#             # Extract text from the image
#             raw_text = extract_text_from_image(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from image saved to: {output_text_path}")

#         except Exception as e:
#             print(f"Error during image text extraction: {e}")
    
#     elif file_path.suffix.lower() == ".pdf":
#         print("PDF file detected. Extracting text from PDF...")
#         try:
#             # Call the PDF OCR function, passing the file path
#             extract_text_from_pdf(file_path)

#         except Exception as e:
#             print(f"Error during PDF OCR extraction: {e}")

#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")

# if __name__ == "__main__":
#     main()























# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import extract_text_from_pdf
# from text_preprocessing import preprocess_legal_deed_text  # Import your preprocessing function

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check if the input is an image or a PDF
#     if file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         try:
#             # Extract text from the image
#             raw_text = extract_text_from_image(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from image saved to: {output_text_path}")

#             # # Preprocess the extracted text
#             # cleaned_text = preprocess_legal_deed_text(raw_text)

#             # # Save the cleaned text to a new file
#             # cleaned_text_file = output_dir / "cleaned_extracted_text.txt"
#             # with open(cleaned_text_file, "w", encoding="utf-8") as file:
#             #     file.write(cleaned_text)
#             # print(f"Cleaned text saved to: {cleaned_text_file}")

#         except Exception as e:
#             print(f"Error during image text extraction: {e}")
    
#     elif file_path.suffix.lower() == ".pdf":
#         print("PDF file detected. Extracting text from PDF...")
#         try:
#             # Call the PDF OCR function, passing the file path
#             raw_text = extract_text_from_pdf(file_path)

#             # # Preprocess the extracted text
#             # cleaned_text = preprocess_legal_deed_text(raw_text)

#             # # Save the cleaned text to a new file
#             # output_dir = Path("output")
#             # output_dir.mkdir(exist_ok=True)
#             # cleaned_text_file = output_dir / "cleaned_extracted_text.txt"
#             # with open(cleaned_text_file, "w", encoding="utf-8") as file:
#             #     file.write(cleaned_text)
#             # print(f"Cleaned text saved to: {cleaned_text_file}")

#         except Exception as e:
#             print(f"Error during PDF OCR extraction: {e}")

#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")

# if __name__ == "__main__":
#     main()


















# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import extract_text_from_pdf
# from text_preprocessing import preprocess_legal_deed_text  # Import your preprocessing function
# from chatbot_model import main as chatbot_main  # Import the main function from chatbot_model.py

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check if the input is an image or a PDF
#     if file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         try:
#             # Extract text from the image
#             raw_text = extract_text_from_image(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from image saved to: {output_text_path}")

#             # Pass the extracted text to the chatbot model
#             chatbot_main()  # This calls the main function in chatbot_model.py and processes the text

#         except Exception as e:
#             print(f"Error during image text extraction: {e}")
    
#     elif file_path.suffix.lower() == ".pdf":
#         print("PDF file detected. Extracting text from PDF...")
#         try:
#             # Call the PDF OCR function, passing the file path
#             raw_text = extract_text_from_pdf(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from PDF saved to: {output_text_path}")

#             # Pass the extracted text to the chatbot model
#             chatbot_main()  # This calls the main function in chatbot_model.py and processes the text

#         except Exception as e:
#             print(f"Error during PDF OCR extraction: {e}")

#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")

# if __name__ == "__main__":
#     main()





























# import asyncio
# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import extract_text_from_pdf
# from chatbot_model import main as chatbot_main  # Import async main from chatbot_model.py

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check if the input is an image or a PDF
#     if file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         try:
#             # Extract text from the image
#             raw_text = extract_text_from_image(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from image saved to: {output_text_path}")

#             # Now call the chatbot model with the extracted text
#             asyncio.run(chatbot_main())  # Pass the extracted text to chatbot model

#         except Exception as e:
#             print(f"Error during image text extraction: {e}")
    
#     elif file_path.suffix.lower() == ".pdf":
#         print("PDF file detected. Extracting text from PDF...")
#         try:
#             # Call the PDF OCR function, passing the file path
#             raw_text = extract_text_from_pdf(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from PDF saved to: {output_text_path}")

#             # Now call the chatbot model with the extracted text
#             asyncio.run(chatbot_main())  # Pass the extracted text to chatbot model

#         except Exception as e:
#             print(f"Error during PDF OCR extraction: {e}")

#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")

# if __name__ == "__main__":
#     main()





















# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import extract_text_from_pdf
# from chatbot_model import process_with_groq_model  # Import the function to call Groq model

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check if the input is an image or a PDF
#     if file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         try:
#             # Extract text from the image
#             raw_text = extract_text_from_image(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from image saved to: {output_text_path}")

#             # Process the extracted text with the Groq model
#             model_response = process_with_groq_model(raw_text)
#             print(f"Model Response: {model_response}")

#         except Exception as e:
#             print(f"Error during image text extraction: {e}")

#     elif file_path.suffix.lower() == ".pdf":
#         print("PDF file detected. Extracting text from PDF...")
#         try:
#             # Call the PDF OCR function, passing the file path
#             raw_text = extract_text_from_pdf(file_path)

#             # Save the extracted text to a text file
#             output_dir = Path("output")
#             output_dir.mkdir(exist_ok=True)
#             output_text_path = output_dir / f"extracted_text.txt"

#             with open(output_text_path, "w", encoding="utf-8") as file:
#                 file.write(raw_text)
#             print(f"Extracted text from PDF saved to: {output_text_path}")

#             # Process the extracted text with the Groq model
#             model_response = process_with_groq_model(raw_text)
#             print(f"Model Response: {model_response}")

#         except Exception as e:
#             print(f"Error during PDF OCR extraction: {e}")

#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")

# if __name__ == "__main__":
#     main()

























# from pathlib import Path
# from image_ocr import extract_text_from_image
# from pdf_ocr import extract_text_from_pdf
# # from text_preprocessing import preprocess_legal_deed_text  # Import your preprocessing function

# def main():
#     # Ask the user for the file path
#     file_path = input("Enter the full path of the file (PDF or Image): ").strip()
#     file_path = Path(file_path)

#     if not file_path.exists():
#         print("Error: File does not exist. Please check the path and try again.")
#         return

#     # Check if the input is an image or a PDF
#     if file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#         print("Image file detected. Extracting text from Image...")
#         try:
#             # Extract text from the image
#             raw_text = extract_text_from_image(file_path)

#             if raw_text:
#                 # Save the extracted text to a text file
#                 output_dir = Path("output")
#                 output_dir.mkdir(exist_ok=True)
#                 output_text_path = output_dir / f"extracted_text.txt"

#                 with open(output_text_path, "w", encoding="utf-8") as file:
#                     file.write(raw_text)
#                 print(f"Extracted text from image saved to: {output_text_path}")
#             else:
#                 print("Error: No text extracted from image.")

#         except Exception as e:
#             print(f"Error during image text extraction: {e}")
    
#     elif file_path.suffix.lower() == ".pdf":
#         print("PDF file detected. Extracting text from PDF...")
#         try:
#             # Call the PDF OCR function, passing the file path
#             raw_text = extract_text_from_pdf(file_path)

#             if raw_text:
#                 # Save the extracted text to a text file
#                 output_dir = Path("output")
#                 output_dir.mkdir(exist_ok=True)
#                 output_text_path = output_dir / f"extracted_text.txt"

#                 with open(output_text_path, "w", encoding="utf-8") as file:
#                     file.write(raw_text)
#                 print(f"Extracted text from PDF saved to: {output_text_path}")
#             else:
#                 print("Error: No text extracted from PDF.")

#         except Exception as e:
#             print(f"Error during PDF OCR extraction: {e}")

#     else:
#         print("Error: Unsupported file type. Please provide a valid PDF or image file.")

# if __name__ == "__main__":
#     main()



















import os
from dotenv import load_dotenv
from pathlib import Path
from pdf_ocr import extract_text_from_pdf
from chatbot_model import process_with_groq_model

# Load environment variables from .env file
load_dotenv()

# Path for input PDF file
pdf_path = input("Enter the full path of the file (PDF or Image): ")

# Check if the file is a PDF
input_pdf_path = Path(pdf_path)

# Extract text from the PDF if it's a PDF file
if input_pdf_path.suffix.lower() == ".pdf":
    print("PDF file detected. Extracting text from PDF...")
    extract_text_from_pdf(input_pdf_path)
else:
    print("Unsupported file format. Please provide a PDF.")

# Read the extracted text from the output file
extracted_text_path = Path("output/extracted_text.txt")
if extracted_text_path.exists():
    with open(extracted_text_path, "r", encoding="utf-8") as file:
        extracted_text = file.read()

    # Now, pass the extracted text to the chatbot model for processing
    print("Passing extracted text to chatbot for processing...")
    response = process_with_groq_model(extracted_text)

    # Optionally, save the response to a file or print it out
    response_file = Path("output/processed_response.txt")
    with open(response_file, "w", encoding="utf-8") as file:
        file.write(response)
    print(f"Processed response saved to: {response_file}")

else:
    print("Error: Extracted text file not found.")

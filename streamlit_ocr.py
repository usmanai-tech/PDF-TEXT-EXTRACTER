# #proper working terminal
# import streamlit as st
# from io import BytesIO
# from pathlib import Path
# from pdf_ocr import extract_text_from_pdf
# from image_ocr import extract_text_from_image
# from chatbot_model import process_with_groq_model

# def main():
#     st.title("OCR Text Extraction and Chatbot Processing")

#     # File uploader to accept PDF or image files
#     uploaded_file = st.file_uploader("Choose a file (PDF or Image)", type=["pdf", "jpg", "jpeg", "png", "bmp", "tiff"])

#     if uploaded_file is not None:
#         # Handle the uploaded file (PDF or image) in memory
#         file_path = Path(uploaded_file.name)

#         st.write(f"File uploaded: {file_path}")

#         # Process based on the file type
#         if file_path.suffix.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
#             st.write("Processing image file...")

#             # Extract text from image using your image OCR function
#             try:
#                 # Read image as BytesIO
#                 img_bytes = BytesIO(uploaded_file.read())
#                 extracted_text = extract_text_from_image(img_bytes)
#                 st.text_area("Extracted Text", extracted_text, height=200)

#                 # Process with chatbot model
#                 if st.button("Process with Chatbot"):
#                     result = process_with_groq_model(extracted_text)
#                     st.write(result)

#             except Exception as e:
#                 st.error(f"Error during image OCR extraction: {e}")

#         elif file_path.suffix.lower() == ".pdf":
#             st.write("Processing PDF file...")

#             # Extract text from PDF using your PDF OCR function
#             try:
#                 # Read PDF as BytesIO
#                 pdf_bytes = BytesIO(uploaded_file.read())
#                 extracted_text = extract_text_from_pdf(pdf_bytes)
#                 st.text_area("Extracted Text", extracted_text, height=200)

#                 # Process with chatbot model
#                 if st.button("Process with Chatbot"):
#                     result = process_with_groq_model(extracted_text)
#                     st.write(result)

#             except Exception as e:
#                 st.error(f"Error during PDF OCR extraction: {e}")

# if __name__ == "__main__":
#     main()


















#streamlit
import streamlit as st
from io import BytesIO
from pdf_ocr import extract_text_from_pdf
from image_ocr import extract_text_from_image
from chatbot_model import process_with_groq_model

def main():
    st.title("OCR Text Extraction and Chatbot Processing")

    # File uploader to accept PDF or image files
    uploaded_file = st.file_uploader("Choose a file (PDF or Image)", type=["pdf", "jpg", "jpeg", "png", "bmp", "tiff"])

    if uploaded_file is not None:
        # Handle the uploaded file (PDF or image) in memory
        file_path = uploaded_file.name

        st.write(f"File uploaded: {file_path}")

        # Process based on the file type
        if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            st.write("Processing image file...")

            # Extract text from image using your image OCR function
            try:
                # Read image as BytesIO
                img_bytes = BytesIO(uploaded_file.read())
                extracted_text = extract_text_from_image(img_bytes)
                st.text_area("Extracted Text", extracted_text, height=200)

                # Process with chatbot model
                if st.button("Process with Chatbot"):
                    result = process_with_groq_model(extracted_text)
                    st.write(result)

            except Exception as e:
                st.error(f"Error during image OCR extraction: {e}")

        elif file_path.lower().endswith('.pdf'):
            st.write("Processing PDF file...")

            # Extract text from PDF using your PDF OCR function
            try:
                # Read PDF as BytesIO
                pdf_bytes = BytesIO(uploaded_file.read())
                extracted_text = extract_text_from_pdf(pdf_bytes)
                st.text_area("Extracted Text", extracted_text, height=200)

                # Process with chatbot model
                if st.button("Process with Chatbot"):
                    result = process_with_groq_model(extracted_text)
                    st.write(result)

            except Exception as e:
                st.error(f"Error during PDF OCR extraction: {e}")

if __name__ == "__main__":
    main()

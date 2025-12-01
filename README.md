# PDF-TEXT-EXTRACTER

## Project Description

The **PDF-TEXT-EXTRACTER** is a comprehensive tool for extracting and analyzing text from PDF and image files. It uses OCR (Optical Character Recognition) technology and AI-based processing to analyze legal deed documents in English and Spanish. 

### Key Features
- **OCR for PDFs and Images**: Extract text from PDF documents and various image formats.
- **Multilingual Support**: Processes English and Spanish text for wider applicability.
- **AI-Powered Analysis**: Automatically identifies and extracts critical details from legal deed documents, such as:
  - Date of Sale
  - Sales Price
  - Seller and Buyer Names
  - Property Details (Lot Size, Cadaster Number, etc.)
- **User-Friendly Interface**: Built using Streamlit for an intuitive file upload and result presentation experience.
- **Advanced AI Integration**: Utilizes Groq AI's LLaMA-3.3 model for high-accuracy data analysis.

### How It Works
1. Upload a **PDF** or **image file** through the Streamlit interface.
2. The application extracts text using `pytesseract` and `pdf2image` for OCR.
3. AI processes the extracted text to provide structured information specific to legal documents.
4. The results are displayed in an organized format on the Streamlit web app.

---

## Installation

### Prerequisites
- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Poppler Utilities](https://poppler.freedesktop.org/)
- Streamlit

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-text-extracter.git
   cd pdf-text-extracter

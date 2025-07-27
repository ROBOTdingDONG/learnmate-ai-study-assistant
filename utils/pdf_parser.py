import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    try:
        for page in doc:
            text += page.get_text()
    finally:
        doc.close()  # Ensure document is properly closed
    return text
import fitz #pymupdf

def extract_text_from_pdf(pdf):
    doc = fitz.open(pdf)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


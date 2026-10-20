import io
import re

def extract_resume_text(uploaded_file):
    if uploaded_file is None:
        return ""
    data = uploaded_file.getvalue()
    name = uploaded_file.name.lower()
    if name.endswith(".pdf"):
        from PyPDF2 import PdfReader
        pages = PdfReader(io.BytesIO(data)).pages
        text = "\n".join(page.extract_text() or "" for page in pages)
    elif name.endswith(".docx"):
        from docx import Document
        document = Document(io.BytesIO(data))
        text = "\n".join(p.text for p in document.paragraphs)
    else:
        raise ValueError("Only PDF and DOCX files are supported")
    if not text.strip():
        raise ValueError("No extractable text was found. Scanned-image resumes require OCR.")
    return re.sub(r"\s+", " ", text).strip()

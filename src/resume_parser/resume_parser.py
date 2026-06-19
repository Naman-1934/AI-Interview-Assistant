import pdfplumber

def parse_resume(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    return text.strip()
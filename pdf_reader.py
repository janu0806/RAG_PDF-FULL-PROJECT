from pypdf import PdfReader

def read_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    print("Pages:", len(reader.pages))

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    print("Text Length:", len(text))

    return text.strip()
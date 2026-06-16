import PyPDF2
import re


def extract_text(pdf_file):

    text = ""

    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def clean_text(text):

    text = text.lower()

    text = re.sub(r"\n", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text
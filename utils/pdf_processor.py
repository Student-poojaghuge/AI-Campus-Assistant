from pathlib import Path

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def extract_text_from_pdf(pdf_path):
    """
    Extract text from all pages of a PDF.
    """

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    if pdf_path.stat().st_size == 0:
        raise ValueError("The PDF file is empty.")

    reader = PdfReader(str(pdf_path))

    text = ""

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


def clean_text(text):
    """
    Basic text cleaning.
    """

    text = text.replace("\x00", " ")

    # Remove unnecessary multiple spaces
    text = " ".join(text.split())

    return text


def split_text(text):
    """
    Split text into smaller chunks for AI processing.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = text_splitter.split_text(text)

    return chunks


def process_pdf(pdf_path):
    """
    Complete PDF processing pipeline.
    """

    text = extract_text_from_pdf(pdf_path)

    cleaned_text = clean_text(text)

    chunks = split_text(cleaned_text)

    return {
        "text": cleaned_text,
        "chunks": chunks,
        "total_characters": len(cleaned_text),
        "total_chunks": len(chunks)
    }
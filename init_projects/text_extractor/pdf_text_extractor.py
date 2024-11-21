"""PDF Text Extractor
This file contains the function needed for extracting text from a PDF file."""

import fitz


def extract_text_pdf(file: str) -> str:
    """
    This function extracts the text from a PDF file.
    Args:
        file (str): PDF file.
    Returns:
        str: The extracted text from the PDF file.
    Raises:
        ValueError: If the file is not a PDF.
    """
    try:
        with fitz.open(file) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            text = text.replace("�", "")
        return text
    except Exception:
        raise ValueError("The file is not a valid PDF.")

"""PDF Text Extractor
This file contains the function needed for extracting text from a PDF file."""

import fitz


def extract_text_pdf(file: str) -> str:

    """This funtion extracts the text from PDF file.

    The ecope of this funtion is extract text from PDF file.

    Args:
        arg_1(str):
            PDF file.

    Returns:
        str: The extracted text from PDF file.

    Raises:
        ValueError: If fike is not a PDF file.
    """

    try:
        doc = fitz.open(file)
    except Exception:
        raise ValueError("The file is not a valid PDF.")

    return "n".join(page.get_text() for page in doc).strip()

"""DOCX Text Extractor
In this file is contained the function needed for extracting text from a DOCX file."""

from docx import Document


def extract_text_docx(file: str) -> str:
    """This funtion the text from DOCX file.
    Args:
        file(str):
        DOCX file.
    Returns:
        str: The extracted text from DOCX file.
    Raises:
        ValueError: If fike is not a DOCX file.
    """
    try:
        document = Document(file)
    except:
        raise ValueError("The file is not a valid DOCX file.")

    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text.strip()

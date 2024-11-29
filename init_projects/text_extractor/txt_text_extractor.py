"""TXT Text Extractor
In this fill is contened the funtion needed for extracting text from TXT file."""


def extract_text_txt(file: str) -> str:

    """This funtion extracts the text from TXT file.

    The ecope of this funtion is extract text from TXT file.

    Args:
        arg_1(str):
             DOCX file.

    Returns:
        str: The extracted text from TXT file.

    Raises:
        ValueError: If fike is not a TXT file.
    """

    try:
        text = file.read()
    except Exception:
        raise ValueError("The file is not a TXT file.")
    return text

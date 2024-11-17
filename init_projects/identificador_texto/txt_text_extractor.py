"""TXT Text Extractor
In this fill is contened the funtion needed for extracting text from TXT file."""


def extract_text_txt(file: str) -> str:

    """This funtion extracts the text from TXT file.
    Args:
        file(str):
        txt file.
    Returns:
        str: The extracted text from txt file.
    Raises:
        ValueError: If fike is not a txt file.
    """
    try:
        text = file.read()
    except Exception:
        raise ValueError("The file is not a TXT file.")
    return text

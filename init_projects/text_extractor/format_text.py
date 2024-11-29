def format_text(file: str) -> str:

    """
    This function replaces '?' with ' ' in the text of a file.
    Args:
        file (str): Extracted text from a file.
    Returns:
        str: The extracted text from a file with '?' replaced by ' '.
    """

    text = file.replace("�", "")
    return text

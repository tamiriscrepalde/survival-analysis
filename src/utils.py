"""Useful general functions."""


def read_file(file_path: str) -> str:
    """Read file and returns its content.

    Args:
        file_path (str): Path of the file.

    Returns:
        str: File's content.
    """
    file = open(file_path, 'r', encoding='utf-8')
    content = file.read()
    file.close()

    return content

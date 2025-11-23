import logging
def load_text(file_path):
    """Load text from a file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the file as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"Error: The file at {file_path} was not found.")
        return ""
    except IOError:
        logging.error(f"Error: An error occurred while reading the file at {file_path}.")
        return ""
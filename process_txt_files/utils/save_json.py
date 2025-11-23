import json

def save_json(data: dict, file_path: str) -> None:
    """Save a dictionary to a JSON file.

    Args:
        data (dict): The data to save.
        file_path (str): The path to the output JSON file.
    """
    
    if data is None:
        data = {}
    if file_path is None:
        raise ValueError("file_path cannot be None")
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
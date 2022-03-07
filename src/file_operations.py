import json
import os.path

"""
    Functions to handle common file operations.
"""


def export_data_to_json(folder_path, data):
    json_data = json.dumps(data, indent=4)
    with open(folder_path, "w") as f:
        f.write(json_data)


def import_data_from_json(json_file: str):
    with open(json_file, "r") as f:
        data = json.load(f)
    return data


def file_exists(path):
    return os.path.isfile(path)


def log_path(name):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Logs", name)
    return path

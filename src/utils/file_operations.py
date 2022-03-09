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
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../Logs", name)
    return path


# Logging file creation and setup
def setup_logging(file_name, rotation_size="250MB", rotation_time=None, _filter=None, _enqueue=True):
    from loguru import logger
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../Logs", file_name)
    if rotation_time is None:
        logger.add(path, rotation=rotation_size, encoding="utf-8", filter=_filter, enqueue=_enqueue)
    else:
        logger.add(path, rotation=rotation_time, encoding="utf-8", filter=_filter, enqueue=_enqueue)
    return logger

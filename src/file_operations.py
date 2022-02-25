import json


def export_table_data(folder_path, data):
    json_data = json.dumps(data, indent=4)
    with open(folder_path, "w") as f:
        f.write(json_data)


def import_table_data(json_file: str):
    with open(json_file) as f:
        data = json.load(f)
    return data

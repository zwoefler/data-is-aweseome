import json

def write_json_data_to_file(json_data, filename):
    with open (filename, "w") as f:
        json.dump(json_data, f)


def open_json(json_file):
    with open(json_file, "r") as f:
        json_data = json.load(f)
    return json_data

import os
import json

def read_json_file(json_path):
    with open(json_path) as f:
        json_data = json.load(f)
    return json_data


def write_json_to_file(json_path, json_data):
    with open(json_path, "w") as f:
        json.dump(json_data, f)

    return


def add_new_data(existing_data, new_data):
    final_data = existing_data
    message = ""

    timestamp = new_data["timestamp"]

    if new_data not in existing_data:
        final_data.append(new_data)
        message = f"Added {timestamp}"
    else:
        message = f"Skipped {timestamp}, it already exists in the dataset"

    return final_data, message


def list_files_in_directory(data_directory):
    files_in_directory = os.listdir(data_directory)
    return files_in_directory


def aggregate_data(data_directory):
    files = os.listdir(data_directory)
    return [{ "timestamp": "", "parkhouses": [] }]
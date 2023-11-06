import os

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
    return []


def aggregate_data(data_directory):
    files = os.listdir(data_directory)
    return [{ "timestamp": "", "parkhouses": [] }]
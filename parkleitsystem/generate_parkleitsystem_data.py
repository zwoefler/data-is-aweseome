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

    return final_data


def list_files_in_directory(data_directory):
    files_in_directory = os.listdir(data_directory)
    file_paths_in_directory = [os.path.join(data_directory, file) for file in files_in_directory]
    return file_paths_in_directory


def aggregate_data(data_files_list, existing_parkhouse_data):
    parkhouse_data = existing_parkhouse_data
    for json_file in data_files_list:
        json_data = read_json_file(json_file)
        parkhouse_data = add_new_data(existing_parkhouse_data, json_data)

    return parkhouse_data


def extract_single_parkhouse_info(parkhouse, parkhouse_timed_data):
    timestamp = parkhouse_timed_data["timestamp"]

    for i, parkhouse_dict in enumerate(parkhouse_timed_data["parkhouses"]):
        if parkhouse_dict["name"] == parkhouse:
            single_parkhouse = {
                "timestamp": timestamp,
                "name": parkhouse_dict["name"],
                "free_spaces": parkhouse_dict["free_spaces"],
                "max_spaces": parkhouse_dict["max_spaces"],
                "occupied_spaces": parkhouse_dict["occupied_spaces"],
            }

    return single_parkhouse


def get_single_parkhouse_data(parkhouse_name, parkhouse_data_file):
    single_parkhouse_info = []
    # Read contents from parkhouse_data_file
    # Iterate that content each dict goes into
    single_parkhouse_info = extract_parkhouse_info(parkhouse_name, parkhouse_timed_data)

    return
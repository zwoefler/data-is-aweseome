import os
from datetime import datetime, timezone
import json
import logging


def aggregate_parkhouse_data(data_dir):
    # Iterate files in folder
    file_list = list_files_in_directory(data_dir)
    # Load each file
    # read it's content
    # get names of parkhouses
    # if scheme for parkhouse doesn#t exist, create one
    # put data into scheme
    # Get next file, read, add to parkhouse scheme
    # once finished with files from folder, write schemes to
    # parkhouse_data/<PARKHOUSE.JSON>
    return


def list_files_in_directory(data_dir):
    file_paths = [os.path.join(data_dir, filename) for filename in os.listdir(data_dir)]
    return file_paths


def convert_timestamp_to_epoch_seconds(timestamp):
    date_format = "%d%m%Y-%H%M"
    date_object = datetime.strptime(timestamp, date_format)
    epoch_seconds = int(date_object.replace(tzinfo=timezone.utc).timestamp())

    return epoch_seconds


def read_json_file(json_path):
    with open(json_path) as json_file:
        json_data = json.load(json_file)
    return json_data


def create_parkhouse_data_folder(data_dir="parkhouse_data"):
    module_dir = os.path.dirname(os.path.dirname(__file__))
    parkhouse_data_dir = os.path.join(module_dir, data_dir)

    if os.path.exists(path=parkhouse_data_dir) and os.path.isdir(data_dir):
        logging.info(f"{data_dir} already exists")
        return

    os.makedirs(name=parkhouse_data_dir, exist_ok=True)
    return


def generate_parkhouse_data(aggregated_data_list):
    parkhouses_data = {}

    for raw_data in aggregated_data_list:
        timestamp = raw_data.get("timestamp", "")

        for parkhouse_info in raw_data.get("parkhouses", []):
            parkhouse_name = parkhouse_info.get("name").strip()

            if parkhouse_name not in parkhouses_data:
                parkhouses_data[parkhouse_name] = {
                    "name": parkhouse_name,
                    "occupation_data": [],
                }

            parkhouses_data[parkhouse_name]["occupation_data"].append(
                {
                    "timestamp": convert_timestamp_to_epoch_seconds(timestamp),
                    "free_spaces": parkhouse_info.get("free_spaces"),
                    "occupied_spaces": parkhouse_info.get("occupied_spaces"),
                    "max_spaces": parkhouse_info.get("max_spaces"),
                }
            )

    for parkhouse in parkhouses_data.keys():
        parkhouses_data[parkhouse]["occupation_data"] = sorted(
            parkhouses_data[parkhouse]["occupation_data"], key=lambda x: x["timestamp"]
        )

    return parkhouses_data


def export_parkhouse_data(data_directory, parkhouses_data):
    for parkhouse in parkhouses_data.keys():
        export_filename = f"{parkhouse.lower()}.json"
        export_path = os.path.join(data_directory, export_filename)
        with open(export_path, mode="w") as export_file:
            json.dump(parkhouses_data[parkhouse], export_file)
    return


def main():
    logging.basicConfig(level=logging.INFO)

    module_dir = os.path.dirname(os.path.dirname(__file__))
    data_directory = os.path.join(module_dir, "data/")

    create_parkhouse_data_folder("parkhouse_data")

    data_files = list_files_in_directory(data_directory)
    aggregated_data_list = [read_json_file(data_file) for data_file in data_files]
    parkhouses_data = generate_parkhouse_data(aggregated_data_list)

    export_parkhouse_data("parkhouse_data", parkhouses_data)
    return


if __name__ == "__main__":
    main()

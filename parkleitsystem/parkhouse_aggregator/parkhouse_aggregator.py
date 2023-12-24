import os
from datetime import datetime, timezone
import json


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

    os.makedirs(name=parkhouse_data_dir, exist_ok=True)
    return


def parkhouse_list_from_data(json_data):
    return [parkhouse["name"] for parkhouse in json_data["parkhouses"]]


def main():
    return


if __name__ == "__main__":
    main()

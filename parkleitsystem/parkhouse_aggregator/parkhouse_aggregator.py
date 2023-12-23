import os
from datetime import datetime, timezone


def aggregate_parkhouse_data(data_dir):
    return


def list_files_in_directory(data_dir):
    return []


def convert_timestamp_to_epoch_seconds(timestamp):
    date_format = "%d%m%Y-%H%M"
    date_object = datetime.strptime(timestamp, date_format)
    epoch_seconds = int(date_object.replace(tzinfo=timezone.utc).timestamp())

    return epoch_seconds


def create_parkhouse_data_folder(data_dir="parkhouse_data"):
    module_dir = os.path.dirname(os.path.dirname(__file__))

    parkhouse_data_dir = os.path.join(module_dir, data_dir)

    os.makedirs(parkhouse_data_dir, exist_ok=True)
    return


def main():
    return


if __name__ == "__main__":
    main()

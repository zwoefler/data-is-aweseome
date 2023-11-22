import os
import json
import datetime
import csv
from io import StringIO
import argparse

def read_json_file(json_path):
    with open(json_path) as f:
        json_data = json.load(f)
    return json_data


def write_json_to_file(json_path, json_data):
    with open(json_path, "w") as f:
        json.dump(json_data, f)

    return


def export_csv_to_file(filename, csv_data):
    with open(filename, "w") as csv_file:
        csv_file.write(csv_data)
    return


def create_export_filename(filename_base):
    today = datetime.datetime.now().strftime("%d%m%Y")
    lower_filename_base = filename_base.lower()
    file_name = f"{lower_filename_base}_data_{today}.json"
    return file_name


def convert_json_to_csv(json_data):
    buffer = StringIO()
    csv_writer = csv.writer(buffer)

    # Write the header
    csv_writer.writerow(json_data[0].keys())

    # Write the values for each key
    for row in json_data:
        csv_writer.writerow(row.values())

    # Get the CSV data from the buffer
    csv_data = buffer.getvalue()
    return csv_data


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


def extract_available_parkhouses(parkhouse_data):
    parkhouses = []
    for timestamped_data in parkhouse_data:
        for parkhouse in timestamped_data["parkhouses"]:
            if parkhouse["name"] not in parkhouses:
                parkhouses.append(parkhouse["name"])

    return parkhouses


def extract_single_parkhouse_info(parkhouse, timestamped_parkhouse_data):
    timestamp = timestamped_parkhouse_data["timestamp"]

    for i, parkhouse_dict in enumerate(timestamped_parkhouse_data["parkhouses"]):
        if parkhouse_dict["name"] == parkhouse:
            single_parkhouse = {
                "timestamp": timestamp,
                "name": parkhouse_dict["name"],
                "free_spaces": parkhouse_dict["free_spaces"],
                "max_spaces": parkhouse_dict["max_spaces"],
                "occupied_spaces": parkhouse_dict["occupied_spaces"],
            }
            break
        else:
            single_parkhouse = {
                "timestamp": timestamp,
                "name": parkhouse,
                "free_spaces": 0,
                "max_spaces": 0,
                "occupied_spaces": 0,
            }


    return single_parkhouse


def get_single_parkhouse_data(parkhouse_name, parkhouse_data_file):
    single_parkhouse_info = []
    all_parkhouse_data = read_json_file(parkhouse_data_file)
    for timestamped_parkhouse_data in all_parkhouse_data:
        parkhouse_info = extract_single_parkhouse_info(parkhouse_name, timestamped_parkhouse_data)
        single_parkhouse_info.append(parkhouse_info)

    export_filename = create_export_filename(parkhouse_name)
    write_json_to_file(export_filename, single_parkhouse_info)

    return



def aggregate_parkhouse_data(folder):
    existing_data = []
    files_list = list_files_in_directory(folder)
    aggregated_data = aggregate_data(files_list, existing_data)

    export_filename = create_export_filename("aggregated_parkhouse")
    write_json_to_file(export_filename, aggregated_data)

    return


def export_single_parkhouse_data_to_csv(parkhouse_json_file):
    json_parkhouse_data = read_json_file(parkhouse_json_file)
    csv_data = convert_json_to_csv(json_parkhouse_data)
    export_csv_to_file("dern-passage_01112023.csv", csv_data)
    return


def main():
    parser = argparse.ArgumentParser(description="Parkleitsystem Module")

    # Add command-line options
    parser.add_argument("--aggregate-json-data", metavar="folder", help="Aggregate JSON data from the specified folder")
    parser.add_argument("--extract-single-parkhouse", metavar=("parkhouse_name", "data_file"), nargs=2,
                        help="Extract data for a single parkhouse from a data file")
    parser.add_argument("--parkhouses", metavar="data_file", help="Show available parkhouses")
    parser.add_argument("--generate_csv", metavar="parkhouse_data_file", help="Create CSV file from JSON Parkhouse Data")

    args = parser.parse_args()

    if args.aggregate_json_data:
        aggregate_parkhouse_data(args.aggregate_json_data)

    if args.extract_single_parkhouse:
        parkhouse_name, data_file = args.extract_single_parkhouse
        get_single_parkhouse_data(parkhouse_name, data_file)

    if args.parkhouses:
        parkhouse_data = read_json_file(args.parkhouses)
        parkhouses = extract_available_parkhouses(parkhouse_data)
        print(parkhouses)

    if args.generate_csv:
        json_data = read_json_file(args.generate_csv)
        csv_data = convert_json_to_csv(json_data)
        filename = f"{args.generate_csv.split('.')[0]}.csv"
        export_csv_to_file(filename, csv_data)


if __name__ == '__main__':
    main()
import json
import csv
import argparse
import os
from datetime import datetime


def epoch_to_hhmm(epoch_time):
    dt = datetime.utcfromtimestamp(epoch_time)
    return dt.isoformat()


def transpose_json_to_csv(json_path):
    with open(json_path, "r") as json_file:
        data = json.load(json_file)

    csv_file = os.path.splitext(json_path)[0] + ".csv"

    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["timestamp", "free_spaces", "occupied_spaces", "max_spaces"])

        for entry in data["occupation_data"]:
            hhmm_time = epoch_to_hhmm(entry["timestamp"])
            writer.writerow(
                [
                    hhmm_time,
                    entry["free_spaces"],
                    entry["occupied_spaces"],
                    entry["max_spaces"],
                ]
            )

    print(f"Data has been written to {csv_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transpose JSON to CSV.")
    parser.add_argument(
        "json_path", type=str, help="Path to the JSON file to be transposed."
    )

    args = parser.parse_args()

    transpose_json_to_csv(args.json_path)

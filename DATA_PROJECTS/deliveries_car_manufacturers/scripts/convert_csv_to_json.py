import csv
import json
import sys


def csv_to_json(csv_file_path, json_file_path):
    data = {"months": [], "data": {}}

    with open(csv_file_path, mode="r", encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        data["months"] = rows[0][1:]

        for row in rows[1:]:
            category = row[0]
            values = [None if value == "*" else int(value) for value in row[1:]]
            data["data"][category] = values

    with open(json_file_path, mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

    print(f"CSV data successfully converted to JSON and saved to {json_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_to_json.py <input_file>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    json_file_path = csv_file_path.rsplit(".", 1)[0] + ".json"
    csv_to_json(csv_file_path, json_file_path)

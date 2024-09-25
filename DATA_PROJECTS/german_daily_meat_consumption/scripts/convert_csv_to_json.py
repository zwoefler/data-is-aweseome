import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = {
        "years": [],
        "data": {}
    }

    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        data["years"] = rows[1][1:]  

        for row in rows[2:]:
            category = row[0]  
            values = [
                None if value == "*" else int(value) for value in row[1:]
            ]  
            data["data"][category] = values

    with open(json_file_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

    print(f"CSV data successfully converted to JSON and saved to {json_file_path}")

csv_file_path = "data/daily_german_meat_consumption.csv" 
json_file_path = "data/daily_german_meat_consumption.json"

csv_to_json(csv_file_path, json_file_path)

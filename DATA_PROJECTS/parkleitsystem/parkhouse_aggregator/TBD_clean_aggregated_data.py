import os
import json
from datetime import datetime, timedelta
import pandas as pd


def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def process_json_file(data):
    parkhouse_name = data["name"]
    occupation_data = data["occupation_data"]

    # Convert to DataFrame
    df = pd.DataFrame(occupation_data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    df.set_index("timestamp", inplace=True)

    # Resample to daily frequency, aggregating with max and min
    daily_max = df.resample("D").max()
    daily_min = df.resample("D").min()

    # Fill the missing hours with the last known value of the day
    filled_data = df.resample("D").pad()

    # Combine max and min for visualization
    daily_data = pd.DataFrame(
        {
            "date": daily_max.index,
            "max_occupied_spaces": daily_max["occupied_spaces"],
            "min_free_spaces": daily_min["free_spaces"],
        }
    )

    return parkhouse_name, daily_data


all_parkhouses_data = {}


data_directory = "parkhouse_data"
for filename in os.listdir(data_directory):
    if filename.endswith(".json"):
        file_path = os.path.join(data_directory, filename)
        data = read_json_file(file_path)
        parkhouse_name, daily_data = process_json_file(data)
        all_parkhouses_data[parkhouse_name] = daily_data

# Example: Display the first few rows of data for one parkhouse
for parkhouse_name, daily_data in all_parkhouses_data.items():
    print(f"Parkhouse: {parkhouse_name}")
    print(daily_data.head())
    break

# Save processed data to CSV for frontend visualization
for parkhouse_name, daily_data in all_parkhouses_data.items():
    daily_data.to_csv(f"{data_directory}/{parkhouse_name}_daily_data.csv", index=False)

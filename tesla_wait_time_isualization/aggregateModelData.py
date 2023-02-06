import glob
import json
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Write function to get ALL data for a given Model

trimID = "$MT324"
data_dir = "final_data"
locale = "en_US"
model = "m3"
files = f"{model}_{locale}_*json"

exportFileName = f"data_{model}_{trimID}_{locale}.json"

def exportModelData(jsonData):
    with open(exportFileName, "w") as f:
        json.dump(jsonData, f)



json_files = glob.glob(os.path.join(data_dir, files))

priceData = []

for file_path in json_files:
    with open(file_path, "r") as f:
        data = json.load(f)

    trims = data["trims"]

    for trim in trims:
        if trim["trimShorthandle"] == trimID:
            price = trim["price"]
            date = data["date"]
            priceData.append((date, price))

sorted_data = sorted(priceData, key=lambda x: x[0])
dates, prices = zip(*sorted_data)

exportModelData(sorted_data)
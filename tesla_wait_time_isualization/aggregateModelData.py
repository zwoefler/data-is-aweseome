import glob
import json
import matplotlib.pyplot as plt
from datetime import datetime
import os

# Write function to get ALL data for a given Model

data_dir = "final_data"
locale = "en_US"
model = "mx"
files = f"{model}_{locale}_*json"

exportFileName = f"aggregatedData_{model}_{locale}.json"

def exportModelData(jsonData):
    with open(exportFileName, "w") as f:
        json.dump(jsonData, f)

####################################################

json_files = glob.glob(os.path.join(data_dir, files))

priceData = []

exportData= {
    model: {}
}

for file_path in json_files:
    with open(file_path, "r") as f:
        data = json.load(f)

    print("FILE:", file_path)
    trims = data["trims"]

    for trimObj in trims:
        if (trimObj["trimShorthandle"] not in exportData[model]):
            exportData[model][trimObj["trimShorthandle"]] = {
                "data": [],
                "name": trimObj["displayedName"]
            }
        price = trimObj["price"]
        date = data["date"]
        exportData[model][trimObj["trimShorthandle"]]["data"].append((date, price))


for model in exportData.keys():
    for trim, trimData in exportData[model].items():
        trimData["data"] = sorted(trimData["data"], key=lambda x: x[0])

exportModelData(exportData)
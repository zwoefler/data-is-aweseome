import glob
import json
import os

# Write function to get ALL importedJSON for a given Model

data_dir = "final_data"
filename = "en_US_*.json"


def exportModelData(jsonData):
    with open(exportFileName, "w") as f:
        json.dump(jsonData, f)

####################################################

json_files = glob.glob(os.path.join(data_dir, filename))
locale = json_files[0][11:16]
exportFileName = f"aggregatedData_{locale}_model_data.json"

priceData = []

exportData= {}

for file_path in json_files:
    with open(file_path, "r") as f:
        importedJSON = json.load(f)

    print("FILE:", file_path)
    trims = importedJSON["trims"]
    model = importedJSON["model"]

    if (model not in exportData):
        exportData[model] = {}

    for trimObj in trims:
        if (trimObj["trimShorthandle"] not in exportData[model]):
            exportData[model][trimObj["trimShorthandle"]] = {
                "data": [],
                "name": trimObj["displayedName"]
            }
        price = trimObj["price"]
        date = importedJSON["date"]
        exportData[model][trimObj["trimShorthandle"]]["data"].append((date, price))


for model in exportData.keys():
    for trim, trimData in exportData[model].items():
        trimData["data"] = sorted(trimData["data"], key=lambda x: x[0])

exportModelData(exportData)
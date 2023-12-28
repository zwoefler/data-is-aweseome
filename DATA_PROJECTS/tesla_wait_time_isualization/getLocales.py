import json
import os

data_folder = "raw_json"
importFileName = "raw_m3_en_US_01022023_143828.json"

modelFile = os.path.join(data_folder, importFileName)

model = importFileName[4:6]
locale = importFileName[7:12]
date = importFileName[13:-5]

# Import JSON
with open(modelFile, "r") as f:
    data = json.load(f)

availableLocales = data[1]["App"]["availableLocales"]

exportFileName = f"locales_{importFileName[4:]}"

# Export Locales to JSON
with open(exportFileName, "w") as f:
    json.dump(availableLocales, f)

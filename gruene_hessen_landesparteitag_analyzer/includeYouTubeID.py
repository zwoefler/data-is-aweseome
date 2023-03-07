import os
import json
import sys
from unidecode import unidecode
# Iterate info objects in given file

# Get YouTTube ID for the given file

def createExportName(info):
    """Returns the export name based on speaker name"""
    export_name = unidecode(info["name"]).strip().lower().replace(" ", "_")
    if info["reminder"]:
        return "reminder_" + export_name

    return export_name


folder = "speeches/"
with open(sys.argv[1], "r") as f:
    speech_info_list = json.load(f)

youtube_id = speech_info_list[0]["youtube_id"]

for info in speech_info_list:
    print("")
    if "youtube_id" in info:
        print("YOUTUBE")
        continue
    export_name = createExportName(info)
    jsonFile = os.path.join(folder, export_name + ".json")
    print(jsonFile)
    try:
        with open(jsonFile, "r") as f:
            speech_json = json.load(f)
    except FileNotFoundError:
        print("FIle:", jsonFile, "not found!")
        continue
    if "youtube_id" in speech_json:
        continue
    speech_json["youtube_id"] = youtube_id
    with open(jsonFile, "w") as f:
        json.dump(speech_json, f)




import json
import os
from datetime import datetime


def exportJSONToFile(filename, data):
    """Exports a json object to a given filename"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def list_files(folder_path):
    files = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            files.append(file)
    return files


def import_html_file(file_path):
    try:
        with open(file_path, 'r') as file:
            html_contents = file.read()
        return html_contents
    except FileNotFoundError:
        print(f'File not found: {file_path}')


def extractJSONFromHTML(archiveHTML):
    endSearchString = "if (typeof window.tesla.env === 'string')"
    beginningSearchString = "window.tesla = "

    begin = archiveHTML.find(beginningSearchString) + len(beginningSearchString)
    end = archiveHTML.find(endSearchString)

    strippedArchiveHTML = archiveHTML[begin:end].strip()
    modelJSON = json.loads(strippedArchiveHTML.rstrip(";"))
    modelJSON["DSServices"] = json.loads(modelJSON["DSServices"])

    return [modelJSON]


def exportRawJSONData(modelJSON):
    # Extract Locale from modelJSON
    if(len(modelJSON) > 1):
        locale = modelJSON[1]["App"]["locale"]
    else:
        locale = modelJSON[0]["App"]["locale"]

    model = modelJSON[0]["DSServices"]["KeyManager"]["keys"]["Lexicon"][0]["query"]["model"]

    # Datetime Object to
    download_date = modelJSON[0]["DSServices"]["date"]
    date = datetime.utcfromtimestamp(download_date / 1000).strftime('%d%m%Y_%H%M%S')

    # Build export filename
    exportID = f"{model}_{locale}_{date}"
    export_filename = "raw_" + exportID + '.json'
    export_path = os.path.join("raw_json", export_filename)

    # Export JSON file to given filename
    exportJSONToFile(export_path, modelJSON)


def exportRawJSON(file, data_dir):
    print("EXPORTING", file)

    file_path = os.path.join(raw_data_dir, file)
    html = import_html_file(file_path)
    modelJSON = extractJSONFromHTML(html)
    exportRawJSONData(modelJSON)

    print("SUCCESSFULLY EXPORTED:", file, "\n")


raw_data_dir = "raw_html"
raw_files = list_files(raw_data_dir)
for file in raw_files[:1]:
    exportRawJSON(file, raw_data_dir)

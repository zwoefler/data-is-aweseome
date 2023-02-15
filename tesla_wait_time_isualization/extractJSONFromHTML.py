import json
import os
from datetime import datetime
import bs4
from bs4 import BeautifulSoup
import re
from subprocess import check_output


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


def import_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()

    except FileNotFoundError:
        print(f'File not found: {file_path}')


def extractNewDataModel(html):
    soup = bs4.BeautifulSoup(html)
    # Find dataJson variable in script tag of html file
    script = soup.find('script', text=re.compile(r'dataJson'))

    # Extract two json variables
    matches = re.finditer(r'const\s*\w*\s*=\s*\{.+?\};', script.text, re.DOTALL)
    dict_matches = [re.sub(r'const\s*\w*\s*=\s*', '', match.group(0)).rstrip(";") for match in matches]
    concat_dicts = ",".join(dict_matches)

    # Make Javascript String to extract json Objects
    js_export_json_string = 'const teslaData = [' + concat_dicts + '];\nprocess.stdout.write(JSON.stringify(teslaData));'

    with open('temp.js', 'w') as f:
        f.write(js_export_json_string)

    modelData = json.loads(check_output(['node','temp.js']).decode())
    os.remove("temp.js")

    return modelData


def extractJSONFromHTML(archiveHTML):
    # Old Tesla Data
    beginningSearchString = "window.tesla = "
    endSearchString = "if (typeof"

    if (html.find("dataJson = ") > 0):
        print("New version of Tesla Data")
        modelJSON = extractNewDataModel(archiveHTML)
        return modelJSON

    begin = archiveHTML.find(beginningSearchString)
    end = archiveHTML.find(endSearchString)

    if (begin < 0 or end < 0):
        return []

    begin += len(beginningSearchString)

    strippedArchiveHTML = archiveHTML[begin:end].strip()
    modelJSON = json.loads(strippedArchiveHTML.rstrip(";"))
    modelJSON["DSServices"] = json.loads(modelJSON["DSServices"])

    return [modelJSON]


def exportRawJSONData(modelJSON):
    # Extract Locale from modelJSON
    export_filename = file[5:-5] + ".json"
    export_path = os.path.join("raw_json", export_filename)

    # Export JSON file to given filename
    exportJSONToFile(export_path, modelJSON)


def getLexicon(modelJSON):
    """Returns the Lxicon for given modelJSON"""
    lexiconKey = modelJSON[0]["DSServices"]["KeyManager"]["keys"]["Lexicon"][0]["key"]
    return modelJSON[0]["DSServices"][lexiconKey]


def getMetaData(modelJSON):
    lexicon = getLexicon(modelJSON)
    meta = lexicon["metadata"]
    if len(modelJSON) > 1:
        # New Format Metadata
        metaData = {
            "country": modelJSON[1]["App"]["uiCountry"],
            "currency": meta["currency_code"],
            "symbol": meta["currency_symbol"],
            "range_units": meta["specs"]["data"][0]["meta"]["specs"]["range"]["units"],
            "range_source": meta["specs"]["data"][0]["meta"]["specs"]["range"]["source"]
        }
    else:
        # Old Format Metadata
        for group in lexicon["groups"]:
            if group["code"] == "BATTERY_AND_DRIVE":
                range_source = group["extra_copy"][3]["content"]


        metaData = {
            "country": modelJSON[0]["App"]["uiCountry"],
            "currency": meta["currency_code"],
            "symbol": meta["currency_symbol"],
            "range_units": meta["specs"]["refs"]["distance"]["label"],
            "range_source": range_source
        }

    return metaData


def getModelData(modelJSON):
    modelData = {
        "model": modelJSON[0]["DSServices"]["KeyManager"]["keys"]["Lexicon"][0]["query"]["model"],
        "date": modelJSON[0]["DSServices"]["date"],
        "meta": getMetaData(modelJSON),
        #"trims": allTrimsInfo(modelJSON),
        #"options": getPriceOptions(modelJSON)
    }
    return modelData


raw_data_dir = "raw_html"
raw_json_dir = "raw_json"

# Only extract data from HTMl files for which their corresponding JSON file is missing!
html_files = list_files(raw_data_dir)
json_files = list_files(raw_json_dir)

json_files_set = set()
for filename in json_files:
    json_files_set.add(filename)

raw_files = []
for html_file in html_files:
    if html_file[-36:-5] + ".json" not in json_files_set:
        raw_files.append(html_file)


for file in raw_files:
    print("Extracting JSON from:", file)
    file_path = os.path.join(raw_data_dir, file)
    html = import_file(file_path)
    modelJSON = extractJSONFromHTML(html)
    if (len(modelJSON) < 1):
        print(file, "does not contain valid JSON!")
        continue

    print("Exporting JSON file", file)
    exportRawJSONData(modelJSON)
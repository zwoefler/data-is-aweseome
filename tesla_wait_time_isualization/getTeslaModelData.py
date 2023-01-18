import urllib.request
import bs4
from bs4 import BeautifulSoup
import re
import os
import json
from subprocess import check_output
import pandas as pd
from datetime import datetime

def timestampToHuman(date):
    return datetime.utcfromtimestamp(date / 1000).strftime('%d%m%Y_%H%M%S')

def getTimeStampFromData(modelJSON):
    date = modelJSON[0]["DSServices"]["date"]
    return date

def downloadTeslaModelPage(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    soup = bs4.BeautifulSoup(html)
    return soup

def buildIDForJSONFile(model, locale, downloadDate):
    return f"{model}_{locale}_{downloadDate}"


def getLocale(modelJSON):
    return modelJSON[1]["App"]["locale"]


def getDownloadDate(jsonData):
    return timestampToHuman(getTimeStampFromData(jsonData))


def getDate(modelJSON):
    """Returns the time of data download as Milliseconds EPOCH"""
    return modelJSON[0]["DSServices"]["date"]


def getModel(modelJSON):
    """Returns the Model Name as shortcut like my for ModelY or m3 for Model3"""
    return modelJSON[0]["DSServices"]["KeyManager"]["keys"]["Lexicon"][0]["query"]["model"]


def getLexicon(modelJSON):
    """Returns the Lxicon for given modelJSON"""
    lexiconKey = modelJSON[0]["DSServices"]["KeyManager"]["keys"]["Lexicon"][0]["key"]
    return modelJSON[0]["DSServices"][lexiconKey]


def getExportData(jsonData):
    return {
        "model": getModel(jsonData),
        "locale": getLocale(jsonData),
        "downloadDate": getDownloadDate(jsonData)
    }


def deleteTempJavascriptFile(tempFile):
    os.remove(tempFile)


def getTeslaModelJSON(soup_page):
    script = soup_page.find('script', text=re.compile(r'dataJson'))
    matches = re.finditer(r'const\s*\w*\s*=\s*\{.+?\};', script.text, re.DOTALL)
    dict_matches = [re.sub(r'const\s*\w*\s*=\s*', '', match.group(0)).rstrip(";") for match in matches]
    concat_dicts = ",".join(dict_matches)
    js_export_json_string = 'const teslaData = [' + concat_dicts + '];\nprocess.stdout.write(JSON.stringify(teslaData));'
    with open('temp.js', 'w') as f:
        f.write(js_export_json_string)
    modelData = json.loads(check_output(['node','temp.js']).decode())
    deleteTempJavascriptFile("temp.js")

    exportData = getExportData(modelData)
    exportID = buildIDForJSONFile(exportData["model"], exportData["locale"], exportData["downloadDate"])
    exportFilename = "raw_" + exportID + '.json'

    exportJSONToFile(data_dir + exportFilename, modelData)
    return exportFilename


def exportJSONToFile(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def importModelJSON(json_file):
    with open(json_file, 'r') as f:
        return f.read()


def dateStringToMonth(datestring, date_format='%m/%d/%Y %H:%M:%S'):
    date = datetime.strptime(datestring, date_format)
    year = date.year
    month_string = date.strftime('%B')
    return month_string, year


def estDeliveryString(start, end, date_format='%m/%d/%Y %H:%M:%S'):
    """Takes the start and end date in the format '%m/%d/%Y %H:%M:%S' and returns the string in the formart
    Month - Month YEAR.
    If the Years are different, it will return
    Month YEAR - Month YEAR"""
    start = dateStringToMonth(start)
    end = dateStringToMonth(end)
    if start[1] == end[1]:
        date_string = f'{start[0]} - {end[0]} {end[1]}'
    else:
        date_string = f'{start[0]} {start[1]} - {end[0]} {end[1]}'

    return date_string


def getDeliveryEstForTrim(trim, modelJSON):
    eD = eddDataForModel(trim, modelJSON)
    deliveryEstForTrim = deliveryEstimateForModel(eD)
    eddString = estDeliveryString(deliveryEstForTrim["start"], deliveryEstForTrim["end"])

    deliveryEstimate = {
        "start": deliveryEstForTrim["start"],
        "end": deliveryEstForTrim["end"],
        "text": eddString
    }

    return deliveryEstimate


def getAllTrims(modelJSON):
    trims = modelJSON[0]["DSServices"]["Lexicon.my"]["sku"]["trims"]
    return trims

def getConfigurableTrims(modelJSON):
    """Scrapes the JSON scraped from the Tesla webpage and returns a dictionary of all configurable trims with corresponding options"""
    all_trims = getAllTrims(modelJSON)
    configurable_trims = {k: v for k, v in all_trims.items() if "configurator" in v}
    return configurable_trims


def explainConfigurableTrims(configurable_trims):
    """Takes the trims dictionary and returns a dictionary with the shortcut and the corresponding name"""
    new_dict = {}
    for key, value in configurable_trims.items():
        new_dict[key] = value["variant"]["name"]

    return new_dict

def explainTrim(trim):
    """Takes the shortcut of one trim and returns the name/description of the trim"""
    try:
        return configurable_trims[trim]["variant"]["name"]
    except:
        print("There is no trim available with the shortcut " + trim)


def priceForOption(option, modelJSON):
    """Receives the option as '$MTY05' and the modelJSON and returns the price for that option"""
    lexicon = getLexicon(modelJSON)

    price = lexicon["options"][option]["price"]
    for jsonObj in lexicon["options"][option]["pricing"]:
        if jsonObj["type"] == "base_plus_trim":
            price = jsonObj["value"]

    return price


def nameForOption(option, modelJSON):
    """Receives the option in '$MTY05' format and the modelJSON, return the name of the option"""
    lexicon = getLexicon(modelJSON)

    name = lexicon["options"][option]["long_name"]
    return name


def eddDataForModel(model, modelJSON):
    """Returns the estimated Delivery Data for given model
    Inputs:
    - model = '$MTY05'
    - modelJSON = the Model JSON object

    Returns:
    List with estDeliveryData for given model
    """

    edd = modelJSON[1]["eddData"]
    eddForModel = []

    for option in edd:
        if model in option["options"]:
            eddForModel.append(option)

    return eddForModel


def getValidEddData(eddDataForModel):
    """Throws away the inStart and inEnd dates that have type None.
    Returns a list of valid est Delivery Data"""

    validEddData = []
    for key, value in enumerate(eddDataForModel):
        if value["inStart"] is not None and value["inEnd"] is not None:
            validEddData.append(value)

    return validEddData


def deliveryEstimateForModel(eddDataForModel):
    """takes the estDelivery Data  as a list of objects
    and returns the start, end and outliers as dict"""
    validEddData = getValidEddData(eddDataForModel)
    start = eddDataForModel[0]["inStart"]
    end = eddDataForModel[0]["inEnd"]

    deliveryEst = {
        "start": start,
        "end": end,
        "outliers": []
    }

    for obj in validEddData:
        if obj["inStart"] != start and obj["inEnd"] != end:
            deliveryEst["outliers"].append(obj)
    return deliveryEst


def allTrimsInfo(modelJSON):
    trims = {}
    configurable_trims = getConfigurableTrims(modelJSON)
    trimsList = list(configurable_trims.keys())
    for trim in trimsList:
        trimName, trimData = getTrimInfo(trim, modelJSON)
        trims[trimName] = trimData

    return trims


def getMetaData(modelJSON):
    lexicon = getLexicon(modelJSON)
    meta = lexicon["metadata"]
    metaData = {
        "country": modelJSON[1]["App"]["uiCountry"],
        "currency": meta["currency_code"],
        "symbol": meta["currency_symbol"],
        "range_units": meta["specs"]["data"][0]["meta"]["specs"]["range"]["units"],
        "range_source": meta["specs"]["data"][0]["meta"]["specs"]["range"]["source"]
    }
    return metaData


def getTrimInfo(trim, modelJSON):
    """Returns the Trim Info for given trim
    Input:
    - trim = '$MTY05'
    - modelJSON = The model JSON

    Returns:
    - trimName as String
    - trimDict as dict with price, delivery est."""

    trimName = nameForOption(trim, modelJSON)
    trimDict = {
        "price": priceForOption(trim, modelJSON),
        "deliveryEstimate": getDeliveryEstForTrim(trim, modelJSON),
        "specs": getSpecsForTrim(trim, modelJSON),
        "standard_config":  getStandardConfiguration(trim, modelJSON),
        "options": getAvailableOptions(trim, modelJSON)
    }


    return trimName, trimDict


def getModelData(modelJSON):
    modelData = {
        "model": getModel(modelJSON),
        "date": getDate(modelJSON),
        "meta": getMetaData(modelJSON),
        "trim": allTrimsInfo(modelJSON),
        "options": getPriceOptions(modelJSON)
    }
    return modelData

# Spec for Trim
def getSpecsForTrim(trim, modelJSON):
    """Takes the trim and modelJSON and returns a list
    with the specs:
    - range
    - max-speed
    - acceleartion
    """
    lexicon = getLexicon(modelJSON)
    trimSpecs = lexicon["metadata"]["specs"]["data"][0]["options"][trim]
    specs = {
        "range": trimSpecs["range"],
        "topspeed": trimSpecs["topspeed"],
        "acceleration": trimSpecs["acceleration"],
        "overrides": specChangingOptions(trimSpecs)
    }

    return specs


def specChangingOptions(specs):
    overrides = specs["overrides"]
    for override in overrides:
        for key, option in enumerate(override['selected_by']['and']):
            if option.startswith('$'):
                override['selected_by']['and'][key] = getOptionPriceAndName(option, modelJSON)
    return overrides


def optionsCodeWithExplanation(modelJSON):
    options = modelJSON[0]["DSServices"]["Lexicon.my"]["options"]
    new_dict = {}
    for key, value in options.items():
        new_dict[key] = value["name"]

    return new_dict


def getOptionPriceAndName(option, modelJSON):
    """For a given option returns the dicitonary
    {
        shortcut: $MTY05
        name: "White Interior",
        price: 1200,
    }
    """
    lexicon = getLexicon(modelJSON)
    try:
        price = lexicon["options"][option]["price"]
        for jsonObj in lexicon["options"][option]["pricing"]:
            if jsonObj["type"] == "base_plus_trim":
                price = jsonObj["value"]
    except KeyError:
        price = None

    try:
        name = lexicon["options"][option]["name"]
    except KeyError:
        name = None

    optionData = {
        "shortcut": option,
        "name": name,
        "price": price,
    }


    return optionData


# All available options
def getPriceOptions(modelJSON):
    """Takes the options object/dict as input and return a dictionary with the options and their correpsonding pricing"""
    lexicon = getLexicon(modelJSON)
    new_dict = {}
    important_values = ["name", "price", "pricing"]
    result = {key: {k: v for k, v in value.items() if k in important_values} for key, value in lexicon["options"].items()}
    return result


def getStandardConfiguration(trim, modelJSON):
    """For the gibven trim returns the base_options list with dicts for the option, price and shortcut"""
    standardConfig = []
    lexicon = getLexicon(modelJSON)
    base_options = lexicon["sku"]["trims"][trim]["configurator"][0]["base_options"]
    for option in base_options:
        standardConfig.append(getOptionPriceAndName(option, modelJSON))
    return standardConfig


def getAvailableOptions(trim, modelJSON):
    """Returns a dict with the available options with their names, prices and shortcuts"""
    availableOptions = []
    lexicon = getLexicon(modelJSON)

    combinations = lexicon["sku"]["trims"][trim]["configurator"][0]["combinations"]
    for combi in combinations:
        for option in combi:
            availableOptions.append(getOptionPriceAndName(option, modelJSON))

    return availableOptions
getModelData

data_dir = "data/"
url = "https://www.tesla.com/modely/design#overview"
model_page = downloadTeslaModelPage(url)
filename = getTeslaModelJSON(model_page)
modelJSON = json.loads(importModelJSON(data_dir + filename))

availableLocales = modelJSON[1]["App"]["availableLocales"]
modelData = getModelData(modelJSON)
exportJSONToFile(data_dir + filename[4:], modelData)

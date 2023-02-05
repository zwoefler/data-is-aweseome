import os
import json

### Helper Functions

def getDate(modelJSON):
    """Returns the time of data download as Milliseconds EPOCH"""
    return modelJSON[0]["DSServices"]["date"]


def getModel(modelJSON):
    """Returns the Model Name as shortcut like my for ModelY or m3 for Model3"""
    modelShort = modelJSON[0]["DSServices"]["KeyManager"]["keys"]["Lexicon"][0]["query"]["model"]
    try:
        mJSON = modelJSON[1]
    except IndexError:
        mJSON = modelJSON[0]

    mJSON["i18n"]
    if(isinstance(mJSON["i18n"], str)):
        mJSON["i18n"] = json.loads(mJSON["i18n"])

    modelString = mJSON["i18n"]["find_my_tesla"]["strings"]["Models"][modelShort]["short_name"]


    return modelShort, modelString


def getLexicon(modelJSON):
    """Returns the Lxicon for given modelJSON"""
    lexiconKey = modelJSON[0]["DSServices"]["KeyManager"]["keys"]["Lexicon"][0]["key"]
    return modelJSON[0]["DSServices"][lexiconKey]

# IMPORT / EXPORT
def exportJSONToFile(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def importModelJSON(json_file):
    with open(json_file, 'r') as f:
        return f.read()


def getVehiclePrice(trim, modelJSON):
    lexicon = getLexicon(modelJSON)

    extra_content = lexicon["options"][trim]["extra_content"]
    price = None

    try:
        for item in extra_content:
            if(item["type"] == "price_indicator_override"):
                price = item["content"][0]["content"]
    except:
        price = None
        print("Couln't get vehicle price via extra_content")

    return price


def getCountry(modelJSON):
    """Returns the country code from the modelJSON"""
    try:
        country = modelJSON[1]["App"]["uiCountry"]
    except IndexError:
        country = modelJSON[0]["App"]["uiCountry"]
    except:
        print("ERROR: Getting Country")

    return country


def getMetaData(modelJSON):
    lexicon = getLexicon(modelJSON)
    meta = lexicon["metadata"]

    try:
        meta_specs = meta["specs"]["data"][0]["meta"]["specs"]
    except (KeyError, IndexError) as e:
        meta_specs = {
            "range": {
                "units": None,
                "source": None
            }
        }
        print("getMetaData Error", e)

    metaData = {
        "country": getCountry(modelJSON),
        "currency": meta["currency_code"],
        "symbol": meta["currency_symbol"],
        "range_units": meta_specs["range"]["units"],
        "range_source": meta_specs["range"]["source"]
    }
    return metaData


def getConfiguratorTrims(modelJSON):
    configurableTrims = []
    lexicon = getLexicon(modelJSON)
    for group in lexicon["groups"]:
        if (group["code"] == "TRIM" and group["context"] == "configurator"):
            configurableTrims = group["options"]

    return configurableTrims


def getModelData(modelJSON):

    lexicon = getLexicon(modelJSON)
    modelShort, _ = getModel(modelJSON)

    trims = []
    for trim in configurableTrims:
        print(trim)
        trim_data = lexicon["metadata"]["specs"]["data"][0]["options"][trim]
        trim_data["price"] = getVehiclePrice(trim, modelJSON)
        trim_data["trimShorthandle"] = trim

        trims.append(trim_data)


    modelData = {
        "model": modelShort,
        "date": getDate(modelJSON),
        "meta": getMetaData(modelJSON),
        "trims": trims,
        # "options": getPriceOptions(modelJSON)
    }
    return modelData


data_dir = "final_data"
source_dir = "raw_json"

for file_name in os.listdir(source_dir):
    # Importing JSON file
    importPath = os.path.join(source_dir, file_name)
    importedJSON = importModelJSON(importPath)
    modelJSON = json.loads(importedJSON)

    print("Model data for file:", file_name)
    configurableTrims = getConfiguratorTrims(modelJSON)
    modelData = getModelData(modelJSON)
    exportJSONToFile(os.path.join(data_dir, file_name[4:]), modelData)



# Available Trims for "old" raw_ms_en_US_16102020_064817.json
# DSServices.Lexicon.groups.
# (context == configurator && code == "TRIM"):
#   configurableTrims = groups[XX]["options"]


# Certain Prices are not int the price entry!
# But
# options.$MT10A.extra_content.[x].type == "price_indicator_override"
# extra_content.1 or 2.content.0.content




def getTrimOptions(modelJSON):

    return trim_metadata

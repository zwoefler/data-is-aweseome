import os
import json

### Helper Functions

def getDate(modelJSON):
    """Returns the time of data download as Milliseconds EPOCH"""
    return modelJSON[0]["DSServices"]["date"]


def getModel(modelJSON):
    """
    Returns the Model Name as shortcut like
    - my for ModelY
    - m3 for Model3
    """
    lexicon = getLexicon(modelJSON)
    modelShort = modelJSON[0]["DSServices"]["KeyManager"]["keys"]["Lexicon"][0]["query"]["model"]
    try:
        mJSON = modelJSON[1]
    except IndexError:
        mJSON = modelJSON[0]

    if(isinstance(mJSON["i18n"], str)):
        mJSON["i18n"] = json.loads(mJSON["i18n"])

    try:
        modelString = mJSON["i18n"]["find_my_tesla"]["strings"]["Models"][modelShort]["short_name"]
    except KeyError:
        for group in lexicon["groups"]:
            if (group["code"] == "MODEL" and group["context"] == "default"):
                trim = group["default_options"][0]

        modelString = lexicon["options"][trim]["name"]

    # For my 22042019 en_US there is no "Model Y" in i18n...
    # But there is one in lexicon.options.$MDLY.name

    # Get it from groups where code == "MODEL" and context == "default"
    # groups.X.options.0
    # Look up $MDLY in lexicon.options.$MDLY

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

    price = 0
    try:
        print("TRY PRICE via extra_content")
        for item in extra_content:
            # Alternative would be "price_indicator_override"
            if(item["type"] == "option_price_override"):
                price = item["content"][0]["content"]
            else:
                price = None

        if(price is None):
            print("pricing Object")
            for jsonObj in lexicon["options"][trim]["pricing"]:
                if jsonObj["type"] == "base_plus_trim":
                    price = jsonObj["value"]
    except:
        print("ERROR getting price for:", trim)


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

    try:
        currency = meta["currency_code"]
        symbol = meta["currency_symbol"]
    except KeyError:
        currency = None
        symbol = None

    metaData = {
        "country": getCountry(modelJSON),
        "currency": currency,
        "symbol": symbol,
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


def getBatteryContentList(modelJSON):
    lexicon = getLexicon(modelJSON)

    battery_content_list = []
    for group in lexicon["groups"]:
        if (group["code"] == "BATTERY_AND_DRIVE" and group["context"] == "configurator"):
            for content in group["extra_content"]:
                if (content["type"] == "performance_specs"):
                    battery_content_list = content

    return battery_content_list


def getRangeViaGroups(trim, battery_content_list):
    trim_metadata = {}
    for item in battery_content_list["content"]:
        if (item["selected_by"]["and"][0] == trim):
            trim_metadata = item

    return trim_metadata


def getDisplayName(trim):
    for item in lexicon["options"][trim]["extra_copy"]:
        if(item["type"] == "name"):
            return item["content"]


def getModelData(modelJSON):

    lexicon = getLexicon(modelJSON)
    modelShort, _ = getModel(modelJSON)

    trims = []
    battery_content_list = getBatteryContentList(modelJSON)
    for trim in configurableTrims:
        print(trim)
        try:
            trim_data = lexicon["metadata"]["specs"]["data"][0]["options"][trim]
        except (KeyError, IndexError):
            trim_data = getRangeViaGroups(trim, battery_content_list)

        trim_data["price"] = getVehiclePrice(trim, modelJSON)
        trim_data["displayedName"] = getDisplayName(trim)
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
    lexicon = getLexicon(modelJSON)

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

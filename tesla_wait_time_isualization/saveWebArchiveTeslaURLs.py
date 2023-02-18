import os
import json
import waybackHelper

def file_exists (file_path):
    return os.path.exists(file_path)


def exportJSONToFile(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def getModelLinks(locale, model, url):
    print("")
    print("Historic URLs for: ", url)
    waybackJSON = waybackHelper.getAvailableWebArchive(url)

    print("Retunring valid Model Archive links")
    waybackLinkList = waybackHelper.getValidModelArchiveLinks(waybackJSON)

    export_path = os.path.join(data_dir, f"{model}_{locale}_LinkList.json")
    print("Exporting to: ", export_path)
    exportJSONToFile(export_path, waybackLinkList)
    return

models = ["models", "model3", "modelx", "modely"]
locales = ["zh_CN", "en_US", "no_NO", "de_DE"]
data_dir = "wayback_LinkLists"

for locale in locales:
    for model in models:
        print("locale:", locale)
        if locale == "zh_CN":
            url = f"tesla.cn/{model}/design"
        elif locale == "en_US":
            url = f"tesla.com/{model}/design"
        else:
            url = url = f"tesla.com/{locale}/{model}/design"
        getModelLinks(locale, model, url)



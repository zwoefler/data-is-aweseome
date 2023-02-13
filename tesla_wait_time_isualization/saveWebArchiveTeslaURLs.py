import os
import json
import waybackHelper

def file_exists (file_path):
    return os.path.exists(file_path)


def exportJSONToFile(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


models = ["models", "model3", "modelx", "modely"]
locales = ["en_US"]


for locale in locales:
    for model in models:
        url = f"tesla.com/{model}/design"
        print("Historic URLs for: ", url)
        waybackJSON = waybackHelper.getAvailableWebArchive(url)

        print("Retunring valid Model Archive links")
        waybackLinkList = waybackHelper.getValidModelArchiveLinks(waybackJSON)

        export_path = f"{model}_{locale}_LinkList.json"
        print("Exporting to: ", export_path)
        exportJSONToFile(export_path, waybackLinkList)



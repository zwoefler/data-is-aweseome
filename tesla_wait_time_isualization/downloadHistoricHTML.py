import waybackHelper
import json
import os
import requests

def download_html(url, locale, model, date, data_dir="raw_html"):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"Failed to download HTML file from url {url}. HTTP status code {response.status_code}")

        filename = f"{data_dir}/html_raw_{locale}_{model}_{date}.html"

        with open(filename, "w") as f:
            f.write(response.text)

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions that may occur
        print(f"An error occurred while trying to download the HTML file from url {url}: {e}")

    except ValueError as e:
        # Handle any value errors that may occur
        print(e)

    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred while trying to save the HTML file: {e}")


def exportJSONToFile(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def importJSONFile(json_file):
    with open(json_file, 'r') as f:
        return f.read()


models = ["models", "model3", "modelx", "modely"]
locales = ["en_US"]
raw_html_dir = "raw_html"
raw_json_dir = "raw_json"
data_dir = "data"

def file_exists (file_path):
    return os.path.exists(file_path)


def getModelsArchiveLinks():
    for locale in locales:
        for model in models[3:]:
            url = f"tesla.com/{model}/design"
            print(url)
            waybackJSON = waybackHelper.getAvailableWebArchive(url)
            waybackLinkList = waybackHelper.getValidModelArchiveLinks(waybackJSON)
            exportJSONToFile(f"{model}_{locale}_LinkList.json", waybackLinkList)


modelLinkFile = "modely_en_US_LinkList.json"
if not file_exists(modelLinkFile):
    getModelsArchiveLinks()
else:
    waybackLinkList = json.loads(importJSONFile(modelLinkFile))


locale = "en_US"
model = "modely"
for item in waybackLinkList:
    downloadLink = waybackHelper.buildDownloadLink(item[1], item[2])
    download_html(downloadLink, locale, model, item[1])

import waybackHelper
import json
import os
import requests
from sys import argv
from compareToAvailableData import get_undownloaded_wayback_URLs

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


def file_exists (file_path):
    return os.path.exists(file_path)


def getModelAndLocale(modelLinkFile):
    """Extracts model and locale from fileName"""
    splitFileName = modelLinkFile.split('_')
    model = splitFileName[0]
    locale = splitFileName[1] + '_' + splitFileName[2]
    return model, locale


raw_html_dir = "raw_html"
raw_json_dir = "raw_json"
data_dir = "data"
script, modelLinkFile = argv

print("Receiving Download Links for:", modelLinkFile)

if file_exists(modelLinkFile):

    missing_wayback_URLs = get_undownloaded_wayback_URLs(modelLinkFile)
    print(missing_wayback_URLs)

    model, locale = getModelAndLocale(modelLinkFile)

    for item in missing_wayback_URLs:
        date = item[1]
        modelURL = item[2]
        print("Building Downloadlink for item dated:", date)
        downloadLink = waybackHelper.buildDownloadLink(date, modelURL)
        print("Downloading HTML for item date:", date)
        download_html(downloadLink, locale, model, date)

else:
    print("Could not find your file:", modelLinkFile)



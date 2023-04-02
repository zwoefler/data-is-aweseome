import requests
from bs4 import BeautifulSoup
import json
import os

def export_to_JSON(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f)


def load_json_data(link_json_file):
    with open(link_json_file, "r") as f:
        return json.load(f)


def download_kmk_webpage(url):
    if("kmk.org" not in url):
        raise Exception("Your URL needs to be of the domain kmk.org")

    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def get_zip_links(webpage):
    soup = BeautifulSoup(webpage, 'html.parser')
    links = soup.find_all('a')
    zip_links = []

    for link in links:
        url = link.get("href")
        if url.endswith('.zip'):
            zip_links.append(url)

    return zip_links


zip_links_file = "zip_links.json"
url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"
archive_url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten/archiv-abiturnoten.html"

def main():
    if os.path.isfile(zip_links_file):
        zip_links = load_json_data(zip_links_file)
        return zip_links
    else:
        webpage = download_kmk_webpage(url)
        zip_links = get_zip_links(webpage)
        export_to_JSON(zip_links_file, zip_links)
        return zip_links



if __name__ == '__main__':
    main()
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


def is_zip_link(download_url):
    response = requests.get(download_url, stream=True)
    content_type = response.headers.get('content-type')
    if content_type == 'application/zip':
        return True
    return False


def get_zip_links(url):
    webpage = download_kmk_webpage(url)
    soup = BeautifulSoup(webpage, 'html.parser')
    links = soup.find_all('a')
    zip_links = []

    domain = "https://www.kmk.org"

    for link in links:
        url = link.get("href")
        if url.endswith('.zip'):
            if "kmk.org" in url:
                continue
            else:
                zip_link = domain + url
            is_zip_link(zip_link)
            zip_links.append(zip_link)

    return zip_links


zip_links_file = "zip_links.json"
url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"
archive_url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten/archiv-abiturnoten.html"
urls = [url, archive_url]

def main():
    if os.path.isfile(zip_links_file):
        zip_links = load_json_data(zip_links_file)
        return zip_links
    else:
        zip_links = []
        for url in urls:
            links = get_zip_links(url)
            zip_links.extend(links)

        export_to_JSON(zip_links_file, zip_links)
        return zip_links


if __name__ == '__main__':
    main()
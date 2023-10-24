from bs4 import BeautifulSoup
import time
import datetime
import requests
import json

def download_parkhouse_html(parkhouse_webpage_url):
    r = requests.get(parkhouse_webpage_url)
    return r.text


def extract_parkhouse_data_from_html_tag(tag):
    soup = BeautifulSoup(tag, 'html.parser')

    free_spaces = int(soup.find('span', {"class": 'free'}).text.split(":")[1].strip())
    max_spaces = int(soup.find('span', {"class": 'max'}).text.split(":")[1].strip())

    return_object = {
        "name": soup.find('span', {"class": 'slot-name'}).text,
        "free_spaces": free_spaces,
        "occupied_spaces": max_spaces - free_spaces,
        "max_spaces": max_spaces
        }

    return return_object


def get_text_from_html_tag(html_string, search_object):
    """A function that takes an HTML string and a search object and returns the resulting HTML string"""
    soup = BeautifulSoup(html_string, 'html.parser')
    html_text = soup.find(search_object["html_element"], {
        search_object["html_attribute"]: search_object["attribute_value"]
    })
    if html_text == None:
        raise TypeError(f"No {search_object['html_element']} element with {search_object['html_attribute']} '{search_object['attribute_value']}' found")

    html_string = str(html_text)

    return html_string


def extract_parkhouse_data(html):
    soup = BeautifulSoup(html, "html.parser")
    soup_info_panels = soup.find_all("div", {"class": "info-panel"})
    parkhouses = []
    for panel in soup_info_panels:
        parkhouses.append(extract_parkhouse_data_from_html_tag(str(panel)))

    return parkhouses


def get_last_updated_time(html):
    soup = BeautifulSoup(html, "html.parser")
    find_result = soup.find("small", { "class": "last-update" }).text
    last_updated = find_result.split(":", 1)[1].strip()
    time = "".join(last_updated.split()[0].split(":"))
    date = "".join(last_updated.split()[-1].split("."))

    return f"{date}-{time}"


def scrape_webpage(html):
    return {
        "timestamp": get_last_updated_time(html),
        "parkhouses": extract_parkhouse_data(html)
    }


def main():
    url = "https://www.giessen.de/Umwelt_und_Verkehr/Parken/"

    html = download_parkhouse_html(url)
    scraped_parkleitsystem = scrape_webpage(html)
    print(json.dumps(scraped_parkleitsystem, indent=2))

if __name__ == "__main__":
    main()
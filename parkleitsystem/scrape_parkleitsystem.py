import requests
from bs4 import BeautifulSoup
import datetime


def get_parkhouse_info(tag):
    parkhouse_info = {
        "parkhouse" : tag.find('span', {"class": 'slot-name'}).text,
        "free_spaces" : tag.find('span', {"class": 'free'}).text.split(":")[1].strip(),
        "max_spaces" : tag.find('span', {"class": 'max'}).text.split(":")[1].strip()
    }

    return parkhouse_info


url = "https://www.giessen.de/Umwelt_und_Verkehr/Parken/"
timestamp = f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S%z}'

resp = requests.get(url)
html_doc = resp.text
soup = BeautifulSoup(html_doc, 'html.parser')
parking_info_panels = soup.find_all("div", {"class": "info-panel"})

parkhouses_list = []
for parkhouse in parking_info_panels:
    parkhouses_list.append(get_parkhouse_info(parkhouse))

parkhouses_information = {
    "timestamp": timestamp,
    "parkhouse_info": parkhouses_list
}








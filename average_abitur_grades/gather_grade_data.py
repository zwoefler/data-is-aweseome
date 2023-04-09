from bs4 import BeautifulSoup
import requests
import os
import json
import pandas as pd

url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"
domain = "https://www.kmk.org"

# 1. Download HTML
def get_xlsx_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.endswith(".xlsx"):
            download_link = domain + href
            links.append(download_link)
    return links


def get_year_of_grade_report(excel_file):
    noten_sheet = pd.read_excel(excel_file, sheet_name="Noten")
    title = noten_sheet.iloc[1,0]
    year = int(title.split(' ')[-1])
    return year


def return_excel_as_JSON(excel_file):
    noten_sheet = pd.read_excel(excel_file, sheet_name="Noten")
    noten_sheet = noten_sheet.dropna()
    noten_sheet.columns = noten_sheet.iloc[0]
    noten_sheet = noten_sheet.drop(3)

    index = noten_sheet["Land"].tolist()
    states = noten_sheet.iloc[:,1:].to_dict(orient='list')

    for k,v, in states.items():
        states[k] = dict(zip(index, v))

    excel_json = {
        "year" : 2022,
        "states": states
    }

    return excel_json



# 2. Get list of excel downloadlinks from HTML
# 3. Import Excel to Pandas and return list of germany
def main():
    get_xlsx_links(url)


if __name__ == '__main__':
    main()
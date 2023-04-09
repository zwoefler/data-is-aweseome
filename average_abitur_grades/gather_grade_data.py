from bs4 import BeautifulSoup
import requests
import os
import json
import pandas as pd

url = "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html"
domain = "https://www.kmk.org"

# 1. Download HTML
def return_html_from_url(url):
    response = requests.get(url)
    return response.text


def get_xlsx_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.endswith(".xlsx"):
            download_link = domain + href
            links.append(download_link)
    return links


def get_excel_file_name(excel_link):
    filename = excel_link.split('/')[-1]
    return filename


def download_excel_to_folder(excel_link, filename, folder="excel_files"):
    response = requests.get(excel_link)
    if response.status_code == 200:
        with open(os.path.join(folder, filename), 'wb') as f:
            f.write(response.content)
    else:
        print('Error downloading file')
    return


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
        "year" : get_year_of_grade_report(excel_file),
        "states": states
    }

    return excel_json

def abitur_grades_as_JSON(excel_files_list, folder="excel_files"):
    grades_json = {}
    for file in excel_files_list:
        filename = os.path.join(folder, file)
        year = get_year_of_grade_report(filename)
        excel_json = return_excel_as_JSON(filename)
        grades_json[year] = excel_json
    return grades_json


def export_garde_JSON(grade_json, filename="abitur_grades.json"):
    with open(filename, 'w') as f:
        json.dump(grade_json, f)
    return

# 3. Import Excel to Pandas and return list of germany
def main():
    html = return_html_from_url(url)
    excel_links = get_xlsx_links(html)
    for link in excel_links:
        file_name = get_excel_file_name(link)
        download_excel_to_folder(link, file_name)

    excel_files = os.listdir('excel_files/')
    grade_json = abitur_grades_as_JSON(excel_files)
    export_garde_JSON(grade_json)






if __name__ == '__main__':
    main()
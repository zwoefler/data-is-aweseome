from bs4 import BeautifulSoup
import requests
import io
import zipfile
import os
import json
import pandas as pd
import shutil

urls = [
    "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html",
    "https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten/archiv-abiturnoten.html",
]

domain = "https://www.kmk.org"
DATA_DIR = "data/"


# 1. Download HTML
def return_html_from_url(url):
    response = requests.get(url)
    return response.text


def get_xlsx_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href.endswith(".xlsx") or href.endswith(".xls"):
            download_link = domain + href
            links.append(download_link)
    return links


def download_excel_files_from_zip_download(zip_link, extract_folder="extract_folder"):
    response = requests.get(zip_link)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    zip_file.extractall(extract_folder)
    zip_file.close()
    for file in os.listdir(extract_folder):
        if not file.endswith(".xls"):
            filepath = os.path.join(extract_folder, file)
            os.remove(filepath)
    extracted_excel_files = os.listdir(extract_folder)
    return extracted_excel_files


def get_excel_file_name(excel_link):
    filename = excel_link.split("/")[-1]
    return filename


def download_excel_to_folder(excel_link, filename, folder="excel_files"):
    response = requests.get(excel_link)
    if response.status_code == 200:
        with open(os.path.join(folder, filename), "wb") as f:
            f.write(response.content)
    else:
        print("Error downloading file")
    return


def return_excel_as_JSON(excel_file):
    noten_sheet = pd.read_excel(excel_file, sheet_name="Noten")
    title = noten_sheet.iloc[1, 0]
    year = int(title.split(" ")[-1])

    noten_sheet = noten_sheet.dropna()
    noten_sheet.columns = noten_sheet.iloc[0]
    noten_sheet = noten_sheet.drop(3)

    index = noten_sheet["Land"].tolist()
    states = noten_sheet.iloc[:, 1:].to_dict(orient="list")

    country_grades = noten_sheet.iloc[5:, 1:17].sum(axis=1).tolist()
    index_country_grades = index[5:]

    country_aggregated_grades_weights = [
        a * b for a, b in (zip(country_grades, index_country_grades))
    ]

    number_of_tests = noten_sheet.iloc[0, 1:].sum()
    passed = noten_sheet.iloc[1, 1:].sum()
    number_failed = noten_sheet.iloc[2, 1:].sum()
    average_grade = sum(country_aggregated_grades_weights) / passed
    percentage_failed = (number_failed / number_of_tests) * 100

    for k, v in states.items():
        states[k] = dict(zip(index, v))

    excel_json = {
        "year": year,
        "grades": dict(zip(index_country_grades, country_grades)),
        "states": states,
        "number_of_tests": number_of_tests,
        "passed": passed,
        "number_failed": number_failed,
        "average_grade": average_grade,
        "percentage_failed": percentage_failed,
    }

    return excel_json, year


def abitur_grades_as_JSON(excel_files_list, folder="excel_files"):
    grades_json = {}
    grades_json["average_grade"] = {
        "Total": [],
    }
    grades_json["years"] = []

    for file in excel_files_list:
        filename = os.path.join(folder, file)
        excel_json, year = return_excel_as_JSON(filename)

        grades_json[year] = excel_json
        grades_json["years"].append(year)

    grades_json["years"] = sorted(grades_json["years"])

    for year in grades_json["years"]:
        for state, value in grades_json[year]["states"].items():
            if isinstance(value, dict):
                if state not in grades_json["average_grade"]:
                    grades_json["average_grade"][state] = []
                grades_json["average_grade"][state].append(
                    grades_json[year]["states"][state]["Notenmittel"]
                )

        average_grade_for_year = grades_json[year]["average_grade"]
        grades_json["average_grade"]["Total"].append(average_grade_for_year)

    return grades_json


def export_garde_JSON(grade_json, filename="abitur_grades.json"):
    export_file = os.path.join(DATA_DIR, filename)
    with open(export_file, "w") as f:
        json.dump(grade_json, f)
    return


zip_download_link = (
    "https://kmk.org/fileadmin/Dateien/pdf/Statistik/Aus_Abiturnoten_2006_2013.zip"
)
exctract_folder = "excel_files"


def main():
    zip_excel_files = download_excel_files_from_zip_download(
        zip_download_link, exctract_folder
    )

    for link in urls:
        html = return_html_from_url(link)
        excel_links = get_xlsx_links(html)

        for link in excel_links:
            file_name = get_excel_file_name(link)
            download_excel_to_folder(link, file_name)

    print("Saving Excel files to excel_files/ dir")
    excel_files = os.listdir("excel_files/")
    grade_json = abitur_grades_as_JSON(excel_files)
    export_garde_JSON(grade_json)
    print("REMOVING excel_files/")
    shutil.rmtree("excel_files/")


if __name__ == "__main__":
    main()

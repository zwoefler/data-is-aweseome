import json
import requests
import os
import errors


def pull_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
    else:
        json_data = {}
    return json_data


def create_filename(folder, query_string):
    filename = os.path.join(folder, query_string)
    return filename


def create_url(search_string, base_url):
    url = os.path.join(base_url, search_string)
    return url


def write_json_data_to_file(json_data, filename):
    with open (filename, "w") as f:
        json.dump(json_data, f)


def create_query_string(intervall_query_string, date_query_string):
    search_string = intervall_query_string + "_" + str(date_query_string) + ".json"
    return search_string


def download_energy_data(url):
    return


def main():
    year_list = list(range(1990, 2023))
    domain = "https://www.energy-charts.info"
    base_url = "https://www.energy-charts.info/charts/power/data/de/"
    # /charts/power/raw_data/de/year_2010.json
    intervall_query_string = "year"
    search_string_list = []
    folder = "energy_data"

    for year in year_list:
        search_string_list.append(create_query_string(intervall_query_string, year))

    for search_string in search_string_list:
        filename = create_filename("", search_string)
        url = create_url(search_string, base_url)
        print(url)
        energy_data = pull_data_from_url(url)

        if len(energy_data) > 0:
            write_json_data_to_file(energy_data, filename)

if __name__ == "__main__":
    main()
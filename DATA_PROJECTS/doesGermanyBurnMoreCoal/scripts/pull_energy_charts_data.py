import json
import requests
import os


def pull_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
    else:
        json_data = {}
    return json_data


def write_json_data_to_file(folder, filename, json_data):
    if not os.path.exists(folder):
        raise FileNotFoundError(f"{folder}/ - Folder does not exist.")
    export_path = os.path.join(folder, filename)
    with open(export_path, "w") as f:
        json.dump(json_data, f)


def create_query_string(intervall_query_string, date_query_string):
    search_string = intervall_query_string + "_" + str(date_query_string) + ".json"
    return search_string


def read_search_urls_list_from_file(search_string_file):
    with open(search_string_file, "r") as f:
        search_urls = json.load(f)

    return search_urls


def create_export_filename(url):
    split_url = url.split("/")
    export_filename = split_url[5] + "_" + split_url[-1]
    return export_filename


def file_exists(folder, filename):
    filepath = os.path.join(folder, filename)
    return os.path.isfile(filepath)


def main():
    """
    Downloads the coal prduction data from energycharts and write to data/ directory
    """
    url_file = "search_urls.json"
    folder = "data"
    search_urls = read_search_urls_list_from_file(url_file)
    for url in search_urls:
        filename = create_export_filename(url)
        if file_exists(folder, filename):
            continue
        try:
            energy_data = pull_data_from_url(url)
            if len(energy_data) > 1:
                write_json_data_to_file(folder, filename, energy_data)
        except Exception as e:
            print("skipping url", url)
            print(e.message)


if __name__ == "__main__":
    main()

import glob
import json
import os
import sys

def import_wayback_JSON(linkFile):
    with open(linkFile) as f:
        waybackJSON = json.load(f)

    return waybackJSON


def timestamps_from_HTML_files(html_dir, filename):
    filenames = glob.glob(os.path.join(html_dir, filename))

    filename_timestamps = set()
    for filename in filenames:
        filename_timestamp = filename.split('_')[6].split('.')[0]
        filename_timestamps.add(filename_timestamp)

    return filename_timestamps


def get_missing_wayback_URLs(html_timestamps, wayback_timestamps):
    missing_wayback_URLs = []
    for item in wayback_timestamps:
        if item[1] not in html_timestamps:
            missing_wayback_URLs.append(item)
    return missing_wayback_URLs


def compareHTMLToAvailableJSON(html_dir, json_dir):
    """Compare the files in the 'raw_html' dir with 'raw_json'"""
    amount_files_raw_html = os.listdir(html_dir)
    amount_files_raw_json = os.listdir(json_dir)
    if len(amount_files_raw_html) == len(amount_files_raw_json):
        return
    return


def compare_to_set(base_list, comparison_set):
    differences = []
    for item in base_list:
        if item not in comparison_set:
            differences.append(item)
    return differences


def get_undownloaded_wayback_URLs(linkFile):
    html_dir = "raw_html"
    model = linkFile[:6]
    locale = linkFile[7:12]
    html_filename_template = f"html_raw_{locale}_{model}_*.html"

    waybackJSON = import_wayback_JSON(linkFile)
    html_timestamps = timestamps_from_HTML_files(html_dir, html_filename_template)
    missing_wayback_URLs = get_missing_wayback_URLs(html_timestamps, waybackJSON)
    return missing_wayback_URLs


linkFile = sys.argv[1]
get_undownloaded_wayback_URLs(linkFile)


import glob
import json
import os
import sys

def get_wayback_timestamps(linkFile):
    with open(linkFile) as f:
        waybackJSON = json.load(f)

    timestamps = []
    for item in waybackJSON:
        timestamps.append(item[1])

    return timestamps


def timestamps_from_HTML_files(html_dir, filename):
    filenames = glob.glob(os.path.join(html_dir, filename))

    filename_timestamps = set()
    for filename in filenames:
        filename_timestamp = filename.split('_')[6].split('.')[0]
        filename_timestamps.add(filename_timestamp)

    return filename_timestamps


def get_missing_timestamps(html_timestamps, wayback_timestamps):
    missing_timestmaps = [timestamp for timestamp in wayback_timestamps if timestamp not in html_timestamps]
    return missing_timestmaps


def get_undownloaded_timestamps(linkFile):
    html_dir = "raw_html"
    model = linkFile[:6]
    locale = linkFile[7:12]
    html_filename_template = f"html_raw_{locale}_{model}_*.html"

    wayback_timestamps = get_wayback_timestamps(linkFile)
    html_timestamps = timestamps_from_HTML_files(html_dir, html_filename_template)
    missing_timestamps = get_missing_timestamps(html_timestamps, wayback_timestamps)
    print("Model: ", model, "and locale:", locale, missing_timestamps)

    return missing_timestamps


linkFile = sys.argv[1]
get_undownloaded_timestamps(linkFile)


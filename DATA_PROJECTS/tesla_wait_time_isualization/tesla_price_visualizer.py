import argparse
from bs4 import BeautifulSoup
import json


def read_html_file(html_file_path):
    with open(html_file_path, "r") as f:
        html_content = f.read()

    return html_content


def extract_json_from_html(html_content):
    beginningSearchString = "window.tesla = "
    endSearchString = "if (typeof"

    begin = html_content.find(beginningSearchString) + len(beginningSearchString)
    end = html_content.find(endSearchString)

    stripped_html = html_content[begin:end].strip()
    json_data = json.loads(stripped_html.rstrip(";"))
    return json_data


def main():
    parser = argparse.ArgumentParser(description="Tesla Price Visualizer")
    parser.add_argument(
        "--extract_json", help="extract JSON from HTML file", metavar="<path_to_HTML>"
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()

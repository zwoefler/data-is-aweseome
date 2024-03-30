import argparse
from bs4 import BeautifulSoup
import json


def extract_json_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    json_element = soup.find(id="json_data")
    json_text = json_element.get_text()
    json_data = json.loads(json_text)

    return json_data


def main():
    parser = argparse.ArgumentParser(description="Tesla Price Visualizer")
    parser.add_argument(
        "--extract_json", help="extract JSON from HTML file", metavar="<path_to_HTML>"
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()

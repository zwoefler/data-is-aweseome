import argparse
from bs4 import BeautifulSoup
import json


def read_html_file():
    return


def extract_json_from_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    # Find script tag
    script_tag = soup.find("script", type="text/javascript")

    start_index = script_tag.text.find("window.tesla =") + len("window.tesla =")
    end_index = script_tag.text.find(";", start_index)
    json_text = script_tag.text[start_index:end_index].strip()

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

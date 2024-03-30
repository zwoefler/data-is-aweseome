import argparse


def extract_json_from_html(html_content):
    return {"example_key": "example_value"}


def main():
    parser = argparse.ArgumentParser(description="Tesla Price Visualizer")
    parser.add_argument(
        "--extract_json", help="extract JSON from HTML file", metavar="<path_to_HTML>"
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()

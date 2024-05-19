import argparse
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup


def extract_totals_from_table(html_table):
    """Extracts the total production number from table in press release"""
    totals = {"production": 0, "deliveries": 0}

    pandas_html_import = pd.read_html(html_table)
    df = pandas_html_import[0]
    totals["deliveries"] = int(df[2][3])
    totals["production"] = int(df[1][3])
    return totals


def extract_table(html):
    """Extract html tbale from HTML string"""
    soup = BeautifulSoup(html, "html.parser")
    table = str(soup.table)
    return table


def extract_totals(html):
    html_table = extract_table(html)
    totals = extract_totals_from_table(html_table)
    return totals


def fetch_html(url):
    html = requests.get(url)
    return html.text


def get_numbers_from_press_release(url):
    press_release_html = fetch_html(url)
    html_table = extract_table(press_release_html)
    totals = extract_totals_from_table(html_table)
    return totals


def extract_publishing_date(html):
    soup = BeautifulSoup(html, "html.parser")
    time_tag = soup.find("time")
    datetime_value = time_tag["datetime"]
    return datetime_value


def get_press_release_links(url):
    return []


def main():
    parser = argparse.ArgumentParser(
        description="Script to rerieve Tesla deliveries and production data from the press releases"
    )
    parser.add_argument("URL", help="URL of the Tesla press release")

    args = parser.parse_args()

    if not args.url:
        parser.print_help()
        return

    print(f"Processing data from URL: {args.url}")


if __name__ == "__main__":
    main()

import argparse
import re
import requests
import pandas as pd
from bs4 import BeautifulSoup


def fetch_html(url):
    html = requests.get(url)
    return html.text


def extract_table(html):
    """Extract html tbale from HTML string"""
    soup = BeautifulSoup(html, "html.parser")
    table = str(soup.table)
    return table


def extract_totals_from_table(html_table):
    """Extracts the total production number from HTML table"""
    totals = {"production": 0, "deliveries": 0}

    df = pd.read_html(html_table)[0]

    totals["deliveries"] = int(df[2][3])
    totals["production"] = int(df[1][3])
    return totals


def extract_publishing_date(html):
    """Extract publishing date from the HTML content"""
    soup = BeautifulSoup(html, "html.parser")
    time_tag = soup.find("time")
    datetime_value = time_tag["datetime"]

    return datetime_value


def get_numbers_from_press_release(url):
    """Get production, delivery and publishing date from a Tesla press release URL"""
    html = fetch_html(url=url)
    html_table = extract_table(html)
    totals = extract_totals_from_table(html_table)
    return totals


def get_press_release_links(url):
    return []


def main():
    parser = argparse.ArgumentParser(
        description="Script to rerieve Tesla deliveries and production data from a press releases"
    )
    parser.add_argument("URL", help="URL of the Tesla press release")
    args = parser.parse_args()

    if not args.URL:
        parser.print_help()
        return

    url = args.URL
    html = fetch_html(url)
    html_table = extract_table(html)
    totals = extract_totals_from_table(html_table)
    publishing_date = extract_publishing_date(html)
    print("Date:", publishing_date)
    print("Production:", totals["production"])
    print("Deliveries:", totals["deliveries"])


if __name__ == "__main__":
    main()

import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract_totals_from_table(html_table):
    """Extracts the total production number from table in press release"""
    totals = {
        "production": 0,
        "deliveries": 0
    }

    pandas_html_import = pd.read_html(html_table)
    df = pandas_html_import[0]
    totals["deliveries"] = int(df[2][3])
    totals["production"] = int(df[1][3])
    return totals


def extract_table(html):
    """Extract html tbale from HTML string"""
    soup = BeautifulSoup(html, 'html.parser')
    table = str(soup.table)
    return table

def extract_totals(html):
    html_table = extract_table(html)
    totals = extract_totals_from_table(html_table)
    return totals 


def retrieve_webpage(url):
    html = requests.get(url)
    return html.text


def get_numbers_from_press_release(url):
    press_release_html = retrieve_webpage(url)
    html_table = extract_table(press_release_html)
    totals = extract_totals_from_table(html_table)
    return totals

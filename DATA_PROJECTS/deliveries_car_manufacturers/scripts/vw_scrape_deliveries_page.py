import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.volkswagen-group.com/en/deliveries-to-customers-15741"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

pdf_divs = soup.find_all('div', class_="file-attachment is-pdf")

pdf_links = []

for div in pdf_divs:
    anchor = div.find('a')
    if anchor and anchor.get('href'):
        link_text = anchor.get_text(strip=True)
        link_url = anchor['href']
        pdf_links.append([link_text, link_url])

with open("vw_deliveries_pdf_links.csv", mode="w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Link Text", "URL"])  # Header
    writer.writerows(pdf_links)

print("PDF links have been written to pdf_links.csv")

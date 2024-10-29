import os
import sys
import csv
import requests

def download_pdfs(csv_path, download_dir="data/vw"):
    os.makedirs(download_dir, exist_ok=True)

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            link_text, url = row
            file_name = os.path.join(download_dir, f"{link_text}.pdf")

            try:
                response = requests.get(url)
                response.raise_for_status()

                with open(file_name, 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded {file_name}")

            except requests.RequestException as e:
                print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vw_download_deliveries_pdfs.py <path_to_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    download_pdfs(csv_path)

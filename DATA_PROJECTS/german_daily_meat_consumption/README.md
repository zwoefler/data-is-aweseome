# German daily meat consumption

# Extract Table from Nutrition Report 2024

Extract table from page 11 of the **Ernährungsreport 2024** published by the **German Federal Ministry of Food and Agriculture (BMEL)** and convert it into a structured dataset.

🔗 URL: https://www.bmel.de/SharedDocs/Downloads/DE/_Ernaehrung/forsa-ernaehrungsreport-2024-tabellen.pdf

<div align="center">
  <img src="https://www.bmel.de/SharedDocs/Bilder/DE/Logos/Logo-BMEL.png" alt="BMEL Logo" width="150"/>
</div>

## 🚀 Usage
The `extract_table.py` script reads the table from page 11 of the PDF document and exports it as a CSV dataset.

```SHELL
python3 extract_table.py
```

## 🏗️ How to use / Development?
Python3.10

**Requirements**:
- pdfplumber
- pandas

Downloaded PDF in root of this data directory.
Link in the Sources at the end.

1. Clone this repository and navigate to the project folder:
```SHELL
git clone git@github.com:zwoefler/data-is-awesome.git
cd data-is-awesome/german_daily_meat_consumption
```

2. Set up the Python virtual environment and install dependencies:
```SHELL
python3 -m venv Env
source Env/bin/activate
pip install -r requirements.txt
```

3. Extract the table from the PDF and save it as a CSV:
```SHELL
python3 extract_table.py
```

## The dataset format

The extracted dataset will have the following structure (example):
```CSV
"",2015, 2016, 2017 ...
"Obst und Gemüse", 76, 74, 72 ...
"Milchprodukte", *, 59, 65 ...
...
```

## What and where?
- `data/` Extracted CSV data
- `scripts/` Python3 scripts to extract table from PDF and export to csv

## Limits
- Only extracts page 11 from that specific report
- Ensure PDF is accurate!

## Debugging for pdfplumber
Trying to detect the table with `extract_tables()` didn't work.
It didn't correctly interpret the year headings.
Using the `to_image()` export to debug if you are on the correct path is a gift from heaven!

```Python
im = page.to_image()
with pdfplumber.open(pdf_path) as pdf:
    table_settings = {
        "vertical_strategy": "text",
        "horizontal_strategy": "text",
    }
    page = pdf.pages[11-1]
    lower_half_bbox = (0, 470, page.width, page.height - 180)
    cropped_page = page.within_bbox(lower_half_bbox)
    debug_table = cropped_page.debug_tablefinder(table_settings)
    table = cropped_page.extract_table(table_settings)

im.debug_tablefinder(table_finder)
```

## 📚 Resources
Nutrition Report 2024: [Ernährungsreport 2024 Ergebnisse einer repräsentativen Bevölkerungsbefragung](https://www.bmel.de/SharedDocs/Downloads/DE/_Ernaehrung/forsa-ernaehrungsreport-2024-tabellen.pdf?__blob=publicationFile&v=2)

# Car makers deliveres & Ppoducton numbers
Lately the car market has taken a hit.
Many people belive that this is because of some state guided factor.
However, it is a global phenomenon.

## 🚀 Vision
Dataset for car manufactureres showing deliveries by quarter (or lowest resolution data).

- [ ] VW
- [ ] BMW
- [ ] Mercedes


## Dev Setup
```bash
python3 -m venv Env
source Env/bin/activate
pip install -r requirements.txt
```

## Get VW Data
1. Run `python3 scripts/vw_scrape_deliveries_page.py`
2. Run `python3 scripts/vw_download_deliveries_pdfs.py vw_deliveries_pdf_links.csv`
3. Run `python3 scripts/vw_extract_and_append_data.py`


## Lessons learned
VW made a mistake... Or I didn't find the corrct footnote.
Many aggregated numbers by region are missing 100 vehicles.

Take a look at "July 2022"
https://uploads.vw-mms.de/system/production/files/cws/035/741/file/c5bf90c9ac96aa01a62fd3b65c6443c30a71851d/20220812_Deliveries_Tables_Juli.pdf?1681808466

Calculate the total of the column "Jul 2022" and tell me you receive "725500" instead of the stated "worldwide" deliveries of 725400.
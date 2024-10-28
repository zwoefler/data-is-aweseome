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
3. Run `python3 scripts/vw_extract_regions_deliveries_table.py data/vw`
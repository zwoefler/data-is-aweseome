import sys
import pdfplumber
import pandas as pd

def extract_first_table(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]

        tables = first_page.extract_tables()

        if not tables:
            print(f"No tables found in {pdf_path}")
            return None

        first_table_df = pd.DataFrame(tables[0])
        return first_table_df

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vw_extract_regions_deliveries_table.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    table_df = extract_first_table(pdf_path)

    if table_df is not None:
        print(table_df)
    else:
        print("No table data extracted.")

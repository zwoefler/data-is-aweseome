import sys
import pdfplumber
import pandas as pd
import os


def extract_first_table(pdf_path):
    """Extracts the region and latest month columns from the first table of a PDF."""
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        tables = first_page.extract_tables()

        if not tables:
            print(f"No tables found in {pdf_path}")
            return None

        df = pd.DataFrame(tables[0])

        if df.shape[1] < 2:
            print(f"Unexpected table structure in {pdf_path}")
            return None

        region_col = df[0].str.strip()
        value_col = df[1].str.replace(",", "").astype(float, errors="ignore")

        latest_month_data = pd.DataFrame(
            {
                "Region": region_col,
                os.path.basename(pdf_path).replace(".pdf", ""): value_col,
            }
        )

        for index in range(len(latest_month_data)):
            if (
                latest_month_data.iloc[index, 0] == ""
                and latest_month_data.iloc[index, 1] != ""
            ):
                latest_month_data.iloc[index, 0] = "Worldwide"

        latest_month_data.dropna(inplace=True)

        return latest_month_data


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

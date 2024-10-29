import os
import pdfplumber
import pandas as pd
from vw_extract_regions_deliveries_table import extract_first_table


# def extract_first_table(pdf_path):
#     """Extracts the region and latest month columns from the first table of a PDF."""
#     with pdfplumber.open(pdf_path) as pdf:
#         first_page = pdf.pages[0]
#         tables = first_page.extract_tables()

#         if not tables:
#             print(f"No tables found in {pdf_path}")
#             return None

#         df = pd.DataFrame(tables[0])

#         if df.shape[1] < 2:
#             print(f"Unexpected table structure in {pdf_path}")
#             return None

#         region_col = df[0].str.strip()
#         value_col = df[1].str.replace(",", "").astype(float, errors="ignore")

#         latest_month_data = pd.DataFrame(
#             {
#                 "Region": region_col,
#                 os.path.basename(pdf_path).replace(".pdf", ""): value_col,
#             }
#         )

#         for index in range(len(latest_month_data)):
#             if latest_month_data.iloc[index, 0] == "":
#                 latest_month_data.iloc[index, 0] = "Worldwide"

#         latest_month_data.dropna(inplace=True)

#         return latest_month_data


def build_dataset_from_pdfs(pdf_dir, output_csv="vw_deliveries.csv"):
    """Builds a dataset by extracting region and latest month data from each PDF."""
    data_dict = {}

    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, filename)
            print(f"Processing {pdf_path}")

            pdf_df = extract_first_table(pdf_path)
            if pdf_df is None:
                print(f"Skipping {filename} due to extraction issues.")
                continue

            for _, row in pdf_df.iterrows():
                region = row["Region"]
                latest_month_value = row[filename.replace(".pdf", "")]

                if region in data_dict:
                    data_dict[region][filename.replace(".pdf", "")] = latest_month_value
                else:
                    data_dict[region] = {
                        filename.replace(".pdf", ""): latest_month_value
                    }

    all_data = pd.DataFrame.from_dict(data_dict, orient="index").reset_index()
    all_data.columns = ["Region"] + list(all_data.columns[1:])  # Rename columns

    all_data.to_csv(output_csv, index=False)
    print(f"Data saved to {output_csv}")


if __name__ == "__main__":
    pdf_dir = "data/vw"
    build_dataset_from_pdfs(pdf_dir)

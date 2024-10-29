import os
import pandas as pd
from vw_extract_regions_deliveries_table import extract_first_table


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

                if "China" in region:
                    region = "China"

                latest_month_value = row[filename.replace(".pdf", "")]

                if region in data_dict:
                    data_dict[region][filename.replace(".pdf", "")] = latest_month_value
                else:
                    data_dict[region] = {
                        filename.replace(".pdf", ""): latest_month_value
                    }

    all_data = pd.DataFrame.from_dict(data_dict, orient="index").reset_index()
    all_data.columns = ["Region"] + list(all_data.columns[1:])

    all_data.to_csv(output_csv, index=False)
    print(f"Data saved to {output_csv}")


if __name__ == "__main__":
    pdf_dir = "data/vw"
    build_dataset_from_pdfs(pdf_dir)

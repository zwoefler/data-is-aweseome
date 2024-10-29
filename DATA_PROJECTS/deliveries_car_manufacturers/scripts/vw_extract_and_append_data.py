import os
import pandas as pd
from vw_extract_regions_deliveries_table import extract_first_table


def build_dataset_from_pdfs(pdf_dir):
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
    all_data.columns = ["Region"] + list(all_data.iloc[0, 1:])

    return all_data


def sort_columns_by_date(all_data):
    month_map = {
        "jan.": 1,
        "feb.": 2,
        "mar.": 3,
        "apr.": 4,
        "may": 5,
        "jun.": 6,
        "jul.": 7,
        "aug.": 8,
        "sep.": 9,
        "oct.": 10,
        "nov.": 11,
        "dec.": 12,
    }

    months = all_data.iloc[0, 1:].str.lower()
    years = all_data.iloc[1, 1:].astype(int)

    sort_keys = []
    divider_dash = "–"

    for month, year in zip(months, years):
        if divider_dash in month:
            start_month_string = month.split(divider_dash)[0].strip()
            start_month = month_map.get(start_month_string)
            sort_keys.append((year, start_month))
        else:
            month_number = month_map.get(month)
            sort_keys.append((year, month_number))

    sorted_columns = sorted(range(len(sort_keys)), key=lambda x: sort_keys[x])

    ordered_data = all_data.iloc[:, [0] + [i + 1 for i in sorted_columns]].reset_index(
        drop=True
    )

    return ordered_data


def create_single_header(all_data):
    months = all_data.iloc[0, 1:].str.lower()
    years = all_data.iloc[1, 1:].astype(str)

    new_header = [f"{month.capitalize()} {year}" for month, year in zip(months, years)]

    all_data.columns = ["Region"] + new_header
    all_data = all_data.dropna()
    all_data = all_data.drop(index=[0, 1]).reset_index(drop=True)

    return all_data


def export_to_csv(df, output_csv="vw_deliveries.csv"):
    df.to_csv(path_or_buf=output_csv, index=False)
    print(f"Data saved to {output_csv}")


if __name__ == "__main__":
    pdf_dir = "data/vw"
    df: pd.DataFrame = build_dataset_from_pdfs(pdf_dir)
    sorted_data: pd.DataFrame = sort_columns_by_date(df)
    finished_data_set = create_single_header(sorted_data)
    export_to_csv(finished_data_set)

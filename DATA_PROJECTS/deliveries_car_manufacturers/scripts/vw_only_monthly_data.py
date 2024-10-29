import pandas as pd
import sys


def remove_quarterly_data(input_csv: str, output_file: str) -> str:
    df = pd.read_csv(input_csv)

    df_filtered = df.loc[:, ~df.columns.str.contains("–")]

    df_filtered.to_csv(output_file, index=False)

    print(f"Filtered data saved to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_quarterly_data.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.rsplit(".", 1)[0] + "_filtered.csv"
    remove_quarterly_data(input_file, output_file)

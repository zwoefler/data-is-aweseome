import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import json
import os
import argparse


def load_json_from_file(file_path):
    """
    Load JSON data from a file.

    Parameters:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Dictionary containing the loaded JSON data.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def plot_data(file_path):
    # parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # file_path = os.path.join(parent_directory, "parkhouse_data", "am bahnhof.json")
    data = load_json_from_file(file_path)

    # Convert timestamp to datetime
    data["occupation_data"] = [
        {"timestamp": pd.to_datetime(entry["timestamp"], unit="s"), **entry}
        for entry in data["occupation_data"]
    ]

    # Flatten the data
    flat_data = [
        {"timestamp": entry["timestamp"], "value": entry["occupied_spaces"]}
        for entry in data["occupation_data"]
    ]

    df = pd.DataFrame(flat_data)

    sns.set(style="whitegrid")

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x="timestamp", y="value", marker="o")

    plt.xlabel("Timestamp")
    plt.ylabel("Occupied Spaces")
    plt.title(f"Occupation over Time - {data['name']}")

    plt.show()


def list_datasets():
    """
    List available datasets in the 'parkhouse_data/' directory.
    """
    parkhouse_data_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "parkhouse_data"
    )

    datasets = {}
    for file_name in os.listdir(parkhouse_data_dir):
        if file_name.endswith(".json"):
            file_path = os.path.join(parkhouse_data_dir, file_name)
            with open(file_path, "r") as file:
                data = json.load(file)
                parkhouse_name = data.get("name", "")
                relative_path = os.path.relpath(
                    file_path, start=os.path.dirname(os.path.abspath(__file__))
                )
                name_as_key = parkhouse_name.strip().lower().replace(" ", "_")
                datasets[name_as_key] = {
                    "relative_path": relative_path,
                    "path": file_path,
                    "name": parkhouse_name,
                }

    return datasets


def argument_parser():
    """
    Create an argument parser for the provided requirements.

    Returns:
        argparse.ArgumentParser: Argument parser with defined attributes
    """
    parser = argparse.ArgumentParser(description="Parkhouse Data Visualizer")
    parser.add_argument(
        "--show-data", action="store_true", help="SHow list of available datasets"
    )
    parser.add_argument(
        "--plot",
        metavar="DATASET",
        help="Plot the specified dataset. Example: --plot dataset.json",
    )

    return parser.parse_args()


def main():
    python_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    args = argument_parser()
    datasets = list_datasets()
    if args.show_data:
        if datasets:
            for dataset in datasets.values():
                print(f'{dataset["name"]} - {dataset["relative_path"]}')
        else:
            print("No datasets found.")
    elif args.plot:
        parkhouse_to_plot = datasets[args.plot.lower()]["path"]
        plot_data(parkhouse_to_plot)


if __name__ == "__main__":
    main()

import json
import datetime
import os


def write_json_data_to_file(json_data, filename):
    with open(filename, "w") as f:
        json.dump(json_data, f)


def open_json(json_file):
    with open(json_file, "r") as f:
        json_data = json.load(f)
    return json_data


def get_json_data_files():
    matching_files = []
    for filename in os.listdir("data/"):
        if filename.startswith("data_year_") and filename.endswith(".json"):
            matching_files.append(filename)
    return sorted(matching_files)


def get_daily_electricity_consumption(energy_consumption_data):
    daily_electricity_production = []
    hourly_energy_production = energy_consumption_data[::4]
    daily_sum = 0

    for i in range(0, len(hourly_energy_production), 24):
        step_sum = sum(hourly_energy_production[i : i + 24])
        daily_electricity_production.append(step_sum)

    return daily_electricity_production


def find_brown_and_hard_coal(
    values_for_year, search_terms=["Braunkohle", "Steinkohle"]
):
    coal_lists = []
    for source in values_for_year:
        for term in search_terms:
            try:
                if term in source["name"]["de"]:
                    coal_lists.append(source)
            except TypeError:
                pass

    return coal_lists


def timestamp_to_human_readable_time(timestamp):
    timestamp_seconds = timestamp / 1000
    dt = datetime.datetime.fromtimestamp(timestamp_seconds)
    formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


def aggregate_energy_types(energy_1, energy_2):
    return [x + y for x, y in zip(energy_1, energy_2)]


def get_aggreagted_electricity_data(data_set):
    coal_sources = find_brown_and_hard_coal(data_set)

    quarter_hour_timestamps = data_set[0]["xAxisValues"]
    daily_timestamps = quarter_hour_timestamps[::4][::24]
    daily_datetime_timestamps = [
        timestamp_to_human_readable_time(stamp) for stamp in daily_timestamps
    ]

    quarter_hour_coal = aggregate_energy_types(
        coal_sources[0]["data"], coal_sources[1]["data"]
    )
    daily_coal = get_daily_electricity_consumption(quarter_hour_coal)
    return daily_coal, daily_datetime_timestamps


def main():
    """
    Aggregates coal data from data/ into coal_data.json
    """
    electricty_source_data_json = "coal_data.json"
    json_files = get_json_data_files()
    electricity_data = {"time": [], "data": []}
    for file in json_files:
        yearly_electricity_data = open_json(f"data/{file}")
        daily_coal, daily_timestamps = get_aggreagted_electricity_data(
            yearly_electricity_data
        )
        electricity_data["time"].extend(daily_timestamps)
        electricity_data["data"].extend(daily_coal)

    write_json_data_to_file(electricity_data, electricty_source_data_json)
    return


if __name__ == "__main__":
    main()

import pandas as pd
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, "de_DE.utf-8")
# insolvenz_url = "https://www.destatis.de/DE/Themen/Branchen-Unternehmen/Unternehmen/Gewerbemeldungen-Insolvenzen/Tabellen/Insolvenzen.html#fussnote-1-241898"

def export_df_to_JSON(data, json_file_name):
    with open(json_file_name, 'w') as f:
        json.dump(data, f)


def convert_month_year_date_to_datetime_object(date_string, date_format="%Y %b"):
    date = datetime.strptime(date_string, date_format)
    return date


def visualize_data(x_axis, data, title, x_label, y_label):
    for data_column in data:
        plt.plot(x_axis, data_column)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_minor_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_minor_formatter(mdates.DateFormatter("%b"))
    plt.gca().tick_params(axis='x', which='major', length=0, labelsize=10)
    plt.gca().tick_params(axis='x', which='minor', length=2, labelsize=7, rotation=90)

    plt.show()


data = pd.read_html("insolvenzen_seit_1953.html")[0][:-1]
print(data)

# date_column = data[data.columns[0]] + " " + data[data.columns[1]]
# date_column = date_column.apply(lambda x: convert_month_year_date_to_datetime_object(x)).tolist()
# insolvencies = data[data.columns[2]].apply(lambda x: int("".join(x.split()))).tolist()


# data = [insolvencies]


# visualize_data(date_column, data, title="Insolvenzen Deutschland", x_label="Months", y_label="Insolvencies (total)")
import pandas as pd
import json
import matplotlib.pyplot as plt
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


data = pd.read_html("insolvenzen.html")[0][:-1]
date_column = data[data.columns[0]] + " " + data[data.columns[1]]
date_column = date_column.apply(lambda x: convert_month_year_date_to_datetime_object(x)).tolist()
insolvencies = data[data.columns[2]].apply(lambda x: int("".join(x.split()))).tolist()



plt.plot(date_column, insolvencies)
plt.title("Insolvenzen Deutschland")
plt.xlabel("Months")
plt.ylabel("Insolvencies (total)")
plt.show()






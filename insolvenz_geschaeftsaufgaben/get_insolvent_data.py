import pandas as pd
import json
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL, '')

def export_df_to_JSON(data, json_file_name):
    with open(json_file_name, 'w') as f:
        json.dump(data, f)



# insolvenz_url = "https://www.destatis.de/DE/Themen/Branchen-Unternehmen/Unternehmen/Gewerbemeldungen-Insolvenzen/Tabellen/Insolvenzen.html#fussnote-1-241898"
data = pd.read_html("insolvenzen.html")[0][:-1]
date_column = data[data.columns[0]] + " " + data[data.columns[1]].tolist()
insolvencies = data[data.columns[2]].apply(lambda x: int("".join(x.split()))).tolist()

print(insolvencies)

plt.plot(date_column, insolvencies)
plt.title("Insolvenzen Deutschland")
plt.xlabel("Months")
plt.ylabel("Insolvencies (total)")
plt.show()






import pandas as pd
import matplotlib.pyplot as plt

file_path = "OECD-economic-outlook-june-2023-GDP-data.xlsx"
sheet_name = "Data"
start_cell = "B7"
end_cell = "M57"

df = pd.read_excel(file_path, sheet_name=sheet_name, header=None, skiprows=6, usecols="B:M")
df.columns = df.iloc[0]
df = df.iloc[1:]

value_column = 2023.0
label_column = "Country EN"

df_sorted = df.sort_values(value_column, ascending=True)

fig, ax = plt.subplots(figsize=(15,20))

bars = ax.barh(df_sorted[label_column], df_sorted[value_column])
ax.set_title("OECD 2023 Real GDP Growth Forecast", fontsize=20)
ax.set_xlabel("Real GDP Forecast 2023 by OECD", fontsize=16)
ax.set_ylabel("Countries", fontsize=16)

for i, value in enumerate(df_sorted[value_column]):
    ax.text(value, i, "{:.2f}".format(value), ha='left', va='center', fontsize=12)

for bar, label, economy in zip(bars, df_sorted[label_column], df_sorted["Economy"]):
    if "World" in label:
        bar.set_color('gray')
    elif "OECD" in label:
        bar.set_color('gray')
    elif "Euro area" in label:
        bar.set_color('gray')
    elif "OECD countries" in economy:
        bar.set_color('orange')

# Adjust max x value to fit largest number on chart
max_value = df_sorted[value_column].max()
ax.set_xlim(right=max_value * 1.5)

plt.show()
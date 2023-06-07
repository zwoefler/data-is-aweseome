import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from helpers import open_json

coal_data = open_json("coal_data.json")

df = pd.DataFrame(coal_data)
df['time'] = pd.to_datetime(df['time'])
df['year'] = df['time'].dt.year

filtered_df = df[df['year'].between(2015, 2023)]

fig, ax = plt.subplots()

grouped_df = filtered_df.groupby('year')

for year, data in grouped_df:
    days = (data['time'] - pd.Timestamp(year=year, month=1, day=1)).dt.days
    if year == 2023:
        ax.plot(days, data["data"], label=str(year), alpha=1)
    else:
        ax.plot(days, data['data'], label=str(year), alpha=0.2)

ax.set_xlabel('Days in Year')
ax.set_ylabel('Coal Production in TWh')
ax.set_title('Data Comparison across Years')
ax.legend()

plt.show()
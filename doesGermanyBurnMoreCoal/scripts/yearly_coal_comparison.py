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
        ax.plot(days, data['data'], label=str(year), alpha=0.1)

# Add a horizontal red line at the 105th day
ax.axvline(x=105, color='red', label="Nuclear phaseout in Germany 15.04.23")

formatter = ticker.FuncFormatter(lambda x, pos: f'{x/1e3:.1f}')
ax.yaxis.set_major_formatter(formatter)

ax.set_xlabel('Days in Year')
ax.set_ylabel('Daily Coal Production in GWh')
ax.set_title('Daily Germany Net Coal Production - Data Comparison 2015 through 2023')
ax.legend()

plt.show()
import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from helpers import open_json

coal_data = open_json("coal_data.json")

df = pd.DataFrame(coal_data)
df["time"] = pd.to_datetime(df["time"])

df['year'] = df['time'].dt.year
grouped_df = df.groupby('year')

fig, ax = plt.subplots(figsize=(12, 8))

for year, data in grouped_df:
    ax.plot(data['time'], data['data'], label=str(year))

ax.set_xlabel('Time')
ax.set_ylabel('Net Electricity Produced (TWh)')
ax.set_title('Coal production compared years 2015 through 2023')

plt.show()
import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from helpers import open_json

coal_data = open_json("coal_data.json")

df = pd.DataFrame(coal_data)
df["time"] = pd.to_datetime(df["time"])

df['year'] = df['time'].dt.year

fig, ax = plt.subplots()

sns.lineplot(data=df, x='time', y='data', hue='year', ax=ax)

ax.xaxis.set_major_locator(plt.MaxNLocator(10))

ax.set_xlabel('Year')
ax.set_ylabel('Data')
ax.set_title('Data over the years')
ax.legend(title='Year')

plt.xticks(rotation=45)

plt.show()
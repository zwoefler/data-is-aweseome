import matplotlib.pyplot as plt
import json
from datetime import datetime
import sys

model = sys.argv[1]
dataFile = "aggregatedData_en_US_model_data.json"
locale = dataFile[15:20]
country = locale[3:]

with open(dataFile, "r") as f:
    modelData = json.load(f)


fig, ax = plt.subplots()

for trimObj in modelData[model].values():
    name = trimObj["name"]
    dates = [item[0] for item in trimObj["data"]]
    dates = [datetime.fromtimestamp(date / 1000) for date in dates]
    prices = [item[1] for item in trimObj["data"]]

    ax.plot(dates, prices, label=name)

# Add horizontal lines for every 10,000
for i in range(0, int(ax.get_ylim()[1]), 10000):
    ax.axhline(i, color='gray', linestyle='dotted')


ax.legend()
ax.set_ylim(bottom=0)

plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.title(model + " in " + country)
plt.show()
import matplotlib.pyplot as plt
import json
from datetime import datetime
import sys

model = sys.argv[1]
dataFile = "aggregatedData_en_US_model_data.json"
locale = dataFile[15:20]

with open(dataFile, "r") as f:
    modelData = json.load(f)


fig, ax = plt.subplots()

for trimObj in modelData[model].values():
    name = trimObj["name"]
    dates = [item[0] for item in trimObj["data"]]
    dates = [datetime.fromtimestamp(date / 1000) for date in dates]
    prices = [item[1] for item in trimObj["data"]]

    ax.plot(dates, prices, label=name)

ax.legend()
# plt.plot(dates, prices)
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.title("Price changes for: " + model + " In " + locale)
plt.show()
import matplotlib.pyplot as plt
import json
from datetime import datetime
import sys


model = sys.argv[1]
trim = sys.argv[2]
dataFile = f"aggregatedData_{model}_en_US.json"

with open(dataFile, "r") as f:
    modelData = json.load(f)

print(modelData[model][trim])
sorted_data = sorted(modelData[model][trim]["data"], key=lambda x: x[0])
dates, prices = zip(*sorted_data)
dates = [datetime.fromtimestamp(date / 1000) for date in dates]
plt.plot(dates, prices)
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.title("Price changes for" + modelData[model][trim]["name"])
plt.show()
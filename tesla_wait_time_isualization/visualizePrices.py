import glob
import json
import matplotlib.pyplot as plt
from datetime import datetime
import os

trimID = "$MT324"
data_dir = "final_data"
files = "m3_en_US_*json"

json_files = glob.glob(os.path.join(data_dir, files))

priceData = []

for file_path in json_files:
    with open(file_path, "r") as f:
        data = json.load(f)

    trims = data["trims"]

    for trim in trims:
        if trim["trimShorthandle"] == trimID:
            price = trim["price"]
            date = datetime.fromtimestamp(data["date"] / 1000)
            priceData.append((date, price))

sorted_data = sorted(priceData, key=lambda x: x[0])
dates, prices = zip(*sorted_data)
plt.plot(dates, prices)
plt.xlabel("Date")
plt.ylabel("Price in USD")
plt.title("Price changes for" + trimID)
plt.show()
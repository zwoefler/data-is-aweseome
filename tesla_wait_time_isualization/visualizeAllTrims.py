import os
import matplotlib.pyplot as plt
import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import io
import base64
import json
import sys

def importModelJSON(dataFile):
    with open(dataFile, "r") as f:
        modelData = json.load(f)

    return modelData


def plotModel(modelData, model, country):

    currency = modelData["meta"]["currency"]

    fig, ax = plt.subplots(figsize=(16,9))

    for trimObj in modelData["models"][model].values():
        name = trimObj["name"]
        dates = [item[0] for item in trimObj["data"]]
        dates = [datetime.fromtimestamp(date / 1000) for date in dates]
        prices = [item[1] for item in trimObj["data"]]

        ax.plot(dates, prices, label=name)

    max_y_value = int(ax.get_ylim()[1])
    if max_y_value < 180000:
        dotted_line_every = 10000
    else:
        dotted_line_every = 100000

    # Add horizontal lines for every 10,000
    for i in range(0, max_y_value, dotted_line_every):
        ax.axhline(i, color='gray', linestyle='dotted')

    # format the y-axis ticks with comma delimiter for thousands
    fmt = ticker.StrMethodFormatter("{x:,.0f}")
    ax.yaxis.set_major_formatter(fmt)

    ax.legend()
    ax.set_ylim(bottom=0)
    plt.rcParams['font.family'] = ['Noto Sans CJK JP']
    plt.xlabel("Date")
    plt.ylabel("Price in" + currency)
    plt.title(model + " in " + country)

    return fig


def createBase64Image(fig):
    image = io.BytesIO()
    fig.savefig(image, format='png')
    image.seek(0)
    image_base64 = base64.b64encode(image.getvalue()).decode('utf-8')

    return image_base64


def base64_to_png(base64_image, file_path):
    with open(file_path, "wb") as f:
        f.write(base64.b64decode(base64_image))

dataFile = sys.argv[1]
exportDirectory = "price_charts"
modelJSON = importModelJSON(dataFile)
locale = dataFile[15:20]
country = locale[3:]

for model in modelJSON["models"].keys():
    figure = plotModel(modelJSON, model, country)
    base64_image = createBase64Image(figure)
    export_filename = f"tesla_{country}_{model}_prices.png"
    export_path = os.path.join(exportDirectory, export_filename)
    base64_to_png(base64_image, export_path)

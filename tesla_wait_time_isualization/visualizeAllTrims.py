import matplotlib.pyplot as plt
import json
from datetime import datetime
import matplotlib.pyplot as plt
import io
import base64
import json
import sys


def importModelJSON(dataFile):
    with open(dataFile, "r") as f:
        modelData = json.load(f)

    return modelData

def plotModel(modelData, model, country):
    fig, ax = plt.subplots(figsize=(16,9))

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

    return fig

def createImage(fig):
    image = io.BytesIO()
    fig.savefig(image, format='png')
    image.seek(0)
    image_base64 = base64.b64encode(image.getvalue()).decode('utf-8')

    return image_base64


def visualizeModel(model, dataFile="aggregatedData_en_US_model_data.json"):
    dataFile = "aggregatedData_en_US_model_data.json"
    locale = dataFile[15:20]
    country = locale[3:]

    modelJSON = importModelJSON(dataFile)
    figure = plotModel(modelJSON, model, country)
    image= createImage(figure)

    return image


def base64_to_png(base64_image, file_path):
    with open(file_path, "wb") as f:
        f.write(base64.b64decode(base64_image))


model = sys.argv[1]
base64_image = visualizeModel(model)
base64_to_png(base64_image, f"tesla_us_{model}_prices.png")

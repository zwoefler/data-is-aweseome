from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64
import json
from datetime import datetime
import createPriceCharts

app = Flask(__name__)

with open('aggregatedData_en_US_model_data.json', 'r') as f:
    model_data = json.load(f)

models = model_data.keys()

@app.route("/model_selected", methods=["POST"])
def model_selected():
    model = request.form["model"]
    image_base64 = createPriceCharts.visualizeModel(model)

    return render_template("index.html", models=models, selected_model=model, image=image_base64)


@app.route("/trim_selected", methods=["POST"])
def trim_selected():
    trim = request.form['trim']
    model = request.form['model']

    data = model_data[model][trim]['data']
    trims = list(model_data[model].items())
    trim_name = model_data[model][trim]["name"]

    dates = [item[0] for item in data]
    prices = [item[1] for item in data]
    dates = [datetime.fromtimestamp(date / 1000) for date in dates]

    fig = plt.figure()
    plt.plot(dates, prices)
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.title(f"{model}: {trim_name} - {trim} Price over time")

    image = io.BytesIO()
    fig.savefig(image, format='png')
    image.seek(0)
    image_base64 = base64.b64encode(image.getvalue()).decode('utf-8')

    return render_template('index.html', models=models, selected_model=model, trims=trims, selected_trim=trim, trim_name=trim_name, image=image_base64)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', models=models)


if __name__ == "__main__":
    app.run()

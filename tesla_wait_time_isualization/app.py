from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64
import json
from datetime import datetime
import logging

app = Flask(__name__)

with open('aggregatedData_en_US_model_data.json', 'r') as f:
    model_data = json.load(f)

models = model_data.keys()
trims = []

@app.route("/model_selected", methods=["POST"])
def model_selected():
    model = request.form["model"]
    logging.warning(model)
    trims = list(model_data[model].keys())
    return render_template("index.html", models=models, selected_model=model, trims=trims)


@app.route("/trim_selected", methods=["POST"])
def trim_selected():
    trim = request.form['trim']
    model = request.form['model']

    data = model_data[model][trim]['data']

    dates = [item[0] for item in data]
    prices = [item[1] for item in data]
    dates = [datetime.fromtimestamp(date / 1000) for date in dates]

    fig = plt.figure()
    plt.plot(dates, prices)
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.title(f"{model} {trim} Price over time")

    image = io.BytesIO()
    fig.savefig(image, format='png')
    image.seek(0)
    image_base64 = base64.b64encode(image.getvalue()).decode('utf-8')

    return render_template('index.html', models=models, trims=trims, selected_model=model, selected_trim=trim, image=image_base64)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', models=models)


if __name__ == "__main__":
    app.run()

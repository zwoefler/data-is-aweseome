from flask import Flask, render_template, request
import json

app = Flask(__name__)

# @app.route("/")
# def index():
#     with open("aggregatedData_m3_en_US.json", "r") as f:
#         model_data = json.load(f)
#     models = list(model_data.keys())
#     return render_template("index.html", models=models, modelData=model_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('aggregatedData_m3_en_US.json', 'r') as f:
        data = json.load(f)

    trims = []
    trims = list(data["m3"].keys())

    return render_template('index.html', data=data, trims=trims)


if __name__ == "__main__":
    app.run()

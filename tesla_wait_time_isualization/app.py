from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    with open('aggregatedData_m3_en_US.json', 'r') as f:
        model_data = json.load(f)

    if request.method == 'POST':
        model = "m3"
        trim = request.form['trim']
        data = model_data[model][trim]['data']

        x = [item[0] for item in data]
        y = [item[1] for item in data]

        fig = plt.figure()
        plt.plot(x, y)
        plt.xlabel('Timestamp')
        plt.ylabel('Price')
        plt.title(f"{model} {trim} Price over time")

        image = io.BytesIO()
        fig.savefig(image, format='png')
        image.seek(0)
        image_base64 = base64.b64encode(image.getvalue()).decode('utf-8')

        return render_template('index.html', model_data=model_data, trim=trim, image=image_base64)


    return render_template('index.html', model_data=model_data)


if __name__ == "__main__":
    app.run()

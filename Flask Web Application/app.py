import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("HDI.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'GET':
        return render_template("indexnew.html")

    try:
        print("Form Data:", request.form)

        life_expectancy = float(request.form.get("life_expectancy"))
        schooling = float(request.form.get("schooling"))
        gni = float(request.form.get("gni"))
        internet_users = float(request.form.get("internet_users"))

        print(life_expectancy, schooling, gni, internet_users)

        features = np.array([[life_expectancy, schooling, gni, internet_users]])

        prediction = model.predict(features)

        output = round(float(prediction[0]), 3)

        return render_template(
            "indexnew.html",
            prediction_text=f"Predicted HDI Score: {output}"
        )

    except Exception as e:
        print("ERROR:", e)
        return render_template(
            "indexnew.html",
            prediction_text=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)
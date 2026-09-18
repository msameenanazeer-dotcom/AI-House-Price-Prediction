from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

X = np.array([
    [500],
    [800],
    [1000],
    [1200],
    [1500],
    [1800],
    [2000]
])

y = np.array([
    20,
    30,
    40,
    48,
    60,
    72,
    80
])

model = LinearRegression()
model.fit(X, y)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":
        area = float(request.form["area"])
        prediction = round(model.predict([[area]])[0], 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

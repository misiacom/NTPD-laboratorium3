from flask import Flask, jsonify, request
import numpy as np
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY", "default_key")
#dane treningowe
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

#trenowanie modelu
model = LinearRegression()
model.fit(X, y)

#endpoint główny
@app.route("/")
def home():
    return jsonify({"message": "Witaj w moim API!",
                    "api_key": API_KEY})

#endpoint predykcji
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Brak danych JSON"}), 400

    if "x" not in data:
        return jsonify({"error": "Brak pola 'x' w danych wejściowych"}), 400

    try:
        x_value = float(data["x"])
    except (ValueError, TypeError):
        return jsonify({"error": "Pole 'x' musi być liczbą"}), 400

    x_array = np.array([[x_value]])
    prediction = model.predict(x_array)

    return jsonify({
        "input": x_value,
        "prediction": prediction[0]
    })

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "model": "LinearRegression",
        "number_of_features": X.shape[1],
        "training_samples": len(X)
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

#uruchomienie aplikacji
if __name__ == "__main__":
    app.run(debug=True)
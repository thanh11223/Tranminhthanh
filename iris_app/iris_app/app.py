from flask import Flask, render_template, request, jsonify
from sklearn.datasets import load_iris
import numpy as np
import pickle
import os

app = Flask(__name__)

MODEL_PATH = os.environ.get("MODEL_PATH", "model.pkl")

# Load model at startup
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

iris = load_iris()
target_names = iris.target_names  # ['setosa', 'versicolor', 'virginica']

def to_species_name(idx: int) -> str:
    # Chuẩn hoá thành tên hiển thị đẹp
    mapping = {
        "setosa": "Iris setosa",
        "versicolor": "Iris versicolor",
        "virginica": "Iris virginica",
    }
    raw = target_names[idx]
    return mapping.get(raw, raw)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])  # JSON only
def predict():
    try:
        data = request.get_json(force=True) or {}
        vals = [
            data.get("sepal_len", None),
            data.get("sepal_wid", None),
            data.get("petal_len", None),
            data.get("petal_wid", None),
        ]

        # Convert to floats, allow None -> np.nan
        features = [float(v) if v is not None and str(v).strip() != "" else np.nan for v in vals]
        X = np.array(features, dtype=float).reshape(1, -1)

        # Pipeline có SimpleImputer nên xử lý được NaN
        probs = None
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(X)[0]
        pred_idx = int(model.predict(X)[0])

        resp = {
            "species": to_species_name(pred_idx),
        }

        if probs is not None:
            resp["probabilities"] = {
                to_species_name(i): float(p) for i, p in enumerate(probs)
            }

        return jsonify(resp)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

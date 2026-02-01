from __future__ import annotations

import time
from pathlib import Path
from typing import Any, Dict

import joblib
from flask import Flask, jsonify, render_template, request


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "Model"

DEFAULT_JOBLIB_PATH = MODEL_DIR / "spam_classifier.joblib"
DEFAULT_PKL_PATH = MODEL_DIR / "spam_classifier.pkl"


def load_model() -> Any:
    """Load the sklearn pipeline once at startup (fast inference)."""
    if DEFAULT_JOBLIB_PATH.exists():
        return joblib.load(DEFAULT_JOBLIB_PATH)

    if DEFAULT_PKL_PATH.exists():
        # joblib can load plain pickle too; keep single loader
        return joblib.load(DEFAULT_PKL_PATH)

    raise FileNotFoundError(
        "Model file not found. Expected one of: "
        f"{DEFAULT_JOBLIB_PATH} or {DEFAULT_PKL_PATH}"
    )


MODEL = load_model()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024  # 1 MB


def _predict_one(message: str) -> Dict[str, Any]:
    message = (message or "").strip()
    if not message:
        return {
            "ok": False,
            "error": "Message is empty.",
        }

    if len(message) > 5000:
        return {
            "ok": False,
            "error": "Message too long (max 5000 characters).",
        }

    start = time.perf_counter()

    pred = MODEL.predict([message])[0]

    spam_probability = None
    if hasattr(MODEL, "predict_proba"):
        try:
            proba = MODEL.predict_proba([message])[0]
            # Our training uses target: ham=0, spam=1
            spam_probability = float(proba[1])
        except Exception:
            spam_probability = None

    elapsed_ms = (time.perf_counter() - start) * 1000

    label = "SPAM" if int(pred) == 1 else "HAM"

    return {
        "ok": True,
        "label": label,
        "prediction": int(pred),
        "spam_probability": spam_probability,
        "latency_ms": round(elapsed_ms, 2),
    }


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/predict")
def api_predict():
    payload = request.get_json(silent=True) or {}
    message = payload.get("message", "")
    result = _predict_one(message)
    status = 200 if result.get("ok") else 400
    return jsonify(result), status


if __name__ == "__main__":
    # For production, run with: python -m flask --app app run
    app.run(host="127.0.0.1", port=5000, debug=True)

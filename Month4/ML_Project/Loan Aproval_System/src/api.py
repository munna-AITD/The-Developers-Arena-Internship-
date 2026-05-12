from flask import Flask, request, jsonify
from src.model_inference import predict
from config.config import DEBUG, HOST, PORT

app = Flask(__name__)

# ====================================
# SINGLE PREDICTION API
# ====================================
@app.route("/predict", methods=["POST"])
def predict_api():
    try:
        data = request.get_json()

        model_name = data.get("model", "best_model")

        prediction = predict(data, model_name)

        return jsonify({
            "status": "success",
            "prediction": prediction
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


# ====================================
# BATCH PREDICTION
# ====================================
@app.route("/predict_batch", methods=["POST"])
def predict_batch():
    try:
        data_list = request.get_json()

        results = []

        for data in data_list:
            model_name = data.get("model", "best_model")
            pred = predict(data, model_name)
            results.append(pred)

        return jsonify({
            "status": "success",
            "predictions": results
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


# ====================================
# HEALTH CHECK
# ====================================
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"})


# ====================================
# AVAILABLE MODELS
# ====================================
@app.route("/models", methods=["GET"])
def models():
    return jsonify({
        "available_models": [
            "random_forest",
            "decision_tree",
            "logistic_regression",
            "best_model"
        ]
    })


# ====================================
# RUN API SERVER
# ====================================
if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
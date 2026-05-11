from flask import Flask, render_template, request
from src.model_inference import predict
from config.config import DEBUG, HOST, PORT

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def make_prediction():
    data = {
        "no_of_dependents": int(request.form["dependents"]),
        "education": request.form["education"],
        "self_employed": request.form["self_employed"],
        "income_annum": float(request.form["income"]),
        "loan_amount": float(request.form["loan_amount"]),
        "loan_term": float(request.form["loan_term"]),
        "cibil_score": int(request.form["cibil"]),
        "residential_assets_value": float(request.form["residential"]),
        "commercial_assets_value": float(request.form["commercial"]),
        "luxury_assets_value": float(request.form["luxury"]),
        "bank_asset_value": float(request.form["bank"])
    }

    model = request.form["model"]

    result = predict(data, model)

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
from flask import Flask, render_template, request
from src.model_inference import predict
from config.config import DEBUG
import os
# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#print("BASE_DIR:", BASE_DIR)

#template_path = os.path.join(BASE_DIR, "templates")
#print("Template path:", template_path)

#if os.path.exists(template_path):
#    print("Templates folder exists ✅")
#    print("Files inside:", os.listdir(template_path))
#else:
#    print("Templates folder NOT found ❌")
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)  
    

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def make_prediction():
    data = {
            "Area": float(request.form["area"]),
            "Bedrooms": int(request.form["bedrooms"]),
            "Bathrooms": int(request.form["bathrooms"]),
            "Age": int(request.form["age"]),
            "Location": request.form["location"],
            "Property_Type": request.form["property_type"]
        }

    result = predict(data)

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=DEBUG)
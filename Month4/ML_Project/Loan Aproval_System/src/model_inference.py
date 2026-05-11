import joblib
import pandas as pd

from config.config import (
    RF_MODEL_PATH,
    DT_MODEL_PATH,
    LR_MODEL_PATH,
    BEST_MODEL_PATH,
    PREPROCESSOR_PATH,
    FEATURE_COLUMNS
)

# Load models
rf_model = joblib.load(RF_MODEL_PATH)
dt_model = joblib.load(DT_MODEL_PATH)
lr_model = joblib.load(LR_MODEL_PATH)
best_model = joblib.load(BEST_MODEL_PATH)

preprocessor = joblib.load(PREPROCESSOR_PATH)

def predict(data, model_name="best_model"):
    
    df = pd.DataFrame([data])
    
    df.columns = df.columns.str.lower()
    
    df = df[FEATURE_COLUMNS]
    
    # Transform
    X = preprocessor.transform(df)
    
    # Select model
    if model_name == "random_forest":
        model = rf_model
    elif model_name == "decision_tree":
        model = dt_model
    elif model_name == "logistic_regression":
        model = lr_model
    else:
        model = best_model
    
    prediction = model.predict(X)
    
    return "Approved ✅" if prediction[0] == 1 else "Rejected ❌"
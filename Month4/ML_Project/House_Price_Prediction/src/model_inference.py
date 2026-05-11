import joblib
import os
import pandas as pd
from config.config import MODEL_PATH, PREPROCESSOR_PATH, FEATURE_COLUMNS

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)


def predict(input_data: dict):
    df = pd.DataFrame([input_data])
    df = df[FEATURE_COLUMNS]
    
    X_processed = preprocessor.transform(df)
    prediction = model.predict(X_processed)
    
    return round(prediction[0], 2)
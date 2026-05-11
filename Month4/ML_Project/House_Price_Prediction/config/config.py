import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "models", "preprocessor.pkl")

# Features (VERY IMPORTANT)
FEATURE_COLUMNS = ['Area', 'Bedrooms', 'Bathrooms', 'Location', 'Property_Type', 'Age']

# App settings
DEBUG = True
import os

# =====================================
# BASE DIRECTORY
# =====================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =====================================
# DATA PATHS
# =====================================
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_PATH = os.path.join(DATA_DIR, "loan_data.csv")

# =====================================
# MODEL PATHS
# =====================================
MODEL_DIR = os.path.join(BASE_DIR, "models")

RF_MODEL_PATH = os.path.join(MODEL_DIR, "random_forest.pkl")
DT_MODEL_PATH = os.path.join(MODEL_DIR, "decision_tree.pkl")
LR_MODEL_PATH = os.path.join(MODEL_DIR, "logistic_regression.pkl")
BEST_MODEL_PATH = os.path.join(MODEL_DIR, "best_model.pkl")

PREPROCESSOR_PATH = os.path.join(MODEL_DIR, "preprocessor.pkl")

# =====================================
# MODEL SETTINGS
# =====================================
RANDOM_STATE = 42
TEST_SIZE = 0.2
CV_FOLDS = 5

# =====================================
# FLASK SETTINGS
# =====================================
DEBUG = True
HOST = "127.0.0.1"
PORT = 5000

# =====================================
# FEATURE CONFIG
# =====================================
FEATURE_COLUMNS = [
    'no_of_dependents',
    'education',
    'self_employed',
    'income_annum',
    'loan_amount',
    'loan_term',
    'cibil_score',
    'residential_assets_value',
    'commercial_assets_value',
    'luxury_assets_value',
    'bank_asset_value'
]

TARGET_COLUMN = "loan_status"

# =====================================
# LABEL MAPPING
# =====================================
TARGET_MAPPING = {
    "approved": 1,
    "rejected": 0
}
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def process_data(path):
    df = pd.read_csv(path)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Drop ID
    df.drop("loan_id", axis=1, inplace=True)

    # Target encoding
    df['loan_status'] = df['loan_status'].str.strip().str.lower()
    df['loan_status'] = df['loan_status'].map({'approved':1, 'rejected':0})

    # Split
    y = df['loan_status']
    X = df.drop('loan_status', axis=1)

    # Columns
    cat_cols = ['education', 'self_employed']
    num_cols = [col for col in X.columns if col not in cat_cols]

    # Preprocessor
    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(drop='first', handle_unknown='ignore'), cat_cols),
        ("num", StandardScaler(), num_cols)
    ])

    X_processed = preprocessor.fit_transform(X)

    return X_processed, y, preprocessor
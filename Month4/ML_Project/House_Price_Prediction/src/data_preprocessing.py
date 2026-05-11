from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
import pandas as pd

def process_data(path):
    df = pd.read_csv(path)
    df = df.dropna()
    df = df.drop(columns=["Property_ID"], errors="ignore")

    # Separate
    y = df["Price"]
    X = df.drop("Price", axis=1)

    # Columns
    cat_cols = X.select_dtypes(include=['object']).columns
    num_cols = X.select_dtypes(exclude=['object']).columns

    # Transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(drop='first', handle_unknown='ignore', sparse_output=False), cat_cols),
            ("num", StandardScaler(), num_cols)
        ]
    )

    # Transform
    X_processed = preprocessor.fit_transform(X)

    # Get correct feature names
    cat_features = preprocessor.named_transformers_["cat"].get_feature_names_out(cat_cols)
    all_features = list(cat_features) + list(num_cols)

    print("Shape from transformer:", X_processed.shape)
    print("Number of columns:", len(all_features))

    # Convert safely
    X_processed = pd.DataFrame(X_processed, columns=all_features)

    return X_processed, y, preprocessor
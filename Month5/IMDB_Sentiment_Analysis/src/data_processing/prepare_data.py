import pandas as pd
from preprocess import clean_text

df = pd.read_csv("data/raw/IMDB Dataset.csv")

df["clean_review"] = df["review"].apply(clean_text)

df.to_csv(
    "data/processed/imdb_cleaned.csv",
    index=False
)

print("Dataset saved")
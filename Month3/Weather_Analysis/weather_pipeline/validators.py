def validate_data(df):
    if df.empty:
        raise ValueError("Empty Data")

    required = ["time", "temperature", "humidity", "wind_speed"]

    for col in required:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    return True
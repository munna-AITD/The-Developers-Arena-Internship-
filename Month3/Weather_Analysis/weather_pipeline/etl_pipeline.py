import pandas as pd
from api_client import fetch_weather
from database import insert_data, create_table
from validators import validate_data
from monitor import log_info, log_error

# -------------------------------
# TRANSFORM FUNCTION
# -------------------------------
def transform(data):
    import pandas as pd

    record = {
        "time": data["dt"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }

    df = pd.DataFrame([record])

    # Convert timestamp
    df["time"] = pd.to_datetime(df["time"], unit="s")

    return df
# -------------------------------
# MAIN PIPELINE
# -------------------------------
def run_pipeline():
    try:
        log_info("ETL pipeline started")

        # Step 1: Create table
        create_table()

        # Step 2: Extract
        data = fetch_weather()
        log_info("Data extracted successfully")

        # Step 3: Transform
        df = transform(data)
        log_info("Data transformed successfully")

        # Step 4: Validate
        validate_data(df)
        log_info("Data validation passed")

        # 🔥 IMPORTANT FIX (Database Error Solution)
        df = df[["time", "temperature", "humidity", "wind_speed"]]
        df["time"] = df["time"].astype(str)

        # Step 5: Load
        insert_data(df)
        log_info("Data loaded into database")

        print("✅ ETL Pipeline Completed Successfully")

    except Exception as e:
        log_error(f"ETL pipeline failed: {e}")
        print("❌ Pipeline failed:", e)


# -------------------------------
# RUN SCRIPT
# -------------------------------
if __name__ == "__main__":
    run_pipeline()


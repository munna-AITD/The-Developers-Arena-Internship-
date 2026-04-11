import sqlite3
import pandas as pd
from config import DB_PATH, REPORT_DIR

def generate_report():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql("SELECT * FROM weather", conn)

    if df.empty:
        print("No data available")
        return
    # convert time
    df['time'] = pd.to_datetime(df['time'])

    #Analytics
   
    report = df.describe()

    file_path = f"{REPORT_DIR}/report.csv"
    report.to_csv(file_path)

    conn.close()

    print("Report generated:", file_path)
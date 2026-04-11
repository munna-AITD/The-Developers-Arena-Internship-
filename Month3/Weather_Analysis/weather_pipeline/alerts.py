import sqlite3
import pandas as pd

def check_alerts():
    conn = sqlite3.connect("weather.db")

    df = pd.read_sql("SELECT * FROM weather ORDER BY time DESC LIMIT 1", conn)

    if df.empty:
        return

    temp = df["temperature"].iloc[0]
    humidity = df["humidity"].iloc[0]

    # 🔥 Alert conditions
    if temp > 35:
        print(" ALERT: High Temperature!")

    if humidity > 80:
        print("ALERT: High Humidity!")

    conn.close()
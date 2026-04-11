import sqlite3
from config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        time TEXT,
        temperature REAL,
        humidity REAL,
        wind_speed REAL
    )
    """)

    conn.commit()
    conn.close()

def insert_data(df):
    conn = get_connection()
    df.to_sql("weather", conn, if_exists="append", index=False)
    conn.close()
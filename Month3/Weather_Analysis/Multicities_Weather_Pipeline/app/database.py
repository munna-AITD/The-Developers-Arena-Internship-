import sqlite3
import os

DB_PATH = "data/weather_data.db"

def connect():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def setup_database():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cities (
            city_id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_name TEXT NOT NULL UNIQUE,
            country TEXT,
            latitude REAL,
            longitude REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            record_id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_id INTEGER,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            temperature_c REAL,
            humidity INTEGER,
            pressure_hpa REAL,
            wind_speed_mps REAL,
            weather_condition TEXT,
            FOREIGN KEY (city_id) REFERENCES cities (city_id)
        )
    """)

    conn.commit()
    conn.close()


# ✅ INSERT CITY FUNCTION (PUT HERE)
def insert_city(city_name, country=None, lat=None, lon=None):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO cities (city_name, country, latitude, longitude)
        VALUES (?, ?, ?, ?)
    """, (city_name, country, lat, lon))

    conn.commit()
    conn.close()


# ✅ GET CITY ID FUNCTION (PUT HERE)
def get_city_id(city_name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT city_id FROM cities WHERE city_name = ?", (city_name,))
    result = cursor.fetchone()

    conn.close()

    return result[0] if result else None
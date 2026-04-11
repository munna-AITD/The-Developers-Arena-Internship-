from app.database import setup_database, insert_city
from app.config import CITIES
from app.extract import fetch_weather
from app.transform import transform
from app.load import load
from app.validate import validate

def initialize_cities():
    for city in CITIES:
        insert_city(city)

def run_pipeline():
    setup_database()
    initialize_cities()   # ⭐ VERY IMPORTANT

    for city in CITIES:
        raw = fetch_weather(city)

        if raw:
            data = transform(raw)

            if validate(data):
                load(data)
                print(f"Stored: {city}")

if __name__ == "__main__":
    run_pipeline()
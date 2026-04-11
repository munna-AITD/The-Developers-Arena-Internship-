import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

CITIES = [
    "Delhi", "Mumbai", "Lucknow",
    "Bangalore", "Chennai",
    "Kolkata", "Hyderabad"
]

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
DB_NAME = "data/weather.db"
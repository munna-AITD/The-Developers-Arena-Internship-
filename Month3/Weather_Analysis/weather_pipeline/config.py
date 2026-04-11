import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "weather.db")
LOG_DIR = os.path.join(BASE_DIR, "logs")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

API_KEY = os.getenv("API_KEY")

CITY = "Delhi"
API_URL = "https://api.openweathermap.org/data/2.5/weather"
print("CURRENT DIR:", os.getcwd())
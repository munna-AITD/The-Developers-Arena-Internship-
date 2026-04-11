import requests
from config import API_KEY, API_URL, CITY
import time

def fetch_weather():
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }

    for i in range(3):
        try:
            response = requests.get(API_URL, params=params, timeout=10)

            print("Attempt:", i+1, "Status:", response.status_code)
            print("RESPONSE:", response.text)   # 🔥 DEBUG

            data = response.json()

            return data

        except Exception as e:
            print("Error:", e)

        time.sleep(2)

    raise Exception("API failed after retries")


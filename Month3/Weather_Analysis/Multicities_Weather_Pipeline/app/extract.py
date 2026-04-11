import requests
from app.config import API_KEY, BASE_URL

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    except Exception as e:
        print(f"[ERROR] API failed for {city}: {e}")
        return None
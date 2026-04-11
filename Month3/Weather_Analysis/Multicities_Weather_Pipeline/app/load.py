from app.database import connect, get_city_id

def load(data):
    conn = connect()
    cursor = conn.cursor()

    city_id = get_city_id(data["city"])

    if city_id is None:
        print(f"City not found: {data['city']}")
        return

    cursor.execute("""
        INSERT INTO weather_data
        (city_id, temperature_c, humidity, pressure_hpa, wind_speed_mps, weather_condition)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        city_id,
        data["temperature"],
        data["humidity"],
        data["pressure"],
        data["wind_speed"],
        data["weather"]
    ))

    conn.commit()
    conn.close()
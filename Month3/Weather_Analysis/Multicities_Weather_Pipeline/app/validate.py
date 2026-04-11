def validate(data):
    if not data:
        return False

    if not (-50 <= data["temperature"] <= 60):
        return False

    if not (0 <= data["humidity"] <= 100):
        return False

    return True
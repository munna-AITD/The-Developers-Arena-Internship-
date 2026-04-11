import os
def check_system():
    if not os.path.exists("weather.db"):
        print(" Database missing")

    if not os.path.exists("logs"):
        print(" Logs folder missing")

    print(" System OK")
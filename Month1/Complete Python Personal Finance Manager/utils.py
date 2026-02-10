from datetime import datetime

def get_amount():
    while True:
        try:
            amt = float(input("Enter amount: "))
            if amt <= 0:
                raise ValueError
            return amt
        except ValueError:
            print("❌ Invalid amount")


def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("❌ Invalid date format")

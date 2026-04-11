import schedule
import time
from etl_pipeline import run_pipeline

schedule.every(1).hours.do(run_pipeline)

print("Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(60)
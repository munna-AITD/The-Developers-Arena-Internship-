import json
import os

METRICS_FILE = "reports/metrics/model_metrics.json"


def save_metrics(metrics_dict):

    os.makedirs("reports/metrics", exist_ok=True)

    with open(METRICS_FILE, "w") as f:
        json.dump(metrics_dict, f, indent=4)


def load_metrics():

    if not os.path.exists(METRICS_FILE):
        return {}

    with open(METRICS_FILE, "r") as f:
        return json.load(f)
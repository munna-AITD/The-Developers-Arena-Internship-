
import os
import pandas as pd


def save_metrics(metrics):
    os.makedirs("reports/metrics", exist_ok=True)

    df = pd.DataFrame([metrics])

    df.to_csv(
        "reports/metrics/model_metrics.csv",
        index=False
    )

    print(
        "\nMetrics Saved Successfully"
    )
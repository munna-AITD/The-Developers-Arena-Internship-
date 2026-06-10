import logging
import os

os.makedirs("reports/logs", exist_ok=True)

logging.basicConfig(
    filename="reports/logs/predictions.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def log_prediction(review, sentiment, confidence):

    logging.info(
        f"Review={review[:100]} "
        f"Sentiment={sentiment} "
        f"Confidence={confidence:.4f}"
    )
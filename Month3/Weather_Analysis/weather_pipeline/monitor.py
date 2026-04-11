import logging
from config import LOG_DIR
import os


log_file = os.path.join(LOG_DIR, "pipeline.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_info(msg):
    logging.info(msg)

def log_error(msg):
    logging.error(msg)


log_info("Pipeline started")
log_info("Data extracted")
log_error("API failed")
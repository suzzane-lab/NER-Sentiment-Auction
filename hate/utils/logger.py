import logging
import os

from hate.constants import LOGS_DIR, LOGS_FILE_NAME

def setup_loggin():
    os.makedirs(LOGS_DIR, exist_ok=True)
    log_file_path = os.path.join(LOGS_DIR, LOGS_FILE_NAME)

    logging.basicConfig(
        format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler(),
        ],
    )
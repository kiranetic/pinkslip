import logging
from config import LOG_FILE


logger = logging.getLogger("psjob")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("[%(levelname)s] %(asctime)s — %(message)s", "%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)


import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

BASE_DIR = Path(__file__).parent
LOGS_DIR = BASE_DIR / 'logs'
LOG_FILE = LOGS_DIR / 'saber_app.log'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
LOG_DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'


def configure_logging():
    """Описание конфигурации для логирования"""
    LOGS_DIR.mkdir(exist_ok=True)
    rotating_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=10**6, backupCount=5, encoding='utf-8',
    )

    logging.basicConfig(
        datefmt=LOG_DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(
            rotating_handler,
        ),
    )

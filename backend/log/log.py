import logging
from logging.config import fileConfig


class Logging:
    def __init__(self, log_file_name: str = 'log.txt') -> logging:
        fileConfig('./log/log_config_time.ini')

    def object(self) -> logging.Logger:
        return logging.getLogger('uvicorn')

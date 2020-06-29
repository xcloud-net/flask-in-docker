# coding=utf-8
import logging
from pythonjsonlogger import jsonlogger
from logging import handlers

logging.basicConfig(level=logging.INFO)


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def __init__(self, *args, **kwargs):
        jsonlogger.JsonFormatter.__init__(self, *args, **kwargs)

    def add_fields(self, log_record, record, message_dict):
        jsonlogger.JsonFormatter.add_fields(self, log_record, record, message_dict)

        log_record['app'] = 'flask-app'

        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


formatter = CustomJsonFormatter('(timestamp) (level) (name) (message)', timestamp=True)


def get_logger(name):
    global formatter
    logger = logging.getLogger(name if name else 'default')

    # console
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # 5 * 1024 * 1024
    # file_handler = logging.FileHandler(filename='./x.log')
    file_handler = logging.handlers.RotatingFileHandler(filename='./logs/size_test.log',
                                                        maxBytes=5 * 1024,
                                                        backupCount=10)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    time_file_handler = logging.handlers.TimedRotatingFileHandler(filename='./logs/time_test.log',
                                                                  when='h',
                                                                  interval=1,
                                                                  backupCount=10,
                                                                  utc=True)
    time_file_handler.setFormatter(formatter)
    logger.addHandler(time_file_handler)

    return logger

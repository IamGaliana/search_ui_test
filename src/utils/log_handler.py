__author__ = 'gaoyanjun'
# NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
import logging
from logging.handlers import TimedRotatingFileHandler
# BASIC_LOG_PATH = './'
# filename = 'test'

LOG_FILE = 'test.log'

file_handler = logging.FileHandler(LOG_FILE)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# logger = logging.getLogger()
# formatter = logging.Formatter('%(name)-12s %(asctime)s level-%(levelname)-8s thread-%(thread)-8d %(message)s')
# fileTimeHandler = TimedRotatingFileHandler(BASIC_LOG_PATH + filename, 'S', 1, 10)
# fileTimeHandler.suffix = "%Y%m%d.log"
# fileTimeHandler.setFormatter(formatter)
# logging.basicConfig(level=logging.INFO)
# fileTimeHandler.setFormatter(formatter)
# logger.addHandler(fileTimeHandler)


def log_debug(message):
    logger.debug(message)


def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning("WARNING: " + message)


def log_error(message):
    logger.error("ERROR: " + message)


def log_critical(message):
    logger.critical(message)
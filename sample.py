#! /usr/bin/python
import logging.config

logging.config.fileConfig("logging.conf")

logger = logging.getLogger()

logger.info("info level log")
logger.debug("debug level log")
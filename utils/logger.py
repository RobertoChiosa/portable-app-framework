# Author:       Roberto Chiosa
# Copyright:    Roberto Chiosa, © 2023
# Email:        roberto.chiosa@polito.it
#
# Created:      23/02/23
# Script Name:  logger.py
# Path:         utils
#
# Script Description:
# This script contains the logger class. Load the Custom logger in your file
# to access to customized logger configuration
# Example code:
#
# from utils.logger import CustomLogger
#
# if __name__ == "__main__":
#     logger = CustomLogger().get_logger()
#     logger.info("Hello World")
#
# Notes: https://docs.python.org/3/howto/logging.html
# https://realpython.com/python-logging/
# https://towardsdatascience.com/why-and-how-to-set-up-logging-for-python-projects-bcdd4a374c7a
# https://github.com/Husseinjd/keras-tensorflow-template
# https://github.com/MrGemy95/Tensorflow-Project-Template
# https://coderzcolumn.com/tutorials/python/logging-config-simple-guide-to-configure-loggers-from-dictionary-and-config-files-in-python


import logging.config
import os


class ColoredFormatter(logging.Formatter):
    """
    Colored formatter
    """

    def __init__(self, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)
        self.COLORS = {
            'DEBUG': '\u001b[37;1m',
            'INFO': '\u001b[32;1m',
            'WARNING': '\u001b[33;1m',
            'ERROR': '\033[91m',
            'CRITICAL': '\u001b[31;1m',
            'RESET': '\033[0m',
        }

    def format(self, record) -> str:
        """
        Defines the colors of the logs depending on the level
        :param record: The log string
        :return: Formatted string
        """
        levelname = record.levelname
        message = record.msg
        if levelname in self.COLORS:
            levelname_color = self.COLORS[levelname] + levelname + self.COLORS['RESET']
            message_color = self.COLORS[levelname] + message + self.COLORS['RESET']
            record.levelname = levelname_color
            record.msg = message_color
        return super(ColoredFormatter, self).format(record)


class CustomLogger:
    """
    This class is used to instantiate a logger object

    example:
    logger = CustomLogger().get_logger()
    """

    def __init__(self, filename=None) -> None:
        """Init logger

        :param filename: name of the file to log
        """
        self.logger = logging.getLogger(filename)

    def get_logger(self, filename="dev") -> logging.Logger:
        """
        Return logger

        :param filename: name of the file to log
        :return: logger
        """

        # gets the path depending on the env stage
        # config_path = f"../config/logger_config_{stage}.ini"
        config_path = os.path.join("..", "config", 'logger', f'{filename}.ini')

        if filename == "dev":
            # if dev does not create file output
            logging.config.fileConfig(
                config_path,
                disable_existing_loggers=False
            )
        elif filename == "prod":
            # if prod logs output to file
            logging.config.fileConfig(
                config_path,
                disable_existing_loggers=False,
                # defaults={"logfilename": os.path.join("..", "logs", f"{module_name}{timestamp}.log")}
                defaults={"logfilename": os.path.join("..", "logs", "log.log")}
            )
        else:
            pass

        # Set the formatter for the console handler
        console_handler = self.logger.handlers[0]
        console_formatter = ColoredFormatter(
            # fmt='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s',
            fmt='%(asctime)s [%(levelname)s] (%(filename)s > %(funcName)s) %(message)s',
            # fmt='%(asctime)s [%(levelname)s] (%(filename)s > %(funcName)s > line %(lineno)d) %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)

        return self.logger


def example_logs(logger) -> None:
    """
    Example of logs
    :param logger: logger object
    :return: None
    """
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

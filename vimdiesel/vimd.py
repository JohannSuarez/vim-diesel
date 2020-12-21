"""
Main file
"""
# pylint: disable=R0903

# standard
# import argparse

# 3rd party

# vim-diesel library
from vimdiesel.vimdutils.diesel_logger import DieselLogger

logger = DieselLogger().get_logger()


class VimDiesel:
    """
    Execution Code
    """


if __name__ == '__main__':
    logger.info('This is an informational message')
    logger.debug('This is a debug message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a system critical message')

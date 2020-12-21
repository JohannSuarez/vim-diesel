"""
Main file
"""
# pylint: disable=R0903

# standard
# import argparse

# 3rd party

# vim-diesel library
from vimdiesel.vimdutils import diesel_logger as dl

logger = dl.DieselLogger().get_logger()

logger.info('Testing')


class VimDiesel:
    """
    Execution Code
    """


if __name__ == '__main__':
    logger.info('Testing')

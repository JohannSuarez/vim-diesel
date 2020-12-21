"""
Static System wide configurations defined here
"""
# pylint: disable=R0903

from typing import Literal
from pathlib import PosixPath

APP_NAME = 'vim-diesel'
VERSION = '0.1.0'
LOGGER_NAME = 'dev'

# Path Base
CONFIG = PosixPath.home() / '.config'
DATA = PosixPath.home() / '.local' / 'share'
NVIM = CONFIG / 'nvim'


# We need these two files available before the config is fully loaded,
# instead of making them a global constant, wrap them in a Literal param
# function so they can still be used and passed around during the systems
# boot up with some type checking
def system_files(system_file: Literal['log', 'config']) -> PosixPath:
    """
    wrapper around the system config files so
    they can't be manipulated globally
    :raises: FileNotFoundError
    :param: string literal, only log and config are accepted
    :return: PosixPath object pointing to a system file
    """
    if system_file in 'log':
        system_log_file = DATA / APP_NAME / 'log' / 'vim-diesel.log'
        return system_log_file
    if system_file in 'config':
        system_config_file = CONFIG / APP_NAME / 'config.yaml'
        return system_config_file

    raise FileNotFoundError(
        f'{system_file} was not found, accepted entries are config and log')


class SystemConfigKeywords:
    """Only Root Keywords"""
    RuntimeStorage = "RuntimeStorage"
    Files = "Files"


class PluginConfigKeyWords:
    """Only Root Keywords"""
    Plugins = "Plugins"


SYSTEM_CONFIG = {
    "{0}".format(SystemConfigKeywords.RuntimeStorage): {
        "app_store": "{0}".format(CONFIG / APP_NAME),
        "log_store": "{0}".format(DATA / APP_NAME / 'log'),
        "plugin_store":
        "{0}".format(NVIM / 'after' / 'pack' / APP_NAME / 'start')
    },
    "{0}".format(SystemConfigKeywords.Files): {
        "config_file": "{0}".format(system_files('config')),
        "log_file": "{0}".format(system_files('log')),
        "plugin_file": "{0}".format(NVIM / 'vim-deisel-plugings.yaml'),
    }
}

USER_PLUGIN_CONFIG = {
    "{0}".format(PluginConfigKeyWords.Plugins): {
        # example
        "preservim/nerdtree",
    }
}


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "colored": {
            "()": "colorlog.ColoredFormatter",
            'format': "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s"
        },
        "simple": {
            "format": "%(levelname)s - %(message)s"
        },
        "pedantic": {
            "format": "%(asctime)s - %(module)s - %(funcName)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console-color": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "colored",
            "stream": "ext://sys.stdout"
        },
        "file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "filename": "{0}".format(system_files('log')),
            "formatter": "pedantic"
        }
    },
    "loggers": {
        # dev
        "{}".format(LOGGER_NAME): {
            "handlers": ["console-color", "file_handler", ],
            "level": "DEBUG",
            "propagate": False
        },
        "production": {
            "handlers": ["file_handler", ],
            "level": "DEBUG",
            "propagate": False
        }
    },
    "root": {
        "handlers": ["file_handler"]
    }
}

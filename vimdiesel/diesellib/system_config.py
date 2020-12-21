"""
Static System wide configurations defined here
"""
# pylint: disable=R0903

from pathlib import PosixPath
import pkg_resources

APP_NAME = 'vim-diesel'
VERSION = pkg_resources.require('vimdiesel')[0].version

# Path Base
CONFIG = PosixPath.home() / '.config'
DATA = PosixPath.home() / '.local' / 'share'


class ConfigKeywords:
    """Only Root Keywords"""
    RuntimeStorage = "RuntimeStorage"
    Files = "Files"


SYSTEM_CONFIG = {
    "{0}".format(ConfigKeywords.RuntimeStorage): {
        "app_store":
        "{0}".format(CONFIG / APP_NAME),
        "log_store":
        "{0}".format(DATA / APP_NAME / 'log'),
        "plugin_store":
        "{0}".format(CONFIG / 'nvim' / 'after' / 'pack' / APP_NAME / 'start')
    },
    "{0}".format(ConfigKeywords.Files): {
        "config_file": "{0}".format(CONFIG / APP_NAME / 'config.yaml'),
        "log_file": "{0}".format(DATA / APP_NAME / 'log' / 'vim-deisel.log'),
        "plugin_file":
        "{0}".format(CONFIG / 'nvim' / 'vim-deisel-plugings.yaml'),
    }
}

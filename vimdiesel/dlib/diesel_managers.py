"""
Managers for vimdiesel
ConfigurationManager
PluginManger
"""

# pylint: disable=R0903

# standard
import sys

# 3rd party
import yaml

# diesel
import system_config as sysconf
from system_config import SystemConfigKeywords as sck
from system_config import PluginConfigKeyWords as pck


class _DieselManager:
    """
    Base class for managers
    """
    ...


class ConfigurationManager(_DieselManager):
    """
    Handle vim-deisel set up,
    and all configuration files
    """
    ...


class PluginManager(_DieselManager):
    """
    Handle plugin management
    """
    ...

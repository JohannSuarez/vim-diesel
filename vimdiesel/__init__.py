"""
Get the version from setup.py the smart way
"""
import pkg_resources
__version__ = pkg_resources.require('vimdiesel')[0].version

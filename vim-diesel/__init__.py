"""
Get the version from setup.py the smart way
"""
import pkg_resources
__version__ = pkg_resources.require('vim-diesel')[0].version

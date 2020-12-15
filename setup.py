"""
When packaging LTF software, as libraries, or applications
this is the setup.py template that should be used
"""
from setuptools import setup

# constants that should be front and center
AUTHOR = 'Matt Williams'
VERSION = '0.1.0'
LICENSE = 'GPLv3'
PKG_NAME = 'vimdiesel'
REPO_URL = 'https://github.com/mattcoding4days/vim-diesel'
EMAIL = 'mattltf@pm.me'

# dependency files
REQS: str = 'requirements/dependencies.txt'

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open(REQS, 'r') as depends:
    requirements = depends.read().splitlines()

setup(name=PKG_NAME,
      version=VERSION,
      install_requires=requirements,
      author=AUTHOR,
      author_email=EMAIL,
      description="A modular asynchronous neovim plugin/package manager",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url=REPO_URL,
      license=LICENSE,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GPL License',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.8',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ])

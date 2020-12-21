"""
Custom exceptions for vim-deisel
"""


class VimDeiselError(Exception):
    """
    Obligatory Base class
    """
    ...


class ConfigFileError(VimDeiselError):
    """
    Report when method is not coded yet
    """
    def __init__(self, message: str = 'Not valid config file: '):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

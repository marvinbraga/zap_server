# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Application Exceptions Module
"""
from core.exceptions.bases import CustomBaseException


class ParserCommandException(CustomBaseException):
    """
    Exception Class to use in parser commands.
    """
    DEFAULT_MESSAGE = 'Command Parser Error: The command is invalid.'

    def __init__(self):
        super().__init__()
        self._message = self.DEFAULT_MESSAGE

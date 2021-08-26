# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Zap Server Application Module
"""


class CustomBaseException(Exception):
    """
    Base class to exceptions.
    """
    DEFAULT_MESSAGE = 'This is the basic exception.'

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        message = self.DEFAULT_MESSAGE
        if args:
            message = args[0]
        self._message = message

    def __str__(self):
        return self._message

    @property
    def message(self):
        """
        Return attribute message.
        :return: Str with message attribute.
        """
        return self._message

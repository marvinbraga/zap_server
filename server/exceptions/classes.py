# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Basic Exceptions to Business Rules Module.
"""
from core.exceptions.bases import CustomBaseException


class DefaultMessage:
    """
    Class to maintain the default message producer.
    """
    @staticmethod
    def build_message(msg):
        """
        Method to create the message from args.
        :param msg: Message data.
        :return: Message string.
        """
        return f'Execution failed on: "{msg}".'


class WhatsappBaseException(CustomBaseException, DefaultMessage):
    """
    Basic class of exceptions for Whatsapp.
    """
    _TEXT = None

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        message = 'This is the basic exception for whatsapp.'
        if self._TEXT:
            message = self.build_message(self._TEXT)
        if args:
            message = args[0]
        self._message = message

# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Properties Commands Exceptions Module
"""
from server.exceptions.classes import WhatsappBaseException


class GetQrCodeException(WhatsappBaseException):
    """
    Exception to retrieve authentication qr-code.
    """
    _TEXT = 'Recover QR Code'


class CheckPointException(WhatsappBaseException):
    """
    Exception for authentication information verification exception.
    """
    _TEXT = 'Check Authentication on the Site'


class IsConnectedException(WhatsappBaseException):
    """
    Exception for connection state check.
    """
    _TEXT = 'Check Whatsapp Connection with Server'


class ConnectionLostException(WhatsappBaseException):
    """
    Exception for lost connection.
    """
    _TEXT = 'Lost Connection With Whatsapp'

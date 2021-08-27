# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Message Commands Exceptions Module
"""
from server.exceptions.classes import WhatsappBaseException


class SendMessageException(WhatsappBaseException):
    """
    Exception class for sending a message.
    """
    _TEXT = 'Send Message'


class SendPictureException(WhatsappBaseException):
    """
    Exception class for image submission.
    """
    _TEXT = 'Send Picture'


class SendDocumentException(WhatsappBaseException):
    """
    Exception class for document submission.
    """
    _TEXT = 'Send Document'

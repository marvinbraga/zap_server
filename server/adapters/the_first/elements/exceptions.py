# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Selenium Driver Elements Exceptions Module
"""
from core.exceptions.bases import CustomBaseException


class InvalidElementName(CustomBaseException):
    """
    Exception message for invalid name.
    """
    DEFAULT_MESSAGE = 'Invalid element name.'

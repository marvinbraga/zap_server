# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

The First Selenium Whatsapp Exceptions Module
"""
from core.exceptions.bases import CustomBaseException
from core.utils.exception_info_sender import ExceptionInfoSender
from server.exceptions.classes import DefaultMessage


class DescriptionGroupsUniqueException(CustomBaseException):
    """
    Custom exception class to handle group image file format validation.
    """
    DEFAULT_MESSAGE = 'The group description will not be added in duplicate. ' \
                      'Please, enter a new group with a new description.'


class FormatTypeArchiveException(CustomBaseException):
    """
    Custom exception class to handle pdf to excel conversion file format.
    """
    DEFAULT_MESSAGE = 'Past file(s) must be in png or jpeg format.'

    def __init__(self, archive: str):
        super().__init__()
        if archive:
            self._message = f'The file passed {archive} needs to be in PNG or JPEG format.'


class CampaignsNotExistException(CustomBaseException):
    """
    Custom exception class to validate if the user registered at least one campaign so that it can be used by the user.
    """
    DEFAULT_MESSAGE = "It's necessary to register at least one campaign to be able to create a group."


class MemberNotExistException(CustomBaseException):
    """
    Class to validate if members were provided for creating a new group.
    """
    DEFAULT_MESSAGE = 'Two valid numbers are required to create group. Please, add a contact member.'


class InvalidGroupValuesException(CustomBaseException):
    """
    Exception for invalid group form parameters.
    """
    DEFAULT_MESSAGE = 'The fields "Total Groups" and "Starting Number" must be greater than zero!'


class WhatsappElementChanged(CustomBaseException):
    """
    Exception to inform about element change by Whatsapp.
    """

    def __init__(self, element):
        super().__init__(f"[{element}] {DefaultMessage.build_message('Access an invalid element in Whatsapp')}")
        self._sendmail(element)

    def _sendmail(self, element):
        """
        Send a mail to inform about the throw Whatsapp Exception.
        :param element: Used element.
        :return: None.
        """
        print('### Element Changed Error: ', self._message)
        if not element == 'search_edit':
            ExceptionInfoSender(message=self._message).send()

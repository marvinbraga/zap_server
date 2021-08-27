# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Group Commands Exceptions Module
"""
from server.exceptions.classes import WhatsappBaseException


class InitialException(WhatsappBaseException):
    """
    Class for launch exception.
    """
    _TEXT = 'Initialization'


class QuitException(WhatsappBaseException):
    """
    Exception class for exiting the messaging connection.
    """
    _TEXT = 'Quit'


class GotoMainException(WhatsappBaseException):
    """
    Exception class for the main menu go function.
    """
    _TEXT = 'Go to Home'


class RenameGroupException(WhatsappBaseException):
    """
    Exception class for renaming group.
    """
    _TEXT = 'Change Group Name'


class CreateGroupException(WhatsappBaseException):
    """
    Exception class for creating groups.
    """
    _TEXT = 'Create Group'


class SetGroupPictureException(WhatsappBaseException):
    """
    Exception to inform group image.
    """
    _TEXT = 'Change Group Name'


class GetInviteLinkForGroupException(WhatsappBaseException):
    """
    Exception to recover group link.
    """
    _TEXT = 'Get Invite Group Link'


class OnlyAdminsChangeGroupDataException(WhatsappBaseException):
    """
    Exception for only admins to change group data.
    """
    _TEXT = 'Admins Only Can Change Group Data'


class AllUsersChangeGroupDataException(WhatsappBaseException):
    """
    Exception for all users change group data.
    """
    _TEXT = 'All Users Can Change Group Data'


class OnlyAdminsSendMessagesException(WhatsappBaseException):
    """
    Exception for only admins send messages.
    """
    _TEXT = 'Admins Only Send Messages'


class AllUsersSendMessagesException(WhatsappBaseException):
    """
    Exception for all users send messages.
    """
    _TEXT = 'All Users Send Messages'


class ConnectionLostException(WhatsappBaseException):
    """
    Exception for lost connection.
    """
    _TEXT = 'Lost Connection With Whatsapp'


class ExitGroupException(WhatsappBaseException):
    """
    Exception for leaving a group.
    """
    _TEXT = 'Leave The Group'


class JoinGroupException(WhatsappBaseException):
    """
    Exception for joining a group.
    """
    _TEXT = 'Join Group'


class GroupParticipantsException(WhatsappBaseException):
    """
    Exception for retrieving group participants.
    """
    _TEXT = 'Retrieve Group Participants'


class GroupParticipantCountException(WhatsappBaseException):
    """
    Exception to recover number of group participants.
    """
    _TEXT = 'Number of Group Participants'


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


class TokenIsAlreadyConnected(WhatsappBaseException):
    """
    Exception for information that the used token is already connected.
    """
    _TEXT = 'This token is already connected'

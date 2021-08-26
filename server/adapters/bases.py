# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Whatsapp Factories Module
"""

from abc import ABCMeta, abstractmethod


class AdapterBase(metaclass=ABCMeta):
    """
    Port Class to create new adapters to messengers.
    """

    @property
    @abstractmethod
    def message(self):
        """
        Object to get messages methods.
        :return: Self.
        """
        pass

    @property
    @abstractmethod
    def group(self):
        """
        Object to get group methods.
        :return: Self.
        """
        pass

    @property
    @abstractmethod
    def person(self):
        """
        Object to get person methods.
        :return: Self.
        """
        pass

    @property
    @abstractmethod
    def manager(self):
        """
        Object to get manager methods.
        :return: Self.
        """
        pass

    @property
    @abstractmethod
    def properties(self):
        """
        Object to get properties methods.
        :return: Self.
        """
        pass


class AdapteeBase(AdapterBase):
    """
    Adaptee Base.
    """

    def __init__(self, token, no_headless=False):
        """
        Number of seconds to timeout, default 5 days Use the manager's override_timeout function to change this value.
        """
        self._no_headless = no_headless
        self._token = token

        self._object = None
        self._message = None
        self._group = None
        self._person = None
        self._manager = None
        self._properties = None

    @property
    def message(self):
        """
        Grouping of message methods.
        :return: Message object.
        """
        return self._message

    @property
    def group(self):
        """
        Grouping of group methods.
        :return: Group object.
        """
        return self._group
        pass

    @property
    def person(self):
        """
        Grouping of people methods.
        :return: Person object.
        """
        return self._person

    @property
    def manager(self):
        """
        Grouping of methods for management.
        :return: Manager object.
        """
        return self._manager

    @property
    def properties(self):
        """
        Grouping methods for properties.
        :return: Properties object.
        """
        return self._properties


class GroupAdapterBase(metaclass=ABCMeta):
    """
    Port Class to group methods.
    """

    @abstractmethod
    def participants_count(self, group_name):
        """
        Method to retrieve the number of participants in a group.
        :param group_name: Group name.
        :return:
        """
        pass

    @abstractmethod
    def get_participants(self, group_name):
        """
        Method to retrieve the names of all group members.
        :param group_name: Group name.
        :return:
        """
        pass

    @abstractmethod
    def create_group(self, group_name, members, picture_location=None):
        """
        Method to creating a new group.
        :param group_name: Group name.
        :param members: List of names to include.
        :param picture_location: Location of the group image.
        :return:
        """
        pass

    @abstractmethod
    def join_group(self, invite_link):
        """
        Method for joining a group.
        :param invite_link: Group name.
        :return:
        """
        pass

    @abstractmethod
    def get_invite_link(self, group_name):
        """
        Method to retrieve group link.
        :param group_name: Group name.
        :return:
        """
        pass

    @abstractmethod
    def exit_group(self, group_name):
        """
        Method for leaving a group.
        :param group_name: Group name.
        :return:
        """
        pass


class MessageAdapterBase(metaclass=ABCMeta):
    """
    Port Class to message methods.
    """

    @abstractmethod
    def send_message(self, name, message):
        """
        Method for sending messages.
        :param name: To whom the message goes.
        :param message: Text message.
        :return:
        """
        pass

    @abstractmethod
    def send_blind_message(self, message):
        """
        Message for active chat.
        *Avoid using this method.*
        :param message: Text message.
        :return:
        """
        pass

    @abstractmethod
    def send_anon_message(self, phone, text):
        """
        Message to a phone number.
        *Avoid using this method as the SIM card may be blocked.*
        :param phone: Phone number.
        :param text: Text message.
        :return:
        """
        pass

    @abstractmethod
    def send_picture(self, name, picture_location, caption=None):
        """
        Method for sending images.
        :param name: Name of person or group.
        :param picture_location: Image path.
        :param caption: Text message (optional).
        :return:
        """
        pass

    @abstractmethod
    def send_document(self, name, document_location):
        """
        Method for sending document.
        :param name: Name of person or group.
        :param document_location: Image path.
        :return:
        """
        pass

    @abstractmethod
    def get_last_message_for(self, name):
        """
        Method to get the last message from a contact.
        :param name: Contact name.
        :return:
        """
        pass

    @abstractmethod
    def is_message_present(self, username, message):
        """
        Method to check if a message is present in the contact's chat.
        :param username: Contact name.
        :param message: Text message.
        :return:
        """
        pass

    @abstractmethod
    def get_starred_messages(self, delay=10):
        """
        Recovers messages marked as favorites.
        :param delay: Delay (optional).
        :return:
        """
        pass


class PersonAdapterBase(metaclass=ABCMeta):
    """
    Port to People methods.
    """

    @abstractmethod
    def get_status(self, name):
        """
        Method for retrieving a contact's status.
        :param name: Contact name.
        :return:
        """
        pass

    @abstractmethod
    def get_last_seen(self, name, timeout=10):
        """
        Retrieve the last read message from a contact.
        :param name: Contact name.
        :param timeout: Timeout (optional).
        :return:
        """
        pass


class ManagerAdapterBase(metaclass=ABCMeta):
    """
    Port to Management Methods.
    """

    @abstractmethod
    def goto_home(self):
        """
        Method to go to main page.
        :return:
        """
        pass

    @abstractmethod
    def clear_chat(self, name):
        """
        Method to clear the chat.
        :param name: Contact or group name.
        :return:
        """
        pass

    @abstractmethod
    def override_timeout(self, new_timeout):
        """
        Method to increase timeout.
        :param new_timeout: Time to add.
        :return:
        """
        pass

    @abstractmethod
    def get_profile_pic(self, name):
        """
        Method to retrieve the profile image.
        :param name: Contact or group name.
        :return:
        """
        pass

    @abstractmethod
    def unread_user_names(self, scrolls=100):
        """
        Method for usernames that have unread messages.
        :param scrolls: Scroll (optional).
        :return:
        """
        pass

    @abstractmethod
    def get_driver(self):
        """
        Method to recover the drive (browser).
        :return:
        """
        pass

    @abstractmethod
    def quit(self):
        """
        Method to exit browser.
        :return:
        """
        pass


class PropertiesAdapterBase(metaclass=ABCMeta):
    """
    This class has the function of being base to return all the properties of the whatsapp object already created.
    """

    @abstractmethod
    def get_qrcode(self):
        """
        This method is the signature of the function that will be responsible for retrieving the qrcode image
        from whatsapp.
        """
        pass

    @abstractmethod
    def check_point(self):
        """
        This method checks if the main screen of whatsapp web is available.
        :return: String 'true' ou 'false'.
        """
        pass

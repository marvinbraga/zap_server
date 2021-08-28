# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Mock Adapter Module
"""
import json
import secrets
from random import randint
from time import sleep

from core.utils.classes import MessageConsole
from core.utils.qr_code.classes import QrCode
from server.commands.groups.exceptions import RenameGroupException, GotoMainException, CreateGroupException, \
    SetGroupPictureException
from server.commands.messages.exceptions import SendMessageException, SendPictureException, SendDocumentException
from server.commands.properties.exceptions import ConnectionLostException


class MockPrintConsole:
    """
    Class to print mock infos in console.
    """

    def __init__(self):
        self.cs = MessageConsole()

    def show(self, token, message):
        """
        Method to present message to console.
        :param token: User token.
        :param message: Message to display.
        :return: Self.
        """
        self.cs.show(f'MOCK MESSAGE => Token<{token}>: {message}')
        return self


class MockWhatsapp:
    """
    Mock class for selenium controller with Whatsapp.
    """

    def __init__(self, token, timeout=1000, print_console=MockPrintConsole()):
        self._token = token
        self.cs = print_console
        self.timeout = timeout
        self._free_for_use = True

    def check_point(self) -> str:
        """
        Checks if the main screen of whatsapp web is available.
        :return: string 'true' or 'false'
        """
        result = 'false'
        if self._free_for_use:
            sleep(4)
            result = 'true'
        return result

    @property
    def get_signin_qrcode(self) -> str:
        """
        It retrieves the image from the qr-code shown in the sign in of Whatsapp, here you can add a signal informing
        the capture of the image.
        :return: Json with QrCode and path information.
        """
        self._free_for_use = False
        try:
            file_name = f'qrcode_{secrets.token_hex(nbytes=8)}.png'
            img = {
                'file_name': file_name,
                'image': QrCode(data='Whatsapp Test.').as_base64()
            }
            result = json.dumps(img, ensure_ascii=False)
        finally:
            self._free_for_use = True
        return result

    @staticmethod
    def is_connected(refresh=True):
        """
        Check if you are connected with Whatsapp.
        :param refresh: Refresh Browser.
        :return: Bool.
        """
        result = True
        if refresh:
            if randint(1, 100) % 99 == 0:
                raise ConnectionLostException()
            elif randint(1, 100) % 50 == 0:
                result = False
        return result

    def send_message(self, name: str, message: str):
        """
        This method is used to send the message to the individual person or a group.
        :param name: Str with contact or group name.
        :param message: Str Bool.
        """
        if randint(1, 100) % 99 == 0:
            raise SendMessageException()
        msg = f'name: {name}, message: {message}'
        self.cs.show(self._token, msg)
        return 'True'

    def rename_group(self, old_name, new_name):
        """
        This method is for renaming Whatsapp groups.
        :param old_name: With the group's old name.
        :param new_name: With the group's new name.
        :return: Bool.
        """
        if randint(1, 100) % 99 == 0:
            raise RenameGroupException()
        msg = f'[rename_group] old_name: {old_name}, new_name: {new_name}'
        self.cs.show(self._token, msg)
        return True

    def participants_count_for_group(self, group_name):
        """
        Retrieves the number of participants in a group.
        :param group_name: Group Name.
        :return: Int.
        """
        msg = f'[participants_count_for_group] group_name: {group_name}'
        self.cs.show(self._token, msg)
        participants_count = randint(2, 12)
        return participants_count

    def get_group_participants(self, group_name):
        """
        Retrieve the participants of a group.
        :param group_name: Group name.
        :return:
        """
        msg = f'[get_group_participants] group_name: {group_name}'
        self.cs.show(self._token, msg)
        total = randint(1, 12)
        participants = [f'Participant {x}' for x in range(total)]
        return participants

    def goto_main(self):
        """
        Opens the Whatsapp home screen in the browser.
        :return: Bool.
        """
        if randint(1, 100) % 99 == 0:
            raise GotoMainException()
        msg = '[goto_main]'
        self.cs.show(self._token, msg)
        return True

    def get_status(self, name):
        """
        This method retrieves the status of the Whatsapp contact.
        :param name: Contact name.
        :return: Str.
        """
        msg = f'[get_status] name: {name}'
        self.cs.show(self._token, msg)
        return msg

    def get_last_seen(self, name, timeout=10):
        """
        Checks the last user check.
        :param name: Contact's name.
        :param timeout: Int.
        :return: Str.
        """
        msg = f'[get_last_seen] name: {name}, timeout: {timeout}'
        self.cs.show(self._token, msg)
        return msg

    def send_blind_message(self, message):
        """
        Send a blind message.
        :param message: Text message.
        :return: Bool.
        """
        msg = f'[send_blind_message] message: {message}'
        self.cs.show(self._token, msg)
        return True

    def send_picture(self, name, picture_location, caption=None):
        """
        Send a picture.
        :param name: Contact or group name.
        :param picture_location: Picture path.
        :param caption: Text.
        :return: Bool.
        """
        if randint(1, 100) % 99 == 0:
            raise SendPictureException()
        msg = f'[send_picture] name: {name}, picture_location: {picture_location}, caption: {caption}'
        self.cs.show(self._token, msg)
        return True

    def send_document(self, name, document_location):
        """
        Send a document.
        :param name: Contact or group name.
        :param document_location: Document path.
        :return: Bool.
        """
        if randint(1, 100) % 99 == 0:
            raise SendDocumentException()
        msg = f'[send_document] name: {name}, document_location: {document_location}'
        self.cs.show(self._token, msg)
        return True

    def clear_chat(self, name):
        """
        Clears the contact's chat.
        :param name: Contact's name.
        :return: Bool.
        """
        msg = f'[clear_chat] name: {name}'
        self.cs.show(self._token, msg)
        return True

    def override_timeout(self, new_timeout):
        """
        Update timeout.
        :param new_timeout: New timeout value.
        :return: Bool.
        """
        self.timeout = new_timeout
        return True

    def get_profile_pic(self, name):
        """
        This method retrieves the contact's profile image.
        :param name: Contact name.
        :return: Bool.
        """
        msg = f'[get_profile_pic] name: {name}'
        self.cs.show(self._token, msg)
        return True

    def create_group(self, group_name, members, picture_location=None):
        """
        In this method you create a group on Whatsapp.
        :param group_name: Group name.
        :param members: Initial members list.
        :param picture_location: Group picture location.
        :return: Bool.
        """
        if randint(1, 100) % 99 == 0:
            raise CreateGroupException()
        sleep(4)
        msg = f'[create_group] group_name: {group_name}, members: {members}, picture_location: {picture_location}'
        self.cs.show(self._token, msg)
        return True

    def set_group_picture(self, group_name, picture_location):
        """
        This method updates the image of a group.
        :param group_name: Group name.
        :param picture_location: Group picture location.
        :return: Bool.
        """
        if randint(1, 100) % 99 == 0:
            raise SetGroupPictureException()
        msg = f'[set_group_picture] group_name: {group_name}, picture_location: {picture_location}'
        self.cs.show(self._token, msg)
        return True

    def join_group(self, invite_link):
        """
        Join a Whatsapp group.
        :param invite_link: Group link.
        :return: Bool.
        """
        msg = f'[join_group] invite_link: {invite_link}'
        self.cs.show(self._token, msg)
        return True

    def get_invite_link_for_group(self, group_name):
        """
        Retrieve the group link.
        :param group_name: Group's name.
        :return: Str.
        """
        msg = f'[get_invite_link_for_group] group_name: {group_name}'
        self.cs.show(self._token, msg)
        return 'https://whatsapp.com/link/group_registration_link'

    def only_admins_change_group_data(self, group_name):
        """
        Only administrators change group data.
        :param group_name: Group's name.
        :return: Bool.
        """
        msg = f'[only_admins_change_group_data] group_name: {group_name}'
        self.cs.show(self._token, msg)
        return True

    def all_users_change_group_data(self, group_name):
        """
        All users can change group data.
        :param group_name: Group's name.
        :return: Bool.
        """
        msg = f'[all_users_change_group_data] group_name: {group_name}'
        self.cs.show(self._token, msg)
        return True

    def only_admins_send_messages(self, group_name):
        """
        Only administrators can send messages.
        :param group_name: Group's name.
        :return: Bool.
        """
        msg = f'[only_admins_send_messages] group_name: {group_name}'
        self.cs.show(self._token, msg)
        return True

    def all_users_send_messages(self, group_name):
        """
        All users can send messages.
        :param group_name: Group's name.
        :return: Bool.
        """
        msg = f'[all_users_send_messages] group_name: {group_name}'
        self.cs.show(self._token, msg)
        return True

    def exit_group(self, group_name):
        """
        Leave a group.
        :param group_name: Group's name.
        :return: Bool.
        """
        msg = f'[exit_group] group_name: {group_name}'
        self.cs.show(self._token, msg)
        return True

    def send_anon_message(self, phone, text):
        """
        Send an anonymous message.
        :param phone: Phone number.
        :param text: Text message.
        :return: Bool.
        """
        msg = f'[send_anon_message] phone: {phone}, text: {text}'
        self.cs.show(self._token, msg)
        return True

    @staticmethod
    def is_message_present(username, message):
        """
        Checks if a message is present in the chat.
        :param username: Contact's name.
        :param message: Text message.
        :return: Bool.
        """
        _, _ = username, message
        if randint(1, 100) % 2 == 0:
            return True
        else:
            return False

    @staticmethod
    def get_starred_messages(delay=10):
        """
        Recovers Favorite Messages.
        :param delay: Int.
        :return: List.
        """
        _ = delay
        starred_messages = ['Starred Message 01', 'Starred Message 02']
        return starred_messages

    @staticmethod
    def unread_usernames(scrolls=100):
        """
        Contacts with unread messages.
        :param scrolls: Int.
        :return: List.
        """
        _ = scrolls
        usernames = ['User 1', 'User 2']
        usernames = list(set(usernames))
        return usernames

    @staticmethod
    def get_driver():
        """
        Recover the browser.
        :return: Object.
        """
        return None

    @staticmethod
    def get_last_message_for(name):
        """
        Retrieves the contact's last message.
        :param name: Contact's name.
        :return: List.
        """
        _ = name
        messages = list()
        return messages

    @staticmethod
    def quit():
        """
        Closes browser connection.
        :return: Bool.
        """
        result = True
        return result

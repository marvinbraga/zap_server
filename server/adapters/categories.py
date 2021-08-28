# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Categories Adapters Module
"""
from server.adapters.bases import MessageAdapterBase, PersonAdapterBase, GroupAdapterBase, ManagerAdapterBase, \
    PropertiesAdapterBase
from server.adapters.utils import SaveFile


class MessageAdapterWhatsApp(MessageAdapterBase):
    """
    Interface to message methods.
    """

    def __init__(self, wa_object):
        self.wa_object = wa_object

    def send_message(self, name, message):
        """
        Method for sending messages.
        :param name: Contact name.
        :param message: Message text.
        :return:
        """
        return self.wa_object.send_message(name=name, message=message)

    def send_blind_message(self, message):
        """
        Message for active chat.
        *Avoid using this method.*
        :param message: Message text.
        :return:
        """
        self.wa_object.send_blind_message(message=message)
        return self

    def send_anon_message(self, phone, text):
        """
        Message to a phone number.
        Avoid using this method as the SIM card may be blocked.
        :param phone: Phone number.
        :param text: Message text.
        :return:
        """
        self.wa_object.send_anon_message(phone=phone, text=text)
        return self

    def send_picture(self, name, picture_location, caption=None):
        """
        Method for sending images.
        :param name: Contact or group name.
        :param picture_location: Image path.
        :param caption: Text (optional).
        :return:
        """
        self.wa_object.send_picture(name=name, picture_location=picture_location, caption=caption)
        return self

    def send_document(self, name, document_location):
        """
        Method for sending document.
        :param name: Contact or group name.
        :param document_location: Image path.
        :return:
        """
        self.wa_object.send_document(name=name, document_location=document_location)
        return self

    def get_last_message_for(self, name):
        """
        Method to get the last message from a contact.
        :param name: Contact name.
        :return:
        """
        return self.wa_object.get_last_message_for(name=name)

    def is_message_present(self, username, message):
        """
        Method to check if a message is present in the contact's chat.
        :param username: Contact name.
        :param message: Text of the message.
        :return:
        """
        return self.wa_object.is_message_present(username=username, message=message)

    def get_starred_messages(self, delay=10):
        """
        Recovers messages marked as favorites.
        :param delay: Delay (optional).
        :return:
        """
        return self.wa_object.get_starred_messages(delay=delay)


class PersonAdapterWhatsApp(PersonAdapterBase):
    """
    Interface to People methods.
    """

    def __init__(self, wa_object):
        self.wa_object = wa_object

    def get_status(self, name):
        """
        Method for retrieving a contact's status.
        :param name: Contact name.
        :return:
        """
        return self.wa_object.get_status(name=name)

    def get_last_seen(self, name, timeout=10):
        """
        Retrieves the last message read from a contact.
        :param name: Contact name.
        :param timeout: Timeout (optional).
        :return:
        """
        return self.wa_object.get_last_seen(name=name, timeout=timeout)


class GroupAdapterWhatsApp(GroupAdapterBase):
    """
    Interface to group methods.
    """

    def __init__(self, wa_object):
        self.wa_object = wa_object

    def _adjust_image(self, picture_location):
        """
        Method for adjusting the image path.
        Download the image and save it to local folder.
        :param picture_location: Location of the image on the server.
        :return: self.
        """
        print('1. create_group:', picture_location)
        SaveFile(picture_location).from_url()
        print('2. create_group:', picture_location)
        return self

    def create_group(self, group_name, members, picture_location=None):
        """
        Method for creating a new group.
        :param group_name: Group's name.
        :param members: List of names to include.
        :param picture_location: Location of the group image.
        :return:
        """
        self._adjust_image(picture_location)
        return self.wa_object.create_group(
            group_name=group_name, members=members, picture_location=picture_location)

    def get_invite_link(self, group_name):
        """
        Method to retrieve group link.
        :param group_name: Group's name.
        :return:
        """
        return self.wa_object.get_invite_link_for_group(group_name=group_name)

    def rename(self, old_name, new_name):
        """
        Method for renaming groups.
        :param old_name: Old group's name.
        :param new_name: New group's name.
        :return:
        """
        return self.wa_object.rename_group(old_name=old_name, new_name=new_name)

    def set_picture(self, group_name, picture_location):
        """
        Method to change group image.
        :param group_name: Group's name.
        :param picture_location: Image location.
        :return:
        """
        self._adjust_image(picture_location)
        return self.wa_object.set_group_picture(group_name=group_name, picture_location=picture_location)

    def only_admins_send_messages(self, group_name):
        """
        Method to configure that only admins send messages.
        :param group_name: Group's name.
        :return:
        """
        return self.wa_object.only_admins_send_messages(group_name=group_name)

    def all_users_send_messages(self, group_name):
        """
        Method to configure that all contacts send messages.
        :param group_name: Group's name.
        :return:
        """
        return self.wa_object.all_users_send_messages(group_name=group_name)

    def only_admins_change_group_data(self, group_name):
        """
        Method to configure that only admins change group data.
        :param group_name: Group's name.
        :return:
        """
        return self.wa_object.only_admins_change_group_data(group_name=group_name)

    def all_users_change_group_data(self, group_name):
        """
        Method to configure that all users change group data.
        :param group_name: Group's name.
        :return:
        """
        return self.wa_object.all_users_change_group_data(group_name=group_name)

    def participants_count(self, group_name):
        """
        Method to retrieve the number of participants in a group.
        :param group_name: Group's name.
        :return:
        """
        return self.wa_object.participants_count_for_group(group_name=group_name)

    def get_participants(self, group_name):
        """
        Method to retrieve the names of all group members.
        :param group_name: Group's name.
        :return:
        """
        return self.wa_object.get_group_participants(group_name=group_name)

    def join_group(self, invite_link):
        """
        Method for joining a group.
        :param invite_link: Group link.
        :return:
        """
        self.wa_object.join_group(invite_link=invite_link)
        return self

    def exit_group(self, group_name):
        """
        Method for leaving a group.
        :param group_name: Group's name.
        :return:
        """
        self.wa_object.exit_group(group_name=group_name)
        return self


class ManagerAdapterWhatsApp(ManagerAdapterBase):
    """
    Interface to Management Methods.
    """

    def __init__(self, wa_object):
        self.wa_object = wa_object

    def goto_home(self):
        """
        Method to go to main page.
        :return:
        """
        self.wa_object.goto_main()
        return self

    def clear_chat(self, name):
        """
        Method to clear the chat.
        :param name: Contact or group name.
        :return:
        """
        self.wa_object.clear_chat(name=name)
        return self

    def override_timeout(self, new_timeout):
        """
        Method to increase timeout.
        :param new_timeout: Time to add.
        :return:
        """
        self.wa_object.override_timeout(new_timeout=new_timeout)
        return self

    def get_profile_pic(self, name):
        """
        Method to retrieve the profile image.
        :param name: Contact or group name.
        :return:
        """
        self.wa_object.get_profile_pic(name=name)
        return self

    def unread_user_names(self, scrolls=100):
        """
        Method for usernames that have unread messages.
        :param scrolls: Scroll (optional).
        :return:
        """
        return self.wa_object.unread_usernames(scrolls=scrolls)

    def get_driver(self):
        """
        Method to recover the drive (browser).
        :return:
        """
        return self.wa_object.get_driver()

    def quit(self):
        """
        Method to exit browser.
        :return:
        """
        return self.wa_object.quit()


class PropertiesAdapterWhatsApp(PropertiesAdapterBase):
    """
    This class has the function of being an adapter of the properties of the whatsapp object.
    """

    def __init__(self, wa_object):
        self.wa_object = wa_object

    def get_qrcode(self):
        """
        Retrieve whatsapp web access qr-code image to login.
        :return:
        """
        return self.wa_object.get_signin_qrcode

    def check_point(self):
        """
        Returns 'true' if whatsapp web main screen is available.
        :return:
        """
        return self.wa_object.check_point()

    def is_connected(self):
        """
        Check if you are connected with Whatsapp.
        :return:
        """
        return self.wa_object.is_connected()


class MockGroupAdapterWhatsApp(GroupAdapterWhatsApp):
    """
    Class overrides group creation method.
    """

    def create_group(self, group_name, members, picture_location=None):
        """
        Method for creating a new group.
        :param group_name: Group's name.
        :param members: List of names to include.
        :param picture_location: Location of the group image.
        :return:
        """
        return self.wa_object.create_group(
            group_name=group_name, members=members, picture_location=picture_location)

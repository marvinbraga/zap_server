# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

The First Adapter Tests Module
*These tests cannot currently be run by Github Actions as they require authentication via QR-Code.
However it must be done locally.*
"""
import os
from datetime import datetime
from time import sleep, strftime

import pytest

from core.settings import BASE_DIR, TEST_CONTACT_GROUP_MEMBER
from server.adapters.the_first.classes import WhatsApp
from server.commands.properties.exceptions import ConnectionLostException


class WhatsappConnected:
    """
    Class for retrieves a connected instance of Whatsapp.
    """
    _instance = None

    def __init__(self):
        if not self._instance:
            self._instance = WhatsApp(
                wait=500000, token='B9dK01w5KgiLCrrETlzyTh7spwJqMRXhESLcPRC_vaE', no_headless=True)

    @property
    def instance(self):
        """
        Returns the instance of the loaded Whatsapp object.
        :return: Whatsapp Object.
        """
        return self._instance


whatsapp = WhatsappConnected().instance


def get_resource(file_name):
    """
    Method to retrieve the path a file in the resource directory.
    :param file_name: Path to resource file.
    :return: File Path.
    """
    return os.path.normpath(
        os.path.join(f'{BASE_DIR}/server/adapters/the_first/tests/resources/', file_name))


@pytest.fixture
def initialize_whatsapp():
    """
    Initializes Whatsapp object.
    :return: Instance.
    """
    global whatsapp
    result = whatsapp.connect() if whatsapp else False
    return result


def test_instance(initialize_whatsapp):
    """
    Checks if you managed to instantiate the Whatsapp object.
    :param initialize_whatsapp: Object.
    :return: None.
    """
    assert initialize_whatsapp


def test_get_qr_code():
    """
    Check if the QR-Code is being generated.
    :return: None.
    """
    global whatsapp
    sleep(7)
    result = False
    if whatsapp:
        qr_code = whatsapp.get_signin_qrcode
        result = qr_code != 'False'
    assert result


def is_connected():
    """
    Check if you closed the connection with Whatsapp.
    :return: None.
    """
    global whatsapp
    nr = 0
    result = False
    while nr < 25:
        try:
            result = whatsapp.is_connected(False)
        except ConnectionLostException:
            sleep(1)
        else:
            if result:
                break
            else:
                sleep(1)
        nr += 1
    assert result


def test_create_group():
    """
    Test to see if you can create a group on Whatsapp.
    :return: None.
    """
    global whatsapp
    sleep(7)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        picture = get_resource('picture01.jpg')
        members = [TEST_CONTACT_GROUP_MEMBER]
        try:
            result = whatsapp.create_group(group, members, picture)
        except Exception as e:
            print(e)
            result = False

    assert result


def test_only_admins_change_data():
    """
    Test to verify the only_admins_change_group_data method.
    :return: None.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        try:
            whatsapp.only_admins_change_group_data(group)
            result = True
        except Exception as e:
            print(e)
            result = False
    assert result


def test_only_admins_send_messages():
    """
    Test to verify the only_admins_send_messages method.
    :return: None.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        try:
            whatsapp.only_admins_send_messages(group)
            result = True
        except Exception as e:
            print(e)
            result = False
    assert result


def test_all_users_send_messages():
    """
    Test to verify the all_users_send_messages method.
    :return: None.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        try:
            whatsapp.all_users_send_messages(group)
            result = True
        except Exception as e:
            print(e)
            result = False
    assert result


def test_send_messages():
    """
    Test to verify the send_message method.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        try:
            whatsapp.send_message(group, 'Hi! Be very welcome. :-D')
            result = True
        except Exception as e:
            print(e)
            result = False
    assert result


def test_get_invite_link_for_group():
    """
    Test to verify the get_invite_link_for_group method.
    :return: None.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        try:
            link = whatsapp.get_invite_link_for_group(group)
            result = True
        except Exception as e:
            print(e)
            result = False
        else:
            try:
                whatsapp.send_message(group, link)
            except Exception as e:
                print(e)
    assert result


def test_set_group_picture():
    """
    Test to verify the set_group_picture method.
    :return: None.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        picture = get_resource('picture02.jpg')
        try:
            whatsapp.set_group_picture(group, picture)
            result = True
        except Exception as e:
            print(e)
            result = False
    assert result


def test_send_picture():
    """
    Test to verify the send_picture method.
    :return: None.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        picture = get_resource('picture01.jpg')
        try:
            whatsapp.send_picture(group, picture)
            result = True
        except Exception as e:
            print(e)
            result = False
    assert result


def test_send_document():
    """
    Test to verify the send_document method.
    :return: None.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        doc = get_resource('test_doc.pdf')
        try:
            whatsapp.send_document(group, doc)
            result = True
        except Exception as e:
            print(e)
            result = False
    assert result


def test_rename_group():
    """
    Test to verify the send_message method.
    :return: None.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        group = 'TEST GROUP'
        try:
            strftime('%Y')
            whatsapp.rename_group(group, 'TEST GROUP ' + datetime.now().strftime('%Y%m%d%H%M%S'))
            result = True
        except Exception as e:
            print(e)
            result = False
    assert result


def test_close_whatsapp():
    """
    Test to close the Whatsapp window.
    :return: None.
    """
    global whatsapp
    sleep(3)
    result = is_connected
    if result:
        try:
            whatsapp.quit()
        except Exception as e:
            print(e)
            result = False
    assert result

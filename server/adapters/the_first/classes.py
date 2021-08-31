# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

The First Selenium Whatsapp Adapter Module
"""
import base64
import datetime as dt
import json
import os
import pickle
import secrets
from io import BytesIO
from threading import Thread
from time import sleep
from urllib.parse import urlencode

from PIL import Image
from bs4 import BeautifulSoup

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.ui import WebDriverWait

from core.utils.browsers.classes import BrowserType
from core.utils.browsers.local_storage import LocalStorage
from core.utils.numbers_gen import SleepRandom
from core.utils.qr_code.classes import QrCode
from server.adapters.the_first.elements.drivers import DriveElements
from server.adapters.the_first.exceptions import WhatsappElementChanged
from server.commands.groups.exceptions import InitialException, RenameGroupException, GotoMainException, \
    CreateGroupException, SetGroupPictureException, GetInviteLinkForGroupException, \
    OnlyAdminsChangeGroupDataException, OnlyAdminsSendMessagesException, AllUsersSendMessagesException
from server.commands.messages.exceptions import SendMessageException, SendDocumentException
from server.commands.properties.exceptions import ConnectionLostException


class WhatsApp:
    """
    This class provides access to Whatsapp Web through Selenium.
    """
    _TIMEOUT_EXCEPTION_TEXT = 'Your request has been timed out. Please, try overriding timeout.'

    def __init__(self, wait: int, token=None, session=None, no_headless=False):
        self._no_headless = no_headless
        self._token = token
        self.session = session
        self.emoji = {}
        self.timeout = wait
        self._free_for_use = True
        self.driver = None
        self.browser = None
        self.search_elements = None

    def __del__(self):
        if self.driver:
            if self.browser:
                self._save_storage()
            del self.driver
            self.browser = None

    def _load_storage(self):
        storage = LocalStorage(driver=self.browser, token=self._token, init_js=True)
        profile, exists = storage.load()
        if exists:
            for key in profile:
                storage.set(key, profile[key])
        return self

    def _save_storage(self):
        """
        Save Browser Local Storage.
        :return: Self.
        """
        def execute(browser, token):
            """
            Thread Execute Method.
            :param browser: Selenium browser.
            :param token: User token.
            :return: None.
            """
            LocalStorage(driver=browser, token=token, init_js=True).save()

        t = Thread(target=execute, args=[self.browser, self._token])
        t.start()
        t.join(timeout=7.0)

        return self

    def _get_cookies(self):
        """
        Recovers cookies if file exists.
        :return: None.
        """
        if self.driver.save_cookies and os.path.isfile(self.driver.cookies_file):
            cookies = pickle.load(open(self.driver.cookies_file, 'rb'))
            for cookie in cookies:
                self.browser.add_cookie(cookie)

    def connect(self, screenshot=None):
        """
        Connect with to Whatsapp Web Application.
        :param screenshot: To Save a Browser Screenshot.
        :return: Bool.
        """
        try:
            self.driver = BrowserType.FIREFOX.new_instance(token=self._token, no_headless=self._no_headless)
            self.browser = self.driver.browser
            self.search_elements = DriveElements(self.browser)
            self.browser.set_window_size(1600, 1200)
            self.browser.get("https://web.whatsapp.com/")
            self._load_storage()._get_cookies()
        except Exception:
            raise InitialException()

        if screenshot:
            self.browser.save_screenshot(screenshot)
        return True

    def get_element(self, element_name):
        """
        Short method to retrieve the element.
        :param element_name: String with the element name identification.
        :return: Selenium Element.
        """
        try:
            result = self.search_elements.get_element(element_name=element_name)
        except NoSuchElementException:
            raise WhatsappElementChanged(element=element_name)
        return result

    def get_presence_of_element(self, element_name):
        """
        Short method to retrieve an element awaiting its presence.
        :param element_name: Selenium Element Name.
        :return: Selenium Element.
        """
        try:
            result = self.search_elements.get_presence_of_element(element_name=element_name)
        except NoSuchElementException:
            raise WhatsappElementChanged(element=element_name)
        return result

    def wait_for_element(self, element_name, time_out=10):
        """
        Short method to retrieve an element awaiting its presence.
        :param element_name: Selenium Element Name.
        :param time_out: Int.
        :return: Selenium Element.
        """
        local_timeout = self.timeout
        if time_out:
            local_timeout = time_out
        try:
            result = WebDriverWait(self.browser, local_timeout).until(exp_cond.presence_of_element_located(
                self.get_presence_of_element(element_name=element_name)))
        except NoSuchElementException:
            raise WhatsappElementChanged(element=element_name)
        return result

    def check_point(self) -> str:
        """
        Checks if the main screen of whatsapp web is available.
        :return: String Bool.
        """
        result = 'false'
        if self.driver and self._free_for_use:
            try:
                elem = self.get_element('search_edit')
            except WhatsappElementChanged:
                result = 'false'
            else:
                if elem:
                    result = 'true'
        return result

    def _retry_for_qr_code(self):
        """
        Performs a forced check by QR-Code.
        :return: Selenium Element.
        """
        self.browser.refresh()
        SleepRandom(end_number=3.0, start_number=2.5).execute()

        max_attempt = 5
        attempt = 0
        elem = None
        while attempt < max_attempt:
            try:
                self.is_connected(refresh=False)
                return "True"
            except ConnectionLostException as e:
                print(e)
                try:
                    elem = self.wait_for_element('qr_code', 4)
                    break
                except TimeoutException as e:
                    print(e)
                attempt += 1
        return elem

    @property
    def get_signin_qrcode(self) -> str:
        """
        It retrieves the image from the qr-code shown in the sign in of Whatsapp, here you can add a signal informing
        the capture of the image.
        :return: String Boll or Image Json.
        """
        result = 'False'
        self._free_for_use = False
        try:
            if self.driver is None:
                self.connect()

            try:
                elem = self.wait_for_element('qr_code', 22)
            except TimeoutException:
                elem = self._retry_for_qr_code()
                if elem == 'True':
                    return elem

            if elem:
                qr_code = Image.open(BytesIO(base64.b64decode(elem.screenshot_as_base64)))
                file_name = f'qrcode_{secrets.token_hex(nbytes=8)}.png'
                img = {
                    'file_name': file_name,
                    'image': QrCode(data=QrCode.decode_from_image(qr_code)['data']).as_base64()
                }
                result = json.dumps(img, ensure_ascii=False)
        finally:
            self._free_for_use = True
        return result

    def is_connected(self, refresh=True):
        """
        Method to check if you have an active connection with Selenium.
        :param refresh: Browser Refresh.
        :return: Bool.
        """
        if self.driver is None:
            return False

        result = False
        try:
            if self.get_element('search_edit'):
                result = True
        except Exception as e:
            print(e)
            if self.browser and refresh:
                self.browser.refresh()
            raise ConnectionLostException()
        return result

    def send_message(self, name, message):
        """
        This method is used to send the message to the individual person or a group.
        :param name: Contact or Group Name.
        :param message: Text Message.
        :return: String Bool.
        """
        try:
            message = self.emojify(message)
            self.access_search_panel(name)
            send_msg = self.wait_for_element('send_message')
            is_http = message.find('http') > -1

            messages = message.split("\n")
            for msg in messages:
                send_msg.send_keys(msg)
                send_msg.send_keys(Keys.SHIFT + Keys.ENTER)
            if is_http:
                SleepRandom(end_number=3.0, start_number=2.0).execute()
            send_msg.send_keys(Keys.ENTER)
            SleepRandom(end_number=2.1, start_number=1.2).execute()
        except Exception as e:
            print(e)
            raise SendMessageException()
        return 'True'

    def access_search_panel(self, search_name):
        """
        Run Whatsapp Search Panel Access.
        :param search_name: Contact or Group Name.
        :return: Self.
        """
        search = self.get_element('search_edit')
        search.clear()
        search.send_keys(search_name + Keys.ENTER)
        SleepRandom(end_number=2.1, start_number=1.1).execute()
        return self

    def access_group_panel(self):
        """
        Run Whatsapp Group Panel Access.
        :return: Self.
        """
        try:
            click_menu = self.wait_for_element('group_menu_button')
            click_menu.click()
        except TimeoutException:
            raise TimeoutError(self._TIMEOUT_EXCEPTION_TEXT)
        except NoSuchElementException:
            return self
        except Exception as e:
            print(e)
            return None
        SleepRandom(1.7).execute()
        return self

    def close_group_panel(self):
        """
        Close Whatsapp Group Panel.
        :return: Self.
        """
        SleepRandom(0.7).execute()
        close = self.get_element('group_close_panel_btn')
        close.click()
        return self

    def rename_group(self, old_name, new_name):
        """
        Run Whatsapp function to rename groups.
        :param old_name: Str.
        :param new_name: Str.
        :return: Bool.
        """
        try:
            self.access_search_panel(old_name)
            self.get_element('group_menu').click()
            SleepRandom(0.9).execute()
            data_button = self.wait_for_element('group_data_button')
            data_button.click()
            SleepRandom(0.9).execute()
            rename_button = self.get_element('group_edit_button')
            rename_button.click()
            SleepRandom(0.7).execute()
            group_name_text = self.get_element('group_name_edit')
            group_name_text.clear()
            group_name_text.send_keys(new_name + Keys.ENTER)
            self.close_group_panel()
        except Exception as e:
            print(e)
            raise RenameGroupException()
        return True

    def participants_count_for_group(self, group_name):
        """
        Count the number of participants for the group name provided.
        TODO: Adjust this method.
        :param group_name: Group Name.
        :return: Int.
        """
        if self.access_search_panel(group_name).access_group_panel() is None:
            return 0
        current_time = dt.datetime.now()
        participants_selector = self.search_elements.get_element_path('participants_selector')
        while True:
            try:
                participants_count = self.browser.find_element_by_css_selector(participants_selector).text
                if 'participants' in participants_count:
                    return participants_count
            except Exception as e:
                print(e)
            new_time = dt.datetime.now()
            elapsed_time = (new_time - current_time).seconds
            if elapsed_time > self.timeout:
                return 0

    def get_group_participants(self, group_name):
        """
        Get participants for the group name provided.
        TODO: Adjust this method.
        :param group_name: Group Name.
        :return: List.
        """
        self.participants_count_for_group(group_name)
        if self.access_search_panel(group_name) is None:
            return []
        try:
            click_menu = self.wait_for_element('main_menu')
            click_menu.click()
        except TimeoutException:
            raise TimeoutError(self._TIMEOUT_EXCEPTION_TEXT)
        except NoSuchElementException:
            return []
        except Exception as e:
            print(e)
            return []
        sleep_random = SleepRandom(1.1)
        sleep_random.execute()

        participants = []
        scrollbar = self.get_element('scroll_bar')
        for v in range(1, 70):
            print(v)
            self.browser.execute_script('arguments[0].scrollTop = ' + str(v * 300), scrollbar)
            sleep(0.10)
            elements = self.browser.find_elements_by_tag_name("span")
            for element in elements:
                try:
                    html = element.get_attribute('innerHTML')
                    soup = BeautifulSoup(html, "html.parser")
                    class_participant_1 = self.search_elements.get_element_path('participant_1')
                    for i in soup.find_all("span", class_=class_participant_1):  # '_3TEwt'
                        if i.text not in participants:
                            participants.append(i.text)
                            print(i.text)
                except Exception as e:
                    print(e)
                    pass
            elements = self.browser.find_elements_by_tag_name("div")
            for element in elements:
                try:
                    html = element.get_attribute('innerHTML')
                    soup = BeautifulSoup(html, "html.parser")
                    class_participant_2 = self.search_elements.get_element_path('participant_2')
                    class_participant_3 = self.search_elements.get_element_path('participant_3')
                    for i in soup.find_all("div", class_=class_participant_2):  # "_25Ooe"
                        j = i.find("span", class_=class_participant_3)  # "_1wjpf"
                        if j:
                            j = j.text
                            if "\n" in j:
                                j = j.split("\n")
                                j = j[0]
                                j = j.strip()
                                if j not in participants:
                                    participants.append(j)
                                    print(j)
                except Exception as e:
                    print(e)

        sleep_random.execute()
        return participants

    def goto_main(self):
        """
        Go to Whatsapp main page.
        :return: None.
        """
        try:
            self.browser.refresh()
            Alert(self.browser).accept()
            self.wait_for_element('search_edit')
            SleepRandom(1.9, 1.1).execute()
        except Exception as e:
            print(e)
            raise GotoMainException()

    def get_status(self, name):
        """
        Get a contact status.
        TODO: Adjust this method.
        :param name: Contact Name.
        :return: Status.
        """
        try:
            self.access_search_panel(name)
            click_menu = self.wait_for_element('group')
            click_menu.click()
        except TimeoutException:
            raise TimeoutError(self._TIMEOUT_EXCEPTION_TEXT)
        except NoSuchElementException:
            return None
        except Exception as e:
            print(e)
            return None
        try:
            self.wait_for_element('status_css_selector')
            status = self.get_element('status_css_selector').text
            for i in range(10):
                if len(status) > 0:
                    return status
                else:
                    sleep(1)  # we need some delay
            return "None"
        except TimeoutException:
            raise TimeoutError(self._TIMEOUT_EXCEPTION_TEXT)
        except NoSuchElementException:
            return "None"
        except Exception as e:
            print(e)
            return "None"

    def get_last_seen(self, name, timeout=10):
        """
        Get last seen message.
        TODO: Adjust this method.
        :param name: Contact or group name.
        :param timeout: Int.
        :return: Str.
        """
        _ = timeout
        self.access_search_panel(name)
        start_time = dt.datetime.now()
        try:
            self.wait_for_element('last_seen')
            while True:
                last_seen = self.get_element('last_seen').text
                if last_seen and "click here" not in last_seen:
                    return last_seen
                end_time = dt.datetime.now()
                elapsed_time = (end_time - start_time).seconds
                if elapsed_time > 10:
                    return None
        except TimeoutException:
            raise TimeoutError(self._TIMEOUT_EXCEPTION_TEXT)
        except NoSuchElementException:
            return None
        except Exception as e:
            print(e)
            return None

    def send_blind_message(self, message):
        """
        Send a blind message.
        :param message: Text Message.
        :return: Bool.
        """
        try:
            message = self.emojify(message)
            send_msg = self.wait_for_element('send_message')
            messages = message.split("\n")
            for msg in messages:
                send_msg.send_keys(msg)
                send_msg.send_keys(Keys.SHIFT + Keys.ENTER)
            send_msg.send_keys(Keys.ENTER)
            return True
        except Exception as e:
            print(e)
            return False

    def send_picture(self, name, picture_location, caption=None):
        """
        Send a Picture to contact or group.
        :param name: Content or group name.
        :param picture_location: Path.
        :param caption: Text (optional).
        :return: None.
        """
        self.access_search_panel(name)
        try:
            attach_btn = self.get_element('attach')
            attach_btn.click()
            SleepRandom(end_number=1.5, start_number=1.1).execute()
            attach_img_btn = self.get_element('picture_attach_type')
            attach_img_btn.send_keys(picture_location)
            SleepRandom(end_number=1.5, start_number=1.1).execute()
            if caption:
                send_caption = self.get_element('picture_caption')
                send_caption.send_keys(caption)
                SleepRandom(end_number=0.9, start_number=0.1).execute()

            send_btn = self.get_element('send_file')
            send_btn.click()
            SleepRandom(end_number=1.5, start_number=1.1).execute()

        except (NoSuchElementException, ElementNotVisibleException) as e:
            print(str(e))

    def send_document(self, name, document_location):
        """
        Send a document to a contact or group.
        :param name: Contact or group name.
        :param document_location: Path.
        :return: None.
        """
        try:
            self.access_search_panel(name)
            attach_btn = self.get_element('attach')
            attach_btn.click()
            SleepRandom(end_number=1.5, start_number=1.1).execute()
            attach_img_btn = self.get_element('document_attach_type')
            attach_img_btn.send_keys(document_location)
            SleepRandom(end_number=1.5, start_number=1.1).execute()
            send_btn = self.wait_for_element('send_document_attach_button')
            send_btn.click()
            SleepRandom(end_number=1.5, start_number=1.1).execute()
        except Exception as e:
            print(e)
            raise SendDocumentException()

    def clear_chat(self, name):
        """
        Clear the chat.
        TODO: Adjust this method.
        :param name: Contact or group name.
        :return: None.
        """
        self.access_search_panel(name)
        self.wait_for_element('chat_menu')
        menu = self.get_element('chat_menu')
        menu.click()
        chains = ActionChains(self.browser)
        for i in range(4):
            chains.send_keys(Keys.ARROW_DOWN)
        chains.send_keys(Keys.ENTER)
        chains.perform()
        button = self.wait_for_element('clear_chat')
        button.click()

    def override_timeout(self, new_timeout):
        """
        Update timeout property.
        :param new_timeout: Int.
        :return: Self.
        """
        self.timeout = new_timeout
        return self

    def get_profile_pic(self, name):
        """
        Get the profile picture from a contact or group.
        TODO: Adjust this method.
        :param name: Contact or group name.
        :return: None.
        """
        self.access_search_panel(name)
        try:
            open_profile = self.wait_for_element('open_profile')
            open_profile.click()
        except Exception as e:
            print(e)
        try:
            open_pic = self.wait_for_element('open_profile_picture')
            open_pic.click()
        except Exception as e:
            print(e)
        try:
            img = self.wait_for_element('profile_image')
        except Exception as e:
            print(e)
            print("Couldn't find the URL to the image")
        else:
            img_src_url = img.get_attribute('src')
            self.browser.get(img_src_url)
            self.browser.save_screenshot(name + "_img.png")

    def create_group(self, group_name, members, picture_location=None):
        """
        Create a new Whatsapp group.
        :param group_name: Group name.
        :param members: List of members.
        :param picture_location: Path.
        :return: Bool.
        """
        try:
            bt = self.wait_for_element('group_menu_button')
            bt.click()
            SleepRandom(1.9, 1.1).execute()
            new_button = self.wait_for_element('new_group_button')
            new_button.click()
            SleepRandom(1.2, 0.7).execute()
            for member in members:
                contact_name = self.get_element('group_contact_name')
                contact_name.send_keys(member + Keys.ENTER)
                SleepRandom(1.9, 1.1).execute()
            next_step = self.get_element('create_group_next_step')
            next_step.click()
            SleepRandom(1.9, 1.1).execute()

            if picture_location:
                try:
                    self._change_group_image(picture_location, create=True)
                except Exception as e:
                    print(e)

            group_text = self.get_element('create_group_edit')
            group_text.send_keys(group_name + Keys.ENTER)
            SleepRandom(1.9, 1.1).execute()
        except Exception as e:
            print(e)
            self.browser.refresh()
            raise CreateGroupException()
        return True

    def set_group_picture(self, group_name, picture_location):
        """
        Method to change the image of a group.
        :param group_name: Group name.
        :param picture_location: Path.
        :return: Bool.
        """
        try:
            self._goto_group_data(group_name)
            self._change_group_image(picture_location)
            btn = self.get_element('group_settings_exit_button')
            btn.click()
            SleepRandom(0.9).execute()
        except Exception as e:
            print(e)
            self.browser.refresh()
            raise SetGroupPictureException()
        return True

    def _change_group_image(self, picture_location, create=False):
        """
        Change a group image.
        :param picture_location: Path.
        :param create: If you are creating a new group.
        :return: None.
        """
        elem = 'group_image_button'
        if create:
            elem = 'group_create_image_button'

        SleepRandom(0.5, 0.3).execute()
        img = self.wait_for_element(elem)
        img.send_keys(picture_location)
        SleepRandom(0.9).execute()
        zoom_out = self.wait_for_element('group_zoom_out')
        for i in range(0, 5):
            zoom_out.click()
        button_save = self.wait_for_element('group_image_save_button')
        button_save.click()
        SleepRandom(0.9).execute()

    def join_group(self, invite_link):
        """
        Method for joining a group.
        TODO: Adjust this method.
        :param invite_link: URL Link.
        :return: None.
        """
        self.browser.get(invite_link)
        try:
            Alert(self.browser).accept()
        except Exception as e:
            print(e)

        self.get_element('group_join_chat').click()
        self.wait_for_element('group_join')
        self.get_element('group_join').click()

    def get_invite_link_for_group(self, group_name):
        """
        Retrieves the invitation link for the group.
        :param group_name: Group name.
        :return: Str URL Link.
        """
        try:
            self._goto_group_data(group_name=group_name)
            link_button = self.wait_for_element('group_link_button')
            link_button.click()
            SleepRandom(0.9).execute()
            link = self.wait_for_element('group_invite_link_anchor').text
            self.close_group_panel()
            self.exit_group_panel()
        except Exception as e:
            print(e)
            try:
                self._exit_group_settings()
                self.exit_group_panel()
            except Exception as error:
                print(error)
            raise GetInviteLinkForGroupException()
        return link

    def _goto_group_data(self, group_name):
        """
        Open the group data panel.
        :param group_name: Group name.
        :return: None.
        """
        self.access_search_panel(group_name)
        SleepRandom(0.9).execute()
        self.get_element('group_menu').click()
        SleepRandom(0.9).execute()
        data_button = self.wait_for_element('group_data_button')
        data_button.click()
        SleepRandom(0.9).execute()

    def _goto_group_settings(self, group_name):
        """
        Go to group settings.
        :param group_name: Group name.
        :return: None.
        """
        self._goto_group_data(group_name=group_name)
        self.wait_for_element('group_settings').click()
        SleepRandom(0.5).execute()

    def _exit_group_settings(self):
        """
        Exit group settings.
        :return: None.
        """
        SleepRandom(0.9).execute()
        button_1 = self.wait_for_element('group_settings_exit_button')
        button_1.click()
        SleepRandom(0.9).execute()

    def only_admins_change_group_data(self, group_name):
        """
        Only administrators change group data.
        :param group_name: Group name.
        :return: Bool.
        """
        try:
            self._goto_group_settings(group_name=group_name)
            edit_group_data = self.wait_for_element('group_settings_edit_group_data')
            edit_group_data.click()
            SleepRandom(0.5).execute()
            self.wait_for_element('group_settings_edit_group_data_only_admins').click()
            SleepRandom(0.7).execute()
            button = self.get_element('group_settings_edit_group_data_confirm_button')
            button.click()
            self._exit_group_settings()
            self.exit_group_panel()
        except Exception as e:
            print(e)
            try:
                self._exit_group_settings()
                self.exit_group_panel()
            except Exception as error:
                print(error)
            raise OnlyAdminsChangeGroupDataException()
        return True

    def all_users_change_group_data(self, group_name):
        """
        All users can change group data.
        TODO: Adjust this method.
        :param group_name: Group name.
        :return: Bool.
        """
        _, _ = self, group_name
        return False

    def only_admins_send_messages(self, group_name):
        """
        Only administrators send messages.
        :param group_name: Group name.
        :return: Bool.
        """
        try:
            self._goto_group_settings(group_name=group_name)
            self.wait_for_element('group_settings_send_messages').click()
            SleepRandom(0.5).execute()
            self.wait_for_element('group_settings_send_messages_only_admins').click()
            SleepRandom(0.7).execute()
            button = self.get_element('group_settings_send_messages_confirm_button')
            button.click()
            self._exit_group_settings()
            self.exit_group_panel()
        except Exception as e:
            print(e)
            try:
                self._exit_group_settings()
                self.exit_group_panel()
            except Exception as error:
                print(error)
            raise OnlyAdminsSendMessagesException()
        return True

    def exit_group_panel(self):
        """
        Method for exiting the selected group's panel.
        :return: Self.
        """
        try:
            button = self.get_element('group_exit_info')
            button.click()
        except Exception as e:
            print(e)
        return self

    def all_users_send_messages(self, group_name):
        """
        All users can send messages.
        :param group_name: Group Name.
        :return: Bool.
        """
        try:
            self._goto_group_settings(group_name=group_name)
            self.wait_for_element('group_settings_send_messages').click()
            SleepRandom(0.5).execute()
            self.wait_for_element('group_settings_send_messages_all_participants').click()
            SleepRandom(0.7).execute()
            button = self.get_element('group_settings_send_messages_confirm_button')
            button.click()
            self._exit_group_settings()
            self.exit_group_panel()
        except Exception as e:
            print(e)
            try:
                self._exit_group_settings()
                self.exit_group_panel()
            except Exception as error:
                print(error)
            raise AllUsersSendMessagesException()
        return True

    def exit_group(self, group_name):
        """
        Leave a group.
        TODO: Adjust this method.
        :param group_name: Group Name.
        :return: None.
        """
        self.access_search_panel(group_name)
        self.get_element('group_menu').click()
        self.wait_for_element('group_leave')
        sleep(3)
        self.get_element('group_leave').click()
        button = self.wait_for_element('group_leave_button')
        button.click()

    def send_anon_message(self, phone, text):
        """
        Send anonymous message.
        TODO: Adjust this method.
        :param phone: Phone Number.
        :param text: Text Message.
        :return: None.
        """
        payload = urlencode({"phone": phone, "text": text, "source": "", "data": ""})
        self.browser.get("https://api.whatsapp.com/send?" + payload)
        try:
            Alert(self.browser).accept()
        except Exception as e:
            print(e)
        WebDriverWait(self.browser, self.timeout).until(
            exp_cond.presence_of_element_located((By.CSS_SELECTOR, "#action-button")))
        send_message = self.browser.find_element_by_css_selector("#action-button")
        send_message.click()
        confirm = WebDriverWait(self.browser, self.timeout + 5).until(exp_cond.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")))
        confirm.clear()
        confirm.send_keys(text + Keys.ENTER)

    def is_message_present(self, username, message):
        """
        Checks if a message exists in the contact's chat.
        TODO: Adjust this method.
        :param username: Contact Name.
        :param message: Text Message.
        :return: Bool.
        """
        self.access_search_panel(username)
        search_bar = WebDriverWait(self.browser, self.timeout).until(exp_cond.presence_of_element_located(
            (By.CSS_SELECTOR, "._1i0-u > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")))
        search_bar.click()
        message_search = self.browser.find_element_by_css_selector(
            "._1iopp > div:nth-child(1) > label:nth-child(4) > input:nth-child(1)")
        message_search.clear()
        message_search.send_keys(message + Keys.ENTER)
        try:
            WebDriverWait(self.browser, self.timeout).until(exp_cond.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div/div/div[2]/div[3]/span/div/div/div[2]/div/div/div/div/div[1]/div/div/div/" +
                 "div[2]/div[1]/span/span/span")))
            return True
        except TimeoutException:
            return False

    def get_starred_messages(self, delay=10):
        """
        Get starred messages from a contact.
        TODO: Adjust this method.
        :param delay: Int.
        :return: Str.
        """
        starred_messages = []
        self.browser.find_element_by_css_selector(
            "div.rAUz7:nth-child(3) > div:nth-child(1) > span:nth-child(1)").click()
        chains = ActionChains(self.browser)
        sleep(2)
        for i in range(4):
            chains.send_keys(Keys.ARROW_DOWN)
        chains.send_keys(Keys.ENTER)
        chains.perform()
        sleep(delay)
        messages = self.browser.find_elements_by_class_name("MS-DH")
        for message in messages:
            try:
                message_html = message.get_attribute("innerHTML")
                soup = BeautifulSoup(message_html, "html.parser")
                _from = soup.find("span", class_="_1qUQi")["title"]
                to = soup.find("div", class_="copyable-text")["data-pre-plain-text"]
                message_text = soup.find("span", class_="selectable-text invisible-space copyable-text").text
                message.click()
                selector = self.browser.find_element_by_css_selector(
                    "#main > header > div._5SiUq > div._16vzP > div > span")
                title = selector.text
                selector.click()
                sleep(2)
                WebDriverWait(self.browser, 5).until(exp_cond.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     "div._14oqx:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > " +
                     "span:nth-child(1)")))
                phone = self.browser.find_element_by_css_selector(
                    "div._14oqx:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > " +
                    "span:nth-child(1)").text
                if title in _from:
                    _from = _from.replace(title, phone)
                else:
                    to = to.replace(title, phone)
                starred_messages.append([_from, to, message_text])
            except Exception as e:
                print("Handled: ", e)
        return starred_messages

    def unread_usernames(self, scrolls=100):
        """
        Check unread messages.
        TODO: Adjust this method.
        :param scrolls: Int.
        :return: Str.
        """
        self.goto_main()
        initial = 10
        usernames = []
        for j in range(0, scrolls):
            self.browser.execute_script("document.getElementById('pane-side').scrollTop={}".format(initial))
            soup = BeautifulSoup(self.browser.page_source, "html.parser")
            for i in soup.find_all("div", class_="_2WP9Q"):
                if i.find("div", class_="_1ZMSM"):
                    username = i.find("div", class_="_3H4MS").text
                    usernames.append(username)
            initial += 10
        usernames = list(set(usernames))
        return usernames

    def get_driver(self):
        """
        Get Browser property.
        :return: Browser instance.
        """
        return self.browser

    def get_last_message_for(self, name):
        """
        Get Last Message from a Contact.
        TODO: Adjust this method.
        :param name: Contact Name.
        :return: Str.
        """
        messages = list()
        self.access_search_panel(name)
        sleep(3)
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        for i in soup.find_all("div", class_="FTBzM message-in"):
            message = i.find("div", class_="_12pGw")
            if message:
                messages.append(message.text)
        messages = list(filter(None, messages))
        return messages

    def quit(self):
        """
        Close the Browser and Save Local Storage Info.
        :return: Bool.
        """
        result = False
        if self.browser:
            self._save_storage()
            self.browser.quit()
            self.browser = None
            result = True
        return result

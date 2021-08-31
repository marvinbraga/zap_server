# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Selenium Driver Elements Module
"""

from abc import ABCMeta, abstractmethod
from enum import Enum, unique

from selenium.webdriver.common.by import By

from server.adapters.the_first.elements.data import ManagerElementsData
from server.adapters.the_first.elements.exceptions import InvalidElementName


class ElementsData:
    """
    Class to inform elements and their settings.
    """

    @staticmethod
    def get():
        """
        Find the elements to Selenium.
        :return: Dict.
        """
        data = ManagerElementsData().data
        return {
            'search_edit':
                ElementItem(data.get('search_edit'), ElementPathType.X_PATH),
            'qr_code':
                ElementItem(data.get('qr_code'), ElementPathType.X_PATH),
            'send_message':
                ElementItem(data.get('send_message'), ElementPathType.X_PATH),
            'group':
                ElementItem(data.get('group'), ElementPathType.X_PATH),
            'group_menu_button':
                ElementItem(data.get('group_menu_button'), ElementPathType.X_PATH),
            'group_edit_button':
                ElementItem(data.get('group_edit_button'), ElementPathType.X_PATH),
            'group_name_edit':
                ElementItem(data.get('group_name_edit'), ElementPathType.X_PATH),
            'group_close_panel_btn':
                ElementItem(data.get('group_close_panel_btn'), ElementPathType.X_PATH),
            'participants_selector':
                ElementItem(data.get('participants_selector'), ElementPathType.CSS),
            'group_more':
                ElementItem(data.get('group_more'), ElementPathType.X_PATH),
            'new_group_button':
                ElementItem(data.get('new_group_button'), ElementPathType.X_PATH),
            'group_contact_name':
                ElementItem(data.get('group_contact_name'), ElementPathType.X_PATH),
            'create_group_next_step':
                ElementItem(data.get('create_group_next_step'), ElementPathType.X_PATH),
            'create_group_edit':
                ElementItem(data.get('create_group_edit'), ElementPathType.X_PATH),
            'main_menu':
                ElementItem(data.get('main_menu'), ElementPathType.CSS),
            'chat_menu':
                ElementItem(data.get('chat_menu'), ElementPathType.X_PATH),
            'group_menu':
                ElementItem(data.get('group_menu'), ElementPathType.X_PATH),
            'group_data_button':
                ElementItem(data.get('group_data_button'), ElementPathType.X_PATH),
            'group_link_button':
                ElementItem(data.get('group_link_button'), ElementPathType.X_PATH),
            'group_invite_link_anchor':
                ElementItem(data.get('group_invite_link_anchor'), ElementPathType.X_PATH),
            'group_info':
                ElementItem(data.get('group_info'), ElementPathType.X_PATH),
            'group_image_button':
                ElementItem(data.get('group_image_button'), ElementPathType.X_PATH),
            'group_create_image_button':
                ElementItem(data.get('group_create_image_button'), ElementPathType.X_PATH),
            'group_load_photo':
                ElementItem(data.get('group_load_photo'), ElementPathType.CSS),
            'group_image_input':
                ElementItem(data.get('group_image_input'), ElementPathType.X_PATH),
            'group_zoom_out':
                ElementItem(data.get('group_zoom_out'), ElementPathType.X_PATH),
            'group_image_save_button':
                ElementItem(data.get('group_image_save_button'), ElementPathType.X_PATH),
            'group_exit_info':
                ElementItem(data.get('group_exit_info'), ElementPathType.X_PATH),
            'group_join_chat':
                ElementItem(data.get('group_join_chat'), ElementPathType.CSS),
            'group_join':
                ElementItem(data.get('group_join'), ElementPathType.X_PATH),
            'group_leave':
                ElementItem(data.get('group_leave'), ElementPathType.X_PATH),
            'group_leave_button':
                ElementItem(data.get('group_leave_button'), ElementPathType.X_PATH),
            'group_settings':
                ElementItem(data.get('group_settings'), ElementPathType.X_PATH),
            'group_settings_send_messages':
                ElementItem(data.get('group_settings_send_messages'), ElementPathType.X_PATH),
            'group_settings_send_messages_all_participants':
                ElementItem(data.get('group_settings_send_messages_all_participants'), ElementPathType.X_PATH),
            'group_settings_send_messages_only_admins':
                ElementItem(data.get('group_settings_send_messages_only_admins'), ElementPathType.X_PATH),
            'group_settings_send_messages_confirm_button':
                ElementItem(data.get('group_settings_send_messages_confirm_button'), ElementPathType.X_PATH),
            'group_settings_edit_group_data':
                ElementItem(data.get('group_settings_edit_group_data'), ElementPathType.X_PATH),
            'group_settings_edit_group_data_only_admins':
                ElementItem(data.get('group_settings_edit_group_data_only_admins'), ElementPathType.X_PATH),
            'group_settings_edit_group_data_confirm_button':
                ElementItem(data.get('group_settings_edit_group_data_confirm_button'), ElementPathType.X_PATH),
            'group_settings_exit_button':
                ElementItem(data.get('group_settings_exit_button'), ElementPathType.X_PATH),
            'scroll_bar':
                ElementItem(data.get('scroll_bar'), ElementPathType.CSS),
            'participant_1':
                ElementItem(data.get('participant_1'), ElementPathType.CLASS),
            'participant_2':
                ElementItem(data.get('participant_2'), ElementPathType.CLASS),
            'participant_3':
                ElementItem(data.get('participant_3'), ElementPathType.CLASS),
            'status_css_selector':
                ElementItem(data.get('status_css_selector'), ElementPathType.CSS),
            'last_seen':
                ElementItem(data.get('last_seen'), ElementPathType.CSS),
            'attach':
                ElementItem(data.get('attach'), ElementPathType.X_PATH),
            'send_file':
                ElementItem(data.get('send_file'), ElementPathType.X_PATH),
            'picture_attach_type':
                ElementItem(data.get('picture_attach_type'), ElementPathType.X_PATH),
            'document_attach_type':
                ElementItem(data.get('document_attach_type'), ElementPathType.X_PATH),
            'picture_caption':
                ElementItem(data.get('picture_caption'), ElementPathType.X_PATH),
            'send_document_attach_button':
                ElementItem(data.get('send_document_attach_button'), ElementPathType.X_PATH),
            'clear_chat':
                ElementItem(data.get('clear_chat'), ElementPathType.X_PATH),
            'open_profile':
                ElementItem(data.get('open_profile'), ElementPathType.X_PATH),
            'open_profile_picture':
                ElementItem(data.get('open_profile_picture'), ElementPathType.X_PATH),
            'profile_image':
                ElementItem(data.get('profile_image'), ElementPathType.X_PATH),
        }


class AbstractElementByScope(metaclass=ABCMeta):
    """
    Base class for instantiating element object by scope.
    """

    def __init__(self, driver, element):
        self._driver = driver
        self._element = element

    @abstractmethod
    def get(self):
        """
        Abstract method to retrieve the element according to scope.
        """
        pass


class ElementByXPath(AbstractElementByScope):
    """
    Class to retrieve the element by XPath.
    """

    def get(self):
        """
        Retrieves the element via XPath.
        :return: Selenium Element.
        """
        return self._driver.find_element_by_xpath(self._element.path)


class ElementByCss(AbstractElementByScope):
    """
    Class to retrieve the element by CSS.
    """

    def get(self):
        """
        Retrieves the element via CSS.
        :return: Selenium Element.
        """
        return self._driver.find_element_by_css_selector(self._element.path)


class ElementByClassName(AbstractElementByScope):
    """
    Class to retrieve the element by class name.
    """

    def get(self):
        """
        Retrieves the element by class_name.
        :return: Selenium Element.
        """
        return self._driver.find_element_by_class_name(self._element.path)


@unique
class ElementPathType(Enum):
    """
    Class representing the type of the element's path.
    """
    X_PATH = 1
    CLASS = 2
    CSS = 3

    def new_element_by(self, driver, element):
        """
        Factory Method to select the method to be used.
        :param driver: Selenium Driver.
        :param element: Selenium Element.
        :return: Dict.
        """
        element_class = {ElementPathType.X_PATH: ElementByXPath,
                         ElementPathType.CLASS: ElementByClassName,
                         ElementPathType.CSS: ElementByCss, }[self]
        return element_class(driver, element).get()

    def new_element_by_presence(self, element):
        """
        Factory Method to select the set of information for Wait.
        :param element: Selenium Element.
        :return: Dict.
        """
        return {ElementPathType.X_PATH: (By.XPATH, element.path),
                ElementPathType.CLASS: (By.CLASS_NAME, element.path),
                ElementPathType.CSS: (By.CSS_SELECTOR, element.path), }[self]


class ElementItem:
    """
    Class representing the element item.
    """

    def __init__(self, path, path_type):
        self._path = path
        self._path_type = path_type

    @property
    def path(self):
        """
        Returns the element item path.
        :return: Path property value.
        """
        return self._path

    @property
    def path_type(self):
        """
        Returns the type of element item path.
        :return: Path Type property value.
        """
        return self._path_type


class DriveElements:
    """
    Class for element controllers.
    """

    def __init__(self, browser):
        """
        Initializes driver elements.
        :param browser: Selenium driver.browser object.
        """
        self._browser = browser
        self._items = DriveElements._set_items()

    @staticmethod
    def _set_items():
        """
        Recovers elements and their settings.
        :return: Dict.
        """
        return ElementsData.get()

    def get_element(self, element_name):
        """
        Retrieves the element by searching according to the element's type.
        :param element_name: Element name.
        :return: Selenium element object.
        """
        elem = self._items.get(element_name)
        if elem is None:
            raise InvalidElementName()

        return elem.path_type.new_element_by(self._browser, elem)

    def get_element_path(self, element_name):
        """
        Retrieves the path of the entered element.
        :param element_name: Element name.
        :return: Element identifier.
        """
        elem = self._items.get(element_name)
        if elem is None:
            raise InvalidElementName()

        return elem.path

    def get_presence_of_element(self, element_name):
        """
        Retrieves the element by searching according to the element's type.
        :param element_name: Element name.
        :return: By object tuple and Selenium element.
        """
        elem = self._items.get(element_name)
        if elem is None:
            raise InvalidElementName()

        return elem.path_type.new_element_by_presence(elem)

# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Selenium Data Elements Module
"""

import os
import pickle

from core import settings


class ManagerElementsData:
    """
    Whatsapp elements data manager.
    """

    def __init__(self):
        self._file_name = settings.ELEMENTS_DATA_FILE
        self._data = self._get()

    @property
    def data(self):
        """
        Property that returns data.
        :return: Data value.
        """
        return self._data

    def load(self):
        """
        Method for loading data from file.
        :return: Self.
        """
        self._data = pickle.load(open(self._file_name, 'rb'))
        return self

    def save(self):
        """
        Method for saving information to file.
        :return: Self.
        """
        if os.path.isfile(self._file_name):
            os.remove(self._file_name)
        pickle.dump(self._data, open(self._file_name, 'wb'))
        return self

    @staticmethod
    def _get():
        """
        Method to retrieve Whatsapp paths.
        :return: Dict.
        """
        return {
            'search_edit':
                '/html/body/div/div/div/div[3]/div/div[1]/div/label/div/div[2]',
            'qr_code':
                '/html/body/div/div[1]/div/div[2]/div[1]/div/div[2]/div/canvas',
            'send_message':
                "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]",
            'group':
                "/html/body/div/div/div/div[3]/header/div[1]/div/span/img",
            'group_menu_button':
                "/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[3]/div",
            'group_edit_button':
                '/html/body/div/div/div/div[2]/div[3]/span/div/span/div/div/section/div[1]/div[2]/div[1]/span[2]/div',
            'group_name_edit':
                '/html/body/div/div/div/div[2]/div[3]/span/div/span/div/div/section/div[1]/div[2]/div[1]/div/div[2]',
            'group_close_panel_btn':
                '//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/header/div/div[1]/button',
            'participants_selector':
                "div._2LSbZ:nth-child(5) > div:nth-child(1) > div:nth-child(1) > "
                "div:nth-child(1) > div:nth-child(1) > span:nth-child(1)",
            'group_more':
                '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span',
            'new_group_button':
                '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div',
            'group_contact_name':
                '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input',
            'create_group_next_step':
                '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span',
            'create_group_edit':
                '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]',
            'main_menu':
                "#main > header > div._1WBXd > div._2EbF- > div > span",
            'chat_menu':
                "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/div/span",
            'group_menu':
                "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div",
            'group_data_button':
                '/html/body/div/div[1]/span[4]/div/ul/div/div/li[1]',
            'group_link_button':
                '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[3]',
            'group_invite_link_anchor':
                '/html/body/div/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[2]/div[2]/div/span',
            'group_info':
                '/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/span/div/ul/li[1]/div',
            'group_image_button':
                '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[1]'
                '/div[1]/div/input',
            'group_create_image_button':
                '/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div/div[1]/div/input',
            'group_load_photo':
                '#app > div > span:nth-child(4) > div > ul > li:nth-child(2) > div',
            'group_image_input':
                '/html/body/div[1]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[1]/div/input',
            'group_zoom_out':
                '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[1]/div[1]/div[2]',
            'group_image_save_button':
                '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/span/div/div/div[2]/span/div/div/span',
            'group_exit_info':
                '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/header/div/div[1]/button',
            'group_join_chat':
                "#action-button",
            'group_join':
                '//*[@id="app"]/div/span[3]/div/div/div/div/div/div/div[2]/div[2]',
            'group_leave':
                '//*[@id="main"]/header/div[3]/div/div[3]/span/div/ul/li[5]/div',
            'group_leave_button':
                '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]',
            'group_settings':
                '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[4]/div[4]',
            'group_settings_send_messages':
                '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/div[3]/div',
            'group_settings_send_messages_all_participants':
                '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/form/ol/li[1]/label',
            'group_settings_send_messages_only_admins':
                '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/form/ol/li[2]/label',
            'group_settings_send_messages_confirm_button':
                '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[3]/div[2]',
            'group_settings_edit_group_data':
                '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/div[1]/div',
            'group_settings_edit_group_data_only_admins':
                '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[2]/form/ol/li[2]/label',
            'group_settings_edit_group_data_confirm_button':
                '/html/body/div/div[1]/span[2]/div[1]/div/div/div/div/div/div[3]/div[2]',
            'group_settings_exit_button':
                '/html/body/div/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/header/div/div[1]/button',
            'scroll_bar':
                "#app > div > div > div.MZIyP > div._3q4NP._2yeJ5 > span > div > span > div > div",
            'participant_1':
                '_3TEwt',
            'participant_2':
                '_25Ooe',
            'participant_3':
                '_1wjpf',
            'status_css_selector':
                ".drawer-section-body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > " +
                "span:nth-child(1) > span:nth-child(1)",
            'last_seen':
                '._315-i',
            'attach':
                '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[2]/div/div',
            'send_file':
                '/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span',
            'picture_attach_type':
                '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]'
                '/button/input',
            'document_attach_type':
                '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[3]'
                '/button/input',
            'send_document_attach_button':
                '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div',
            'picture_caption':
                "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/span/div" +
                "/div[2]/div/div[3]/div[1]/div[2]",
            'clear_chat':
                '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]',
            'open_profile':
                "/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img",
            'open_profile_picture':
                "/html/body/div[1]/div/div/div[1]/div[3]/span/div/span/div/div/div/div[1]/div[1]/div/img",
            'profile_image':
                '//*[@id="app"]/div/span[2]/div/div/div[2]/div/div/div/div/img',
        }

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
from server.adapters.the_first.elements.classes import *


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
            'search_edit': SearchEdit().path,
            'search_edit_clear_button': SearchClearButton().path,
            'qr_code': QRCode().path,
            'send_message': SendMessage().path,
            'group': Group().path,
            'group_menu_button': GroupMenuButton().path,
            'group_edit_button': GroupEditButton().path,
            'group_name_edit': GroupNameEdit().path,
            'group_close_panel_btn': GroupClosePanelButton().path,
            'participants_selector': ParticipantsSelector().path,
            'group_more': GroupMore().path,
            'new_group_button': NewGroupButton().path,
            'group_contact_name': GroupContactName().path,
            'create_group_next_step': CreateGroupNextStep().path,
            'create_group_edit': CreateGroupEdit().path,
            'main_menu': MainMenu().path,
            'chat_menu': ChatMenu().path,
            'group_menu': GroupMenu().path,
            'group_data_button': GroupDataButton().path,
            'group_link_button': GroupLinkButton().path,
            'group_invite_link_anchor': GroupInviteLinkAnchor().path,
            'group_info': GroupInfo().path,
            'group_image_button': GroupImageButton().path,
            'group_create_image_button': GroupCreateImageButton().path,
            'group_load_photo': GroupLoadPhoto().path,
            'group_image_input': GroupImageInput().path,
            'group_zoom_out': GroupZoomOut().path,
            'group_image_save_button': GroupImageSaveButton().path,
            'group_exit_info': GroupExitInfo().path,
            'group_join_chat': GroupJoinChat().path,
            'group_join': GroupJoin().path,
            'group_leave': GroupLeave().path,
            'group_leave_button': GroupLeaveButton().path,
            'group_settings': GroupSettings().path,
            'group_settings_send_messages': GroupSettingsSendMessages().path,
            'group_settings_send_messages_all_participants': GroupSettingsSendMessagesAllParticipants().path,
            'group_settings_send_messages_only_admins': GroupSettingsSendMessagesOnlyAdmins().path,
            'group_settings_send_messages_confirm_button': GroupSettingsSendMessagesConfirmButton().path,
            'group_settings_edit_group_data': GroupSettingsEditGroupData().path,
            'group_settings_edit_group_data_only_admins': GroupSettingsEditGroupDataOnlyAdmins().path,
            'group_settings_edit_group_data_confirm_button': GroupSettingsEditGroupDataConfirmButton().path,
            'group_settings_exit_button': GroupSettingsExitButton().path,
            'scroll_bar': ScrollBar().path,
            'participant_1': Participant1().path,
            'participant_2': Participant2().path,
            'participant_3': Participant3().path,
            'status_css_selector': StatusCssSelector().path,
            'last_seen': LastSeen().path,
            'attach': Attach().path,
            'send_file': SendFile().path,
            'picture_attach_type': PictureAttachType().path,
            'document_attach_type': DocumentAttachType().path,
            'send_document_attach_button': SendDocumentAttachButton().path,
            'picture_caption': PictureCaption().path,
            'clear_chat': ClearChat().path,
            'open_profile': OpenProfile().path,
            'open_profile_picture': OpenProfilePicture().path,
            'profile_image': ProfileImage().path,
        }

# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Group Commands Classes Module
"""
from core.commands.bases import AbstractCommand
from server.commands.groups.exceptions import GroupParticipantCountException, GroupParticipantsException, \
    CreateGroupException, JoinGroupException, GetInviteLinkForGroupException, ExitGroupException, \
    RenameGroupException, \
    SetGroupPictureException, OnlyAdminsSendMessagesException, AllUsersSendMessagesException, \
    OnlyAdminsChangeGroupDataException, AllUsersChangeGroupDataException


class GroupParticipantCount(AbstractCommand):
    """
    Command for counting the participants of a group.
    """
    name = 'GroupParticipantCount'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._group_name = args[0]

    def __str__(self):
        return f'{self.name} - group_name: [{self._group_name}] count: [{self._result}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.participants_count(group_name=self._group_name)
            except GroupParticipantCountException as e:
                self._result = e.message
        return self


class GroupParticipants(AbstractCommand):
    """
    Command to retrieve participants from a group.
    """
    name = 'GroupParticipants'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._group_name = args[0]

    def __str__(self):
        return f'{self.name} - group_name: [{self._group_name}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.get_participants(group_name=self._group_name)
            except GroupParticipantsException as e:
                self._result = e.message
        return self


class GroupCreate(AbstractCommand):
    """
    Command to create a group.
    """
    name = 'GroupCreate'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._group_name = args[0]
        self._members = list(args[1])
        self._picture_location = args[2]

    def __str__(self):
        return f'{self.name} - group_name: [{self._group_name}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.create_group(group_name=self._group_name, members=self._members,
                                                               picture_location=self._picture_location)
            except CreateGroupException as e:
                self._result = e.message
        return self


class GroupJoin(AbstractCommand):
    """
    Command to join a group.
    """
    name = 'GroupJoin'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._invite_link = args[0]

    def __str__(self):
        return f'{self.name} - link: [{self._invite_link}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.join_group(invite_link=self._invite_link)
            except JoinGroupException as e:
                self._result = e.message
        return self


class GroupGetInviteLink(AbstractCommand):
    """
    Command to retrieve the link of a group.
    """
    name = 'GroupGetInviteLink'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._name = args[0]

    def __str__(self):
        return f'{self.name} - name: [{self._name}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.get_invite_link(group_name=self._name)
            except GetInviteLinkForGroupException as e:
                self._result = e.message
        return self


class GroupExit(AbstractCommand):
    """
    Command to leave a group.
    """
    name = 'GroupExit'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._name = args[0]

    def __str__(self):
        return f'{self.name} - name: [{self._name}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.exit_group(group_name=self._name)
            except ExitGroupException as e:
                self._result = e.message

        return self


class GroupRename(AbstractCommand):
    """
    Command to rename a group.
    """
    name = 'GroupRename'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._old_name = args[0]
        self._new_name = args[1]

    def __str__(self):
        return f'{self.name} - old_name: [{self._old_name}] new_name: [{self._new_name}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.rename(old_name=self._old_name, new_name=self._new_name)
            except RenameGroupException as e:
                self._result = e.message
        return self


class GroupSetPicture(AbstractCommand):
    """
    Command to change the image of a group.
    """
    name = 'GroupSetPicture'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._name = args[0]
        self._picture_location = args[1]

    def __str__(self):
        return f'{self.name} - name: [{self._name}] picture_location: [{self._picture_location}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.set_picture(group_name=self._name,
                                                              picture_location=self._picture_location)
            except SetGroupPictureException as e:
                self._result = e.message
        return self


class GroupOnlyAdminsSendMessages(AbstractCommand):
    """
    Command to configure that only admins send messages to a group.
    """
    name = 'GroupOnlyAdminsSendMessages'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._name = args[0]

    def __str__(self):
        return f'{self.name} - name: [{self._name}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.only_admins_send_messages(group_name=self._name)
            except OnlyAdminsSendMessagesException as e:
                self._result = e.message
        return self


class GroupAllUsersSendMessages(AbstractCommand):
    """
    Command to configure that all users can send messages in a group.
    """
    name = 'GroupAllUsersSendMessages'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._name = args[0]

    def __str__(self):
        return f'{self.name} - name: [{self._name}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.all_users_send_messages(group_name=self._name)
            except AllUsersSendMessagesException as e:
                self._result = e.message
        return self


class GroupOnlyAdminsChangeGroupData(AbstractCommand):
    """
    Command to configure that only admins change data of a group.
    """
    name = 'GroupOnlyAdminsChangeGroupData'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._name = args[0]

    def __str__(self):
        return f'{self.name} - name: [{self._name}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.only_admins_change_group_data(group_name=self._name)
            except OnlyAdminsChangeGroupDataException as e:
                self._result = e.message
        return self


class GroupAllUsersChangeGroupData(AbstractCommand):
    """
    Command to configure that all users can change data in a group.
    """
    name = 'GroupAllUsersChangeGroupData'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._name = args[0]

    def __str__(self):
        return f'{self.name} - name: [{self._name}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.group.all_users_change_group_data(group_name=self._name)
            except AllUsersChangeGroupDataException as e:
                self._result = e.message
        return self


class GroupCommandsRegister:
    """
    Register for commands.
    """

    available_classes = (
        GroupCreate, GroupGetInviteLink, GroupRename, GroupSetPicture,
        GroupOnlyAdminsSendMessages, GroupAllUsersSendMessages,
        GroupOnlyAdminsChangeGroupData, GroupAllUsersChangeGroupData,
        GroupParticipantCount, GroupParticipants, GroupJoin, GroupExit,
    )

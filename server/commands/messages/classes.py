# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Messages Commands Classes Module
"""
from core.commands.bases import AbstractCommand
from server.commands.messages.exceptions import SendMessageException, SendPictureException, SendDocumentException


class SendMessage(AbstractCommand):
    """
    Command to send message.
    """
    name = 'SendMessage'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._contact_name = args[0]
        self._message = args[1]

    def __str__(self):
        return f'{self.name} - contact: [{self._contact_name}] and message: [{self._message}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.message.send_message(name=self._contact_name, message=self._message)
            except SendMessageException as e:
                self._result = e.message
        return self


class SendPicture(AbstractCommand):
    """
    Command to send message.
    """
    name = 'SendPicture'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._name = args[0]
        self._picture_location = args[1]
        self._caption = args[2]

    def __str__(self):
        return f'{self.name} - name: [{self._name}], path: [{self._picture_location}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.message.send_picture(
                    name=self._name, picture_location=self._picture_location, caption=self._caption)
            except SendPictureException as e:
                self._result = e.message
        return self


class SendDocument(AbstractCommand):
    """
    Command to send document.
    """
    name = 'SendDocument'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._name = args[0]
        self._document_location = args[1]

    def __str__(self):
        return f'{self.name} - name: [{self._name}], location: [{self._document_location}] '

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.message.send_document(
                    name=self._name, document_location=self._document_location)
            except SendDocumentException as e:
                self._result = e.message
        return self


class MessageCommandsRegister:
    """
    Register for message commands.
    """
    available_classes = (
        SendMessage, SendPicture, SendDocument,
    )

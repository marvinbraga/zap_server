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
from server.commands.properties.exceptions import GetQrCodeException, CheckPointException, ConnectionLostException, \
    IsConnectedException


class GetQrCode(AbstractCommand):
    """
    Command to retrieve the QR-Code.
    """
    name = 'GetQrCode'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)

    def __str__(self):
        return self.name

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.properties.get_qrcode()
            except GetQrCodeException as e:
                self._result = e.message
        return self


class CheckPoint(AbstractCommand):
    """
    Command to verify authentication is complete.
    """
    name = 'CheckPoint'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)

    def __str__(self):
        return self.name

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.properties.check_point()
            except CheckPointException as e:
                self._result = e.message
        return self


class IsConnected(AbstractCommand):
    """
    Command to check if it is connected.
    """
    name = 'IsConnected'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)
        self._result = False

    def __str__(self):
        return self.name

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        if self.adaptee:
            try:
                self._result = self.adaptee.properties.is_connected()
            except (IsConnectedException, ConnectionLostException) as e:
                self._result = e.message
        return self


class PropertiesCommandsRegister:
    """
    Register for the property command.
    """
    available_classes = (
        GetQrCode, CheckPoint, IsConnected,
    )

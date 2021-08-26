# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Adaptee Module
"""
from server.adapters.bases import AdapteeBase


class MockWhatsapp:
    """
    TODO: Create This Class.
    """

    def __init__(self, token):
        self.token = token


class WhatsApp:
    """
    TODO: Create this class.
    """

    def __init__(self, timeout, token, no_headless):
        self.timeout = timeout
        self.token = token
        self.no_headless = no_headless


class AdapteeMockWhatsapp(AdapteeBase):
    """
    Adaptee class for a Console Mock.
    """

    def __init__(self, token, no_headless=False):
        """
        Number of seconds to timeout, default 5 days Use the manager's override_timeout function to change this value.
        """
        super(AdapteeMockWhatsapp, self).__init__(token, no_headless)
        self._object = MockWhatsapp(token=self._token)

        self._message = None  # MessageAdapterMockApp(self._object)
        self._group = None  # GroupAdapterMockApp(self._object)
        self._person = None  # PersonAdapterMockApp(self._object)
        self._manager = None  # ManagerAdapterMockApp(self._object)
        self._properties = None  # PropertiesAdapterMockApp(self._object)


class AdapteeTheFirstWhatsApp(AdapteeBase):
    """
    First implementation for connecting to Whatsapp.
    """

    def __init__(self, token, no_headless=False, timeout=432000):
        """
        Number of seconds to timeout, default 5 days Use the manager's override_timeout function to change this value.
        """
        super(AdapteeTheFirstWhatsApp, self).__init__(token, no_headless)
        self._object = WhatsApp(timeout, token=self._token, no_headless=self._no_headless)

        self._message = None  # MessageAdapterTheFirstWhatsApp(self._object)
        self._group = None  # GroupAdapterTheFirstWhatsApp(self._object)
        self._person = None  # PersonAdapterTheFirstWhatsApp(self._object)
        self._manager = None  # ManagerAdapterTheFirstWhatsApp(self._object)
        self._properties = None  # PropertiesAdapterTheFirstWhatsApp(self._object)

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
from server.adapters.categories import MessageAdapterWhatsApp, MockGroupAdapterWhatsApp, PersonAdapterWhatsApp, \
    ManagerAdapterWhatsApp, PropertiesAdapterWhatsApp, GroupAdapterWhatsApp
from server.adapters.mocks import MockWhatsapp
from server.adapters.the_first.classes import WhatsApp
from core.logs import logging

logger = logging.getLogger(__name__)


class AdapteeMockWhatsapp(AdapteeBase):
    """
    Adaptee class for a Console Mock.
    """

    def __init__(self, token, no_headless=False):
        """
        Number of seconds to timeout, default 5 days Use the manager's override_timeout function to change this value.
        """
        super().__init__(token, no_headless)
        self._object = MockWhatsapp(token=self._token)

        self._message = MessageAdapterWhatsApp(self._object)
        self._group = MockGroupAdapterWhatsApp(self._object)
        self._person = PersonAdapterWhatsApp(self._object)
        self._manager = ManagerAdapterWhatsApp(self._object)
        self._properties = PropertiesAdapterWhatsApp(self._object)


class AdapteeTheFirstWhatsApp(AdapteeBase):
    """
    First implementation for connecting to Whatsapp.
    """

    def __init__(self, token, no_headless=False, timeout=432000):
        """
        Number of seconds to timeout, default 5 days Use the manager's override_timeout function to change this value.
        """
        super().__init__(token, no_headless)
        logger.debug("Initializing AdapteeTheFirstWhatsApp")
        self._object = WhatsApp(timeout, token=self._token, no_headless=self._no_headless)

        self._message = MessageAdapterWhatsApp(self._object)
        self._group = GroupAdapterWhatsApp(self._object)
        self._person = PersonAdapterWhatsApp(self._object)
        self._manager = ManagerAdapterWhatsApp(self._object)
        self._properties = PropertiesAdapterWhatsApp(self._object)
        logger.debug(f"WhatsApp instance: {self._object}")
        logger.debug("AdapteeTheFirstWhatsApp Initialized")

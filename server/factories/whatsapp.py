# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Whatsapp Factories Module
"""

from enum import Enum

from server.adapters.adapts import AdapteeMockWhatsapp, AdapteeTheFirstWhatsApp


class FactoryWhatsappAdapter(Enum):
    """
    Factory to get Whatsapp Adapter.
    """

    MOCK = 0, 'AdapteeMockWhatsapp'
    DEFAULT = 1, 'AdapteeTheFirstWhatsApp'

    @property
    def get_cls(self):
        """
        Returns respective class.
        :return:
        """
        return {
            FactoryWhatsappAdapter.MOCK: AdapteeMockWhatsapp,
            FactoryWhatsappAdapter.DEFAULT: AdapteeTheFirstWhatsApp,
        }[self]

    def get_new(self, token, no_headless=False):
        """
        Create instance of _adapter class.
        :param token: Token string.
        :param no_headless: Don't show browser window.
        :return: Adapter.
        """
        return self.get_cls(token=token, no_headless=no_headless)

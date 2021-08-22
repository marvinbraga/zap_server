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


class FactoryWhatsappAdapter(Enum):
    """
    Factory to get Whatsapp Adapter.
    """

    MOCK = 0, 'AdapterMockWhatsapp'
    DEFAULT = 1, 'AdapterTheFirstWhatsapp'

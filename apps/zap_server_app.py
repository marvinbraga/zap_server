# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Zap Server Application Module
"""
from multiprocessing.connection import Listener

from core.factories.whatsapp import FactoryWhatsappAdapter
from core.utils.classes import MessageConsole


class ZapServerApp:
    """
    TCP Socket Server to Selenium.
    """

    def __init__(self, address, authkey, adapter=FactoryWhatsappAdapter.DEFAULT, no_headless=False):
        self.con = MessageConsole()
        self.con.show('Authorizing...')
        self.serv = Listener(address, authkey=authkey)
        self.con.show(f'Zap Server Application: Host [{address[0]}], Port[{address[1]}].')
        self.con.show('Instantiating the Manager...')
        self.manager = None
        self.con.show('Initialization is Complete...')

    def execute(self):
        """
        Start workers and wait client connections.
        :return: None
        """
        return self

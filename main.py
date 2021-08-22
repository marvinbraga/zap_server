# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Main Application Module
"""
import sys

from core.factories.whatsapp import FactoryWhatsappAdapter
from core.utils.classes import MessageConsole


class MainApplication:
    """
    Class to implement the initial point of application.
    """

    def __init__(self):
        self.con = MessageConsole()
        self.host = '0.0.0.0'
        self.port = 8777
        self.adapter = None

    def _start_message(self):
        self.con.show('Starting Zap Server...')
        return self

    def _verify_args(self, *args, **kwargs):
        self.con.show('Verifying args...')
        if len(args) <= 2:
            pass
        elif len(args) != 3:
            self.con.show('To start the Zap Server use command: zap_server_app.py <host> <port>', file=sys.stderr)
            raise SystemExit(1)
        else:
            self.host = args[1]
            self.port = int(args[2])
        return self

    def _is_mock_args(self, args):
        if '--mock' in args:
            self.adapter = FactoryWhatsappAdapter.MOCK
            self.con.show('--mock')
        else:
            self.adapter = FactoryWhatsappAdapter.DEFAULT
        return self

    def start(self, *args, **kwargs):
        """
        Start Server Application Instance and send args.
        :param args:
        :param kwargs:
        :return:
        """
        result = self if args else False
        if result:
            self._start_message()._verify_args(*args)._is_mock_args(args)
        return result

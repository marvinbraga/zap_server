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

from apps.zap_server_app import ZapServerApp
from core import settings
from core.factories.whatsapp import FactoryWhatsappAdapter
from core.utils.classes import MessageConsole


class MainApplication:
    """
    Class to implement the initial point of application.
    """

    def __init__(self):
        self._con = MessageConsole()
        self.host = '0.0.0.0'
        self.port = 8777
        self.adapter = None
        self.no_headless = False

    def _start_message(self):
        self._con.show('Starting Zap Server...')
        return self

    def _verify_args(self, *args, **kwargs):
        self._con.show('Verifying args...')
        if len(args) <= 2:
            pass
        elif len(args) != 3:
            self._con.show('To start the Zap Server use command: zap_server_app.py <host> <port>', file=sys.stderr)
            raise SystemExit(1)
        else:
            self.host = args[1]
            self.port = int(args[2])
        return self

    def _is_mock_args(self, args):
        if '--mock' in args:
            self.adapter = FactoryWhatsappAdapter.MOCK
            self._con.show('--mock')
        else:
            self.adapter = FactoryWhatsappAdapter.DEFAULT
        return self

    def _is_no_headless(self, args):
        self.no_headless = '--no_headless' in args
        if self.no_headless:
            self._con.show('--no_headless')
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
            self._start_message()._verify_args(*args)._is_mock_args(args)._is_no_headless(args)
        return result

    def execute(self, server_cls):
        """
        Execute the server application.
        :return: self
        """
        if server_cls:
            self._con.show('Starting server...')
            server_cls(
                address=(self.host, self.port),
                authkey=settings.AUTH_KEY.encode(),
                adapter=self.adapter, no_headless=self.no_headless
            ).execute()
        self._con.show('Ending server.')
        return self


if __name__ == '__main__':
    MainApplication().start(*sys.argv).execute(server_cls=ZapServerApp)

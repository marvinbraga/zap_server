# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Zap Server Application Module
"""
import traceback
from multiprocessing.connection import Listener

from core.factories.whatsapp import FactoryWhatsappAdapter
from core.utils.classes import MessageConsole


class ZapServerApp:
    """
    TCP Socket Server to Selenium.
    """

    def __init__(self, address, authkey, adapter=FactoryWhatsappAdapter.DEFAULT, no_headless=False):
        self._con = MessageConsole()
        self._con.show('Authorizing...')
        self._serv = Listener(address, authkey=authkey)
        self._con.show(f'Zap Server Application: Host [{address[0]}], Port[{address[1]}].')
        self._con.show('Instantiating the Manager...')
        self._manager = None
        self._con.show('Initialization is Complete...')

    def worker(self, client):
        """
        Waiting for client action.
        :param client: Thread accepted.
        :return:
        """
        try:
            while True:
                command = client.recv()
                if command:
                    self._con.show(f'Executing command: {command}...')
                    if self._manager:
                        result = self._manager.run_command(command_data=command)
                    else:
                        result = f'Echo: {command}'
                    self._con.show(f'Command executed {command}...')
                    client.send(result)
                    self._con.show(f'Output Value [{result}]...')
        except EOFError as e:
            self._con.show(e)
            self._con.show('Connection Closed with Client.')

    def execute(self):
        """
        Start workers and wait client connections.
        :return: None
        """
        while True:
            try:
                self._con.show('Waiting for client connection.')
                client = self._serv.accept()
                self._con.show(f'Connected by{client}.')
                self.worker(client)
            except Exception as e:
                self._con.show(e)
                traceback.print_exc()

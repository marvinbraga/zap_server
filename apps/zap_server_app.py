# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Zap Server Application Module
"""

import signal
import traceback
from multiprocessing.connection import Listener
from threading import Thread

from apps.names import Colossal
from core.utils.classes import MessageConsole
from server.factories.whatsapp import FactoryWhatsappAdapter
from server.managers import ManagerSingleton


class ZapServerApp:
    """
    TCP Socket Server to Selenium.
    """

    def __init__(self, address, authkey, adapter=FactoryWhatsappAdapter.DEFAULT, no_headless=False):
        Colossal.show()
        self._con = MessageConsole()
        self._con.show('Authorizing...')
        self._serv = Listener(address, authkey=authkey)
        self._con.show(f'Zap Server Application: Host [{address[0]}], Port[{address[1]}].')
        self._con.show('Instantiating the Manager...')
        self._manager = ManagerSingleton().set_adapter(adapter).set_no_headless(no_headless)
        self._con.show('Initialization is Complete...')
        self._worker_thread = None
        self._running = True

        signal.signal(signal.SIGINT, self._signal_handler)

    def _signal_handler(self, signum, frame):
        self._con.show('Received SIGINT. Stopping the worker thread...')
        self._running = False
        if self._worker_thread and self._worker_thread.is_alive():
            self._worker_thread.join()
        self._con.show('Worker thread stopped. Exiting...')
        exit(0)

    def worker(self, client):
        """
        Waiting for client action.
        :param client: Thread accepted.
        :return:
        """
        try:
            while self._running:
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
        while self._running:
            try:
                self._con.show('Waiting for client connection.')
                client = self._serv.accept()
                self._con.show(f'Connected by{client}.')
                self._worker_thread = Thread(target=self.worker, args=(client,))
                self._worker_thread.start()
            except Exception as e:
                self._con.show(e)
                traceback.print_exc()

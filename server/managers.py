# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Manager Module
"""
from multiprocessing import Semaphore

from apps.exceptions import ParserCommandException
from core.singletons.singleton_meta import Singleton
from server.commands.managers import CommandManager
from server.commands.splitters import SplitterCommand
from server.factories.whatsapp import FactoryWhatsappAdapter


class ManagerSingleton(metaclass=Singleton):
    """
    Manager to execute _adapter and commands.
    """

    _adapter = FactoryWhatsappAdapter.DEFAULT
    _managers = {}
    _semaphore = Semaphore()
    _no_headless = False

    @property
    def adapter(self):
        """
        Get value of _adapter property.
        :return: Object
        """
        return self._adapter

    @property
    def no_headless(self):
        """
        Get value of _no_headless property.
        :return: Boolean
        """
        return self._no_headless

    def set_no_headless(self, value):
        """
        Change the value of attribute "_no_headless".
        :param value: New value.
        :return: Self.
        """
        self._no_headless = value
        return self

    def set_adapter(self, value):
        """
        Set _adapter to run commands.
        :param value: Adapter object.
        :return: Self.
        """
        self._adapter = value
        return self

    def _get_manager(self, token):
        """
        Get manager to execute command instance.
        :param token: Token string.
        :return: CommandManager instance.
        """
        manager = self._managers.get(token)
        if manager is None:
            manager = CommandManager(
                self._adapter.get_cls(
                    token=token,
                    no_headless=self._no_headless
                )
            )
            self._semaphore.acquire()
            try:
                self._managers[token] = manager
            finally:
                self._semaphore.release()

        return manager

    def run_command(self, command_data):
        """
        Method to execute the selected command.
        :param command_data: Command Data.
        :return: Str with the command result or exception.
        """
        try:
            token, command, args = SplitterCommand(command_data).process().result()
        except ParserCommandException as e:
            return e.message
        else:
            manager = self._get_manager(token)
            try:
                cmd = manager.parse_command(command, args)
                try:
                    result = cmd.invoke().result
                finally:
                    if cmd.name == 'Quit':
                        self._semaphore.acquire()
                        try:
                            self._managers.pop(token)
                        finally:
                            self._semaphore.release()
                        del manager
            except Exception as e:
                result = str(e)
            return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Kill _managers instances.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        for manager in self._managers:
            cmd = manager.parse_command('Quit', None)
            cmd.invoke()
        self._managers = None

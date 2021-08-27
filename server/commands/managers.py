# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Command Manager Module
"""
from server.commands.classes import NoCommand


class AvailableCommands:
    """
    Register for available commands.
    """

    @staticmethod
    def get():
        """
        Method for exposing commands.
        :return:
        """
        return []


class CommandManager:
    """
    Class for command management.
    """

    def __init__(self, adaptee):
        self._adaptee = adaptee
        self._commands = AvailableCommands.get()

    def __del__(self):
        del self._adaptee
        self._commands = None

    def parse_command(self, name, args):
        """
        Method to retrieve command and populate parameters.
        :param name: Command name.
        :param args: Attributes for the command.
        :return:
        """
        command = NoCommand
        for com in self._commands:
            if name == com['name']:
                command = com['class']
                break
        return command(self._adaptee, args)

    def check(self, text):
        """
        Method for verifying the exposure of a command.
        :param text: Information to look for.
        :return: True/False.
        """
        for com in self._commands:
            if text in com['name']:
                return True
        return False

# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Command Manager Module
"""


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

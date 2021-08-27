# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Abstract Command Module
"""

from abc import ABCMeta, abstractmethod


class AbstractCommand(metaclass=ABCMeta):
    """
    Abstract class for commands.
    """

    def __init__(self, adaptee, args):
        self._adaptee = adaptee
        self._args = args
        self._result = None

    @property
    def adaptee(self):
        """
        Property to give access to the adapter.
        :return: Adaptee.
        """
        return self._adaptee

    @property
    def command_args(self):
        """
        Property to give access to arguments.
        :return: Args.
        """
        return self._args

    @property
    def result(self):
        """
        Property to give access to the command result.
        :return: Result.
        """
        return self._result

    @abstractmethod
    def invoke(self):
        """
        Abstract method to run the command.
        :return: Self.
        """
        pass

    @abstractmethod
    def name(self):
        """
        Abstract method to expose the command name.
        :return: Command name.
        """
        pass

# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Abstract Strategy Pattern Module
"""

from abc import ABCMeta, abstractmethod


class StrategyBase(metaclass=ABCMeta):
    """
    Basic strategy pattern class.
    """

    @abstractmethod
    def execute(self):
        """
        Method to run main process.
        :return: Self.
        """
        return self


class StrategyValueBase(StrategyBase):
    """
    Strategy pattern with basic value.
    """

    @abstractmethod
    def execute(self):
        """
        Method to run main process.
        :return: Self.
        """
        return self

    @abstractmethod
    def value(self):
        """
        Method to perform value process.
        :return:
        """
        pass

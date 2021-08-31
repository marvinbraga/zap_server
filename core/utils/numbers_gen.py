# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Generate Number Module
"""
from random import uniform
from time import sleep

from core.utils.strategies import StrategyValueBase


class GenerateNumber(StrategyValueBase):
    """
    Class to generate random numbers.
    """

    def __init__(self, end_number, start_number=0.0):
        self._end_number = end_number
        self._start_number = start_number
        self._value = None

    def execute(self):
        """
        Method to perform the choice of random numbers among the given range.
        """
        self._value = uniform(self._start_number, self._end_number)
        return self

    @property
    def value(self):
        """
        Property that retrieves the random value.
        """
        if self._value is None:
            self.execute()
        return self._value


class SleepRandom(GenerateNumber):
    """
    Class that performs a pause of a random value period.
    """

    def __init__(self, end_number, start_number=0.0):
        super().__init__(end_number=end_number, start_number=start_number)
        self._delay = uniform(0.2, 0.5)

    def execute(self):
        """
        Method to perform pause with random delay.
        """
        sleep(super(SleepRandom, self).execute()._value + self._delay)
        return self

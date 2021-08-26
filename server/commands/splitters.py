# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Zap Server Application Module
"""
from apps.exceptions import ParserCommandException


class SplitterCommand:
    """
    Class to separate args of command.
    """
    SEPARATOR = '||'

    def __init__(self, data):
        self._data = data
        self._token = ''
        self._command = ''
        self._args = []

    def process(self):
        """
        Split data and values of command.
        :return: Tuple with token, command and args.
        """
        self._args = self._data.split(self.SEPARATOR)
        if len(self._args) < 2:
            raise ParserCommandException()
        self._token = self._args.pop(0)
        self._command = self._args.pop(0)
        self.adjust_args()
        return self

    def adjust_args(self):
        """
        Create args list.
        :return: Self.
        """
        args = []
        for arg in self._args:
            if arg and arg.startswith('[') and arg.endswith(']'):
                temp = arg[1:-1]
                temp = temp.split(', ') if ',' in temp else [temp]
            else:
                temp = arg

            args.append(temp)
        self._args = args
        return self

    def result(self):
        """
        Mount the result values with attributes.
        :return: Tuple.
        """
        return self._token, self._command, self._args

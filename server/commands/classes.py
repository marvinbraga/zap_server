# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Command Classes Module
"""
from core.commands.bases import AbstractCommand


class NoCommand(AbstractCommand):
    """
    Class to represent an unknown command.
    """

    name = 'NoCommand'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)

    def __str__(self):
        return 'Unknown command executed.'

    def invoke(self):
        """
        Run the command.
        :return:
        """
        print(self)

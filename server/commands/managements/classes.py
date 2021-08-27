# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Managements Commands Classes Module
"""
from core.commands.bases import AbstractCommand
from server.commands.managements.exceptions import QuitException


class Quit(AbstractCommand):
    """
    Command to exit Whatsapp.
    """
    name = 'Quit'

    def __init__(self, adaptee, args):
        super().__init__(adaptee, args)

    def __str__(self):
        return self.name

    def invoke(self):
        """
        Run Command.
        :return: Self.
        """
        print(self)
        if self.adaptee:
            try:
                self._result = self.adaptee.manager.quit()
            except QuitException as e:
                self._result = e.message
        return self


class ManagerCommandsRegister:
    """
    Register for management commands.
    """
    available_classes = (
        Quit,
    )

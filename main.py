# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Main Application Module
"""


class MainApplication:
    """
    Class to implement the initial point of application.
    """

    def start(self, *args, **kwargs):
        """
        Start Server Application Instance and send args.
        :param args:
        :param kwargs:
        :return:
        """
        result = self if args else False
        return result

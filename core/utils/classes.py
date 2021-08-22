#!-*- coding: utf8 -*-
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Main Application Module
"""

from datetime import datetime


class MessageConsole:
    """
    Class to show information in console.
    """

    def show(self, *args, file=None):
        """
        Present message.
        :param args: print args.
        :param file: file to print.
        :return: self.
        """
        local_date_time = datetime.strftime(datetime.now(), '%a, %d/%b/%y %H:%M:%S')
        print(f'[{local_date_time}]: ', *args, file=file)
        return self

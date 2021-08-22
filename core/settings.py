# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Settings Server Module
"""

import os

from decouple import config

BASE_DIR = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/server')
AUTH_KEY = config('AUTH_KEY', cast=str)

# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Settings Server Module
"""

import os

from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/server')
AUTH_KEY = os.environ.get('AUTH_KEY')

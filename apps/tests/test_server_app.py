# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Test Server Application Module
"""
from multiprocessing.connection import Client

import pytest

from core import settings


@pytest.fixture
def initialize_client_app():
    """
    Start Instance of client to ZapServer.
    :return: Object or False
    """
    return Client(('127.0.0.1', 8777), authkey=settings.AUTH_KEY.encode())


def test_start_main(initialize_client_app):
    """
    Check Zap Server Initialization.
    :return:
    """
    c = initialize_client_app
    command = 'test_start_main||SendMessage||Contact Name||Initial Test.'
    c.send(command)
    resp = c.recv()
    print(f'Response: {resp}')
    assert initialize_client_app

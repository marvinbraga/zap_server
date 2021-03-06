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
from time import sleep

import pytest

from core import settings
from main import MainApplication

main_app = MainApplication()


@pytest.fixture
def initialize_mock_main():
    """
    Start Instance of Main Class with mock server.
    :return: Object or False
    """
    global main_app
    result = main_app.start('zap_server_app.py', '--mock') if main_app else False
    return result


@pytest.fixture
def initialize_client_app():
    """
    Start Instance of client to ZapServer.
    :return: Object or False
    """
    sleep(5)
    return Client(('0.0.0.0', 8777), authkey=settings.AUTH_KEY.encode())


def test_start_main(initialize_mock_main, initialize_client_app):
    """
    Check Zap Server Initialization.
    :return:
    """
    _ = initialize_mock_main
    c = initialize_client_app
    command = 'test_start_main||SendMessage||Contact Name||Initial Test.'
    c.send(command)
    resp = c.recv()
    print(f'Response: {resp}')
    assert initialize_client_app

# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Test Server Application Module
"""

import pytest
from apps.zap_server_app import ZapServerApp


server_app = ZapServerApp()


@pytest.fixture
def initialize_server_app():
    """
    Start Instance of ZapServer.
    :return: Object or False
    """
    global server_app
    result = server_app.execute() if server_app else False
    return result


def test_start_main(initialize_server_app):
    """
    Check Zap Server Initialization.
    :return:
    """
    assert initialize_server_app


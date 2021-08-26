# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Test Main Module
"""

import pytest

from main import MainApplication
from server.factories.whatsapp import FactoryWhatsappAdapter

main_app = MainApplication()


@pytest.fixture
def initialize_default_main():
    """
    Start Instance of Main Class with default params.
    :return: Object or False
    """
    global main_app
    result = main_app.start('zap_server_app.py', '0.0.0.0', 8777) if main_app else False
    return result


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
def initialize_no_headless_main():
    """
    Start Instance of Main Class with invisible browser.
    :return: Object or False
    """
    global main_app
    result = main_app.start('zap_server_app.py', '--_no_headless') if main_app else False
    return result


def test_start_main(initialize_default_main):
    """
    Check Server Initialization.
    :return:
    """
    assert initialize_default_main


def test_start_mock(initialize_mock_main):
    """
    Check Server Mock Initialization.
    :param initialize_mock_main: Mock fixture.
    :return:
    """
    assert initialize_mock_main.adapter == FactoryWhatsappAdapter.MOCK


def test_start_no_headless(initialize_no_headless_main):
    """
    Check Server Default Initialization in 'no headless' mode.
    :param initialize_no_headless_main: _no_headless fixture.
    :return:
    """
    main = initialize_no_headless_main
    assert main.adapter == FactoryWhatsappAdapter.DEFAULT and main.no_headless

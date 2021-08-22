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

main_app = MainApplication()


@pytest.fixture
def initialize_main():
    """
    Start Instance of Main Class.
    :return: Object or False
    """
    global main_app
    result = main_app.start('0.0.0.0', 8777, '--mock', '--no_headless') if main_app else False
    return result


def test_start_main(initialize_main):
    """
    Check Server Initialization.
    :return:
    """
    assert initialize_main

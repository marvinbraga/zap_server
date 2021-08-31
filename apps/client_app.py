# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Client Application Module
"""

from multiprocessing.connection import Client
from threading import Thread

from core import settings


def connect_to_server():
    """
    Method to connect to server.
    :return:
    """
    c = Client(('127.0.0.1', 8777), authkey=settings.AUTH_KEY.encode())
    commands = [
        'user_token||SendMessage||Group Name||Message Test by Client.',
        # 'user_token||GroupGetInviteLink||Group Name',
        # 'user_token||GroupOnlyAdminsChangeGroupData||Group Name',
        # 'user_token||GroupAllUsersChangeGroupData||Group Name',
        # 'user_token||GroupOnlyAdminsSendMessages||Group Name',
        # 'user_token||GroupAllUsersSendMessages||Group Name',
        # 'user_token||GroupOnlyAdminsSendMessages||Group Name',
        # 'user_token||IsConnected',
    ]
    try:
        for command in commands:
            c.send(command)
            resp = c.recv()
            print(f'Response: {resp}')
    except ConnectionRefusedError:
        print('Operation Canceled: Server refused connection.')
    except ConnectionError as e:
        print(f'Operation canceled: {str(e)}.')


if __name__ == '__main__':
    t = Thread(target=connect_to_server)
    t.start()
    t.join()

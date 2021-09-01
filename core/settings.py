# coding=utf-8
'''
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Settings Server Module
'''

import os
import platform

from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.normpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AUTH_KEY = os.environ.get('AUTH_KEY')

ELEMENTS_DATA_FILE = os.path.normpath(os.path.join(f'{BASE_DIR}/data/', 'elements_data.pkl'))
SETTINGS_TYPE = os.environ.get('SETTINGS_TYPE', default='PRD')

OS_WEB_DRIVER = platform.system()
if OS_WEB_DRIVER == 'Windows':
    CHROME_WEB_DRIVER = os.path.normpath(os.path.join(f'{BASE_DIR}/contrib/drivers/win/', 'chromedriver.exe'))
    FIREFOX_WEB_DRIVER = os.path.normpath(os.path.join(f'{BASE_DIR}/contrib/drivers/win/', 'geckodriver.exe'))
else:
    CHROME_WEB_DRIVER = os.path.normpath(os.path.join(f'{BASE_DIR}/contrib/drivers/linux/', 'chromedriver'))
    FIREFOX_WEB_DRIVER = os.path.normpath(os.path.join(f'{BASE_DIR}/contrib/drivers/linux/', 'geckodriver'))

SITE_ROOT = os.environ.get('SITE_ROOT')
URL_MEDIA_GROUPS = os.environ.get('URL_MEDIA_GROUPS', default=f'https://{SITE_ROOT}/media/images/groups')
# SMTP
EMAIL_HOST = os.environ.get('SMTP_HOST_NAME')
EMAIL_HOST_USER = os.environ.get('EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = EMAIL_PORT == 587
EMAIL_USE_SSL = EMAIL_PORT == 465
DEFAULT_FROM_EMAIL = u'Your Name <{0}>'.format(EMAIL_HOST_USER)

TEST_CONTACT_GROUP_MEMBER = os.environ.get('TEST_CONTACT_GROUP_MEMBER').replace('_', ' ')

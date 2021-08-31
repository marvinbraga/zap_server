# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Browsers Module
"""
import os
import pickle
from abc import ABCMeta
from enum import Enum

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from core import settings
from core.settings import BASE_DIR


class BrowserType(Enum):
    """
    Factory for available Browsers.
    """

    CHROME = 1
    FIREFOX = 2

    def new_instance(self, token=None, save_cookies=False, no_headless=False):
        """
        Method to retrieve an instance of the selected browser.
        :param token: User ID.
        :param save_cookies: Whether it is to save cookies.
        :param no_headless: If not it is to present browser window display.
        :return: Browser instance.
        """
        browser = {
            BrowserType.CHROME: ChromeBrowser,
            BrowserType.FIREFOX: FirefoxBrowser,
        }[self]
        return browser(token=token, save_cookies=save_cookies, no_headless=no_headless)


class BaseBrowser(metaclass=ABCMeta):
    """
    Abstract class for Browsers.
    """

    def __init__(self, token=None, session=None, save_cookies=False, no_headless=False):
        self._no_headless = no_headless
        self._save_cookies = save_cookies
        self._token = token
        self._cookies_file = os.path.normpath(
            os.path.join(f'{BASE_DIR}/server/.temp/', f'cookies_{self._token}.pkl'))
        self._session = session
        self._options = None
        self._browser = None

    def __del__(self):
        if self._browser:
            if self._save_cookies:
                pickle.dump(self._browser.get_cookies(), open(self._cookies_file, 'wb'))
            self._browser.quit()

    @property
    def browser(self):
        """
        Property to retrieve the instantiated browser.
        :return: Browser instance.
        """
        return self._browser

    @property
    def cookies_file(self):
        """
        Property to retrieve the cookie file.
        :return: The file.
        """
        return self._cookies_file

    @property
    def save_cookies(self):
        """
        Property to retrieve information if it is to save cookies.
        :return: Bool.
        """
        return self._save_cookies


class ChromeBrowser(BaseBrowser):
    """
    Chrome browser class.
    """

    def __init__(self, token=None, session=None, save_cookies=False, no_headless=False):
        super().__init__(token=token, session=session, save_cookies=save_cookies, no_headless=no_headless)
        self._options = ChromeOptions()

        if session:
            self._options.add_argument("--user-data-dir={}".format(session))
            self._options.add_argument("lang=pt-br")
            self._browser = webdriver.Chrome(options=self._options)
        else:
            try:
                if not self._no_headless:
                    self._options.add_argument("--headless")
                self._options.add_argument('--no-sandbox')
                self._options.add_argument('--disable-gpu')
                self._options.add_argument('disable-infobars')
                self._options.add_argument("--disable-extensions")
                self._options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

                self._browser = webdriver.Chrome(settings.CHROME_WEB_DRIVER, options=self._options)
                self._browser.delete_all_cookies()
            except Exception as e:
                print(str(e))
                from webdriver_manager.chrome import ChromeDriverManager
                self._browser = webdriver.Chrome(ChromeDriverManager().install(), options=self._options)


class FirefoxBrowser(BaseBrowser):
    """
    Firefox browser class.
    *An instance of this class will not work on Linux if the root user is being used.*
    """

    def __init__(self, token=None, session=None, save_cookies=False, no_headless=False):
        super().__init__(token=token, session=session, save_cookies=save_cookies, no_headless=no_headless)
        self._options = FirefoxOptions()
        if not self._no_headless:
            self._options.add_argument("--headless")
        self._options.add_argument("--lang=pt-br")
        if session:
            self._browser = webdriver.Firefox(options=self._options)
        else:
            try:
                self._options.add_argument('--no-sandbox')
                firefox_capabilities = DesiredCapabilities.FIREFOX
                firefox_capabilities['marionette'] = True
                firefox_capabilities['binary'] = settings.FIREFOX_WEB_DRIVER
                self._browser = webdriver.Firefox(capabilities=firefox_capabilities,
                                                  options=self._options)
            except Exception as e:
                print('Initialization error: ', e)
                from webdriver_manager.firefox import GeckoDriverManager
                self._browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                                  options=self._options)

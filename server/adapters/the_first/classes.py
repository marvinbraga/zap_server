# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

The First Selenium Whatsapp Adapter Module
"""
import base64
import datetime as dt
import json
import os
import pickle
import secrets
import time
from io import BytesIO
from threading import Thread
from urllib.parse import urlencode

from PIL import Image
from bs4 import BeautifulSoup

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.ui import WebDriverWait


class WhatsApp:
    """
    This class provides access to Whatsapp Web through Selenium.
    """

    def __init__(self, timeout, token, no_headless):
        self.timeout = timeout
        self.token = token
        self.no_headless = no_headless

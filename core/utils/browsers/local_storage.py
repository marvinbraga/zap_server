# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Local Storage Browser Module.

Usage Example:
--------------

*Getting the local storage:*
drive = None
storage = LocalStorage(driver)

*Setting an item:*
storage["my_key"] = 1234
storage.set("my_key2", 5678)

*Getting an item:*
print(storage["my_key"])  # raises a KeyError if the key is missing
print(storage.get("my_key"))  # returns None if the key is missing

*Deleting an item:*
storage.remove("my_key")

*Iterating on items:*
for key, value in storage.items():
    print("%s: %s" % (key, value))

*Deleting all items:*
storage.clear()
"""

import os
import pickle

from core.settings import BASE_DIR


class LocalStorage:
    """
    Class to retrieve information from Local Storage.
    """

    def __init__(self, driver, token, init_js=False):
        self._token = token
        self._driver = driver
        self._file_name = os.path.normpath(
            os.path.join(f'{BASE_DIR}/server/.temp/', f'{self._token}.profile'))
        if init_js:
            self._driver.execute_script("""
            function getLocalStoragePropertyDescriptor() {
                const iframe = document.createElement('iframe');
                document.head.append(iframe);
                const pd = Object.getOwnPropertyDescriptor(iframe.contentWindow, 'localStorage');
                iframe.remove();
                return pd;
            }
            Object.defineProperty(window, 'localStorage', getLocalStoragePropertyDescriptor());
            """)

    def __len__(self):
        return self._driver.execute_script('return window.localStorage.length;')

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return key in self.keys()

    def __iter__(self):
        return self.items().__iter__()

    def __repr__(self):
        return self.items().__str__()

    def items(self):
        """
        Method for recovering saved items.
        :return: List items.
        """
        return self._driver.execute_script(
            "var ls = window.localStorage, items = {}; "
            "for (var i = 0, k; i < ls.length; ++i) "
            "  items[k = ls.key(i)] = ls.getItem(k); "
            "return items; ")

    def keys(self):
        """
        Method to retrieve saved keys.
        :return: List of keys.
        """
        return self._driver.execute_script(
            "var ls = window.localStorage, keys = []; "
            "for (var i = 0; i < ls.length; ++i) "
            "  keys[i] = ls.key(i); "
            "return keys; ")

    def get(self, key):
        """
        Method to retrieve key value.
        :param key: The key.
        :return: Value.
        """
        return self._driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    def set(self, key, value):
        """
        Method for associating a value with a key.
        :param key: Key.
        :param value: Value to be recorded.
        :return: None.
        """
        self._driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def has(self, key):
        """
        Method to check if the key exists.
        :param key: Key.
        :return: Bool.
        """
        return key in self.keys()

    def remove(self, key):
        """
        Method for removing an item.
        :param key: Key.
        :return: None.
        """
        self._driver.execute_script("window.localStorage.removeItem(arguments[0]);", key)

    def clear(self):
        """
        Method to clean all items.
        :return: None.
        """
        self._driver.execute_script("window.localStorage.clear();")

    def load(self):
        """
        Method for loading saved file data.
        :return: Tuple (Dict, Bool).
        """
        try:
            if os.path.isfile(self._file_name):
                with open(self._file_name, "rb") as file:
                    return pickle.load(file), True
            else:
                return self.items(), True
        except Exception:
            return {}, False

    def save(self):
        """
        Method for saving information to file.
        :return: Self.
        """
        os.makedirs("./server/.temp/", exist_ok=True)
        with open(self._file_name, "wb") as file:
            pickle.dump(self._parse(), file)
        return self

    def _parse(self):
        """
        Method to populate dictionary with retrieved data.
        :return: Dict.
        """
        profile = {}
        for key, value in self.items().items():
            profile[key] = value
        return profile

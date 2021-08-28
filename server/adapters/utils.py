# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Utils Adapter Module
"""
import os
from abc import ABCMeta, abstractmethod
from enum import Enum

import requests

from core import settings


class FactoryAdjustPath(Enum):
    """
    Factory to instantiate object according to image directory.
    """
    GROUP_IMAGE = 1
    PICTURE = 2
    DOCUMENT = 3

    def new_instance(self, old_path):
        """
        Method in the Factory Method pattern.
        :param old_path: Internal server path.
        :return: Object to adjust the path.
        """
        cls = {
            FactoryAdjustPath.GROUP_IMAGE: AdjustGroupImagePath,
            FactoryAdjustPath.PICTURE: None,
            FactoryAdjustPath.DOCUMENT: None
        }[self]
        return cls(old_path)


class AbstractAdjustPath(metaclass=ABCMeta):
    """
    Abstract class for setting paths.
    """

    def __init__(self, old_path):
        self._old_path = os.path.normpath(old_path)
        self._new_path = None

    @abstractmethod
    def execute(self):
        """
        Abstract method for performing adjustment processing.
        :return: self.
        """
        pass

    @property
    def new_path(self):
        """
        Method to retrieve the adjusted path.
        :return: New path.
        """
        self._new_path = ''
        self.execute()
        return self._new_path


class AdjustGroupImagePath(AbstractAdjustPath):
    """
    Abstract class for adjusting paths related to group images.
    """

    def execute(self):
        """
        Method to retrieve URL from a group image path.
        Mount the URL to retrieve group images.
        :return: self.
        """
        path = self._old_path.split('/')
        self._new_path = f'{settings.URL_MEDIA_GROUPS}/{path[-1]}'
        return self


class SaveFile:
    """
    Save image in path to group images.
    """

    def __init__(self, location):
        self._location = location
        self.url = None

    def from_url(self):
        """
        Retrieves the way to save group images.
        :return: self.
        """
        url = FactoryAdjustPath.GROUP_IMAGE.new_instance(self._location).new_path
        self._save(url)
        return self

    def _save(self, url):
        """
        Save the group image in the given path.
        :param url: Path to save.
        :return: self.
        """
        try:
            if os.path.isfile(self._location):
                return self
            file_data = requests.get(url).content
        except Exception as e:
            print(e)
        else:
            try:
                with open(self._location, 'wb') as handle:
                    handle.write(file_data)
                    handle.close()
            except Exception as e:
                print(e)
        return self

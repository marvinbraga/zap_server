# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

QR-Code's PoCs Module
"""
import base64
from abc import ABCMeta, abstractmethod
from enum import Enum
from io import BytesIO

from PIL import Image

from core.utils.qr_code.classes import QrCode


class AbstractVCard(metaclass=ABCMeta):
    """
    Interface to VCards.
    """

    @abstractmethod
    def get_text(self):
        """
        This method generate a string result.
        """
        pass


class VCardFactory(Enum):
    """
    Factory to VCard.
    """

    VCARD_30 = 30
    VCARD_40 = 40

    def new_instance(self, data_obj):
        """
        Method to get the VCard object.
        :param data_obj: VCard info.
        :return: Instance of VCard.
        """
        result = {
            VCardFactory.VCARD_30: VCard30,
            VCardFactory.VCARD_40: VCard40,
        }[self]
        return result(data_obj)


class VCard30(AbstractVCard):
    """
    Class to implement VCard 3.0
    """

    def __init__(self, data_obj):
        self.data_obj = data_obj

    def get_text(self):
        """
        This method generate a V3.0 string version.
        """
        dt = self.data_obj
        first_part = 'BEGIN:VCARD\n' \
                     'VERSION:3.0\n' \
                     f'N:{dt.last_name};{dt.first_name};;{dt.usage};\n' \
                     f'FN:{dt.first_name} {dt.last_name}\n' \
                     f'ORG:{dt.company}\n' \
                     f'TITLE:{dt.position}\n' \
                     f'URL:{dt.website}\n'
        avatar_photo = ''
        if dt.photo_url:
            avatar_photo = f'PHOTO;VALUE=URI;TYPE={dt.photo_img_type}:{dt.photo_url}\n'

        sec_part = f'EMAIL:{dt.email}\n' \
                   f'TEL;TYPE=voice,work:{dt.phone_work}\n' \
                   f'TEL;TYPE=voice,home:{dt.phone_private}\n' \
                   f'TEL;TYPE=voice,cell,pref:{dt.phone_mobile}\n' \
                   f'ADR;TYPE=WORK,PREF:;;{dt.address};{dt.city};{dt.state};{dt.zipcode};{dt.country}\n' \
                   'END:VCARD'

        result = first_part + avatar_photo + sec_part
        return result


class VCard40(AbstractVCard):
    """
    Class to implement VCard 4.0
    """

    def __init__(self, data_obj):
        self.data_obj = data_obj

    def get_text(self):
        """
        This method generate a V4.0 string version.
        """
        photo = ''
        dt = self.data_obj
        first_part = 'BEGIN:VCARD\n' \
                     'VERSION:4.0\n' \
                     f'N:{dt.last_name};{dt.first_name};;{dt.usage};\n' \
                     f'FN:{dt.first_name} {dt.last_name}\n' \
                     f'ORG:{dt.company}\n' \
                     f'TITLE:{dt.position}\n' \
                     f'URL:{dt.website}\n'
        if dt.photo_url:
            photo = f'PHOTO;MEDIATYPE=image/{dt.photo_img_type}:{dt.photo_url}\n'

        sec_part = f'EMAIL:{dt.email}\n' \
                   f'TEL;TYPE=voice,work:{dt.phone_work}\n' \
                   f'TEL;TYPE=voice,home:{dt.phone_private}\n' \
                   f'TEL;TYPE=voice,cell,pref:{dt.phone_mobile}\n' \
                   f'ADR;TYPE=WORK;PREF=1:;;{dt.address};{dt.city};{dt.state};{dt.zipcode};{dt.country}\n' \
                   'END:VCARD'

        result = first_part + photo + sec_part
        return result


class VCardQrCode:
    """
    Class to create a VCard QR Code.
    """

    def __init__(self, first_name, last_name, phone_mobile, usage='', photo_url='',
                 phone_private='', company='', position='', phone_work='', fax_work='',
                 fax_private='', email='', website='', address='', zipcode='',
                 city='', state='', country='', version=VCardFactory.VCARD_40):
        # Contact info.
        self.version = version
        self.photo_url = photo_url
        self.photo_img_type = ''
        if photo_url:
            self.photo_img_type = 'png'
        self.usage = usage
        self.country = country
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.address = address
        self.website = website
        self.email = email
        self.fax_private = fax_private
        self.fax_work = fax_work
        self.phone_mobile = phone_mobile
        self.phone_private = phone_private
        self.phone_work = phone_work
        self.position = position
        self.company = company
        self.last_name = last_name
        self.first_name = first_name
        # Other properties.
        self._text = ''

    def _make_text(self):
        """
        This method create a byte string with the information of contact.
        """
        self._text = self.version.new_instance(data_obj=self).get_text()
        return self

    @property
    def text(self):
        """
        This method return the text property value.
        """
        return self._text

    def generate_qrcode(self, file_name):
        """
        This method execute the creation of qr-code.
        """
        self._make_text()
        str_b64 = QrCode(data=self.text, box_size=1).as_base64()
        image = Image.open(BytesIO(base64.b64decode(str_b64)))
        image.save(file_name)
        return self


def test_qrcode(file_name, vcard):
    vcard.generate_qrcode(file_name)
    qr_code = Image.open(file_name)
    text = QrCode.decode_from_image(qr_code)['data']
    print(text)


if __name__ == '__main__':
    vcard_marcus = VCardQrCode(first_name='Marcus Vinicius', last_name='Braga',
                               photo_url='https://www.gravatar.com/avatar/7ceb2f2eab9b3329a826eb138d602981?s=28&d=mm',
                               phone_mobile='+55 00 0000-0000',
                               company='marvinbraga.com.br',
                               email='marcus@marvinbraga.com.br',
                               website='https://marvinbraga.com.br',
                               country='Brazil')
    test_qrcode('qr-code-marcus-marvinbraga.png', vcard_marcus)

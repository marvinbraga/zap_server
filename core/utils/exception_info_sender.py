# coding=utf-8
"""
GNU AFFERO GENERAL PUBLIC LICENSE
Version 3, 19 November 2007
https://github.com/marvinbraga/zap_server
Marcus Vinicius Braga, marcus@marvinbraga.com.br
Aug 2021

Exception Information Sender Module.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread

from core.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, DEFAULT_FROM_EMAIL


class ExceptionInfoSender:
    """
    Class for sending email notification of exceptions raised during any usage process.
    """

    def __init__(self, message):
        self._message = message

    def send(self):
        """
        Method for sending notification email.
        """
        t = Thread(target=self._send_multipart_mail, args=[self._message])
        t.start()

    @staticmethod
    def _send_multipart_mail(msg):
        """
        Send a mail.
        :param msg: Text Message.
        :return: None.
        """

        message = MIMEMultipart("alternative")
        message["Subject"] = "Zap Server ERROR"
        message["From"] = DEFAULT_FROM_EMAIL
        message["To"] = DEFAULT_FROM_EMAIL

        text = """\
        The exception below was raised during the usage process.
        {0}
        """.format(msg)
        html = """\
        <html lang="pt-br">\
        <head>\
          <meta charset="UTF-8">\
        </head>\
        <body>\
          <p><b>This exception was raised during the usage process.</b></p>\
          <p>{0}</p>\
        </body>\
        </html>
        """.format(msg)

        message.attach(MIMEText(text))
        message.attach(MIMEText(html, 'html'))
        try:
            with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
                server.starttls()
                server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                server.sendmail(
                    DEFAULT_FROM_EMAIL, DEFAULT_FROM_EMAIL,
                    message.as_string()
                )
        except Exception as e:
            print(f'*** SEND MAIL Error: {str(e)}')

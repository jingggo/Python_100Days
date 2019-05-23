"""

@Author:jyang
@Date:5/21/2019
"""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import urllib


def main():
    message = MIMEMultipart()

    text_content = MIMEText('', 'plain')
"""
下面的代码演示了如何在Python发送邮件

@Author:jyang
@Date:5/21/2019
"""
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    charset = 'utf-8'
    # 请自行修改下面的邮件发送者和接受者
    sender = '673592948@qq.com'
    receivers = ['67']
    message = MIMEText('Hello World - Python', 'plain', charset)
    message['From'] = Header('', charset)
    message['To'] = Header('', charset)
    message['Subject'] = Header('', charset)
    smtper = SMTP('smtp.126.com')
    #
    smtper.login(sender, '')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功！')


if __name__ == '__main__':
    main()


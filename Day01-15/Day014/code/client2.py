"""

@Author:jyang
@Date:5/21/2019
"""

from socket import socket
from json import loads
from base64 import b64decode
import os


def main():
    client = socket()
    client.connect(('127.0.0.1', 5566))
    # 定义一个保存二进制的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转换成字典
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    filename = os.getcwd() + r'\Day01-15\Day014\res\\' + filename
    with open(filename, 'wb') as f:
        f.write(b64decode(filedata))
    print('图片已保存！')


if __name__ == '__main__':
    main()
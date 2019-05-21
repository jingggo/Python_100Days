"""
设计一个使用多线程技术处理多个用户请求的服务器，该服务器会向连接到服务器的客户端发送一张图片。

@Author:jyang
@Date:5/21/2019
"""

from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread
import os

def main():
    # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    server = socket()
    server.bind(('127.0.0.1', 5566))
    server.listen(512)
    print('服务器启动监听...')
    pic_filepath = os.getcwd() + '\Day01-15\Day014\code\guido.jpg'
    print(pic_filepath)
    with open(pic_filepath, 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')

    while True:
        client, addr = server.accept()
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()
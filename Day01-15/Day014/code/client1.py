"""
我们也可以通过Python的程序来实现TCP客户端的功能，相较于实现服务器程序，实现客户端程序就简单多了，代码如下所示

@Author:jyang
@Date:5/21/2019
"""

from socket import socket


def main():
    # 1.创建套接字对象默认使用Ipv4和TCP协议
    client = socket()
    client.connect(('127.0.0.1', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == '__main__':
    main()
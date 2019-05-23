"""
套接字 - 基于TCP协议创建时间客户端(client)
@Author:jyang
@Date:5/21/2019
"""

from socket import *


client = socket()
client.connect(('localhost', 6789))
while True:
    data = client.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
client.close()
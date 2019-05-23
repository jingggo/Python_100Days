"""
套接字 - 基于TCP协议创建时间服务器(server)

@Author:jyang
@Date:5/21/2019
"""

from socket import *
from time import *


server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 6789))
server.listen()
print('服务器已经启动正在监听客户端连接.')

while True:
    client, addr = server.accept()
    print('客户端%s:%d连接成功.' % (addr[0], addr[1]))
    curtime = localtime(time())
    timestr = strftime('%Y-%m-%d %H:%M:%S', curtime)
    client.send(timestr.encode('utf-8'))
    client.close()
server.close()
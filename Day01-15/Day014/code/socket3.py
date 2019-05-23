"""
套接字 - 基于UDP协议Echo服务器

@Author:jyang
@Date:5/21/2019
"""

from socket import *


server = socket(AF_INET, SOCK_DGRAM)
server.bind(('localhost', 6789))
while True:
    data, addr = server.recvfrom(1024)
    server.sendto(data, addr)
server.close()
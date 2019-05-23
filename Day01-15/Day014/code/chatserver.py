"""

@Author:jyang
@Date:5/21/2019
"""

from socket import socket
from threading import Thread

def main():

    class ClientHandler(Thread):

        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            try:
                while True:
                    try:
                        data = self._client.recv(1024)
                        if data.decode('utf-8') == 'bye':
                            clients.remove(self._client)
                            self._client.close()
                            break
                        else:
                            for client in clients:
                                client.send(data)
                    except Exception as e:
                        print(e)
                        clients.remove(self._client)
                        break
            except Exception as e:
                print(e)

    server = socket()
    server.bind(('127.0.0.1', 12345))
    server.listen(512)
    print('服务器启动开始监听...')
    clients = []
    while True:
        cur_client, addr = server.accept()
        print(addr[0], '连接到服务器.')
        clients.append(cur_client)
        ClientHandler(cur_client).start()


if __name__ == '__main__':
    main()
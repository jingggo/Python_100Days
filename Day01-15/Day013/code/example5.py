"""
从已有类Tread创建新类
@Author:jyang
@Date:5/20/2019
"""

from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_dw = randint(5, 10)
        sleep(time_to_dw)
        print('%s下载完成！耗费%d秒' % (self._filename, time_to_dw))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到精通.pdf')
    t1.start()
    t2 = DownloadTask('Ugly Duckling.txt')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费%.2f秒' % (end-start))


if __name__ == '__main__':
    main()
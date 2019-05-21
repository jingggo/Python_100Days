"""

@Author:jyang
@Date:5/20/2019
"""

from random import randint
from time import time, sleep
from multiprocessing import Process

def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = 5 #randint(5,10)
    sleep(time_to_download)
    print('%s下载完成！耗时%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到精通.pdf')
    download_task('Ugly Darking.mp4')
    end = time()
    print('总共耗费了%d秒。' % (end-start) )


def main_mulprocess():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到精通.pd', ))
    p2 = Process(target=download_task, args=('Ugly Darking.mp4', ) )
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%d秒。' % (end - start) )


if __name__ == '__main__':
    print('*' * 20 + '单线程' + '*' * 20)
    main()
    print('*' * 20 + '多线程' + '*' * 20)
    main_mulprocess()
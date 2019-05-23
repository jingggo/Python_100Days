"""
从天行数据网站下载图片
@Author:jyang
@Date:5/21/2019
"""
from time import time
from threading import Thread
import requests
import os


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/')+1:]
        # filename = os.getcwd() + filename
        resp = requests.get(self.url)
        with open(filename, 'wb') as f:
            f.write(resp.content)


def main():
    my_key = '4c732116c7b9c2432f4cf8170abec6e7'
    resp = requests.get(
        'http://api.tianapi.com/meinv/?&key=%s&num=10' % (my_key))
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHandler(url).start()


if __name__ == '__main__':
    main()

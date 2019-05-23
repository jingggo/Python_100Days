"""
中国日报获取新闻
利用requests库和正则表达式
@Author:jyang
@Date:5/23/2019
"""
import requests
import json
import re
import datetime


def _save_context_to_debug():
    # request = requests.get(url)
    if request.status_code == 200:
        try:
            with open('chinadaily.htm', 'w') as f:
                f.write(request.text)
        except IOError as e:
            print(e.strerror)


def get_hrefs(news):
    """

    :param news:
    :return: ["201905/23/WS5ce5f121a3104842260bd40d.html",]
    """
    hrefs = []
    for n in news:
        href = re.search(r'{0}/.*html'.format(today), n).group(0)
        if href not in hrefs:
            hrefs.append(href)
            # print(href)
    return hrefs


def get_news_content():
    pass


if __name__ == '__main__':
    today = '{0}{1}/{2}'.format(
        datetime.datetime.now().year,
        str(datetime.datetime.now().month).zfill(2),
        str(datetime.datetime.now().day).zfill(2)
    )
    url = 'https://language.chinadaily.com.cn/'
    request = requests.get(url, timeout=120.00)
    today_news = re.findall(r'<a.*href="//language.chinadaily.com.cn/a/{0}.*</a>'.format(today), request.text)
    herfs = get_hrefs(today_news)
    for h in herfs:
        url = 'https://language.chinadaily.com.cn/a/{0}'.format(h)
        r = requests(url)
        print(r.text)



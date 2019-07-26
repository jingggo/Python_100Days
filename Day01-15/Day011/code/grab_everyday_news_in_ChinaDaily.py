"""
获取中国日报每日播报
利用requests库和正则表达式等方法
@Author:jyang
@Date:5/23/2019
"""
import requests
from requests.exceptions import ConnectionError
import time
import re
import datetime
from bs4 import BeautifulSoup
from urllib import request,parse
from docx import Document
from docx.oxml.ns import qn

# def _save_context_to_debug():
#     # request = requests.get(url)
#     if req.status_code == 200:
#         try:
#             with open('chinadaily.htm', 'w') as f:
#                 f.write(req.text)
#         except IOError as e:
#             print(e.strerror)


def try_request(url):
    page = ''
    while page == '':
        try:
            page = requests.get(url)
            break
        except ConnectionError:
            print("Connection refused by the server.")
            print("Let me sleep for 5 seconds")
            print("Zzzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
        except Exception as e:
            print(e)
    return page


def get_hrefs(news):
    """
    get 'href' atti from 'a' tag
    :param news:
    :return: ["//language.chinadaily.com.cn/a/201905/27/WS5ceb90b3a3104842260be04a.html",]
    """
    hrefs = []
    for n in news:
        s = BeautifulSoup(n, 'html.parser')
        href = s.a['href']
        if href not in hrefs:
            hrefs.append(href)
            # print(href)
    return hrefs


def get_news_content(html_doc, filename):
    soup = BeautifulSoup(html_doc, "html.parser")
    cn_title = soup.find(class_='main_title1')
    en_title = soup.find(class_='main_title2')
    content_ps = soup.find(id='Content').find_all('p')
    with open(filename, 'w',encoding='utf-8') as f:
        f.write(cn_title.text + '\n')
        f.write(en_title.text + '\n')
        for p in content_ps:
            f.write(p.text + '\n')

    audio_url = soup.audio['src']
    get_audio(audio_url, filename)


def get_wechat_news_content(html_doc, filename):
    soup = BeautifulSoup(html_doc, "html.parser")
    content_ps = soup.find(id='js_content').find_all('p')
    with open(filename, 'w',encoding='utf-8') as f:
        for p in content_ps:
            f.write(p.text + '\n')

    # audio_url = soup.audio['src']
    # get_audio(audio_url, filename)


def get_audio(url, filename):
    url = "https:" + url
    filename = filename.split('.')[0] + '.' + url.split('.')[-1]
    request.urlretrieve(url, filename)


def transfer_txt_to_doc(transfer_file):
    file = Document()
    file.styles['Normal'].font.name = u'微软雅黑'
    file.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'微软雅黑')

    # transfer_file = 'CNDaily_20190529.txt'
    with open(transfer_file, 'r', encoding='utf-8') as f:
        file.add_paragraph(f.read().strip())

    file.save(transfer_file[:transfer_file.rindex('.') + 1] + 'docx')


def main():
    y = str(datetime.datetime.now().year)
    m = str(datetime.datetime.now().month).zfill(2)
    d = str(datetime.datetime.now().day).zfill(2)
    today = '{0}{1}/{2}'.format(y, m, d)
    url = 'https://language.chinadaily.com.cn/audio_cd'  # https://language.chinadaily.com.cn/
    req = try_request(url)
    # _save_context_to_debug()
    today_news = re.findall(r'<a.*href="//language.chinadaily.com.cn/a/{0}.*</a>'.format(today), req.text) # get all needed tags
    herfs = get_hrefs(today_news)
    print('%s 有%d篇新闻。' % (today, len(herfs)))
    for i, h in enumerate(herfs):
        url = 'https:{0}'.format(h)
        print('新闻播报: %s' % url)
        r = try_request(url)
        filename = 'CNDaily_' + today.replace('/', '') + '.txt'
        get_news_content(r.text, filename)
        transfer_txt_to_doc(filename)


def wechat():
    y = str(datetime.datetime.now().year)
    m = str(datetime.datetime.now().month).zfill(2)
    d = str(datetime.datetime.now().day).zfill(2)
    today = '{0}{1}/{2}'.format(y, m, d)
    url = 'https://mp.weixin.qq.com/s/--cwNHH9juwbjDqeD9R8YQ'
    req = try_request(url)
    filename = 'CNDaily_' + today.replace('/', '') + '.txt'
    get_news_content(req.text, filename)


if __name__ == '__main__':
    main()
    # wechat()




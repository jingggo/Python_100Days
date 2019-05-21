"""

@Author:jyang
@Date:5/18/2019
"""

import requests
import json


def main():
    my_key = 'youKey'
    resp = requests.get('http://api.tianapi.com/txapi/joke/?&key=%s&num=10' % (my_key))
    data_model = json.loads(resp.text) # 字符串反序列化为Python对象
    newslist = data_model['newslist']

    try:
        f = open('jokes.txt', 'w+', encoding='utf-8')
        for news in newslist:
            title = news['title'] + '\n'
            content = news['content'] + '\n'
            f.write(title)
            f.write(content)
    except IOError as e:
        print(e)
    finally:
        f.close()



if __name__ == '__main__':
    main()
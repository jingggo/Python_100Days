"""
从一段文字中提取出国内手机号码

@Author:jyang
@Date:5/19/2019
"""
import re


def main():
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现的数字
    pattern = re.compile(r'(?<=\D)1[35874]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    mylist = re.findall(pattern, sentence)
    print(mylist)

    print('-'*10 + '华丽的分割线' + '-'*10)
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('-' * 10 + '华丽的分割线' + '-' * 10)

    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()
"""
实现判断一个数是不是回文数的函数
12321,1234321
@Author:jyang
@Date:5/14/2019
"""


def is_palindrome1(num):
    """
    利用list的reversed函数倒叙
    :param num:
    :return:
    """
    l = list(str(num))
    is_palindrome = True
    for i in range(len(l)):
        if l[i] != l[-1-i]:
            is_palindrome = False
    if is_palindrome:
        print('%d是回文数！' % num)
    else:
        print('%d不是回文数！' % num)


def is_palindrome2(num):
    """
    用数学方法求出倒数 除10取余得个位数
    :param num:
    :return:
    """
    temp = num
    total = 0
    while temp>0:
        total = total*10 + temp%10
        temp //= 10 #取整
    if num==total:
        print('%d是回文数！' % num)
    else:
        print('%d不是回文数！' % num)

if __name__=='__main__':
    num=int(input('Please input a number...\n'))
    is_palindrome1(num)
    is_palindrome2(num)
"""
输入一个正整数N判断它是否为素数
思路：
1. 取N的平方根为end，如果2~end之间无能被N整数的数，则为素数
@Author:jingo
@Date:5/9/2019
"""

from math import sqrt

def method1():
    num = int(input('Please input a positive integer: '))
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end+1):
        if num % x == 0:
            is_prime = False
            break

    if is_prime and num!=1:
        print('%d is a Prime' % num)
    else:
        print('%d is not a Prime' % num)

if __name__=='__main__':
    method1()
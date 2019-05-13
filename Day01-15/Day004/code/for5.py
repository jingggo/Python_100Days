"""
输入两个正整数计算最大公约数和最小公倍数
如果数a能被数b整除，a就叫做b的倍数，b就叫做a的约数。
几个整数中公有的约数，叫做这几个数的公约数；其中最大的一个，叫做这几个数的最大公约数。
几个自然数公有的倍数，叫做这几个数的公倍数，其中最小的一个自然数，叫做这几个数的最小公倍数。
@Author:jyang
@Date:5/10/2019
"""


def method1():
    a = int(input('a = '))
    b = int(input('b = '))

    c = 0
    min = (a if a<b else b)
    max = (b if a<b else a)
    l = range(min-1,0,-1)
    for i in range(min-1,0,-1):
        if a%i==0 and b%i==0:
            c=i
            print('最大公约数为：%d' % c)
            break

    for i in range(max, a*b+1):
        if i%b==0 and i%a==0:
            print('最小公倍数为：%d' % i)
            break


def method2():
    a = int(input('a = '))
    b = int(input('b = '))

    if a>b:
        (a, b) = (b, a)
    for factor in range(a, 0, -1):
        if a%factor==0 and b%factor==0:
            print('%d and %d 的最大公约数为：%d' % (a, b, factor) )
            print('%d and %d 的最小公倍数为：%d' % (a, b, a*b/factor) )
            break

if __name__=='__main__':
    method2()
    method1()

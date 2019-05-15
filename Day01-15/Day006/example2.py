"""
实现计算求最大公约数和最小公倍数的函数。
@Author:jyang
@Date:5/14/2019
"""


def gcd(x, y):
    """
    求最大公约数
    :param x:
    :param y:
    :return:
    """
    (x, y) = (y, x) if x>y else(x, y)
    for i in range(x, 0, -1):
        if x%i==0 and y%i==0:
            return i


def lcm(x, y):
    """
    求最小公倍数
    :param x:
    :param y:
    :return:
    """
    (x, y) = (y, x) if x > y else(x, y)
    for i in range(y, x*y):
        if i%x==0 and i%y==0:
            return i

x = int(input('x='))
y = int(input('y='))
print(gcd(x, y))
print(lcm(x, y))

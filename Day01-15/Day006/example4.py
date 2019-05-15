"""
判读一个数是不是素数
@Author:jyang
@Date:5/14/2019
"""
import math


def is_prime(num):
    is_prime = True
    for _ in range(2, int(math.sqrt(num))):
        if num % _ == 0:
            is_prime = False
    if is_prime is True:
        print('%d is a prime' % num)
    else:
        print('%d is not a prime' % num)

is_prime(17)
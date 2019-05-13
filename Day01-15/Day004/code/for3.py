"""
输入非负整数n计算n!
一个正整数的阶乘（factorial）是所有小于及等于该数的正整数的积，并且0的阶乘为1。自然数n的阶乘写作n!。
n! = 1 * 2 * 3 ~~~ (n-1) *  n
@Author:jyang
@Date:5/9/2019
"""

n = int(input('n = '))
result = 1
for x in range(1, n+1):
    result *= x

print('{} 的阶乘为 {}'.format(n, result))
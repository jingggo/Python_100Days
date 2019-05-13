"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

@Author:jyang
@Date:5/10/2019
"""

import math

l = []
for i in range(100, 1000):
    a = int(i/100)
    b = int(i%100/10)
    c = int(i%100%10)
    if i == math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3):
        l.append(i)

print(l)
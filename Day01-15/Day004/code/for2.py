"""
对1~100之间的偶数求和
@Author:jyang
@Date:5/9/2019
"""


def sum1():
    sum=0
    for x in range(2,101,2):
        sum += x
    print(sum)

def sum2():
    sum=0
    for x in range(101):
        if x%2==0:
            sum += x
    print(sum)


if __name__=='__main__':
    sum1()
    sum2()
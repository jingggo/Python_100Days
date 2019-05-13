"""
用while循环实现1~100求和

@Author:jyang
@Date:5/10/2019
"""


def sum1():
    n = 0
    sum = 0
    max = 100
    while True:
        sum+=n
        n+=1
        if n==max+1:
            break
    print('Sum is from 1 to %d is: %d' % (max, sum))


def sum2():
    n=1
    sum=0
    while n<=100:
        sum+=n
        n+=1
    print(sum)

if __name__=='__main__':
    sum2()
    sum1()
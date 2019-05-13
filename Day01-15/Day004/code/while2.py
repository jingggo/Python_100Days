"""
用while循环实现1~100之间的偶数求和

@Author:jyang
@Date:5/10/2019
"""

def sum():
    n=2
    sum=0
    while n<=100:
        sum+=n
        n+=2

    print(sum)

if __name__=='__main__':
    sum()
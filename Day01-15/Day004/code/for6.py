"""
print *
*
**
***
****
*****


@Author:jyang
@Date:5/10/2019
"""


def method1():
    row = int(input('请输入行数: '))
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


def method2():
    row = int(input('请输入行数: '))

    for i in range(row):
        print('*'*(i+1))

    for i in range(row):
        print(('*'*(i+1)).zfill(row).replace('0', ' '))

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


if __name__=='__main__':
    method1()
    method2()
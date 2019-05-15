"""
通过yield关键字将一个普通函数改造成生成器函数
@Author:jyang
@Date:5/15/2019
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a


def main():
    for v in fib(20):
        print(v)

if __name__ == '__main__':
    main()


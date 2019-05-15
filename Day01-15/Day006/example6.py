"""
global
@Author:jyang
@Date:5/14/2019
"""


def aoo():
    a = 200
    print(a)  # 200

def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    aoo()
    print(a)    # 100

    foo()
    print(a)  # 200
"""

@Author:jyang
@Date:5/15/2019
"""

class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('Hi')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()
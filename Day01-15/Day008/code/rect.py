"""
定义和使用矩形类

@Author:jyang
@Date:5/15/2019
"""


class Rect(object):

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def perimeter(self):
        return (self.__width + self.__height)*2

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        "矩形对象的字符串表达式"""
        return '矩形[%f, %f]' % (self.__width, self.__height)

    def __del__(self):
        """析构器"""
        print('销毁矩形对象')


if __name__ == '__main__':
    rec1 = Rect()
    print(rec1)
    print(rec1.perimeter())
    print(rec1.area())

    rec2 = Rect(3.5, 4.5)
    print(rec2)
    print(rec2.perimeter())
    print(rec2.area())
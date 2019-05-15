"""
另一种创建类的方式

@Author:jyang
@Date:5/15/2019
"""


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print('%s正在学习%s.' % (self._name, course_name))


def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    s1 = Student('韩梅梅')
    s1.study('电磁场与电磁波')


if __name__ == '__main__':
    main()
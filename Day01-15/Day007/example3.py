"""
我们还可以使用列表的生成式语法来创建列表
@Author:jyang
@Date:5/15/2019
"""
import sys

def main():
    f = [ x for x in range(1,10)]
    print(f)

    f = [ x+y for x in 'ABCDE' for y in '123456']
    print(f)

    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要花费较多的内存空间
    f = [ x**2 for x in range(1, 1000)]
    print(sys.getsizeof(f)) # 查看对象占用内存的字节数
    print(f)

    # 下面创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取数据，但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(need extra time)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    for v in f:
        print(v)


if __name__ == '__main__':
    main()


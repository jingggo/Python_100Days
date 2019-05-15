"""
字符串, 列表 和 列表切片
@Author:jyang
@Date:5/14/2019
"""


def main_str():
    str1 = 'hello world!'
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())

    print(str1.find('or'))
    print(str1.find('shit'))

    print(str1.startswith('He'))
    print(str1.startswith('he'))

    print(str1.endswith('!'))

    print(str1.center(50,'*'))

    print(str1.rjust(50, ' '))

    #slice
    str2 = 'abc123456'
    print(str2[2])
    print(str2[2:])
    print(str2[2:5])
    print(str2[2::2])
    print(str2[::2])
    print(str2[::-1])
    print(str2[-3:-1])

    print(str2.isdigit())

    print(str2.isalpha())

    print(str2.isalnum())

    str3='  jjjynag@123.com'
    print(str3)
    print(str3.strip())


def main_list():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2=['hello'] * 5
    print(list2)

    print(len(list1))
    print(list1[0])
    print(list1[4])
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1])
    print(list1[-3])
    list1[2] = 300
    print(list1)                    #[1, 3, 300, 7, 100]

    # 添加元素
    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 2000]
    print(list1)

    # 删除元素
    list1.remove(3)
    del list1[0]

    # 清空列表元素
    list1.clear()
    print(list1)


def main_list_slice():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    for fruit in fruits:
        print(fruit.title(), end=' ') #capitalize()
    print()

    fruits2 = fruits[1:4]
    print(fruits2)

    #fruits3 = fruits #没有复制列表，创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)

    fruits4 = fruits[-3:-1]
    print(fruits4)

    #reversed
    fruits5 = fruits[::-1]
    print(fruits5)

if __name__=='__main__':
    # main_str()
    # main_list()
    main_list_slice()
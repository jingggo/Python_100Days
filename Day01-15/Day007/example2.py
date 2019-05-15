"""
列表排序
@Author:jyang
@Date:5/14/2019
"""


def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)   # sorted函数返回列表排序后的拷贝不会修改传入的列表
    print(list2)

    list3 = sorted(list1, reverse=True)
    print(list3)

    list4 = sorted(list1, key=len)  # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    print(list4)

    list1.sort(reverse=True)    # 给列表对象发出排序消息直接在列表对象上进行排序
    print(list1)

if __name__=='__main__':
    main()
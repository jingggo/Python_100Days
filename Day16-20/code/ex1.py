"""
排序算法 - 选择
@Author:jyang
@Date:5/23/2019
"""

def select_sort(origin_items, comp=lambda x, y: x<y):
    """简单选择排序
    将list由小到大排序, list需为相同type.
    :param origin_items:
    :param comp:
    :return:
    """
    items = origin_items[:]
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1, len(items)):
            if comp(items[j], items[min_index]):
                min_index=j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(origin_items, comp=lambda x, y: x>y):
    """高质量冒泡排序(搅拌排序)
    将list由小到大排序, list需为相同type.
    :param origin_items:
    :param comp:
    :return:
    """
    items = origin_items[:]
    for i in range(len(items)-1):
        swapped = False
        for j in range(i, len(items)-1-i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j] # 大的往后移
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items)-2-i, i, -1):
                if comp(items[j-1], items[j]):
                    items[j], items[j-1] = items[j-1], items[j]
                    swapped = True
        if not swapped:
            break
    return items



test_lst1 = [1, 0, 5, 10]
test_lst2 = ['hello', 'world', 'apple', 'pineapple']
# test_lst2 = [1, 'world', 'apple', 'pineapple']
# print(select_sort(test_lst1))
# print(select_sort(test_lst2))
print(bubble_sort(test_lst1))
print(bubble_sort(test_lst2))
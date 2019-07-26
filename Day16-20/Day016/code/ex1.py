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


def merge_sort(items, comp=lambda x, y: x<=y):
    """归并排序（分治法）"""
    if len(items)<2:
        return items[:]
    mid = len(items)
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并（将两个有序的列表合并成一个有序的列表）
    由小到大排序
    """
    items = []
    index1, index2 = 0, 0
    while index1<len(items1) and index2<len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 2
    items += items1[index1:]
    items += items2[index2:]
    return items


def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items)-1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[min]:
            end = mid - 1
        else:
            return mid
    return -1

s
if __name__ == '__main__':
    test_lst1 = [1, 0, 5, 10]
    test_lst2 = ['hello', 'world', 'apple', 'pineapple']
    # test_lst2 = [1, 'world', 'apple', 'pineapple']
    # print(select_sort(test_lst1))
    # print(select_sort(test_lst2))
    print(bubble_sort(test_lst1))
    print(bubble_sort(test_lst2))
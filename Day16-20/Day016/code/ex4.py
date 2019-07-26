"""
从列表中找出最大的或最小的N个元素
堆结构（大根堆/小跟堆）
@Author:jyang
@Date:5/25/2019
"""

import heapq


list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name':'IBM', 'shares':100, 'prices':91.1},
    {'name':'AAPL', 'shares':50, 'prices':543.33},
    {'name':'FB', 'shares':200, 'prices':21.09},
    {'name':'HPQ', 'shares':35, 'prices':31.75},
    {'name':'YHOO', 'shares':45, 'prices':16.35},
    {'name':'ACME', 'shares':75, 'prices':115.65},
]
print(heapq.nlargest(3, list1)) # 从list1中找出最大的3个Item
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key= lambda x: x['prices']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

"""
迭代工具 - 排列 / 组合 / 笛卡尔积

@Author:jyang
@Date:5/25/2019
"""

import itertools


print(itertools.permutations('ABCD'))
print(itertools.combinations('ABCDE', 3))
print(itertools.product('ABCD','123'))
"""
使用生成式（推导式）语法
说明：生成式（推导式）可以用来生成列表、集合和字典。
@Author:jyang
@Date:5/25/2019
"""

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

#用股票价格大于100元的股票构成一个新的字典
prices2 = [k for k in prices.items() if k[1]>100]
print(type(prices2))
prices3 = {key:value for key, value in prices.items() if value>100 }
print(type(prices3))
prices4 = {k for k in prices.items() if k[1]>100}
print(type(prices4))
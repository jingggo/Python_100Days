"""
输出斐波那契数列的前20个数
在数学上，斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
1 1 2 3 5 8 13 21 ...

@Author:jyang
@Date:5/10/2019
"""

a = 0
b = 1
for _ in range(20):
    (a, b) = (b, a + b)
    print(a, end=' ')

#resursion

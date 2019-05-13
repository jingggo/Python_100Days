"""
求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

@Author:jyang
@Date:5/10/2019
"""
import time


sum = 100
count = 100

start = time.clock()

for x in range(101):
    for y in range(101):
        for z in range(101):
            if x*5 + y*3 + z/3 == sum and x+y+z==count:
                print('公鸡：{}, 母鸡：{}, 小鸡：{}'.format(x, y, z))
                break

end1 = time.clock()
print("执行时间:", (end1 - start), "秒")#执行时间: 0.3541001540757628 秒

for x in range(int(sum/5)):
    for y in range(int(sum/3)):
        z = count-x-y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡：{}, 母鸡：{}, 小鸡：{}'.format(x, y, z))#执行时间: 0.00033477668674319894 秒

end2 = time.clock()
print("执行时间:", (end2 - end1), "秒")

# 通过比较上面两种不同的解决方案的执行时间 意识到优化程序的重要性
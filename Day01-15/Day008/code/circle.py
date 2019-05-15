"""
练习
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

@Author:jyang
@Date:5/15/2019
"""
import math

class SwimmingPool:
    def __init__(self, radius):
        self.r = radius
        self.R = radius+3

        self.price_aisle = 25
        self.price_wall = 32.5

    def aisle_cost(self):
        return math.pi*(self.R**2 - self.r**2) * self.price_aisle

    def wall_cost(self):
        return 2*math.pi*self.R*self.price_wall

if __name__ == '__main__':
    swim = SwimmingPool(int(input('Please input radius of the swimming pool:\n')))
    print('围墙的造价为: ￥%.1f元' % (swim.aisle_cost()))
    print('过道的造价为: ￥%.1f元' % (swim.wall_cost()))


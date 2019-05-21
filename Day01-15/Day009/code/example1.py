"""
奥特曼打小怪兽

@Author:jyang
@Date:5/16/2019
"""
from abc import ABCMeta, abstractclassmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp>=0 else 0

    @property
    def alive(self):
        return self._hp>0

    @abstractclassmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """

        :param name:
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        究极必杀技(打掉对方至少50点或四分之三的血)
        :param other: 被攻击的对象
        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法攻击(群攻)

        :param others: 被攻击的群体
        :return: 使用魔法成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp


class Avenger(Fighter):

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s~~~\n' % self._name + \
               '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    for m in monsters:
        if m.alive:
            return True
    return False

def select_one_alive(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive:
            return monster

def display_info(ultraman, monsters):
    print(ultraman)
    for m in monsters:
        print(m, end='')

def main():
    u = Ultraman('灭霸', 1000, 120)
    m1 = Avenger('Spiderman', 250)
    m2 = Avenger('Ironman', 500)
    m3 = Avenger('StarLord', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========Round%02d========' % fight_round)
        m = select_one_alive(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))

        if m.alive > 0:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1

    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s胜利!' % u.name)
    else:
        print('复仇者联盟胜利!')


if __name__ == '__main__':
    main()
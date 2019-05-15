"""
面向对象版本的猜数字游戏

@Author:jyang
@Date:5/15/2019
"""


from random import randint


class GuessMachine:

    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = '小一点'
        elif your_answer < self._answer:
            self._hint = '大一点'
        else:
            self._hint = '恭喜你猜对了！'
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint


if __name__ == '__main__':
    gm = GuessMachine()
    play_again = True
    while play_again:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input('Please input a number: '))
            game_over = gm.guess(your_answer)
            print(gm.hint)

        if gm.counter > 7:
            print('You are so vegetable~')

        play_again = input('再玩一次?(yer|no)') == 'yes'
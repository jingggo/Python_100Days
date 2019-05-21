"""
下面的例子演示了100个线程向同一个银行账户转账（转入1元钱）的场景，在这个例子中，银行账户就是一个临界资源，在没有保护的情况下我们很有可能会得到错误的结果.
但是有问题的
@Author:jyang
@Date:5/20/2019
"""

from time import sleep
from threading import Thread


class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        """
        计算存款后的余额
        :param money:
        :return:
        """
        new_balance = self._balance + money
        sleep(1)
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 2)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    print('账号余额为：%.2f' % account.balance)


if __name__ == '__main__':
    main()
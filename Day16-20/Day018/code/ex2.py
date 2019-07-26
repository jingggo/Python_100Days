"""
装饰器
@符号是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作

@Author:jyang
@Date:5/28/2019
"""
from enum import Enum, unique
import random
import logging


def use_logging(func):

    def wrapper(*args, **kwargs):
        logging.warning("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper


def bar():
    print('i am bar')


# bar = use_logging(bar)
# bar()
@use_logging
def foo():
    print('i am foo')

foo()
"""

@Author:jyang
@Date:7/22/2019
"""
import pytest


def fnc(x):
    return x + 1


def test_answer():
    return fnc(3) == 5
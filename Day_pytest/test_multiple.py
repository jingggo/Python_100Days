"""

@Author:jyang
@Date:7/23/2019
"""
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


#Execute the test function with 'quite' reporting mode
if __name__ == '__main__':
    pytest.main(['-q', 'test_multiple.py'])
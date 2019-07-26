"""
pytest discovers all tests following its Conventions for Python test discovery,
so it finds both test_ prefixed functions.
There is no need to subclass anything.
We can simply run the module by passing its filename.
@Author:jyang
@Date:7/23/2019
"""
import pytest


class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

if __name__ == '__main__':
    pytest.main(['-q', 'test_class.py'])
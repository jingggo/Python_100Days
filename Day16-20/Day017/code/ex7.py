"""
装饰器函数（使用装饰器和取消装饰器）

@Author:jyang
@Date:5/27/2019
"""
import time
from functools import wraps

# 例子：输出函数执行时间的装饰器。
def record_time(func):
    """自定义装饰函数的装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print('{}:{}秒.'.format(func.__name__, time()-start))
        return result
    return wrapper


# 如果装饰器不希望跟print函数耦合，可以编写带参数的装饰器。
def record(output):
    """"自定义带参数的装饰器"""
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(func.__name__, time()-start)
            return result
        return wrapper
    return decorate
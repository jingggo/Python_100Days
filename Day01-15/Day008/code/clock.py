"""
定义和使用时钟类

@Author:jyang
@Date:5/15/2019
"""
import time
import os

class Clock(object):


    # python中的函数是没有重载的概念的
    # 因为Python中函数的参数没有类型而且支持缺省参数和可变参数
    # 用关键字参数让构造器(__init__)可以传入任意多个参数来实现其他语言中的构造器重载
    def __init__(self, **kw):
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour = kw['hour']
            self._minute = kw['minute']
            self._second = kw['second']
        else:
            #Get current time
            tm = time.localtime(time.time())                # time time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
            # time.struct_time(tm_year=2019, tm_mon=5, tm_mday=15, tm_hour=18, tm_min=19, tm_sec=14, tm_wday=2,
            #                  tm_yday=135, tm_isdst=0)

            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._second = tm.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


if __name__ == '__main__':
    clock = Clock()
    while True:
        # os.system('cls')
        print(clock.show())
        time.sleep(1)
        clock.run()
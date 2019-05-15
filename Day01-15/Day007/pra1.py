"""
在屏幕上显示跑马灯文字
@Author:jyang
@Date:5/15/2019
"""
import os
import time


def main():
    content = 'Life is life, life is an interesting journey of ups and downs...'
    while True:
        # 清理屏幕上的输出
        os.system('cls')        # os.system('clear')
        print(content)
        time.sleep(0.2)         # 200毫秒
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()


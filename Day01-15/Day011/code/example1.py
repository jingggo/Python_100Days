"""

@Author:jyang
@Date:5/17/2019
"""

import time


def main():
    with open('test.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    with open('test.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    with open('test.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
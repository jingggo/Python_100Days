"""

@Author:jyang
@Date:5/18/2019
"""

from math import sqrt


def is_prime(n):
    assert n>0
    flag = True
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            flag = not flag
            return flag
    return flag if n!=1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []

    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for n in range(1, 10000):
            if is_prime(n):
                if n < 100:
                    fs_list[0].write(str(n) + '\n')
                elif n < 1000:
                    fs_list[1].write(str(n) + '\n')
                else:
                    fs_list[2].write(str(n) + '\n')
    except IOError as e:
        print(e)
        print('写文件时发生错误')
    finally:
        for f in fs_list:
            f.close()
    print('Done!')


if __name__ == '__main__':
    main()
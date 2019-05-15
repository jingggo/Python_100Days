"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

@Author:jyang
@Date:5/15/2019
"""
import random


def main(code_len=4):
    # all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_chars = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
    # print(all_chars)

    code = ''
    for _ in range(code_len):
        code += all_chars[random.randint(0, len(all_chars)-1)]
    return code

if __name__ == '__main__':
    print(main())


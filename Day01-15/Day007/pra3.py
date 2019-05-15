"""
设计一个函数返回给定文件名的后缀名。

@Author:jyang
@Date:5/15/2019
"""


def get_suffix(filename, has_dor=False):
    pos = filename.rfind('.')
    if 0<pos<len(filename)-1:
        index = pos if has_dor else pos+1
        return filename[index:]
    else:
        return ''

if __name__ == '__main__':
    filename = '123.xlsx'
    print(get_suffix(filename, True))


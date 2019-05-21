"""
读写二进制文件
@Author:jyang
@Date:5/18/2019
"""

def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))       # <class 'bytes'>
        with open('guido-copy.jpg', 'wb') as fs2:
            fs2.write(data)

    except FileNotFoundError as e:
        print('Cannot open the file')
    except IOError as e:
        print('Error occurred when w/r file')
    print('Done')


if __name__ == '__main__':
    main()
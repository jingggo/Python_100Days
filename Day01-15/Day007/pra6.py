"""
杨辉三角

@Author:jyang
@Date:5/15/2019
"""


def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    # print(yh)
    for row in range(len(yh)):
        yh[row] = [None] * (row+1)
        # print(yh[row])
        for col in range(len(yh[row])):
            if col==0 or col==row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
            print(yh[row][col], end='\t')
        print()

if __name__ == '__main__':
    main()
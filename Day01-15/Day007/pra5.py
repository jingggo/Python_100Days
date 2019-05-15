"""
计算指定的年月日是这一年的第几天
普通闰年:能被4整除但不能被100整除的年份为普通闰年
世纪闰年:能被400整除的为世纪闰年

@Author:jyang
@Date:5/15/2019
"""


def is_leap_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False


def get_days_per_month(year, month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,10):
        return 30
    else:
        if is_leap_year(year):
            return 28
        else:
            return 29


def which_day(year_month_day):
    year = int(year_month_day[:4])
    month = int(year_month_day[4:6])
    day = int(year_month_day[6:])
    is_leap = int(is_leap_year(year))
    total_days =0
    for m in range(month):
        total_days += get_days_per_month(year, m)

    return total_days


if __name__ == '__main__':
    time = input("Please input YYMMDD:\n")
    print(which_day(time))
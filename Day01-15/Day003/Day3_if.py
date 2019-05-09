from random import randint
import math

"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Author: Jing
"""

""" Example
x = float(input('x = '))
if x>1:
    y=3*x-5
elif x>=-1 and x<=1:
    y=x+2
else:
    y=5*x+3

print('f(%.2f) = %.2f' % (x, y))
"""


def incm_transfer():
    value = float(input('请输入长度：'))
    unit = input('请输入单位：')

    if unit=='in' or unit=='英寸':
        print('%f英寸 = %f厘米' % (value, value*2.54))
    elif unit=='cm' or unit=='厘米':
        print('%.2f厘米 = %.2f英寸' % (value, value/2.54))
    else:
        print('请输入有效的单位！')


def random_task_to_do():
    face = randint(1,6)#get a random int among[1-6] a <= N <= b
    if face == 1:
        result = '唱首歌'
    elif face ==2:
        result = '跳个舞'
    elif face ==3:
        result = '学狗叫'
    elif face ==4:
        result = '做俯卧撑'
    elif face ==5:
        result = '念绕口令'
    else:
        result = '讲冷笑话'
    print(result)

def score_to_level():
    score = float(input('请输入成绩：'))
    if score >=90:
        grade = 'A'
    elif score>=80:
        grade = 'B'
    elif score>=70:
        grade = 'C'
    elif score>=60:
        grade = 'D'
    else:
        grade = 'E'
    print('对应的等级是：', grade)

def is_triangle():
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))

    if a+b>c and a+c>b and b+c>a:
        print('周长：%.2f' % (a+b+c) )
        p=(a+b+c)/2
        area=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print('面积：%.2f' % (area))
    else:
        print('不能构成三角形')

def individual_income_tax():
    salary = float(input('本月收入：'))
    insurance = float(input('五险一金：'))
    diff = salary-insurance-3500
    if diff <= 0:
        rate = 0
        deduction=0
    elif diff <1500:
        rate = 0.03
        deduction = 0
    elif diff <4500:
        rate = 0.1
        deduction = 105
    elif diff <9000:
        rate = 0.2
        deduction = 555
    elif diff <35000:
        rate = 0.25
        deduction = 1005
    elif diff <55000:
        rate = 0.3
        deduction = 2755
    elif diff <80000:
        rate = 0.35
        deduction = 5505
    else:
        rate = 0.45
        deduction = 13505
    tax = abs(diff*rate - deduction)
    print('个人所得税：￥%.2f元' % tax )
    print('实际到手收入：￥%.2f元' % (diff+3500-tax))

def verify():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username=='admin' and password=='123456':
        print('身份验证成功！')
    else:
        print('身份验证失败！')


if __name__=="__main__":
    # incm_transfer()
    # random_task_to_do()
    # score_to_level()
    # is_triangle()
    # individual_income_tax()
    # verify()
    pass
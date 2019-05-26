# 练习1：在屏幕上显示跑马灯文字

from random import randint
import os
import time


def marquee():
    content = "我很开心。。。"

    while True:
        os.system("clear")
        print(content)
        time.sleep(.2)
        content = content[1:]+content[0]


# marquee()


# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成


def genrentae_code(l=4):
    all = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    res = ''

    for _ in range(l):
        index = randint(0, len(all)-1)
        res += all[index]

    return res

# print(genrentae_code())
# print(genrentae_code(6))


# 练习3：设计一个函数返回给定文件名的后缀名

def get_suffix(filename):
    pos = filename.rfind(".")

    if pos > 0:
        return filename[pos+1:]

    return ""


# print(get_suffix("a.doc"))
# print(get_suffix("a.tmp.txt"))
# print(get_suffix("abac"))


# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值

def max2(arr):
    l = len(arr)
    m1 = arr[0]
    m2 = arr[1]

    if l < 2:
        return m1, m2 if m1 > m2 else m2, m1

    for i in range(2, l):
        if arr[i] > m1:
            m2 = m1
            m1 = arr[i]
        elif arr[i] > m2:
            m2 = arr[i]

    return m1, m2


# print(max2([1,3,5,7]))


# 练习5：计算指定的年月日是这一年的第几天

def is_leap_year(y):
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


def which_day(y, m, d):
    map = {
        1: 31,
        3: 31,
        5: 31,
        7: 31,
        8: 31,
        10: 31,
        12: 31,
        4: 30,
        6: 30,
        9: 30,
        11: 30,
        2: 29 if is_leap_year(y) else 28,
    }

    day = d
    for i in range(1, m):
        day += map[i]

    return day


# print(which_day(2019, 5, 25))

# 练习6：打印杨辉三角

def pascal_triangle(row):
    if row < 2:
        return print("1")
    # if row<3:
    #     return print("1\n1-1")

    arr = [1]
    brr = arr

    for i in range(1, row+1):
        arr = [1]*i

        for j in range(1, len(arr)-1):
            arr[j] = brr[j-1]+brr[j]

        print('-'.join(str(i) for i in arr))
        brr = arr


pascal_triangle(5)


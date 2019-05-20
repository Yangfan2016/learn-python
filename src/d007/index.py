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
    all='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    res=''

    for _ in range(l):
        index=randint(0,len(all)-1)
        res+=all[index]

    return res

print(genrentae_code())
print(genrentae_code(6))

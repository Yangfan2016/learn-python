# 默认参数


def add(a=0, b=0):
    return a+b


print(add(1, 1))
print(add(2))
print(add())

# 可选参数

def accumulate(*args):
    s = 0

    for i in args:
        s += i
    return s


print(accumulate())
print(accumulate(1))
print(accumulate(1,2))


# 模块

from a import f1,f2

f1()
f2()

from b import f1,f2

f1()
f2()


# 后面的模块覆盖了前面的

from a import f1,f2
from b import f1,f2,f3

f1()
f2()


f3()


# 练习1：实现计算求最大公约数和最小公倍数的函数


def gcd(a,b):
    (a,b)=(b,a) if a>b else (a,b)

    for i in range(a,0,-1):
        if b% i==0 and a %i==0:
            return i


def lcm(a,b):
    return a * b // gcd(a,b)


print(gcd(4,8))
print(lcm(4,8))


# 练习2：实现判断一个数是不是回文数的函数

def is_palindrome(num):
    total=0
    tmp=num

    while tmp>0:
        total=total * 10+tmp % 10
        tmp=tmp//10

    return total==num


print(is_palindrome(121))
print(is_palindrome(123))


# 练习3：实现判断一个数是不是素数的函数

def is_prime(num):
    if num<2:
        return False

    if num==2:
        return True

    for i in range(2,num):
        if num%i==0:
            return False

    return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(9))


# 练习4：写一个程序判断输入的正整数是不是回文素数

num=int(input("请输入一个正整数"))

res=is_prime(num) and is_palindrome(num)

print(res)


# 作用域

b = 1


def foo():
    global b
    b = 2

    a = 2

    def boo():
        # nonlocal a
        # a = 3

        def coo():
            nonlocal a
            a=4

        coo()

    boo()
    print(a) # 3


foo()
# print(b) # 2

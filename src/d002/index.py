import math

# 四则运算

print(2+1)   # 3
print(2-1)   # 1
print(2*1)   # 2
print(2/1)   # 2.0
print(3//2)  # 1
print(3 % 2)   # 1

# 类型转换

print(int(2.6))  # 2
print(float(3))  # 3.0
print(float("3"))  # 3.0

dict = {'runoob': 'runoob.com', 'google': 'google.com'}
print(str(dict))  # {'runoob': 'runoob.com', 'google': 'google.com'}

print(chr(65))  # A
print(ord('A'))  # 65

print(type(3))  # <class 'int'>
print(type(type))  # <class 'type'>

# 运算符

print(2 > 1)  # True
print(2 < 1)  # False
print(2 == 1)  # False
print(2 != 1)  # True

a = 1
a += 1

print(a)  # 2

print(True and False)  # False
print(False or True)  # True
print(1 is 1)  # True
print(1 is not 2)  # True


# 练习

"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""

f = input("请输入华氏度")
f = float(f)
c = (f-32)/1.8

print("摄氏度：%.2f" % c)


"""
输入半径计算圆的周长和面积

l=2*math.pi*r
s=math.pi*r*r

"""

r = input("请输入半径")
r = float(r)
l = 2*math.pi*r
s = math.pi*math.pow(r, 2)

print("周长：%.2f \n 面积：%.2f" % (l, s))


"""
输入年份 如果是闰年输出True 否则输出False
"""

y = input("请输入年分")
y = float(y)
isLeap = (
    y % 4 == 0
    and
    y % 100 != 0
    or
    y % 400 == 0)

print("闰年" if isLeap else "平年")

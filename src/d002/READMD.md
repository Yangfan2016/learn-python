## Day-002

### Notes

- print 输出格式

```py

f=1.234
print("浮点数： %.2f" % f) # 1.23 保留 2 位小数

```

- 三目运算符的替代方案

Python没有三目运算符(?:)，但有类似的替代方案，如下：
```py

# 为真时的结果 if 判定条件 else 为假时的结果
100 if a>b else 60

```

### Practice

1. 将华氏温度转换为摄氏温度

```py
"""
将华氏温度转换为摄氏温度
F = 1.8C + 32
"""

f = input("请输入华氏度")
f = float(f)
c = (f-32)/1.8

print("摄氏度：%.2f" % c)
```

2. 输入半径计算圆的周长和面积
```py

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
```

3. 输入年份 如果是闰年输出True 否则输出False
```py

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
```

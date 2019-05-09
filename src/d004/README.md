## Day-004

### Notes

- range

[文档](https://www.runoob.com/python/python-func-range.html)
```py

range(start,stop,step)

range(10) # [0,9]
range(1,3) # [1,3)
range(0,101,2) # [0,2,4,...100]

```

- print

[文档](https://www.runoob.com/python/python-func-print.html)
```py

print(*objects,end='\n') # 默认以换行符结尾

print("hello",end="---") # hello---

```


### Practice

1. 练习1：输入一个数判断是不是素数
```py
import math

is_prime=True
num=int(input("请输入一个正整数"))

if num<2:
    is_prime=False
elif num==2:
    is_prime=True
else:
    e=int(math.sqrt(num))

    for x in range(2,e+1):
        if num%x==0:
            is_prime=False
        else:
            is_prime=True


print(("是" if is_prime else "不是"+"素数"))
```

2. 练习2：输入两个正整数，计算最大公约数和最小公倍数
```py
[x, y] = input("x=,y=").split(",", 1)

x = int(x)
y = int(y)

num_min = min(x, y)

for i in range(num_min, 0, -1):
    if x % i == 0 and y % i == 0:
        break


print("最小公约数：%d" % (i))
print("最大公倍数：%d" % (x*y/i))

```

3. 练习3：打印三角形图案
```py
"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

"""

row = 5

for i in range(row):
    for j in range(i+1):
        print("*", end='')
    print()


for i in range(row):
    for j in range(row):
        if row-j-1 > i:
            print(" ", end="")
        else:
            print("*", end="")
    print()


for i in range(row):
    for j in range(row):
        if row-j-1 > i:
            print(" ", end="")
        else:
            print("*", end="")
    for j in range(i):
        print("*", end='')
    print()


```

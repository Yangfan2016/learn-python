## Day-003

### Notes

- 分支结构

```py

if a>2:
    # todo
elif a>1:
    # todo
else 
    # todo
```


### Practice

1. 练习1：英制单位与公制单位互换
```py

value = float(input("请输入值"))
unit = input("请输入单位")
res = 0

if unit == "in":
    res = value*2.54
elif unit == "cm":
    res = value/2.54
else:
    pass
print(res)
```

2. 练习2：掷骰子决定做什么
```py
from random import randint

num = randint(1, 6)
res = ""

if num == 1:
    res = "1元"
elif num == 2:
    res = "2元"
elif num == 3:
    res = "3元"
elif num == 4:
    res = "4元"
elif num == 5:
    res = "5元"
elif num == 6:
    res = "6元"
else:
    res="none"

print(res)
```

3. 练习4：输入三条边长如果能构成三角形就计算周长和面积
```py
import math

[a, b, c] = input("请输入边长").split(",", 2)

a = float(a)
b = float(b)
c = float(c)

if a+b > c and a+c > b and b+c > a:
    l = a+b+c
    p = l / 2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("周长：%.2f，面积：%.2f" % (l, s))

else:
    print("不满足三角形的条件")


```

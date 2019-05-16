## Day-006

### Notes


- 作用域

全局作用域  
局部作用域  


函数内部如果要修改全局作用域的变量，需要 `global` 关键字

```py

a=1

def foo():
    global a
    a=2


foo()
print(a) # 2

```


函数内部的嵌套函数如果要修改嵌套作用域，需要关键字 `nonlocal`

```py

def foo():
    b=1

    def bar():
        nonlocal b
        b=2

    bar()
    print(b) # 2    

foo()

```

-  模块


引入模块  

a.py

```py

def foo():
    print("a foo")

```


index.py

```py

from b import foo

foo() # "a foo"

```

防止模块代码自执行

a.py

```py

def foo():
    print("a foo")


# 因为只有直接执行的模块的名字才是“__main__”
if __name__ == "__main__":
    foo()


```


### Practice

1. 练习1：实现计算求最大公约数和最小公倍数的函数

```py
def gcd(a,b):
    (a,b)=(b,a) if a>b else (a,b)

    for i in range(a,0,-1):
        if b% i==0 and a %i==0:
            return i


def lcm(a,b):
    return a * b // gcd(a,b)


print(gcd(4,8))
print(lcm(4,8))
```

2. 练习2：实现判断一个数是不是回文数的函数
```py
def is_palindrome(num):
    total=0
    tmp=num

    while tmp>0:
        total=total * 10+tmp % 10
        tmp=tmp//10

    return total==num


print(is_palindrome(121))
print(is_palindrome(123))
```

3. 练习3：实现判断一个数是不是素数的函数

```py
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
```

4. 练习4：写一个程序判断输入的正整数是不是回文素数

```py 
num=int(input("请输入一个正整数"))

res=is_prime(num) and is_palindrome(num)

print(res)
```

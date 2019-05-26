## Day-007

### Notes


- 字符串切片

```py

content="123456"

print(content[1:])  # 23456  [1,len-1]
print(content[1:3])  # 23 [1,3)
print(content[1::2])  # 246 [1,len-1](+2)
print(content[::3])  # 14 [0,len-1](+3)

```

- str.find(str,pos) 从左往右查找
- str.rfind(str,pos) 从右往左查找

- list

```py

n=10

# 生成指定长度的指定内容的数组
arr=[None]*n

```

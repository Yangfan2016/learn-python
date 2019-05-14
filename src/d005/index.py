'''

水仙花数

水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）

'''

import math


def is_armstrong_num(num):
    g = num % 10
    s = (num-g) // 10 % 10
    b = num // 100

    return math.pow(g, 3)+math.pow(s, 3)+math.pow(b, 3) == num


# res = is_armstrong_num(153)
# print(res)


'''

完全数

它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身
例如：第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。第二个完全数是28，它有约数1、2、4、7、14、28

'''


def is_perfect_num(num):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i

    return s == num


# res=is_perfect_num(6)
# print(res)


# 斐波那契数列

cache = {}


def make_fibonacci(n):
    if n < 3:
        return 1

    if cache.__contains__(n):
        return cache[n]

    cache[n-1] = make_fibonacci(n-1)
    cache[n-2] = make_fibonacci(n-2)

    return cache[n-1] + cache[n-2]


# res = make_fibonacci(6)
# print(res)


'''

百鸡百钱

我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

'''


def hundred_chicken():
    arr = []

    # 5 * x + 3 * y + (100-x-y) / 3== 100
    # 7 * x + 4 * y == 100

    for i in range(0, 26):
        z = (100 - 4 * i)
        if z % 7 == 0:
            x = int(z/7)
            arr.append([x, i, 100-x-i])

    return arr


res = hundred_chicken()

print(res)


'''

Craps赌博游戏

玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束


'''

# todo

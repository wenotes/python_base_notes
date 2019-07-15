#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 23:11
# @Author  : SNCKnight
# @File    : 02_random.py
# @Software: PyCharm
"""
random
"""
import random

# 取随机小数
print(random.random())      # 取0-1之间的小数
print(random.uniform(1, 2))     # 取1-2之间的小数

# 取随机整数
print(random.randint(1, 3))     # [1, 3]  1, 2, 3
print(random.randrange(1, 4))   # [1, 4)  1, 2, 3
print(random.randrange(1, 100, 2))

# 从一个列表中随机取值
lst = ['a', 'b', '(1, 2)', [1, 2, 3]]
print(random.choice(lst))
print(random.sample(lst, 2))


# 打乱一个列表的顺序
lst = ['a', 'b', '(1, 2)', [1, 2, 3]]
random.shuffle(lst)
print(lst)


"""
EXP:随机验证码
"""


def code(n=6):
    s = ""
    for i in range(n):
        num = random.randint(0, 9)
        s += str(num)
    return s


print(code(4))
print(code())


"""
EXP:随机验证码
"""


def code(n=6):
    s = ""
    for i in range(6):
        num = str(random.randint(0, 9))
        alpha_upper = chr(random.randint(65, 90))
        alpha_lower = chr(random.randint(97, 122))
        res = random.choice([num, alpha_upper, alpha_lower])
        s += res
    return s


print(code())

"""
EXP:随机验证码
"""


def code(n=6, alpha=True):
    s = ''
    for i in range(n):
        num = str(random.randint(0, 9))
        if alpha:
            alpha_upper = chr(random.randint(65, 90))
            alpha_lower = chr(random.randint(97, 122))
            num = random.choice([num, alpha_upper, alpha_lower])
        s += num
    return s


print(code(4, False))
print(code(4, 1))
print(code(alpha=False))
print(code(alpha=1))

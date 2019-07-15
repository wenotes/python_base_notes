#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 16:28
# @Author  : SNCKnight
# @File    : 06_built-in_function.py
# @Software: PyCharm
"""常用的内置函数
lambda()    # 匿名函数
sorted()    # 排序函数
filter()    # 过滤函数
map()       # 映射函数
            #  递归函数
            #  二分法
"""

# 普通函数


def func(n):
    return n * n


ret = func(4)
print(ret)

# 匿名函数, 语法: lambda
a = lambda n: n * n
ret = a(4)
print(ret)
print(a.__name__)

ran = lambda x, y: (x, y)
print(ran(56, 66))

"""
EXP:
"""
fn = lambda x, y: max(x, y)
print(fn([1, 2, 3]))

func = lambda *args: max(args)
print(func(22, 1, 24, 2, 4, 3))


"""总结
lambda 匿名函数
    lambda 参数:返回值
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 1:27
# @Author  : SNCKnight
# @File    : 01_generator_expression.py
# @Software: PyCharm
"""生成器表达式

"""

tu = (i for i in range(10))
print(tu)
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())
print(tu.__next__())

"""
EXP:坑
主要是生成器的惰性机制,取过值就没有了,可以理解为将生成器的的内存地址的值,取走换另外的地址存放,
原来的内存地址清空,不在存放值,释放内存
"""


def func():
    print("Hello")
    yield "knight"


g = func()              # 获取生成器
g1 = (i for i in g)     # 生成器
g2 = (i for i in g1)    # 生成器
print(list(g))          # 'Knight'
print(list(g1))         # []
print(list(g2))         # []


"""
EXP:踩坑
"""


def add(a, b):
    """
    # 求和函数
    :param a: 第一个值
    :param b: 第二个值
    :return: 返回两个数的和
    """
    return a + b


def test():
    """
    # 生成器函数
    :return: 返回值0-3
    """
    for r_i in range(4):
        yield r_i


g = test()  # 获取生成器

for n in [2, 10]:
    g = (add(n, i) for i in g)
print(list(g))

"""
EXP:踩坑2,不到最后不拿值
"""


def add(a, b):
    """
    # 求和函数
    :param a: 第一个值
    :param b: 第二个值
    :return: 返回两个数的和
    """
    return a + b


def test():
    """
    # 生成器函数
    :return: 返回值0-3
    """
    for r_i in range(4):
        yield r_i


g = test()  # 获取生成器

for n in [2, 10, 5]:
    g = (add(n, i) for i in g)
print(list(g))


"""
解析过程
不到最后不要向里面放数据
#####
n = 2
g = (add(n, i) for i in g)
n = 10
g = (add(n, i) for i in (add(n, i) for i in g))
n = 5
g = (add(n, i) for i in (add(n, i) for i in (add(n, i) for i in g)))  # 开始计算 n = 5  g = [0, 1, 2, 3]
     [15, 16, 17, 18]   [10, 11, 12, 13]    [5, 6, 7, 8]        [0, 1, 2, 3]
从右往左看     <<<<<<<<<<<<<<<<<=====================
#####
"""


"""总结
生成器表达式 (结果 for循环 条件)
特点:
    1.惰性机制
    2.只能下一步
    3.节省内存
"""
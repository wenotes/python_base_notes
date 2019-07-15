#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 1:10
# @Author  : SNCKnight
# @File    : 02_function_comment.py
# @Software: PyCharm
"""函数注释
EXP:
"""


def add_func(a, b):
    """
    用来计算两个数值的和
    :param a: 第一个数
    :param b: 第二个数
    :return: 返回两个数的和
    """
    return a+b


print(add_func.__doc__)
print(add_func(5, 6))

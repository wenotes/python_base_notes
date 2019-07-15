#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 23:04
# @Author  : SNCKnight
# @File    : 02_built-in_function_iter.py
# @Software: PyCharm
"""迭代器/生成器相关:3
range():
next():
iter():
"""
lst = ["<<老子>>", "<<道德经>>", "<<逍遥叹>>"]
ls = iter(lst)
print(ls.__next__())
print(ls.__next__())
print(ls.__next__())

lst = ["<<老子>>", "<<道德经>>", "<<逍遥叹>>"]
it = iter(lst)      # 内部封装的就是__iter__()
print(it.__next__())
print(next(it))     # 内部封装的是__next__()

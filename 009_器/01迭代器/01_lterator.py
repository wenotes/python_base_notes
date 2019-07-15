#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 1:04
# @Author  : SNCKnight
# @File    : 01_lterator.py
# @Software: PyCharm
"""迭代器
1.dir()     # 内置函数,dir()查看xx类型的数据可以执行那些方法,

"""
print(dir(str))     # __iter__
print(dir(list))    # __iter__
print(dir(int))     # 没有__iter__
print(dir(tuple))   # __iter__
print(dir(dict))    # __iter__
print(dir(set))     # __iter__

"""
2.所有含__iter__()方法的数据,都可以使用for循环,可迭代
"""
str = "Knight"
it = str.__iter__()     # 获取迭代器
print(dir(it))
print(it.__next__())


"""
EXP:
"""

lst = ["Python", "Java", "C##", "PHP"]
for item in lst:
    print(item)

it = lst.__iter__()
while True:
    try:
        el = it.__next__()
        print(el)
    except StopIteration:
        break


"""
Iterable:可迭代对象,内部包含__iter__()函数
Iterator:迭代器,内部包含__iter__()同时包含__next__()
迭代器的特点:
    1.节省内存
    2.惰性机制
    3.不能反复,只能向下执行
"""
lst = ["a", "b", "c", "d"]
it = lst.__iter__()
print("__iter__" in dir(it))
print("__next__" in dir(it))

from collections import Iterable        # 可迭代对象
from collections import Iterator        # 迭代器

print(isinstance(lst, Iterable))
print(isinstance(lst, Iterator))

print(isinstance(it, Iterable))
print(isinstance(it, Iterator))


"""
EXP:list(参数)把参数进行循环迭代
"""
lst = ["Knight", "Queen", "Jack"]
it = lst.__iter__()
lsts = list(it)     # 在list中,一定存在for,一定__next__()
print(lsts)     # ["Knight", "Queen", "Jack"]
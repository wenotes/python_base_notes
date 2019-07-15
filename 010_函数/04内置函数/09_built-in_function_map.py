#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 23:57
# @Author  : SNCKnight
# @File    : 09_built-in_function_map.py
# @Software: PyCharm
"""
map()
映射函数
语法:map(function, iterable) 可以对可迭代对象中的每一个元素进行映射,分别去执行function
"""
# 计算列表中每个数字符的平方

lst = [1, 4, 7, 2, 5, 8]
li = []

# 方式一
for el in lst:
    li.append(el**2)
print(li)


# 方式二
def func(el):
    return el**2


m = map(func, lst)
print(list(m))

# 方式三
s = map(lambda el: el**2, lst)
print(list(s))


"""
EXP:
"""
lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 8, 0]
z = map(lambda x, y: x + y, lst1, lst2)
print(list(z))

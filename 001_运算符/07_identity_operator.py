#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 23:40
# @Author  : SNCKnight
# @File    : 07_identity_operator.py
# @Software: PyCharm
"""身份运算符
is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
"""
# is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。例子用列表比较明白
a = [1, 2, 3]
b = a
print(a, b, a is b, a == b)

b = a[:]
print(a, b, a is b, a == b)

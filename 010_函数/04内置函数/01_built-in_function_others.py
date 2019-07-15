#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 23:09
# @Author  : SNCKnight
# @File    : 01_built-in_function_others.py
# @Software: PyCharm
"""内置函数
"""
"""作用域相关:2
locals():函数会以字典的类型返回当前位置的全部局部变量
globals():函数以字典的类型返回全部全局变量
"""

"""
输入输出:
input():
print():
"""

"""
文件操作相关:
open():
"""

"""
模块相关:
__import__
"""

"""
查看内置属性:
dir()
"""

"""
内存相关:
hash()
id()
"""
lst = (1, 2, 3)
print(id(lst))
print(hash(lst))

"""
调用相关:
callable(),参数是否可以被调用执行
"""
a = 10
print(callable(a))

"""
帮助:
help()
"""
print(help(str))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 1:33
# @Author  : SNCKnight
# @File    : 01_namespace.py
# @Software: PyCharm
# 1.内置, 2.全局, 3.局部(函数调用)
a = 10    # 全局


def fn():   #
    b = 20  # 局部

    def gn():   # 局部
        pass
        print(globals())  # 可以查看全局作用域中的内容
        print(locals())  # 查看当前作用域中的内容
    gn()


fn()


"""
2.global # 全局变量,局部变量
"""
va = 20


def func():
    global va       # 可以把全局中的内容引入到函数内部,2.在全局创建一个变量
    va += 10


func()
print(va)

"""
3.nonlocal    # 寻找外层函数中最近的变量
"""


def outer():
    vb = 10

    def inner():
        nonlocal vb     # 寻找外层函数中最近的变量
        vb += 10
    inner()
    print(vb)


"""总结
命名空间
    1.内置名称空间
    2.全局名称空间
    3.局部名称空间
作用域
    1.全局作用域:内置 + 全局
    2.局部作用域: 局部(函数被调用)
globals()   查看全局中的内容
locals()    查看当前作用域的内容
global和nonlocal关键字
    global: 在局部访问全局中的内容
    nonlocal: 在局部寻找外层函数中声明的最近的变量
"""
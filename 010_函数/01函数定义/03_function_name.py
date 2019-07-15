#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 23:56
# @Author  : SNCKnight
# @File    : 03_function_name.py
# @Software: PyCharm
"""函数名的应用
    函数名的命名规范和变量是一样的
    函数名就是变量名
"""


def func():
    print("我是一个函数")


a = func
print(func)

func()
a()

"""
EXP:1.函数名是一个变量
"""


def func1():
    print("我是函数1")


def func2():
    print("我是函数2")


def func3():
    print("我是函数3")


lst = [func1, func2, func3]
for el in lst:
    el()


"""
3.函数名可以作为一个参数传递给另一个函数
"""


def my():
    print("我是Knight")


def proxy(fn):
    print("start")
    fn()
    print("end")


proxy(my)   # 把函数名作为一个参数传递给另一个函数


"""
4.
"""


def func():
    print("我是func")
    a = 10  # 变量

    def inner():
        print("我是inner")
    return inner


func()()

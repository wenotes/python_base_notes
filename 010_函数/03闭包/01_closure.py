#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 0:25
# @Author  : SNCKnight
# @File    : 01_closure.py
# @Software: PyCharm
"""闭包
1.在内层函数中访问外层函数的变量
闭包的作用
    1.保护变量不受修改
    2.可以让变量常驻内层
"""


def outer():
    a = 10

    def inner():
        print(a)

    inner()


outer()

"""
EXP:1.简易爬虫
"""
from urllib.request import urlopen


def outer():
    """
    # 常驻内存
    """
    url_html = urlopen("http://www.xiaohuar.com/list-1-0.html").read()

    def getcontent():
        return url_html
    return getcontent


ex = outer()
ret = ex()
print(ret)


"""
EXP:2.判断是不是闭包
"""


def outer():
    a = 10

    def inner():
        print(a)
    if inner.__closure__:
        print("这是一个闭包")
    else:
        print("这不是一个闭包")


outer()

def outer():
    a = 10

    def inner():
        print("Hello")
    if inner.__closure__:
        print("这是一个闭包")
    else:
        print("这不是一个闭包")


outer()

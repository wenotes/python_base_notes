#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 22:48
# @Author  : SNCKnight
# @File    : 01_dynamic_parameter.py
# @Software: PyCharm
"""01函数定义
1.位置参数动态传参    # *在这里表示接收位置参数的动态传参,接收的是元组
"""


def brand(*food):
    print(food)


brand("华为", "VIVO", "小米")
brand("IPhone", "OPPO")

"""
2.# 顺序:位置参数=>*arg(arguments) =>默认值参数
"""


def eat_food(name, *food, location="天津"):
    print(name + "吃", food, '在' + location)


eat_food("Knight", "狗不理", "大麻花", "哈根达斯")

"""
3.# 关键字参数动态传参
"""


def drink(**drinks):
    print(drinks)


drink(drink_tea="王老吉", drink_milk="娃哈哈", drink_drunk="五粮液")

"""
顺序
位置参数,*args, 默认值参数, **kwargs
"""


def inf(name, *hobby, location="广州", **info):
    print(name, hobby, location, info)
    print(name + "使用的语言", *hobby, "住在", location, info)


inf("Knight", "python", "java", "QTP", age=26, phone=13078891234)

"""接收所有参数
"""


def func(*args, **kwargs):
    print(args, kwargs)


func(1, 2, 3, a=4, b=5, c=6)

"""
形参的聚合,实参的打散
实参打散:
    list, tuple, set, str 进行迭代打散
"""


def func(*food):    # 聚合,位置参数
    print(food)


lst = ["煎饼果子", "大闸蟹", "探鱼", "海底捞", "北京烤鸭"]
func(*lst)          # 实参,打散


# 实参,dict打散
def func(**kwargs):
    print(kwargs)


dic = {"name": "Knight", "age": 26}
func(**dic)

"""总结
1.实参:
    位置参数
    关键字参数
    混合参数(位置,关键字)
2.形参
    位置参数
    默认值参数
    01函数定义
        *args:位置参数动态传参
        **kwargs:关键字参数动态传参
    顺序:位置参数,*args, 默认值参数, **kwargs
"""
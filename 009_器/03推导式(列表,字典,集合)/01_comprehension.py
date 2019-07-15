#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 23:04
# @Author  : SNCKnight
# @File    : 01_comprehension.py
# @Software: PyCharm

"""列表推导式
推导式:用一句话来生成一个列表
"""

lst = []
for i in range(65, 78):
    lst.append("Chrome" + str(i))
print(lst)

"""
EXP:
"""
lst = ["Chrome" + str(i) for i in range(65, 78)]
print(lst)

"""
列表推导式语法: [结果 for循环 (条件)]
EXP:1.打印100以内能被3整除的数的平方
"""
lst = [i*i for i in range(100) if i % 3 == 0]
print(lst)

"""
EXP:2.寻找名字红带有两个e的人的名字
"""
names = [["Tom", "Billy", "jefferson", "Andrew", "wesley", "steven", "Joe"],
         ["Alice", "Jill", "Ana", "wendy", "Jennifer", "shery", "Evae"]]

lst = [name for line in names for name in line if name.count("e") == 2]
print(lst)


"""
字典推导式
语法: {k: v for循环 (条件)}
EXP:  [11,22,33,44]  ==> {0:11, 1:22, 2:33, 4:44}
"""
lst = [11, 22, 33, 44]
dic = {i: lst[i] for i in range(len(lst))}
print(dic)

"""
EXP:
"""

dic = {'123': "Knight", "456": "Queen", "789": "Jack"}
d = {v: k for k, v in dic.items()}
print(d)

"""
集合推导式
语法:{v for循环 (条件)}
"""
lst = {1, 1, 4, 6, 7, 4, 2, 2, 1}
s = {el for el in lst}
print(s)

"""
EXP:
"""
lst = {1, 1, 4, 6, 7, 4, 2, 2, 1}
s = set(lst)
print(s)



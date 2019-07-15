#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 22:43
# @Author  : SNCKnight
# @File    : A01.py
# @Software: PyCharm

"""
EXP:用户输入成绩,根据成绩的不同打印级别
Tips:if else可以嵌套
"""
score = input("请输入成绩:")
score_int = int(score)
if score_int >= 90:
    print("A")
elif score_int >= 80:
    print("B")
elif score_int >= 70:
    print("C")
else:
    print("D")

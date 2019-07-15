#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 22:42
# @Author  : SNCKnight
# @File    : 02_comparison_operator.py
# @Software: PyCharm
"""比较关系运算符
==	等于 - 比较对象是否相等	(a == b) 返回 False。
!=	不等于 - 比较两个对象是否不相等	(a != b) 返回 True。
>	大于 - 返回x是否大于y	(a > b) 返回 False。
<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	(a < b) 返回 True。
>=	大于等于 - 返回x是否大于等于y。	(a >= b) 返回 False。
<=	小于等于 - 返回x是否小于等于y。	(a <= b) 返回 True。
"""
#
a = 21
b = 10
c = 0

if a == b:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if a != b:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if a < b:
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if a > b:
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if b >= a:
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")

# Tips
print('a' == 'a')
print('a' != 'a')
print('b' > 'a')        # 此时ASCII字符会转换为数字，大小参考ASCII对照表
print('大' > '小')        # 比较的是二进制，一般没有任何场景会运用到
print('小' > '大')

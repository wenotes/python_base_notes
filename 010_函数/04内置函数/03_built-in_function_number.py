#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 23:07
# @Author  : SNCKnight
# @File    : 03_built-in_function_number.py
# @Software: PyCharm
"""数字相关:14
"""

"""
数据类型:4
bool():
int():
float():小数
complex():
"""
print(0.00125e3)    # 小数

"""
进制转换:3
bin():
oct():
hex():
"""
print(bin(2))   # 0b101     # 0b表示二进制
# 注册, 实名认证, 银行卡, 风险评估

print(oct(8))       # 八进制

print(hex(16))      # 十六进制

"""
数字运算:7
abs():  # 绝对值/取模
divmod(): # 计算商和余数
round():    # 四舍五入
pow():      # 求次幂,第三个参数,计算余数
sum():      # 求和
min():  # 取最小数
max():  # 求最大数
"""
print(abs(-8))
print(divmod(10, 2))
print(round(3.49))
print(pow(2, 4, 3))


print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]), 5)

print(min([2, 5, 3, 4, 1]))
print(max([2, 5, 3, 4, 1]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 23:12
# @Author  : SNCKnight
# @File    : 05_序列化模块.py
# @Software: PyCharm
"""序列化模块 #把其他的数据类型转换成 字符串 bytes 序列化的过程
字符串
bytes
"""

dic = {'a': '1'}
lst = [1, 2, 3]
print([str(dic), dic])
print(str(lst), lst)


"""
eval序列化不能使用的场景
    a.用户输入
    b.网络上接收的数据
    c.文件中的内容
"""
str_dic = str([1, 2, 3])
print(str_dic, type(str_dic))
res = eval(str_dic)
print(res, type(res))

"""json
"""

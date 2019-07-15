#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 22:18
# @Author  : SNCKnight
# @File    : 07_built-in_function_sorted.py
# @Software: PyCharm

"""sorted():排序函数
内置函数中提供了一个通用的排序方案
"""
lst = [16, 18, 32, 54, 5]
print(sorted(lst))

lst = ["三国志", "三国演义", "水浒传", "聊斋", "飘"]


def func(s):
    return len(s)


li = sorted(lst, key=func)
print(li)

lis = sorted(lst, key=func, reverse=True)
print(lis)

lst = [
    {'name': "汪峰", "age": 48},
    {'name': "章子怡", "age": 38},
    {'name': "knight", "age": 28}
]

li = sorted(lst, key=lambda el: el['age'])
print(li)

"""
sorted()排序函数
排序函数
    sorted(iterable, key, reverse)
    key:排序规则
    运行流程:把可迭代对象中的每一个元素交给后面的key函数来执行
    得到一个数字(权重),通过这个数字进行排序
"""
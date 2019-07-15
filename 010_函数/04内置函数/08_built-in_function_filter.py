#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 23:16
# @Author  : SNCKnight
# @File    : 08_built-in_function_filter.py
# @Software: PyCharm

lst = ["张无忌", "张铁林", "赵一宁", "史可心", "马大神"]

###########################################################################################################


def func(e1):
    if e1[0] == '张':
        return False    # 不想要的
    else:
        return True     # 想要的


f = filter(func, lst)   # 将lst中的每一项传递给func, 所有返回True, 所有返回True的都会保留, 所有返回False
print("__iter__" in dir(f))
for e in f:
    print(e)

###########################################################################################################

f = filter(lambda el: el[0] != "张", lst)
print("__iter__" in dir(f))
for e in f:
    print(e)


"""
EXP:
"""
st_lst = [
    {'name': "汪峰", "score": 58},
    {'name': "章子怡", "score": 68},
    {'name': "knight", "score": 88}
]

f = filter(lambda el: el['score'] >= 60, st_lst)
print(list(f))

"""
filter() 过滤函数
    filter(function, iterable)
    把可以迭代对象中的数据交给前面的函数进行筛选,函数值返回True或者False
"""
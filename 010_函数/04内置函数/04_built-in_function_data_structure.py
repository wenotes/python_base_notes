#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 23:07
# @Author  : SNCKnight
# @File    : 03_built-in_function_number.py
# @Software: PyCharm
"""数据结构相关
"""

"""列表和元组:4
list(): 将一个可迭代对象转换成列表
tuple(): 将一个可迭代对象转换成元组
reverse() 将一个序列翻转,返回翻转序列的迭代器
slice():列表的切片
"""

# reversed() 反转
lst = ["Knight", "Queen", "jack"]
ls = reversed(lst)
print(list(ls))

# slice()  切片
lst = ["Knight", "Queen", "jack"]
s = slice(1, 3, 2)
print(lst[s])



"""数据集合:3
dict()
set()
frozenset()
"""

s = {1, 2, 3, 4}
s.add(5)
print(hash(s))

str = {"Knight", "Queen", "Jack"}
s = frozenset(str)
print(hash(s))

"""数据结构相关内置函数
len():
sorted():
enumerate():
all():
any():
zip():
fiter():
map():
"""
# enumerate():
lst = ["Knight", "Queen", "Jack"]
for el in lst:
    print(el)

for i in range(len(lst)):
    print(i, lst[i])

for i, el in enumerate(lst):
    print(i, el)

# all()|any()
print(all([True, 1, "False"]))      # and
print(any([True, False, "", 1]))    # or

# zip()
lst1 = ["阿凡达", "初三大四我爱你", "希特勒", "泰囧", "爱宠大机密"]
lst2 = ["美国", "泰国", "德国", "中国"]
lst3 = ["60亿", "5亿", "3亿", "6亿"]
a = zip(lst1, lst2, lst3)       # 水桶效应
print("__iter__" in dir(a))
for el in a:
    print(el)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 22:36
# @Author  : SNCKnight
# @File    : 11_dichotomy_search.py
# @Software: PyCharm
"""二分法查找
EXP:查找lst是否存在
"""

lst = [22, 23, 24, 34, 44, 55, 66, 77, 88, 99, 101, 238, 345, 456, 567, 678, 789]
n = 88
# 方法一
for el in lst:
    if el == n:
        print("lst中存在%s" % n)
        break
else:
    print("lst中不存在%s" % n)

# 方法二
left = 0
right = len(lst)-1
while left <= right:
    mid = (left + right)//2
    if lst[mid] > n:
        right = mid - 1
    if lst[mid] < n:
        left = mid + 1
    if lst[mid] == n:
        print("lst中存在%s" % n)
        break
else:
    print("lst中不存在%s" % n)

"""
二分法复杂度O(n)

while True:
    n = 0
    if 2**n - len(lst)>= 0:
    print(n)        # 计算复杂度
        break
    else:
        n += 1
"""

# 方法三(递归)
lst = [22, 23, 24, 34, 44, 55, 66, 77, 88, 99, 101, 238, 345, 456, 567, 678, 789]


def func(n, left, right):
    if left <= right:
        mid = (left + right)//2
        if n > lst[mid]:
            left = mid + 1
            func(n, left, right)
        if n < lst[mid]:
            right = mid - 1
            func(n, left, right)
        if n == lst[mid]:
            print("lst中存在%s" % n)
            return mid
    else:
        print("lst中不存在%s" % n)
        return -1


index = func(66, 0, len(lst) - 1)
print(index)
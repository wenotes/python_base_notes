#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 0:26
# @Author  : SNCKnight
# @File    : 10_recursive.py
# @Software: PyCharm
"""递归
EXP:遍历 F:\Python全栈\python_base_notes文件夹,打印出所有文件和普通文件的文件名
"""
import os


def func(filepath, n):  # F:\Python全栈\python_base_notes\
    # 1.打开这个文件夹
    files = os.listdir(filepath)    # 查看当前目录中的文件
    # 2.拿到每一个文件名
    for file in files:  # 文件名
        # 3.获取到文件路径
        f_d = os.path.join(filepath, file)  # F:\Python全栈\python_base_notes\文件名
        # 4.判断是否是文件夹
        if os.path.isdir(f_d):
            # 5.如果是文件夹,继续再运行一次func()
            print("\t"*n, file, ":")
            func(f_d, n + 1)
        else:
            # 6.如果不是文件夹,普通文件,打印文件名
            print("\t" * n, file)
    pass


func("F:\Python全栈\python_base_notes", 0)


"""递归
    函数自己调用自己
    最大深度:1000
"""
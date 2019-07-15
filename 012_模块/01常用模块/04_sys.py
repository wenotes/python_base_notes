#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 23:12
# @Author  : SNCKnight
# @File    : 04_sys.py
# @Software: PyCharm
"""sys模块
sys.argv
    # 整个文件路径不能有中文,所有的文件名符合变量命名规范
    # 命令行执行
        >>>python python文件路径 参数1,参数2,参数3....
        sys.argv = ['python文件路径','参数1','参数2','参数3',...]
sys.path
    # 模块搜索路径,是一个列表,这个列表中的值都是文件的绝对路径
    # 一个模块能够被导入,是因为这个模块所在的文件夹在sys.path的列表中
    # 如果一个模块导入不进来,把这个模块的文件夹添加到sys.path中就可以
sys.modules
    # 所有被导入的模块的内存地址都存在sys.modules中
"""
import sys
print(sys.argv)     # sys.argv获取python命令的(参数)值的列表

"""
EXP:
"""
# usr = sys.argv[1]
# pwd = sys.argv[2]
#
# if usr == "Knight" and pwd == "abc1234":
#     print("登录成功!")
# else:
#     print("用户名或者密码错误!")

print(sys.path)
print(sys.modules)
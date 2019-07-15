#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 23:11
# @Author  : SNCKnight
# @File    : 03_os.py
# @Software: PyCharm
"""os模块

"""
import os

os.mkdir('dir1')        # 新建dir1文件夹
os.makedirs('dir2/dir3')    # 新建dir2文件夹,并在dir2文件夹下新建dir3文件夹
os.mkdir('dir1/dir5')   # 存在dir1文件夹,在该目录下新建dir5文件夹

# 只能删除空文件夹
os.rmdir("dir2/dir3")       # 删除dir2文件夹下的dir3文件夹
os.removedirs('dir1/dir5')  # 删除dir1文件夹下的dir5空文件夹和dir1空文件夹
print(os.stat(r'F:\Python全栈\python_base_notes\012_模块\01常用模块\dir2'))
"""
os.listdir()
os.path.join()  
"""
file_lst = os.listdir(r'F:\Python全栈\python_base_notes\012_模块\01常用模块')
for path in file_lst:
    print('\\'.join([r'F:\Python全栈\python_base_notes\012_模块\01常用模块', path]))
    print(os.path.join(r'F:\Python全栈\python_base_notes\012_模块\01常用模块', path))


"""
os.system()     # (执行字符串数据类型的操作系统命令)
os.popen()      # (执行字符串数据类型的操作系统命令,并返回结果)
"""
os.system('dir')    # 执行操作系统的命令,没有返回值

print(os.popen('dir').read())

"""
os.getcwd() # current work dir 当前工作目录
"""
print('-->', os.getcwd())

"""
os.chdir()  # 切换当前工作目录
"""
os.chdir("F:\Python全栈")
print(os.popen('dir').read())


"""
os.path.abspath()
"""
path = os.path.abspath('F:/Python全栈/python_base_notes/012_模块/01常用模块/03_os.py')  # 把路径中的文件路径规范化
print(path)

os.chdir("F:/Python全栈/python_base_notes/012_模块/01常用模块")
path = os.path.abspath('03_os.py')  # 拼接当前工作目录的路径组成绝对路径
print(path)

"""
os.path.split()
    # 把一个路径分成两段,第二段是一个文件/文件夹
"""
path = os.path.split('F:/Python全栈/python_base_notes/012_模块/01常用模块/03_os.py')
print(path)


"""
os.path.dirname()
os.path.basename()
"""
ret1 = os.path.dirname('F:/Python全栈/python_base_notes/012_模块/01常用模块/03_os.py')
print(ret1)
ret2 = os.path.basename('F:/Python全栈/python_base_notes/012_模块/01常用模块/03_os.py')
print(ret2)

"""
os.path.exists()
    # 判断一个文件/文件夹是否存在
"""
print(os.path.exists('F:/Python全栈/python_base_notes/012_模块/01常用模块/dir2'))

"""
os.path.isabs()
    # 判断一个文件是否是绝对路径
"""
res1 = os.path.isabs('F:/Python全栈/python_base_notes/012_模块/01常用模块/03_os.py')
print(res1)
res2 = os.path.isabs('03_os.py')
print(res2)


"""
os.path.isdir()
os.path.isfile()
"""
print(os.path.isdir(r'F:\Python全栈\python_base_notes\012_模块\01常用模块'))
print(os.path.isfile(r'F:\Python全栈\python_base_notes\012_模块\01常用模块\03_os.py'))

"""
os.listdir()
"""
print(os.listdir(r'F:\Python全栈\python_base_notes\012_模块\01常用模块'))
print(os.path.join(r'F:\Python全栈\python_base_notes\012_模块\01常用模块', '03_os.py'))

"""
os.path.getatime()
os.path.getmtime()
"""
print(os.path.getatime(r'F:\Python全栈\python_base_notes\012_模块\01常用模块\03_os.py'))
print(os.path.getmtime(r'F:\Python全栈\python_base_notes\012_模块\01常用模块\03_os.py'))

"""
os.path.getsize()
"""
ret1 = os.path.getsize(r'F:\Python全栈\python_base_notes\012_模块\01常用模块')  # windows操作系统,一个文件大小是4096的倍数
print(ret1)

"""
EXP:统计文件的大小
"""
# 递归


def func(path):
    size_sum = 0
    name_lst =os.listdir(path)
    for name in name_lst:
        path_abs = os.path.join(path, name)
        if os.path.isdir(path_abs):
            size = func(path_abs)
            size_sum += size
        else:
            size_sum += os.path.getsize(path_abs)
    return size_sum


ret = func(r'F:\Python全栈\python_base_notes\012_模块\01常用模块')
print(ret)

# 循环 堆栈思想:先进来的后出去
print("循环")
lst = [r"F:\Python全栈\python_base_notes\012_模块\01常用模块", ]
size_sum = 0
while lst:
    path = lst.pop()
    path_list = os.listdir(path)
    for name in path_list:
        abs_path = os.path.join(path, name)
        if os.path.isdir(abs_path):
            lst.append(abs_path)
        else:
            size_sum += os.path.getsize(abs_path)
print(size_sum)


"""

"""
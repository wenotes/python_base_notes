#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 23:12
# @Author  : SNCKnight
# @File    : 06_time.py
# @Software: PyCharm
"""time
"""
import time

time.sleep(1)

"""
时间格式
# 第一种,格式化时间
    "2019.07.11","2019.7.11" 
# 第二种,时间戳时间
    1562867644.0943308  浮点型数据
    1997.1.1 0:0:0 开始计数
# 第三种,结构化时间
    time.struct_time(tm_year=2019, tm_mon=7, tm_mday=13, tm_hour=12, tm_min=45, tm_sec=0, tm_wday=5, tm_yday=194, tm_isdst=0)
    

"""
print(time.time())          # 时间戳时间
print(time.strftime("%Y-%m-%d %H:%M:%S"))       # 字符串格式化时间
print(time.localtime())
print(time.strftime("%c"))
st_time = time.localtime()
print(st_time)
print(st_time.tm_year)

"""
EXP:1.时间戳时间转换字符串时间
"""
st_time = time.localtime(1562993583.844901)
ret = time.strftime("%Y-%m-%d %H:%M:%S", st_time)
print(ret)


"""
EXP:2.字符串时间转换时间戳时间
"""
st_time = time.strptime('2019-07-13 12:53:03', "%Y-%m-%d %H:%M:%S")
res = time.mktime(st_time)
print(res)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 23:14
# @Author  : SNCKnight
# @File    : 01_re.py
# @Software: PyCharm
"""
模块
    一组功能的集合
模块的类型
    1.内置模块:不需要安装,解析器自带的
    2.第三方模块:需要安装的模块
    3.自定义模块:自己写得模块
"""
"""re模块

"""
import re

"""查找
findall() 
    匹配所有 每一项都是列表中的一个元素
search()
    只能匹配从左到右的第一个,得到一个匹配对象,通过group方法获取匹配值
match()
    从头开始匹配
"""
# findall()
ret = re.findall("\d+", "abcd1234efgh456")
print(ret)

# search()
ret = re.search("\d+", "abcd1234efgh456")
print(ret)

"""
split()
"""
st = 'knight12Queen34Jack56'
print(re.split('\d+', st))


"""
sub()
"""
st = 'knight12Queen34Jack56'
print(re.sub('\d+', "X", st))
print(re.sub('\d+', "X", st, 1))

"""
subn()
    返回一个元组,第二个元素是替换的次数
"""
st = 'knight12Queen34Jack56'
print(re.subn('\d+', "X", st))

"""
compile()
"""
st = 'knight12Queen34Jack56'
ret = re.compile('\d+')
print(ret.findall(st))
print(ret.search(st).group())

"""
finditer()
"""
ret = re.finditer("\d+", 'knight12Queen34Jack56')
for i in ret:
    print(i.group())


"""
EXP
"""
import re
htl = "<a>Knight</a>"
ret = re.search("<(\w+)>(\w+)</(\w+)>", htl)
print(ret)
print(ret.group())
print(ret.group(0))
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))


"""
EXP:
"""
import re
htl = "<a>Knight</a>"
ret = re.findall("(\w+)", htl)
print(ret)
ret = re.findall(">(\w+)<", htl)    # 优先取分组的内容
print(ret)


"""
EXP:取消分组优先(?:正则表达式)
"""
import re
s = '1.234*4.567'
ret = re.findall('\d+\.\d+', s)
print(ret)
ret = re.findall('\d+(\.\d+)?', s)      # 分组优先
print(ret)
ret = re.findall('\d+(?:\.\d+)?', s)    # 取消分组优先
print(ret)


"""
分组命名
    (?P<组名>正则表达式)
"""
import re
htl = "<a>Knight</a>"
ret = re.search(">(?P<con>\w+)<", htl)
print(ret.group(1))
print(ret.group('con'))


"""
EXP:
"""
htl = "<a>Knight</a>"
pattern = "<(?P<tab>\w+)>(\w+)</(?P=tab)>"
ret = re.search(pattern, htl)
print(ret)
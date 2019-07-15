#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 23:02
# @Author  : SNCKnight
# @File    : 05_logical_operators.py
# @Software: PyCharm
"""逻辑运算符
and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
"""
# EXP:逻辑运算
s_list = [
	'True and True',
	'True and False',
	'False and False',
	'True or True',
	'True or False',
	'False or False',
	'not True',
	'not False'
]
string = ''
for s in s_list:
	a = eval(s)		# eval()直接运行字符串代码返回结果
	string += (s+'\t'+'==>'+str(a)+'\n')
print(string.expandtabs(20))

# EXP1：函数入参时，参数为空时会用到


def test1(arg):
	if not arg:
		arg = 'default value'
	return arg


a = test1('')
print(a)


def test2(arg='default value'):
	return arg


print(test2())

# 场景二：用于赋值时


def test2(arg):
	arg = arg or '如果arg为false，则用我'
	return arg


print(test2(''),test2('我是true'),sep='---||---')

# and or  下面返回的结果其实这是因为and 和or的运算规则导致的，和是不是什么数据类型没有关系
# 不是很好一句话总结，先这样
a, b = 'a', ['b']		# 真真  and 返回第二个真，or 返回第一个真
c, d = 1, []  			# 真假  and 返回第二个假，or 返回第一个真
e, f = 0, 2 			# 假真  and 返回第一个假，or 返回第二个真
g, h = (), {}			# 假假  and 返回第一个假，or 返回第二个假
print(a and b, a or b)
print(c and d, c or d)
print(e and f, e or f)
print(g and h, g or h)

print(not c, not d)		# not 返回bool值

print("----下面更晕，遇到写这个的直接打死----")
print(not 0 and 1 or 2 and 3 and 4 or 5)
print(1 == 1 and 1 == 2 or 2 == 2 and 2 ==3)
# 总结：True遇到 and 都得进入下一个，遇到or结束判断；False遇到and结束判断，遇到or继续下一个
# 一般不这么写，尽量用括号来控制优先级

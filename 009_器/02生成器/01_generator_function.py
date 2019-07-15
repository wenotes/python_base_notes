#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 0:00
# @Author  : SNCKnight
# @File    : 01_generator_function.py
# @Software: PyCharm

"""生成器函数
1.yield
"""


def func():
    yield 1


print(func())


"""
函数中如果有yield,这个函数就是生成器函数,生成器函数()获取的是生成器的值,这个时候不执行函数
yield:相当于return,可以返回数据,但是yield不会彻底中断函数,分段执行函数
"""


def func():
    print("start")
    yield 1
    print("end")


gen = func()    # 不会执行func函数,拿到的是生成器
ret = gen.__next__()    # 会执行到下一个yield
print(ret)
gen.__next__()


###
def order():
    for i in range(1000):
        yield str(i) +"$"


g = order()     # 获取生成器
print(g.__next__())
print(g.__next__())

"""
2.send() 和__next__()是一样的,可以执行到下一个yield,可以给上一个yield位置传值
"""


def func():
    print("Knight")
    a = yield 123
    print(a)
    print("Queen")
    b = yield 456
    print(b)
    print("jack")
    c = yield 789
    print(c)
    print("Nike")
    yield 9527


gen = func()
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

"""
EXP:1.
"""


def func():
    print("Knight")
    a = yield 123
    print(a)
    print("Queen")
    b = yield 456
    print(b)
    print("jack")
    c = yield 789
    print(c)
    print("Nike")
    yield 9527


gen = func()
print(gen.__next__())       # 没有上一个yield,所以不能用send()
print(gen.send("Python"))
print(gen.send("java"))
print(gen.send("PHP"))

"""
EXP:2.
"""


def eat():
    print("我想吃什么?")
    a = yield "馒头"
    print("a =", a)
    b = yield "狗不理"
    print("b =", b)
    c = yield "海底捞"
    print("c =", c)
    yield "Game Over"


gen = eat()
ret1 = gen.__next__()
print(ret1)
ret2 = gen.send("哈根达斯")
print(ret2)
ret3 = gen.send("棒棒冰")
print(ret3)
ret4 = gen.send("冰袋")
print(ret4)


"""总结
1.生成器
    a.本质就是迭代器
    b.生成器的特点和迭代器一样,
        取值方式和迭代器一样(__next__(), 
        send():给上一个yield传值
    c.生成器一般由生成器函数或者生成器表达式创建(手写的迭代器)
2.send()和__next__()区别:
    a.send()和__next__都是让生成器执行下一次
    b.send()可以给上一个yield的位置传递值,不能给最后一个yield传值
    c.在第一次执行生成器的时候不能使用send()
3.生成器函数
    a.和普通函数没有区别,里面有yield的函数就是生成器函数
    b.生成器函数在执行的时候,默认不会执行函数体,返回生成器
"""

"""
Tips
for和list()内部一定有__next__()
"""


def func():
    yield 1
    yield 2
    yield 3


for i in func():
    print(i)
print(list(func()))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/7 15:39
# @Author  : SNCKnight
# @File    : 05_built-in_function_str.py
# @Software: PyCharm
"""字符串: 9
str():
format():
bytes():
bytearry():
memoryview(): # 查看bytes在内存中的使用情况
ord():        # 输入字符找带字符编码的位置
chr():        # 输入位置数字找出对应的字符
ascii():      # 是ascii码中的返回值该值,不是就返回"\u..."
repr():        # 返回一个对象的规范输出形式
"""
str = "hello world"
print(memoryview(str.encode('utf-8')))

print(ord('a'))
print(ord('A'))
print(ord('中'))

print(ascii("a"))
print(ascii("中"))

# repr
print('鲁迅说:"不在沉默中爆发,就在沉默中死亡"')
print("鲁迅说:\"不在沉默中爆发,就在沉默中死亡\"")
print(repr("鲁迅说:\"不在沉默中爆发,就在沉默中死亡\""))      # "\" 转义, 不能作为字符串开头或结尾,
print(repr("鲁迅说:\t不在沉默中爆发,就在沉默中死亡\t"))      # 原样输出字符串
print("哈哈\\呵呵")         # \\ 表示是一个 \ , \ 转义, \n 换行. \t 制表符. \". \'

"""
字符串类型代码执行(3):
eval():
exec():
compile():
"""
# eval()
s = "5 + 6"
ret = eval(s)
print(ret)

dic = '{"name": "Knight", "age": "26", "jab": {"test": "python", "tools": "airtest", "salary": "20k"}}'
d = eval(dic)
print(d["name"])

# exec()
s = "a = 10"
exec(s)
print(a)

centent = input("请输入你的代码:a = 10")
exec(centent)
print(a)

# compile()
"""
compile(): # 将字符串类型的代码编译,代码对象能够通过exec()语句来执行或者eval()进行求值
    参数说明:
        1.resource,要执行的代码,动态代码片段
        2.文件名,代码存放的文件名,当传入了第一个参数的时候,这个参数给空就行
        3.模式,取值有3个
            1.exec:一般放流程语句的时候
            2.eval: resource只存放一个求值表达式
            3.single:resource存放的代码有交互的时候,mode值为single
"""
code1 = "for i in range(5): print(i)"
c1 = compile(code1, "", mode="exec")
exec(c1)

code2 = "1+2+3"
c2 = compile(code2, "", mode="eval")
a = eval(c2)
print(a)

code3 = "content = input('请输入你的名字:')"
c3 = compile(code3, "", mode="single")
exec(c3)
print(content)

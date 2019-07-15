#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 12:17
# @Author  : SNCKnight
# @File    : 08_pickle.py
# @Software: PyCharm
"""pickle
# 支持在python中几乎所有的数据类型
# dumps 序列化的结果只能是字节
# 只能在 python中使用
# 在和文件操作的时候,需要使用rb,wb的模式打开文件
# 可以多次dump和load
"""
import pickle
dic = {(1, 2, 3): {'a', 'b'}, 1: 'abc'}
ret = pickle.dumps(dic)
print(ret)
print(pickle.loads(ret))

"""
"""
import pickle
dic = {(1, 2, 3): {'a', 'b'}, 1: 'abc'}
with open('pickle_file', 'wb') as f:
    pickle.dump(dic, f)
f.close()

with open('pickle_file', 'rb') as f:
    ret = pickle.load(f)
    print(ret, type(ret))
f.close()


dic = {(1, 2, 3): {'a', 'b'}, 1: 'abc'}
with open('pickle_file_loop', 'wb') as f:
    for i in range(3):
        pickle.dump(dic, f)
f.close()

with open('pickle_file_loop', 'rb') as f:
    while True:
        try:
            ret = pickle.load(f)
            print(ret, type(ret))
        except EOFError:
            break
f.close()
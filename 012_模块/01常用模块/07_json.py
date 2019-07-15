#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 12:07
# @Author  : SNCKnight
# @File    : 07_json.py
# @Software: PyCharm

"""json
Tips
能处理的数据类型:字符串,列表,字典,数字
字典中的key只能是字符串
dumps  loads
    在内存中做数据转换
        dumps 数据类型转换成 字符串 序列化
        jsons 字符串 转换成数据类型 反序列化
"""
import json             # 序列化
dic = {'name': 'Knight', 'age': '26', 'home': '广州'}
ret = json.dumps(dic)
print(dic, type(dic))
print(ret, type(ret))

res = json.loads(ret)   # 反序列化
print(res, type(res))


dic = {'name': 'Knight', 'age': '26', 'home': '广州'}
ret = json.dumps(dic, ensure_ascii=False)
with open("dic_json.text", mode='w') as f:
    f.write(ret)        # 写入的时候,中文会乱码
f.close()


# 从文件总读取字典
with open('dic_json.text', mode='r') as f:
    str_dic = f.read()
f.close()
print(str_dic)


"""
dump load
    直接将数据类型写入文件,直接从文件中读取数据类型
        dump 数据类型 写入文件  序列化
        load 文件读出 数据类型 反序列化
"""
import json
dic = {"key1": "value1", "key2": "广州"}
with open('dic_json_2.text', 'a') as f:
    json.dump(dic, f, ensure_ascii=False)

with open('dic_json_2.text', 'r') as f:
    dic_lst = json.load(f)
print(dic_lst)


"""
EXP:把一个一个字典放到文件中,再一个一个取出来
"""
dic = {"key1": "value1", "key2": "value2"}
with open('json_file', 'a') as f:
    for i in range(3):
        str_dic = json.dumps(dic)
        f.write(str_dic + '\n')
f.close()

with open('json_file', 'r') as f:
    for line in f:
        dics = json.loads(line.strip())
        print(dics.keys())
f.close()


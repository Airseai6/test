#! python3
# -*- coding:utf-8 -*-

dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

print("字典值 : %s" % dict.items())
print(type(dict.items()))

# 遍历字典列表
for key, values in dict.items():
    print(key, values)

# a = 255
# # print(id(a))
# # a += 1
# # print(id(a))
# #
# # a = 888
# # print(id(a))
# # a += 1
# # print(id(a))
# # b = 889
# # print(id(b))

# import re
#
# tel = 'Tony: 15312345678; Alien: 13512345678.'
# # req = '"keys":([0-9]{11}?),"data"'
# req = r"\d*"
# result = re.findall(req, tel)
#
# print(result)
#
# # key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
# # p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
# # pattern1 = re.compile(p1)#我们在编译这段正则表达式
# # matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
# # print(matcher1.group(0)) #打印出来
#
# key = r"<html><body><h1>hello world<h1></body></html>" #源文本
# p1 = r"<h1>.+<h1>"#我们写的正则表达式，下面会将为什么
# pattern1 = re.compile(p1)
# print(pattern1.findall(key)) #发没发现，我怎么写成findall了？咋变了呢？

# import math
# print(math.sin(90/180*math.pi))
# print(math.asin(1))

# print('' is not None)

# from datetime import datetime
# print(datetime.now())

# from math import *
# a = asin(900/1575)
# a = a/pi*180
#
# delta_h = 212
# Dm = 20
# r = 140
# b = atan(delta_h/r)
# # b = b/pi*180
# delta_r = Dm*(1.009/b - 0.063 + 0.4803*b)
# delta_z = Dm*(2.17 - 0.6589*b + 1.247*b*b)
# theta = 2*asin(0.5*delta_z/r)
# theta = theta/pi*180
#
# print('high_angle:', b)
# print('delta_R:', delta_r)
# print('delta_Z:', delta_z)
# print('next_location:', (r, u"%.3f°"%theta))


import requests

response = requests.get('https://www.baidu.com')
# print(response.text)
print(response.content.decode('utf-8'))
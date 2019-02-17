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

import re

tel = 'Tony: 15312345678; Alien: 13512345678.'
# req = '"keys":([0-9]{11}?),"data"'
req = r"\d*"
result = re.findall(req, tel)

print(result)

# key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
# p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
# pattern1 = re.compile(p1)#我们在编译这段正则表达式
# matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
# print(matcher1.group(0)) #打印出来

key = r"<html><body><h1>hello world<h1></body></html>" #源文本
p1 = r"<h1>.+<h1>"#我们写的正则表达式，下面会将为什么
pattern1 = re.compile(p1)
print(pattern1.findall(key)) #发没发现，我怎么写成findall了？咋变了呢？
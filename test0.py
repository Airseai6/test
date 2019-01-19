# -*- coding:utf-8 -*-
# from decimal import *
# g = Decimal('15.6')
# print(g)
# g = lambda x, y=3, z=5:x*y*z
# print(g(1))
import time

# def counter_timer():
#     m = 0
#     l = []
#     for i in range(1,10):
#         m = i;
#         l.append(m)
#         return l
# #@counter_timer
# def test(i,m):
#     print("in")
#
# tmp=counter_timer([2])
# tmp()
#test(1,2)
#
# d = [1,]
# print(id(d))
# d.append(2)
# print(id(d))
#
# m=1
# print(id(m))
# m+=1
#
# tmp = m +1
# m = tmp
# print(id(m))

class base1:
    def __init__(self):
        pass
    def getname(self):
        print("base1")

class base2:
    def __init__(self):
        pass
    def getname(self):
        print("base2")

class devi(base2):
    def __init__(self):
        super(devi,self).__init__
        pass

if __name__ == "__main__":
    test = devi()
    test.getname()
    print(test.)
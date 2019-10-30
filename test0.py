# # a = 255
# # # print(id(a))
# # # a += 1
# # # print(id(a))
# # #
# # # a = 888
# # # print(id(a))
# # # a += 1
# # # print(id(a))
# # # b = 889
# # # print(id(b))
#
# # print(result)
# # print(pool)
# # str_0 = "alksjdf  alsdkf"
# # print(str_0.split('132'))
#
# # # key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
# # # p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
# # # pattern1 = re.compile(p1)#我们在编译这段正则表达式
# # # matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
# # # print(matcher1.group(0)) #打印出来
# #
# # key = r"<html><body><h1>hello world<h1></body></html>" #源文本
# # p1 = r"<h1>.+<h1>"#我们写的正则表达式，下面会将为什么
# # pattern1 = re.compile(p1)
# # print(pattern1.findall(key)) #发没发现，我怎么写成findall了？咋变了呢？
#
# # import math
# # print(math.sin(90/180*math.pi))
# # print(math.asin(1))
#
# # print('' is not None)
#
# # from datetime import datetime
# # print(datetime.now())
#
# # from math import *
# # a = asin(900/1575)
# # a = a/pi*180
# #
# # delta_h = 212
# # Dm = 20
# # r = 140
# # b = atan(delta_h/r)
# # # b = b/pi*180
# # delta_r = Dm*(1.009/b - 0.063 + 0.4803*b)
# # delta_z = Dm*(2.17 - 0.6589*b + 1.247*b*b)
# # theta = 2*asin(0.5*delta_z/r)
# # theta = theta/pi*180
# #
# # print('high_angle:', b)
# # print('delta_R:', delta_r)
# # print('delta_Z:', delta_z)
# # print('next_location:', (r, u"%.3f°"%theta))
#
# # import requests
# #
# # response = requests.get('https://www.baidu.com')
# # # print(response.text)
# # print(response.content.decode('utf-8'))
#
# # import re
# #
# # tel = 'Tony: 1.5sadgs31234578.; Alien: 13512345678.sfg'
# # # req = '"keys":([0-9]{11}?),"data"'
# # req = r"(\d+\.)\D"
# # result = re.findall(req, tel)
# # print(result)
#
#
# # def find_num(test):
# #     items = list(set(test))
# #     for item in items:
# #         if test.count(item) > len(test)/2.0:
# #             return item
# #     return None
# #
# #
# # if __name__ == '__main__':
# #     test = [1, 1, 2, 2, 2]
# #     print(find_num(test))
#
# # if 'asohf':
# #     print('str')
# #
# # if not None:
# #     print('none')
#
# # import logging
# # logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# # logger = logging.getLogger(__name__)
# #
# # logger.info("Start print log")
# # logger.debug("Do something")
# # logger.warning("Something maybe fail.")
# # logger.info("Finish")
#
#
# # from keras import layers
# # layer = layers.Dense(32, input_shape=(784,))
#
# # from keras import models
# # from keras import layers
# #
# # model = models.Sequential()
# # model.add(layers.Dense(32, input_shape=(784, )))
# # model.add(layers.Dense(32))
#
# # import numpy as np
# #
# # x = np.array(12)
# # print(type(x))
#
# # from keras.datasets import mnist
# #
# # (train_image, train_labels), (test_image, test_labels) = mnist.load_data()
# # digit = train_image[4]
# #
# # import matplotlib.pyplot as plt
# #
# # plt.imshow(digit, camp=plt.cm.binary)
# # plt.show()
#
# from keras import models
# from keras import layers
#
# model = models.Sequential()
# model.add(layers.Dense(32, input_shape=(784, )))
# model.add(layers.Dense(32))

# from pyecharts import Line

# def printLine(columns, data1, data2):
#     line = Line("zhexiantu", "test")
#     line.add("x", columns, data1, is_label_show=True)
#     line.add('y', columns, data2, is_label_show=True)
#     line.render()
#
# def genRandom():
#     columns = []
#     data1 = []
#     data2 = []
#     for i in range(10):
#         columns.append('month:'+str(i))
#         data1.append(i)
#         data1.append(i*10+1)
#
#     return columns, data1, data2
# if __name__ == '__main__':
#     columns, data1, data2 = genRandom()
#     printLine(columns, data1, data2)

# from random import choice
# import matplotlib.pyplot as plt
#
# class RandomWalk():
#     '''一个生成随机漫步数据的类'''
#     def __init__(self,num_points=5000):
#         '''初始化随机漫步的属性'''
#         self.num_points = num_points
#
#         # 所有的随机漫步都始于(0,0)
#         self.x_values = [0]
#         self.y_values = [0]
#     def fill_walk(self):
#         '''计算随机漫步的所有点'''
#
#         # 不断漫步，直到列表到达指定长度
#         while len(self.x_values)<self.num_points:
#             # 决定前进方向以及沿这个方向前进的距离
#             x_direction = choice([1,-1])
#             x_distance = choice([0,1,2,3,4])
#             x_step = x_direction*x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#
#             # 拒绝原地踏步
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             # 计算下一个点的x和y值
#             next_x = self.x_values[-1]+x_step
#             next_y = self.y_values[-1] + y_step
#
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)
#
# if __name__ == '__main__':
#     # 创建一个RandomWalk实例，并将其包含的点都绘制出来
#     rw = RandomWalk()
#     rw.fill_walk()
#     print(rw.x_values)
#     plt.scatter(rw.x_values, rw.y_values, s=15)
#     plt.show()

'''
动态折线图演示示例
'''

# import numpy as np
# import matplotlib.pyplot as plt
# import random
#
#
# def genrandom():
#     ID = {"1": "Deny", "2": "Jame"}
#     id = random.choice(list(ID.keys()))
#     x = random.randint(0, 100)
#     y = random.randint(0, 100)
#     return [id, x, y]
#
#
# def draw():
#     plt.ion()
#     plt.figure("轨迹")
#     plt.xlim((0, 100))
#     plt.ylim((0, 100))
#     x_1 = []
#     y_1 = []
#     x_2 = []
#     y_2 = []
#     while True:
#         # if len(x_1) > 50:
#         #     plt.clf()
#         #     x_1.pop(0)
#         #     y_1.pop(0)
#         # if len(x_2) > 50:
#         #     plt.clf()
#         #     x_2.pop(0)
#         #     y_2.pop(0)
#
#         series = genrandom()
#         if series[0] == "1":
#             x_1.append(series[1])
#             y_1.append(series[2])
#             plt.plot(x_1, y_1, c='r', ls='-', marker='o', mec='b', mfc='w', label='1')
#             plt.pause(0.1)
#         elif series[0] == "2":
#             x_2.append(series[1])
#             y_2.append(series[2])
#             plt.plot(x_2, y_2, c='g', ls='--', marker='x', mec='b', mfc='w', label='2')
#             plt.pause(0.1)
#
#
# if __name__ == '__main__':
#     draw()

import MySQLdb

conn = MySQLdb.connect("localhost", "root", "", "test")
cur = conn.cursor()


def is_existed_table(table_name):
    sql = "show tables from test"
    cur.execute(sql)
    result = cur.fetchall()
    if table_name in str(result):
        return True
    else:
        return False


def creat_tables(table_name):
    sql = "create table %s (nid int,username varchar(20), password varchar(64))" %(table_name)
    cur.execute(sql)
    conn.commit()
    conn.close()


def insert(username, password):
    sql = "insert into user (username,password) values ('%s','%s')" %(username,password)
    cur.execute(sql)
    conn.commit()
    conn.close()


def is_existed(username, password):
    sql = "select * from user where username ='%s' and password ='%s'" %(username, password)
    cur.execute(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True


if __name__ == '__main__':
    tables = 'user'
    if not is_existed_table(tables):
        creat_tables(tables)
    insert('xiaoA', '123')

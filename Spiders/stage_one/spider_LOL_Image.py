#! python
# -*- coding:utf-8 -*-
"""
爬取LOL官网全英雄皮肤
1、官网找到皮肤图片地址"http://ossweb-img.qq.com/images/lol/web201310/skin/big81001.jpg"
2、总结规律，不同英雄不同皮肤只有后面"81001"不同，"81"为英雄ID,"001"为皮肤Index
3、找到储存英雄ID,name等的JS文件，JS有很多 champion.js是测试出来的没啥好方法
4、将所需内容解析、转码成可循环的字典形式
5、生成url列表，生成下载文件名称，下载
"""
import requests
import re
import json
import time
import random


def getLOLImages():
    # 可以加请求头,模拟浏览器去请求(知识点*header怎么写？)
    # header = {'User-Agent':''}
    # 1.获取JS源码
    url_js = 'http://lol.qq.com/biz/hero/champion.js'
    # 获取JS源码内容 （知识点*requests.get学习：requests.get(url_js)得到是'Response [200]'表示JS页面可访问）
    # .txt获取str型 .content获取bytes字节型   → 来获取JS内容
    res_js = requests.get(url_js).content
    # 转码 bytes → str
    html_js = res_js.decode()
    # 正则表达式！！通配符(.*?)匹配的是一个{"ID":"name",...}字典
    req = '"keys":(.*?),"data"'
    # 匹配内容中的ID list_js为一个只有一个元素的列表，list_js[0]为一个全内容的str
    list_js = re.findall(req,html_js)
    # str → dict_js	(知识点*json.loads的运用！)
    dict_js = json.loads(list_js[0])

    # 2.拼接URL地址、获取下载图片的地址"http://ossweb-img.qq.com/images/lol/web201310/skin/big81001.jpg"
    # 定义图片列表
    pic_list = []
    for key in dict_js:
        # key 英雄ID  i 假设最多有20个皮肤，后面有404判断
        for i in range(20):
            num = str(i)
            if len(num) == 1:
                skin_num = "00"+num
            elif len(num) == 2:
                skin_num = "0"+num
            numstr = key+skin_num
            url = "http://ossweb-img.qq.com/images/lol/web201310/skin/big"+numstr+".jpg"
            # print(url)
            pic_list.append(url)
            # 图片名称空列表
            list_filepath = []
            path = "E:\\MyDocuments\\Spider_Download\\LOL\\"
            # print(dict_js.values()) 英雄名称 Aatrox1
            for name in dict_js.values():
                for i in range(20):
                    file_path = path + name + str(i) + '.jpg'
                    # print(file_path) 生成下载图片完整类型列表
                    list_filepath.append(file_path)                    
    # 3.下载图片
    n = 0               
    for picurl in pic_list:
        res = requests.get(picurl)
        n+=1 # n自加位置放后面为什么不行？
        # 获取状态码 200有内容，404空页面
        if res.status_code ==200:
            print("Loading %s"%list_filepath[n])
            # 0-1s 延迟
            # time.sleep(random.random())
            # 'wb':保存模式(知识点*文件写入)
            with open(list_filepath[n],'wb') as f:
                f.write(res.content)


if __name__ == '__main__':
    getLOLImages()
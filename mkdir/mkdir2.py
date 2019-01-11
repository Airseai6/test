#! python
# -*- coding:utf-8 -*-
import os


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


def write_dir(path, f_name, dir_num, f_num):
    """写一个文件夹下多个类似名称的文件"""
    ele = { 0:"逐年降水量", 1:"逐年平均气温", 2:"逐年平均风速", 3:"逐年径流量"}
    dis = {
        0: "",
        1: "",
        2: "",
        3: "状头",
        4: "华县",
        5: "临潼",
        6: "咸阳",
        7: "张家山",
        8: "魏家堡",
        9: "林家村",
        10: "北道",
        11: "武山",
        12: "",
        13: "",
        14: ""
    }
    for i in range(3,12):
        path = dir_name + '(' + str(i) + ')'
        for j in range(f_num):
            # mkdir('E:\\MyDocuments\\Scripts\\' + path)
            mkdir('D:\\Script\\Python\\test\\mkdir\\' + path)
            w_path = 'D:\\Script\\Python\\test\\mkdir\\' + path + '\\' + f_name + str(j) + '.bat'
            with open(w_path, 'w', encoding='ansi') as f:
                # config_0.bat
                # D:\文档-西北大学\HDMS2016\hdms4.exe -p D:\文档-西北大学\HDMS2016\database\北京逐年降水量.txt
                # D:\XXL\Prject\HDMS2016\hdms4.exe -p D:\XXL\Prject\HDMS2016\database\北京逐年降水量.txt
                line = "D:\\XXL\\Project\\HDMS2016\\hdms4.exe -p D:\\XXL\\Project\\HDMS2016\\database\\" + str(dis[i]) + str(ele[j]) + ".txt"
                f.write(line)


if __name__ == '__main__':
    dir_name = '水文站 '
    file_name = 'config_'
    write_dir(dir_name, file_name, 14, 4)

#! python3
# -*- coding:utf-8 -*-

import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
from prettytable import PrettyTable
import sys


def cal_n(date):
    """
    计算某天是一年中的第多少天
    :param date: 日期字符，例如：'2017-12-31'
    :return: 整型变量
    """
    mon_nums = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = int(date[:4])
    mon = int(date[5:7])
    day = int(date[8:10])
    if mon > 1:
        sum_data = sum(mon_nums[:mon - 1]) + day
    else:
        sum_data = day
    if year % 4 == 0 and mon > 2:
        sum_data += 1
    return sum_data


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def read_date(file_name, day_num=20, indent=7):
    """
    读取文件并打印想要内容
    :param file_name:
    :param day_num: 查询天数
    :param indent: 内容的列数
    :return:
    """
    data = xlrd.open_workbook(file_name)
    sheet2 = data.sheet_by_index(1)

    pool1, pool2, pool3 = [], {}, []
    for i in range(1, sheet2.nrows):
        cell_value = sheet2.cell(i, 5).value
        date = datetime(*xldate_as_tuple(cell_value, 0))
        new_date = date.strftime('%Y-%m-%d')
        pool1.append(new_date)
        pool2[cal_n(new_date)] = new_date
        pool3.append(cal_n(new_date))
    sort_pool = sorted(list(set(pool3)))
    today = datetime.now().strftime('%Y-%m-%d')
    i = 0
    for item in sort_pool:
        if item >= cal_n(today):
            break
        i += 1
    print('-'*40)
    print('下一个期限是', pool2[sort_pool[i]], ' 剩余', sort_pool[i] - cal_n(today), '天。')
    print('接下来'+str(day_num)+'天到期的有：')
    rest = sort_pool[i:]
    line_find = []
    for rest_day in rest:
        if 0 <= rest_day - cal_n(today) <= day_num:
            date_find = pool2[rest_day]
            list_index = [j for j, x in enumerate(pool1) if x == date_find]
            for i in range(len(list_index)):
                line_find.append(list_index[i])

    t = PrettyTable([''.join(str(item).split()) for item in sheet2.row_values(0)])
    for row in line_find:
        content = []
        for i in range(indent):
            content_cell = sheet2.row_values(row+1)[i]
            if i == 5:
                date = datetime(*xldate_as_tuple(content_cell, 0))
                content_cell = date.strftime('%Y-%m-%d')
            content.append(str(content_cell))
        t.add_row(content)
    print(t)


if __name__ == '__main__':
    print('-'*40)
    print('请确保本脚本与 license到期表.xlsx 在同一目录。')
    file = 'license到期表.xlsx'
    read_date(file, 20)
    while True:
        n = input('请输入想查询的天数（Q:退出）：')
        if n=='Q' or n=='q':
            sys.exit()
        try:
            n = int(n)
            read_date(file, n)
        except:
            print('输入有误！')

#! python3
# -*- coding:utf-8 -*-

import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime
from prettytable import PrettyTable
import sys
import time


def cal_n(date):
    """
    计算某天距2014-12-31多少天，（2015-01-01是第一天）
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
    if year < 2016 or (year == 2016 and mon < 3):
        sum_data += (year-2015)*365
    elif year >= 2016 or (year == 2016 and mon > 2):
        sum_data += ((year-2015)*365+1)
    elif 2016 < year < 2020 or (year == 2020 and mon < 3):
        sum_data += ((year-2015)*365+1)
    elif year >= 2020 or (year == 2020 and mon > 2):
        sum_data += ((year - 2015) * 365 + 2)
    return sum_data


def read_date(data, sheet_name, day_num=20, indent=8):
    """
    读取文件
    :param data:
    :param day_num: 查询天数
    :param indent: 内容的列数
    :return:
    """
    sheet2 = data.sheet_by_name(sheet_name)
    pool1, pool2, pool3 = [], {}, []
    for i in range(1, sheet2.nrows):
        cell_value = sheet2.cell(i, 5).value
        if cell_value is '':
            pool1.append('0')
        else:
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
    line_find = []
    if day_num >= 0:
        rest = sort_pool[i:]
        for rest_day in rest:
            delta = rest_day - cal_n(today)
            if 0 <= delta <= day_num:
                date_find = pool2[rest_day]
                list_index = [j for j, x in enumerate(pool1) if x == date_find]
                for i in range(len(list_index)):
                    line_find.append([list_index[i], delta])
    if day_num < 0:
        rest = sort_pool[:i]
        for rest_day in rest:
            delta = rest_day - cal_n(today)
            if day_num <= delta < 0:
                date_find = pool2[rest_day]
                list_index = [j for j, x in enumerate(pool1) if x == date_find]
                for i in range(len(list_index)):
                    line_find.append([list_index[i], delta])
    content_list = []

    if sheet_name == '2017年':
        indent += 1
    for row in line_find:
        content = [sheet_name, row[0]+2]
        for i in range(indent):
            content_cell = sheet2.row_values(row[0]+1)[i]
            if i == 0 and content_cell is not '':
                content_cell = int(content_cell)
            if i == 5:
                date = datetime(*xldate_as_tuple(content_cell, 0))
                content_cell = date.strftime('%Y-%m-%d')
            if i == 6:
                continue
            if sheet_name == '2017年' and i == 7:
                continue
            if i == indent-1:
                if len(str(content_cell)) > 10:
                    content_cell = str(content_cell)[:10] + '...'
            content.append(str(content_cell))
        content.append(row[1])
        content_list.append(content)
    return content_list


def print_date(data, sheets, day_num):
    contents = []
    for sheet in sheets:
        sheet_content = read_date(data, sheet, day_num)
        for content in sheet_content:
            contents.append(content)
        contents = sorted(contents, key=lambda x:x[-1])
    header = ['Sheet', 'Index', '编号', '客户名称', '项目名称', '项目编号', '购买产品', 'License到期日', '备注', '剩余天数']
    t = PrettyTable([''.join(str(item).split()) for item in header])
    remaining, deadline = [], []
    for content in contents:
        t.add_row(content)
        remaining.append(content[-1])
        deadline.append(content[-2])

    print('-'*40)
    print('下一个期限是', deadline[remaining.index(min(remaining))], ' 剩余', min(remaining), '天。')
    print('接下来'+str(day_num)+'天到期的有'+str(len(contents))+'项：')
    print(t)


def go():
    monent = time.time()
    file = '2011-2020年License到期统计--王杰.xlsx'
    data = xlrd.open_workbook(file)
    sheets = [str(i)+'年' for i in range(2013, 2022)]
    print('-'*60)
    print('请确保本脚本与 2011-2020年License到期统计--王杰.xlsx 在同一目录。')
    print('正在读取并解析数据，请稍等~~~')
    print_date(data, sheets, 20)
    print('with time:', time.time()-monent, 's')
    print('-'*40)

    while True:
        n = input('请输入想查询的天数（Q:退出）：')
        print('正在读取并解析数据，请稍等~~~')
        if n == 'Q' or n == 'q':
            sys.exit()
        try:
            monent = time.time()
            n = int(n)
            print_date(data, sheets, n)
            print('with time:', time.time() - monent, 's')
            print('-' * 40)
        except:
            print('输入有误！')


if __name__ == '__main__':
    go()

#! python3
# -*- coding:utf-8 -*-

import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime


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


def read_date(file_name):
    data = xlrd.open_workbook(file_name)
    sheet2 = data.sheet_by_index(1)

    pool1 = []
    pool2 = {}
    pool3 = []
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
    print('下一个期限是', pool2[sort_pool[i]], ' 剩余', sort_pool[i] - cal_n(today), '天。')
    print('接下来20天到期的有：')
    while sort_pool[i] - cal_n(today) < 20:
        date_find = pool2[sort_pool[i]]
        delta = sort_pool[i] - cal_n(today)
        print(date_find, delta)
        # list_index = pool1.index(date_find)
        list_index = [j for j, x in enumerate(pool1) if x == date_find]
        print('row:', list_index)
        for row in list_index:
            print(sheet2.row_values(row))
        i += 1


if __name__ == '__main__':
    file = 'license到期表.xlsx'
    read_date(file)

#! python3
# -*- coding:utf-8 -*-

import xlrd
from xlrd import xldate_as_tuple
from datetime import datetime


def read_data(file_name):
    # open file
    data = xlrd.open_workbook(file_name)
    print(data.sheet_names())

    sheet1 = data.sheet_by_index(0)
    # sheet2 = data.sheet_by_name('sheet01')sheet01
    # print(sheet1, sheet2)
    print(sheet1.name, sheet1.nrows, sheet1.ncols)

    rows = sheet1.row_values(2)
    cols = sheet1.col_values(2)

    print(rows, cols)

    print(sheet1.cell(0, 0).value)
    print(sheet1.cell_value(1, 1))
    date = sheet1.cell_value(1, 1)
    date = datetime(*xldate_as_tuple(date, 0))
    new_date = date.strftime('%Y-%m-%d %H:%M:%S')
    print(new_date)

    print(sheet1.row(1)[2].value)

    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    delta = datetime.strptime(today, '%Y-%m-%d %H:%M:%S') - datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S')
    print(delta)


if __name__ == '__main__':
    file = '汇报.xlsx'
    read_data(file)

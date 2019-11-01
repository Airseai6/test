#! python3
# -*- coding:utf-8 -*-

import db
import random

def gen_data():
    data = []
    year = [i for i in range(2009,2020)]
    estate = [chr(i)+'区' for i in range(65, 75)]
    area = [80, 100, 120]


    for j in estate:
        for k in area:
            price = 3000
            for i in year:
                price += random.randint(-500,1800)
                data.append([i, j, k, price])

    return data


if __name__ == '__main__':
    table_name = 'data'
    # db.create_tables(table_name, 0)
    data = gen_data()
    for i in data:
        db.insert_data(table_name, i[0], i[1], i[2], i[3])


#! python3
# -*- coding:utf-8 -*-

import random

import MySQLdb
database = 'db_demo6'
conn = MySQLdb.connect("localhost", "root", "", database, charset="utf8")
cur = conn.cursor()


def is_existed_table(table_name):
    sql = "show tables from %s" % (database)
    cur.execute(sql)
    result = cur.fetchall()
    if table_name in str(result):
        return True
    else:
        return False


def drop_tables(table_name):
    sql = 'drop table %s' % (table_name)
    cur.execute(sql)
    conn.commit()


def create_tables(table_name):
    if is_existed_table(table_name):
        drop_tables(table_name)
    sql = "create table %s (id int unsigned not null auto_increment primary key, " \
          "year int, estate varchar(20), area float, price float)" % (table_name)
    cur.execute(sql)
    conn.commit()


def insert_data(table_name, str_data):
    sql = "insert into %s (year, estate, area, price) values %s"\
          % (table_name, str_data)
    cur.execute(sql)
    conn.commit()


def select1(year):
    result = []
    sql1 = 'select avg(price) from data where year = %s' % (year)
    sql2 = 'select estate, area, price from data where price = (select max(price) from data where year = %s)' % (year)
    sql3 = 'select estate, area, price from data where price = (select min(price) from data where year = %s)' % (year)
    cur.execute(sql1)
    result.append(cur.fetchall())
    cur.execute(sql2)
    result.append(cur.fetchall())
    cur.execute(sql3)
    result.append(cur.fetchall())

    return result


def select2(estate, area):
    sql = 'select year, price from data where estate = "%s" and area = %s' % (estate, area)
    cur.execute(sql)

    return cur.fetchall()


def gen_data():
    '''数据生成'''
    data = []
    year = [i for i in range(2009, 2020)]
    estate = [chr(i) for i in range(65, 76)]
    area = [80, 100, 120]

    for j in estate:
        for k in area:
            price = 3000
            for i in year:
                price += random.randint(-500, 2000)
                data.append([i, j, k, price])

    return data


def write_data():
    '''数据写入到数据库'''
    table_name = 'data'
    create_tables(table_name)

    data = gen_data()
    str_data = ''
    for i in data:
        str_data += '('+str(i[0])+',\''+i[1]+'\','+str(i[2])+','+str(i[3])+'),'

    insert_data(table_name, str_data[:-1])


def conn_close():
    conn.close()


def replace_data(data):
    '''数据替换，此函数以后用ajax异步加载替代'''
    html = r'templates/login_success_simple.html'
    sign = '__sign01__'
    with open(html, 'r', encoding='utf8') as f:
        content = f.read()
    content = content.replace(sign, data)
    with open(html.replace('_simple', ''), 'w', encoding='utf8') as f:
        f.write(content)

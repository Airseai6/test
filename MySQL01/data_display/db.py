#! python3
# -*- coding:utf-8 -*-

import MySQLdb

database = 'test23'
conn = MySQLdb.connect("localhost", "root", "", database, charset="utf8")
cur = conn.cursor()


def conn_close():
    conn.close()


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


def create_tables(table_name, is_user):
    if is_existed_table(table_name):
        drop_tables(table_name)
    if is_user:
        sql = "create table %s (id int unsigned not null auto_increment primary key, " \
              "username varchar(20), password varchar(64))" % (table_name)
    else:
        sql = "create table %s (id int unsigned not null auto_increment primary key, " \
              "year int, estate varchar(20), area float, price float)" % (table_name)
    cur.execute(sql)
    conn.commit()


def insert_user(table_name, username, password):
    sql = "insert into %s (username, password) values ('%s','%s')" % (table_name, username, password)
    cur.execute(sql)
    conn.commit()


# def insert_data(table_name, year, estate, area, price):
#     sql = "insert into %s (year, estate, area, price) values ('%s','%s', '%s','%s')"\
#           % (table_name, year, estate, area, price)
#     cur.execute(sql)
#     conn.commit()


def insert_data(table_name, str_data):
    sql = "insert into %s (year, estate, area, price) values %s"\
          % (table_name, str_data)
    cur.execute(sql)
    conn.commit()


def is_existed(username, password):
    sql = "select * from user where username ='%s' and password ='%s'" % (username, password)
    cur.execute(sql)
    result = cur.fetchall()
    if (len(result) == 0):
        return False
    else:
        return True


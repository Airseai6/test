#! python3
# -*- coding:utf-8 -*-

import MySQLdb

# connect to db
conn = MySQLdb.connect('localhost', 'root', '', 'test')
# create cursor
cur = conn.cursor()
# sql command
name = input("teacher's name:" )
sql = "select * from teacher"
insert_sql = "insert into teacher (name) values ('%s')" %(name)

# execute
cur.execute(insert_sql)
conn.commit()
cur.execute(sql)

# get the result
result = cur.fetchall()
print(type(result))
print(result)
print('*'*30)

for row in result:
    print(row[0])
    print(row[1])

conn.close()

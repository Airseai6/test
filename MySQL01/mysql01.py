#! -*-coding:utf-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表sql语句
# sql = """CREATE TABLE EMPLOYEE (FIRST_NAME CHAR(20) NOT NULL,
#       LAST_NAME CHAR(20),
#       AGE INT, SEX CHAR(1), INCOME FLOAT)"""
sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
         VALUES('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    cursor.execute(sql)
    print('execute')
    db.commit()
    print('commit')
except:
    db.rollback()
    print('back')

# 关闭数据库连接
db.close()


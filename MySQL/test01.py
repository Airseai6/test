#-*- coding:utf-8 -*-
import pymysql
import traceback

#一：查询数据库版本的操作
# 连接MySQL数据库
connection=pymysql.connect(host="localhost",port=3306,user="root",passwd="928542",db="test",charset="utf8")
#创建一个数据库游标
cursor=connection.cursor()

cursor.execute("SELECT VERSION()")
#获取数据库的版本号
data=cursor.fetchone()
print("当前使用的MySQL版本是：{0}".format(data))

#关闭游标资源
cursor.close()
#关闭数据库资源
connection.close()


#库之中插入一个表的操作
#连接数据库
connection=pymysql.connect(host="localhost",port=3306,user="root",password="928542",db="test",charset="utf8")
#获取一个游标
cursor=connection.cursor()

#在数据库之中，使用execute方法执行sql语句，如果存在employee则把这个表给删除掉
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#编写sql语句

sql="""CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)

cursor.close()
connection.close()


#三：数据库插入字段的操作
#1：连接数据库
connection=pymysql.connect(host="localhost",port=3306,user="root",passwd="928542",db="test",charset="utf8")

#2：获取一个游标
cursor=connection.cursor()

#3:编写sql语句
sql="""INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('guo', 'junwei', 24, 'm', 4000)"""


#4:用execute（）方法执行sql语句
cursor.execute(sql)
#5:提交到数据库执行
connection.commit()
#6:关闭资源
cursor.close()
connection.close()


#四：数据库查询操作
#1:连接数据库
connection=pymysql.connect(host="localhost",port=3306,user="root",passwd="928542",db="test",charset="utf8")
#2:获取一个游标
cursor=connection.cursor()

#书写sql文件并执行它
sql="SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)

try:
    #执行sql文件
    cursor.execute(sql)
    data=cursor.fetchall()
    for hang in data:
        first_name=hang[0]
        last_name=hang[1]
        age=hang[2]
        sex=hang[3]
        incom=hang[4]
        print("first_name={0},last_name={1},age={2},sex={3},incom={4}".format(first_name,last_name,age,sex,incom))
except:
    print("try中的代码有问题，无法从数据库中获取符合条件的数据字段")

#关闭资源
connection.close()

#五：将数据库中emloyee表中的性别是男人的年龄自增加1
#连接数据库
connection=pymysql.connect(host="localhost",port=3306,user="root",passwd="928542",db="test",charset="utf8")
#获取一个游标
cursor=connection.cursor()
#编写sql文件
sql="UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

try:
    cursor.execute(sql)
    connection.commit()
except:
    connection.rollback()
#关闭资源
connection.close()

#六：删除数据库中age大于20的数据
#连接数据库
connection=pymysql.connect(host="localhost",port=3306,user="root",passwd="928542",db="test",charset="utf8")
#获取一个游标
cursor=connection.cursor()
#编写sql文件
sql="DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)

try:
    #执行sql文件
    cursor.execute(sql)
    #提交到数据库执行
    connection.commit()
except:
    connection.rollback()
    print("以上代码有问题，无法对数据库进行操作")
#关闭资源
connection.close()





































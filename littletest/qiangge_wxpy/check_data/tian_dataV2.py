#-*-coding:utf-8 -*-
import time
import pymysql

def firstopen():
    use1 = input("请输入您mysql数据库的账户：\n")
    password = input("请输入您mysql数据库的密码：\n")

    db = pymysql.connect(host='localhost', port=3306,user=use1, passwd=password, charset='utf8')
    cur = db.cursor()

    #***************
    #*获取所有的数据库名
    cur.execute("show databases")
    database_list = [tuple[0] for tuple in cur.fetchall()]
    print("MySQL中所有的数据库是:----> {0} <-----\n".format(database_list))
    #***************
    database_choose = input("请输入您所选择的数据库名称：")
    db.close()
    return database_choose ,use1,password

def main1():
    database_choose,use1,password = firstopen()
    #第二次开启指定的数据库
    db = pymysql.connect(host='localhost', port=3306,user=use1,db = database_choose, passwd=password, charset='utf8')
    cur = db.cursor()

    #***************
    #*获取某一个数据库的所有表名
    cur.execute("show tables")

    '''双重元组转成单程列表
    data = cur.fetchall()
    print(data)
    table_list = []
    for tu2 in data:
        for i in tu2:
            table_list.append(i)
    print(table_list)
    '''
    table_list = [tuple[0] for tuple in cur.fetchall()]
    print("该数据库中所有的表单是:----> {0} <-----\n".format(table_list))
    #***************
    table_choose = input("请输入您所选择的table表：")

    selectsql = '''SELECT * FROM {0}'''.format(table_choose)
    cur.execute(selectsql.encode('utf-8'))
    data_row = [tuple for tuple in cur.fetchall()]
    print("该表单中所有的信息记录是:----> {0} <-----\n".format(data_row))
    row_choose = input("请输入您想获取第几行的数据：")
    print()
    print("*"*10)
    print("您想查询的数据是：" ,data_row[(int(row_choose) -1)])
    # row_choose2 =input("请输入到第几行截止：")
    # print("您想查询的数据是：" ,data_row[(int(row_choose) -1):int(row_choose2)])
    print("*"*10)
    db.close()

if __name__ == '__main__':
    flag = True
    while flag:
        try:
            main1()
        except:
            print("连接数据库失败！！账号密码有问题！！\n")
        msg = input("继续使用请输入y,退出程序请按非y键:")
        if msg == "y":
            continue
        else:
            flag = False
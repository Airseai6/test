#! python3
# -*- coding:utf-8 -*-
import MySQLdb


def get_conn():
    host = '127.0.0.1'
    port = 3306
    db = 'jkxy'
    user = 'root'
    password = ''
    conn = MySQLdb.connect(host=host, user=user, password=password, db=db,
                           port=port, charset='utf8')
    return conn


class User():
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def save(self):
        conn = get_conn()
        cursor = conn.cursor()
        sql = 'insert into jikexueyuan(user_id, user_name) values(%s, %s)'
        cursor.execute(sql, (self.user_id, self.user_name))
        conn.commit()
        cursor.close()
        conn.close()

    def query_all():
        conn = get_conn()
        cursor = conn.cursor()
        sql = 'select * from jikexueyuan'
        cursor.execute(sql)
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = (row[0], row[1])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
        return users

    def __str__(self):
        return "id:{}---name:{}".format(self.user_id, self.user_name)


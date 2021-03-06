#! python3
# -*- coding:utf-8 -*-
import sqlite3

def get_conn():
    return sqlite3.connect("test.db")

class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def save(self):
        sql = 'insert into user VALUES (?,?)'
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(sql, (self.id, self.name))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def query(self):
        sql = 'select * from user'
        conn = get_conn()
        cursor = conn.cursor()
        users = []
        rows = cursor.execute(sql, (self.id, self.name))
        for row in rows:
            user = User(row[1], row[2])
            users.append(user)
        conn.commit()
        cursor.close()
        conn.close()
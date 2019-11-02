# -*-coding:utf-8 -*-
__author__ = 'XuShunQiang'
from exsit import db

class UserCount(db.Model):
    __tablesname__ = "usercount"
    count = db.Column(db.String(100),primary_key=True)
    password = db.Column(db.String(100),nullable=True)
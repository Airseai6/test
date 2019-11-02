#! python3
# -*- coding:utf-8 -*-

DEBUG = True


DIALECT = "mysql"
DIADATA = "mysqldb"
COUNT = "root"
PASSWORD = ""
HOST = "127.0.0.1"
PORT = "3306"
DATA_BASE = "db_demo6"
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8".format(COUNT, PASSWORD, HOST, PORT, DATA_BASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

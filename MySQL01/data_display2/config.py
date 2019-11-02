# coding:utf-8

__author__ = 'XuShunQiang'
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxxxx@localhost:3306/test?charset=utf8'

DIALECT = "mysql"
DIADATA = "mysqldb"
COUNT = "root"
PASSWORD = ""
HOST = "127.0.0.1"
PORT = "3306"
DATA_BASE = "db_demo6"
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8".format(COUNT, PASSWORD, HOST, PORT, DATA_BASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Base = declarative_base(engine)

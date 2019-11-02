# -*-coding:utf-8 -*-
__author__ = 'XuShunQiang'

from exsit import db
from models import UserCount
def  register(username,password):
     usercount1 = UserCount(count = username,password = password)
     db.session.add(usercount1)
     db.session.commit()
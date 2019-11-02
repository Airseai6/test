# -*-coding:utf-8 -*-
__author__ = 'XuShunQiang'

from models import UserCount


def select_data(username):
    usercount = UserCount.query.filter(UserCount.count == username).first()
    try:
        password = usercount.password
        if password:
            return password
        else:
            return (None + u"该用户名不存在！！！")
    except:
        print(u"该用户名不存在！！！")


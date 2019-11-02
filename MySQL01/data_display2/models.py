#! python3
# -*- coding:utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class UserCount(db.Model):
    __tablesname__ = "usercount"
    count = db.Column(db.String(40), primary_key=True)
    password = db.Column(db.String(40), nullable=True)


def register(username, password):
    usercount1 = UserCount(count=username, password=password)
    db.session.add(usercount1)
    db.session.commit()


def check_user(username):
    usercount = UserCount.query.filter(UserCount.count == username).first()
    try:
        password = usercount.password
        if password:
            return password
        else:
            return (None + u"该用户名不存在！！！")
    except:
        print(u"该用户名不存在！！！")

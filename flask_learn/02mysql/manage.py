#! python3
# -*- coding:utf-8 -*-
from flask_script import Manager
from app import app
from models import User

manager = Manager(app)


@manager.command
def save():
    user = User(1, 'jikexueyuan')
    user.save()


@manager.command
def query_all():
    result = User.query_all()
    for item in result:
        print(item)


if __name__ == '__main__':
    manager.run()
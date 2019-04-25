#! python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# 用户表
# create table user(id int primary key autoincrement,
#                   username varchar(100) not null)
# 文章表
# create table user(id int primary key autoincrement,
#                   title varchar(100) not null,)
#                   content text not null,)
#                   author_id int,
#                   foreign key 'author_id' references 'users.id')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

db.create_all()


@app.route('/')
def index():
    # 想要添加一篇文章，首先添加一个用户
    return render_template('index.html')


@app.route('/login/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
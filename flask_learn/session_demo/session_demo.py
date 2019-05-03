#! python3
# -*- coding:utf-8 -*-
import os
from flask import Flask, render_template, session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
# 添加数据到session中
# 操作session的时候和操作字典是一样的
# 不设置SECRET_KEY 不能运行的， 他是一个24位的字符串


@app.route('/')
def index():
    session['username'] = 'zhiliao'
    # return render_template('index.html')
    return 'Hello World!'


@app.route('/get/')
def get():
    return session.get('username')


@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'succes'


if __name__ == '__main__':
    app.run(debug=True)
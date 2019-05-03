#! python3
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    print('I am in view function')
    return 'hello world!'

# before_request： 在请求之前,
# 是在视图函数执行之前执行的，
# 这个函数只是一个装饰器，他可以把设置成钩子函数的代码放到装饰器之前执行


@app.before_request
def my_before_request():
    print('I am in hook function')


if __name__ == '__main__':
    app.run(debug=True)

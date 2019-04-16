#! python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
from models import User

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'hello world!'
    # return '<h1>hello world!</h1>'
    return render_template('index.html')


@app.route('/user')
def user_index():
    user = User(1, 'jikexueyuan')
    return render_template('user_index.html', user)


if __name__ == '__main__':
    app.run()

#! python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    class Person(object):
        name = u'黄勇'
        age = 18

    p = Person()

    # return render_template('index.html', username=u'许顺强', gender=u'男', age=u'18')
    context = {
        'username':u'许顺强',
        'gender':u'男',
        'age':23,
        'person':p,
        'websites':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

#! python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    content = [{'user':'huangyong',
         'coment': '123'
         },
        {'coment':'1234',}]

    return render_template('index.html', avata="https://www.baidu.com/img/baidu_jgylogo3.gif", content=content)


if __name__ == '__main__':
    app.run(debug=True)
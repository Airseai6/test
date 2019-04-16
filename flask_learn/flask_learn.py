#! -*- coding:utf-8 -*-

from flask import Flask, redirect, abort, request
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
    # return redirect('https://www.baidu.com')


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>'%name


# @app.route('/user/<id>')
# def get_user(id):
#     # user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, %s!</h1>' % user.name


@app.route('query_user')
def query_user():
    id = request.args.get('id')
    return 'query user:'+id


if __name__ == '__main__':
    app.run(debug=True)

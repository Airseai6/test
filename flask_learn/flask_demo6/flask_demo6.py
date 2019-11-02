# -*- coding: UTF-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from flask import Flask,render_template,request,url_for
import config
from flask_sqlalchemy import SQLAlchemy
from exsit import db
from models import UserCount
from login_filter import select_data
from register_progr import register


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    # db.create_all()
    return render_template("index.html")


@app.route('/regist',methods= ["GET","POST"])
def regist():
    # db.create_all()
    if request.method == "GET":
        return render_template("regist.html")
    else:
        username= request.form["username"]
        password = request.form["password"]
        register(username,password)
        return render_template("regist_succ.html")



@app.route('/login',methods = ["GET","POST"])
def login():

    if request.method =="GET":
        return render_template("login.html")
    else:
        username= request.form["username"]
        password = request.form["password"]
        b = select_data(username)
        if b:
            if password == b:
                return render_template("login_success.html")
            else:
                return render_template("login_mimamistak.html")
        else:
            return render_template("login_null.html")


if __name__ == '__main__':
    app.run()

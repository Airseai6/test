#! python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
import config
from models import *
import operate


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/regist', methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        try:
            register(username, password)
        except:
            return render_template("regist_mistake.html")

        return render_template("regist_succ.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        b = check_user(username)
        if b:
            if password == b:
                operate.write_data()
                print(operate.select1(2019))
                for i in operate.select1(2019):
                    print(i[0][0])
                print(operate.select1(2013)[0][0][0])
                print(operate.select2("A", 100))
                for i in operate.select2("A", 100):
                    print(i[1])

                return render_template("login_success.html")
            else:
                return render_template("login_mistake.html")
        else:
            return render_template("login_null.html")


@app.route('/login_success', methods=["GET", "POST"])
def select():
    if request.method == "GET":
        return render_template("login_success.html")
    else:
        select_year = request.form["select_year"]
        print(select_year)
        avg = int(operate.select1(select_year)[0][0][0])
        max = int(operate.select1(select_year)[1][0][2])
        min = int(operate.select1(select_year)[2][0][2])

        return render_template("login_success.html", select_year=str(select_year), avg_price=str(avg)+'元',
                               max_price=str(max)+'元', min_price=str(min)+'元')


if __name__ == '__main__':
    app.run()

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
    '''用户注册页面'''
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
    '''用户登录页面，post方式，页面获得的账号密码到数据库查询，返回出错，成功，或无此用户页面'''
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        b = check_user(username)
        if b:
            if password == b:
                operate.write_data()

                return render_template("login_success.html")
            else:
                return render_template("login_mistake.html")
        else:
            return render_template("login_null.html")


@app.route('/login_success', methods=["GET", "POST"])
def select():
    '''登录成功界面'''
    if request.method == "GET":
        return render_template("login_success.html")
    else:
        select_year = request.form["select_year"]
        '''解析不同年份的平均，最高最低价格'''
        avg = int(operate.select1(select_year)[0][0][0])
        max = int(operate.select1(select_year)[1][0][2])
        max_estate = operate.select1(select_year)[1][0][0]
        min = int(operate.select1(select_year)[2][0][2])
        min_estate = operate.select1(select_year)[2][0][0]

        '''不同区不同面积，读取历年价格'''
        select_estate = request.form["select_estate"]
        select_area = request.form["select_area"]
        data = operate.select2(select_estate[0], select_area)
        data_form = []
        for i in data:
            data_form.append(i[1])
        operate.replace_data(str(data_form))

        '''数值返回到html'''
        return render_template("login_success.html", select_year=str(select_year), avg_price=str(avg)+'元',
                               max_price=max_estate+'区：'+str(max)+'元', min_price=min_estate+'区：'+str(min)+'元',
                               arr_data=data_form, select_estate=select_estate[0], select_area=select_area)


if __name__ == '__main__':
    app.run()

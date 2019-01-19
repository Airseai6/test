# -*- coding: UTF-8 -*-

from flask import Flask
from flask_mail import Mail,Message
import config
from threading import Thread

app = Flask(__name__)
# app.config.from_object(config)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '1690564676@qq.com' #邮箱账号
app.config['MAIL_PASSWORD'] = 'lqkyanekfhurhjca'  #QQ邮箱授权码
mail = Mail(app)


def send_message_mail(app,message):
    with app.app_context():
        mail.send(message)

@app.route('/')
def sendmail():
    message = Message('凯哥', sender='1690564676@qq.com', recipients=['13051031204@163.com'])
    message.body ="是否有50个邮件呢？？？？？"
    for i in range(5):
        thread = Thread(target=send_message_mail,args=[app,message])
        thread.start()
    return "successfull!!!"
if __name__ == '__main__':
    app.run()

#! python
# -*- coding:utf-8 -*-
# 信息管理，可登陆管理

import json


def interface():
    # 欢迎界面
    print('*'*21)
    print('*		1.登陆		*')
    print('*		2.注册		*')
    print('*		3.退出		*')
    print('*'*21)


def login_user():
    register = input('Please input user name : ')
    try:
        with open(register+'.json') as file_object:  # 读
            user_message = json.load(file_object)
    except FileNotFoundError:
        print('The user name is not found!')
    else:
        register_password = input('Please input password: ')
        if user_message['id'] == register and user_message['password'] == register_password:
            print('登陆成功！')
            # 怎样读取并修改里面内容!!!!!!!!!!!!
            with open(register+'_information.json', 'r') as file_object:
            	user_content = json.load(file_object)
            	print('item: ', user_content['item'])
            	print('content: ', user_content['content'])
            item = input('Item: ')
            content = input('Content: ')
            information = {'item': item, 'content': content}
            with open(register+'_information.json', 'w') as file_object:
                json.dump(information, file_object)
        else:
            print('登陆失败！用户名或密码错误。')


def register_user():
    # 用户注册
    new_user = input('Please input user name : ')
    try:
        with open(new_user+'.json', 'r') as file_object:
            pass
    except FileNotFoundError:
        new_password = input('Set user password: ')
        new_password2 = input('Set user password again: ')
        if new_password == new_password2:
            # 存储信息，信息保存到json文件
            userMessage = {'id': new_user, 'password': new_password2}
            with open(new_user+'.json', 'w') as file_object:  # 写
                # dump将Python格式数据类型保存到json文件中
                json.dump(userMessage, file_object)
                print('注册成功！')
        else:
            print('两次输入密码不一致！')
    else:
        print('该用户已存在！')


def main():
    interface()
    operation = input('Please input the option num : ')
    if operation == '1':
        try:
            user_id, user_stdent_system = login_user()
        except Exception:
            pass
    elif operation == '2':
        register_user()
    elif operation == '3':
        pass
    else:
        print('*******ERROR!********')
        main()


if __name__ == '__main__':
    main()

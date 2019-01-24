#-*-coding:utf-8 -*-
#基于python3.6
__author__ = 'XuShunQiang'

import itchat,time
import sys
from itchat.content import *

itchat.auto_login(hotReload = True)
message = '在吗？？？？'


friendList = itchat.get_friends(update=True)[1:]
print(friendList)


#=========================
# 1：发送凯哥30次的代码
# print(friendList[2]["RemarkName"])
# print(friendList[2])
#
# for i in range(30):
#     a = itchat.send(msg = SINCERE_WISH,toUserName = friendList[2]["UserName"])
#     print(i,a)
#     print(friendList[2]['RemarkName'],'%s 已发送了 %s' % i)
#=================================

#=========================
# 2：发送田�?3次的代码
# print(friendList[0]["RemarkName"])
#
# for i in range(3):
#     a = itchat.send(msg = message,toUserName = friendList[0]["UserName"])
#     print(i,a)
#     print(friendList[0]['RemarkName'],'%s 已发�?'% i)
#
# print("="*20)

#=================================
# 3：for循环获取的好友列表，筛选出指定的好友发送相应的信息，并将发送是否成功的结果返回回来?
# for i in range(0,len(friendList)):
#     if friendList[i]['RemarkName'] == "田田邯郸�?":
#         a = itchat.send(msg = message,toUserName = friendList[i]["UserName"])
#         print(a['BaseResponse']['ErrMsg'])
#         print("已经将信息发送给 %s �?" % friendList[i]['RemarkName'])
#=================================
# print(friendList)
# print(friendList2)

for i in range(0,226):
        print("第 {} 个好友：名字:{}-------->>>> UserName:{}".format(i,friendList[i]['RemarkName'],friendList[i]['UserName']))



# for i in range(0,len(friendList)):
#     if friendList[i]['RemarkName'] == "A暂停收评�?21号（年后上班�?":
#         print( friendList[i]['RemarkName'])






#=================================



# for g in range(0,len(friendList)):
#     itchat.send(SINCERE_WISH,friendList[g]['UserName'])
#     print((friendList[g]['RemarkName'] or friendList[g]['NickName']),'已发�?')
#     sys.stdout.write(str(g+1)+"/"+str(len(friendList))+"\r")
#     sys.stdout.flush()
#     time.sleep(2)
# print('done')






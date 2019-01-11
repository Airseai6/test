#! python
# -*- coding:utf-8 -*- 
# 先启动服务端
import socket


server = socket.socket()   # 声明socket类型，同时生成socket连接对象
server.bind(('localhost', 6969))   # 绑定监听端口
#server.bind(('192.168.1.171', 6969))
server.listen(5)   # 监听

print('我要开始等电话了')
conn, addr = server.accept()   # 等, conn就是客户端的一个连接实例
# print(conn, addr)

print('电话来了')
while True:
	data = conn.recv(1024)
	print('recv:', data.decode())
	msg = input('>>>: ')
	conn.send(msg.encode('utf-8'))


server.close()

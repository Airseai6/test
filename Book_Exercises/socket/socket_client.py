#! python
# -*- coding:utf-8 -*- 

import socket

client = socket.socket()   # 声明socket类型，同时生成socket连接对象
client.connect(('localhost', 6969))
#client.connect(('192.168.78.130', 6969))

print('我要开始打电话了')
while True:
	msg = input('>>>: ').strip()
	client.send(msg.encode('utf-8'))
	data = client.recv(1024)
	print('recv:', data.decode())

client.close()

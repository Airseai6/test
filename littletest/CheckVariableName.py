#! python
# -*- coding:utf-8 -*-

# 判断输入的变量名是否符合规范，若为Python的关键字则返回关键字用法

import keyword


def check_name():
	str0 = input('Please input your variable name : ')
	if ord(str0[0]) in range(48, 59):
		print('Invalid variable name: The first letter is a number.')
		check_name()
	else:
		num = 0
		for i in str0:
			if ord(i) in range(48, 59) or ord(i) in range(65, 90) or ord(i) in range(97, 122) or ord(i) == 95:
				num += 1
		if num != len(str0):
			print('Invalid variable name: It has '+str(len(str0)-num)+' special character!')
			check_name()
		elif str0 in keyword.kwlist:
			print('Invalid variable name: It is a keyword !')
			help(str0)
		else:
			print('It is a valid variable name !')
			check_name()


if __name__ == '__main__':
	check_name()

#! python
# -*- coding:utf-8 -*-
"""
输入一个正整数，偶数则number/2，奇数则number*3-1,不断迭代最终会得到1。这有时候被称为最简单的不可能的数学问题。
知识点：1、input()为str型，数字需要强制转换；2、子函数调用自己传参要用global类型。
"""
def collatz(num):
	if num %2 ==0:
		num /= 2
	else:
		num = 3*num + 1
	print(int(num))
	return num

def input_int():
	global i
	try:
		i = int(input('Please input a positive integer : '))
	except ValueError:
		print('Error !')
		input_int()
	return i
	
def main():
	number = input_int()
	if number < 1:
		number = input_int()
	while number > 1:
		number = collatz(number)
		continue
		
if __name__ == '__main__':
	main()
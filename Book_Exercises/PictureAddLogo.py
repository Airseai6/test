#! python
# -*- coding:utf-8 -*-
# Resize all bigger image in current working directory to fit in a rectangle, and adds a picture to a corner.

import os,sys,time
from PIL import Image


def check_logo():
	x = input('The logo file name is \'logo.png\'? Y/N: ')
	if x == 'y' or x == 'Y':
		return 'logo.png'
	elif x == 'n' or x == 'N':
		f = input('Please input logo file name: ')
		return f
	else:
		check_logo()


def resize_w():
	x = input('Do you want to keep the size of the original pictures? Y/N: ')
	if x =='Y' or x =='y':
		return 'Y'
	elif x =='N' or x =='n':
		s = input('Please input the width of pictures: ')
		try:
			num = int(s)
			return num
		except ValueError:
			resize_w()
	else:
		resize_w()


def left_right():
	x = input('Lower-left corner or lower-right corner? L/R: ')
	if x == 'l' or x == 'R':
		return 'L'
	elif x == 'r' or x == 'R':
		return 'R'
	else:
		left_right()


def add_logo():
	logo_filename = check_logo()
	try:
		logoIm = Image.open(logo_filename)
		logoWidth, logoHeight = logoIm.size
	except FileNotFoundError:
		print('未找到logo文件，程序即将退出。')
		time.sleep(3)
		sys.exit()
	# 询问是否更改大小，logo位置等
	new_w = resize_w()
	lr = left_right()
	# 创建一个新文件夹存放new-picture,存在时防止抛出异常
	os.makedirs('withlogo', exist_ok=True)
	# Loop over all files in the working directory. If a special directory? skip no picture and logo itself
	for filename in os.listdir('.'):
		if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.PNG') or \
				filename.endswith('.JPG')) or filename == logo_filename:
			continue
		im = Image.open(filename)
		width, height = im.size
		# Check if image needs to be resized.
		if new_w != 'Y':
			height = int((new_w / width)*height)
			width = new_w
			im = im.resize((width,height))
		# Add the logo
		print('Adding logo to %s'%(filename))
		r,g,b,a = logoIm.split()
		logoIm.convert('RGBA')
		if lr == 'L':
			im.paste(logoIm, (0, height - logoHeight), mask=a)
		else:
			im.paste(logoIm, (width - logoWidth, height - logoHeight), mask=a)
		im.save(os.path.join('withlogo',filename))


def main():
	print('Please put the batch picture, logo picture and this program in the same directory.')
	add_logo()


if __name__ == '__main__':
	main()

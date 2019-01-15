#! python3
# -*- coding:utf-8 -*-

import os
from PIL import Image


def add_logo(logo_filename, dirname):
	'''
	给图片加logo水印
	'''
	logoIm = Image.open(logo_filename)
	logoWidth, logoHeight = logoIm.size
	# logo最好不要1920*1080
	# 创建一个新文件夹存放new-picture,存在时防止抛出异常
	os.makedirs('withlogo', exist_ok=True)
	# 遍历工作目录下图片
	for filename in os.listdir(dirname):
		filepath = os.path.join(dirname, filename)
		if not (filename.endswith('.png') or filename.endswith('.jpg')):
			continue
		im = Image.open(filepath)
		width, height = im.size
		# Check if logo needs to be resized.
		if logoWidth < width:
			if (width / logoWidth) > (height / logoHeight):
				logoHeight = int((logoHeight / logoWidth) * width)
				logoWidth = width
			else:
				logoWidth = int((logoWidth / logoHeight) * height)
				logoHeight = height
			logoIm = logoIm.resize((logoWidth, logoHeight))
		# Add the logo
		print('Adding logo to %s'%(filename))
		r, g, b, a = logoIm.split()
		logoIm.convert('RGBA')
		im.paste(logoIm, (0, 0), mask=a)
		im.save(os.path.join('withlogo', filename))


if __name__ == '__main__':
	logo_filename = 'logo_01.png'
	dirname = r"workspace"
	add_logo(logo_filename, dirname)
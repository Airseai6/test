#! python
# -*- coding:utf-8 -*-

import os
from PIL import Image


def addLogo():
	'''
	Resize all bigger image in current working directory to fit in a rectangle,
	and adds a picture to the left-lower corner.
	'''
	width_fit_size = 800
	logo_filename = 'LOLlogo.png'

	logoIm = Image.open(logo_filename)
	logoWidth, logoHeight = logoIm.size
	# 创建一个新文件夹存放new-picture,存在时防止抛出异常
	os.makedirs('withlogo', exist_ok=True)
	# Loop over all files in the working directory. If a special directory? skip no picture and logo itself
	for filename in os.listdir('.'):
		if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_filename:
			continue
		im = Image.open(filename)
		width, height = im.size
		# Check if image needs to be resized.
		if width > width_fit_size:
			height = int((width_fit_size / width)*height)
			width = width_fit_size
			im = im.resize((width,height))
		# Add the logo
		print('Adding logo to %s'%(filename))
		r,g,b,a = logoIm.split()
		logoIm.convert('RGBA')
		im.paste(logoIm,(0,height-logoHeight),mask=a)
		im.save(os.path.join('withlogo',filename))


if __name__ == '__main__':
	addLogo()
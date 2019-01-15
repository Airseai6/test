#! python3
# -*- coding:utf-8 -*-
import os
import zipfile
from PIL import Image
import shutil


def add_logo(logo_filename, dirname):
    logoIm = Image.open(logo_filename)
    logoWidth, logoHeight = logoIm.size
    # logo最好不要1920*1080
	# 遍历工作目录下图片
    for filename in os.listdir(dirname):
        filepath = os.path.join(dirname, filename)
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
        r, g, b, a = logoIm.split()
        logoIm.convert('RGBA')
        im.paste(logoIm, (0, 0), mask=a)
        im.save(filepath)


def word2dir(filename):
    with open(filename, 'rb')as f:
        data = f.read()
    if filename.endswith('.doc'):
        new_file = filename.replace('.doc', '_water.zip')
    else:
        new_file = filename.replace('.docx', '_water.zip')
    with open(new_file, 'wb') as f:
        f.write(data)
    azip = zipfile.ZipFile(new_file)
    try:
        os.mkdir(new_file[:-4])
    except:
        pass
    azip.extractall(new_file[:-4])
    azip.close()
    os.remove(new_file)
    return new_file[:-4]


def dir2word(pathname, filename):
    # 新建压缩包，放文件进去,若压缩包已经存在，将覆盖。可选择用a模式，追加
    new_file = pathname + '.zip'
    # azip = zipfile.ZipFile(new_file, 'w')
    # # azip.write(pathname, compress_type=zipfile.ZIP_LZMA)
    # for current_path, subfolders, filesname in os.walk(pathname):
    #     print(current_path, subfolders, filesname)
    #     for file in filesname:
    #         # 将当前路径与当前路径下的文件名组合，就是当前文件的绝对路径
    #         azip.write(os.path.join(current_path, file))
    # azip.close()

    # 第一个参数是归档文件名称，第二个参数是指定的格式，不仅是支持zip，第三个参数是要压缩文件/文件夹的路径
    shutil.make_archive(pathname, 'zip', pathname)
    # os.remove(pathname)

    with open(new_file, 'rb')as f:
        data = f.read()
    with open(filename.replace('.', '_water.'), 'wb')as f:
        f.write(data)
    os.remove(new_file)


if __name__ == '__main__':
    print('请确保脚本与word文件，与\'logo_01.png\'水印图片在同一目录下。')
    logo_filename = 'logo_01.png'
    for filename in os.listdir():
        if filename.endswith('.doc') or filename.endswith('.docx'):
            print('正在解析 '+ filename)
            path = word2dir(filename)
            dirname =os.getcwd() + '\\' + filename[:-5] + '_water' + "\\word\\media"
            print('正在修改 ' + filename + '中的图片')
            add_logo(logo_filename, dirname)
            print('正在合成 ' + filename.replace('.', '_water.'))
            dir2word(path, filename)

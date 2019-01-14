#! python3
# -*- coding:utf-8 -*-
import os
import os.path
import zipfile
import sys
reload(sys)
sys.setdefaultencoding('gbk')  # windows下编码问题


def gzip(zip_name, file_dir):
    zip_name = zip_name.decode('utf-8')
    file_dir = file_dir.decode('utf-8')
    filelist = []
    if os.path.isfile(file_dir):
        filelist.append(file_dir)
    else:
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                filelist.append(os.path.join(root, file))

        zf = zipfile.ZipFile(zip_name, 'w', zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(file_dir):]
            zf.write(tar, arcname)
        zf.close()


def unzip(zip_name, unzip_dir):
    unzip_dir = unzip_dir.decode('utf-8')  # 不转码会乱码
    zip_name = zip_name.decode('utf-8')  # 不转码zipfile报错
    if not os.path.exists(unzip_dir):
        os.mkdir(unzip_dir)
    zfobj = zipfile.ZipFile(zip_name)
    for file_name in zfobj.namelist():
        file_name = file_name.replace('\\', '/')
        if file_name.endswith('/'):
            # try:
            #     file_name = file_name.decode('utf-8')
            # except UnicodeDecodeError:
            #     file_name = file_name.decode('gbk')
            os.mkdir(os.path.join(unzip_dir, file_name))
        else:
            # try:
            ext_filename = os.path.join(unzip_dir, file_name)
            # except UnicodeDecodeError:
            #     ext_filename = os.path.join(unzip_dir, file_name.decode('gbk'))
            ext_filedir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_filedir):
                os.mkdir(ext_filedir)
            data = zfobj.read(file_name)
            with open(ext_filename, 'w') as f:
                f.write(data)
    zfobj.close()


if __name__ == '__main__':
    gzip(r'E:\Project\zip_adv\zip文件.zip', r'E:\Project\zip_adv\压缩文件')
    unzip(r'E:\Project\zip_adv\zip文件.zip', r'E:\Project\zip_adv\解压缩zip')

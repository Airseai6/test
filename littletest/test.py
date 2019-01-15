#! python3
# -*- coding:utf-8 -*-
import os
import zipfile
# os.remove('11.txt')

# azip = zipfile.ZipFile('321.zip', 'w')
# for current_path, subfolders, filesname in os.walk('123'):
#     print(current_path, subfolders, filesname)
#     for file in filesname:
#         # 将当前路径与当前路径下的文件名组合，就是当前文件的绝对路径
#         azip.write(os.path.join(current_path[3:], file))
import shutil
# 第一个参数是归档文件名称，第二个参数是指定的格式，不仅是支持zip，第三个参数是要压缩文件/文件夹的路径
shutil.make_archive('archive_name', 'zip', r'123')
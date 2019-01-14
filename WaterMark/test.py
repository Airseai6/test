#! python3
# -*- coding:utf-8 -*-
import os

for filename in os.listdir():
    if not (filename.endswith('.doc') or filename.endswith('.docx')):
        continue

    with open(filename, 'rb') as f:
        data = f.read()

    if filename.endswith('.doc'):
        new_file = filename.replace('.doc', '_water.zip')
    else:
        new_file = filename.replace('.docx', '_water.zip')
    with open(new_file, 'wb') as f:
        f.write(data)
#! python
# -*- coding:utf-8 -*-

path = "./111.txt"
# 把内容写到内存
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
# 写的方式打开文件
with open(path, "w", encoding="utf-8") as f_w:
    for line in lines:
        if "a" in line:
            old_line = line
            temp_line = line.split()
            temp_line.pop(2)
            new_line = ' '.join(temp_line)
            line = line.replace(old_line, new_line)
        f_w.write(line)


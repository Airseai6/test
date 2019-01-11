#! python3
# -*- coding:utf-8 -*-
from tkinter import *


root = Tk()                              # 创建窗口对象
li = ['C', 'C++', 'Matlab', 'Python']
yang = ['Java', 'C#']
listab = Listbox(root)
listab2 = Listbox(root)

for item in li:
    listab.insert(0, item)
for item in yang:
    listab2.insert(0, item)

listab.pack()                            # 将小部件放到窗口中
listab2.pack()
root.mainloop()                          # 进入循环

#! python3
# -*- coding:utf-8 -*-
import re
# [
#     {
#         "1月1日": "-3分9秒",
#         "1-1": "-3*60+9",
#         "1-1": -189,
# num1 = r'\"(.+?)月'
# num2 = r'月(.+?)日'
# num3 = r'\"(.+?)分'
# num4 = r'分(.+?)秒'
with open('sun.json', 'r', encoding='utf8')as f:
    data = f.readlines()

new_data = {}
for line in data:
    if ':' in line:
        num = re.findall(r'\d+', line)
        mon = num[0]
        day = num[1]
        if len(mon) == 1:
            mon = '0' + mon
        if len(day) == 1:
            day = '0' + day
        minu = int(num[2])
        sec = int(num[3])
        key = mon + '-' + day
        if '-' in line:
            value = str(-minu*60-sec)
        else:
            value = str(minu*60+sec)
        new_data[key] = value
print(new_data)

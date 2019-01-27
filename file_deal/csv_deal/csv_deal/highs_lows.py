#! python3
# -*- coding:utf-8 -*-
import csv
from matplotlib import pyplot as plt
# from decimal import *
from datetime import datetime

file_name = 'sitka_weather_2014.csv'
with open(file_name, 'r')as f:
    # 创建阅读器
    reader = csv.reader(f)
    # 将阅读器传给next，将读下一行
    header_row = next(reader)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    # 阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行。由于我们已经
    # 读取了文件头行，这个循环将从第二行开始——从这行开始包含的是实际数据
    for row in reader:
        current_data = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_data)
        # try:
        #     # high = Decimal(row[1])
        #     high = int(row[1])
        #     low = int(row[3])
        # except:
        #     print(current_data, ' missing data')
        # else:
        #     highs.append(high)
        #     lows.append(low)
        high = int(row[1])
        low = int(row[3])
        highs.append(high)
        lows.append(low)
# 用matplotlib绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
# alpha为透明度
plt.plot(dates, highs, c='red', alpha=0.9)
plt.plot(dates, lows, c='blue', alpha=0.9)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title('Daily high and low temperatures, 2014', fontsize=24)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


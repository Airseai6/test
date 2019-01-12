#! python3
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
'''
散点图
'''
# x_value = [x for x in range(1,6)]
# y_value = [y**2 for y in range(1,6)]
x_value = list(range(1, 100))
y_value = [x**2 for x in x_value]
# 删除数据点的颜色 edgecolors='nono',
plt.scatter(x_value, y_value, edgecolors='none', c=y_value, cmap=plt.cm.Blues, s=10)
plt.title('Square numbers', fontsize=20)
plt.xlabel('numbers', fontsize=10)
plt.ylabel('Square of numbers', fontsize=10)
plt.show()
# plt.savefig('test', bbox_inches='tight')
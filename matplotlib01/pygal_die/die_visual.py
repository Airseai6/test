#! python3
# -*- coding:utf-8 -*-
from die import Die
import pygal

die = Die()
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()
hist.title = 'Result of roll a D6'
hist.x_labels = list(range(1, 7))
hist.x_title = 'Results'
hist.y_title = 'Frequencies of Results'
hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')
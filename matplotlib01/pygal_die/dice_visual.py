#! python3
# -*- coding:utf-8 -*-
from die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_reuslt = die_1.num_sides + die_2.num_sides
for value in range(2, max_reuslt+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'Results of two D6'
hist.x_labels = list(range(2,13))
hist.x_title = 'results'
hist.y_title = 'frequencies of results'

hist.add('D6+D6', frequencies)
hist.render_to_file('two_D6.svg')

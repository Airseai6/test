#! python3
# -*- coding:utf-8 -*-
import json
from countries import get_country_code
import pygal.maps.world
from pygal.style import RotateStyle

# 将数据加载到一个列表中
file_name = 'population_data.json'
with open(file_name, 'r')as f:
    pop_data = json.load(f)

# 打印每个国家2010年人口
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 给国家按人口分组
cc_pops_1, cc_pops_2, cc_pops_3, = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 绘制世界地图
wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World population in 2010, by Country'
# wm.add('2010', cc_populations)
wm.add('<10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')


#! python3
# -*- coding:utf-8 -*-
import json
from countries import get_country_code
# 将数据加载到一个列表中
file_name = 'population_data.json'
with open(file_name, 'r')as f:
    pop_data = json.load(f)

# 打印每个国家2010年人口
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ' : ' + str(population))
        else:
            print('ERROR - '+country_name)


#! python3
# -*- coding:utf-8 -*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
# 将API响应存储在一个变量中
response_dict = r.json()
print('Total Repositories: ', response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(len(repo_dicts))
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
mystyle = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=mystyle, x_label_rotation=45, show_legend=False)
chart.title = 'Most stars Python project in Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')


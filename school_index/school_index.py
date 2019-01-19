#! python3
# -*- coding:utf-8 -*-
from xpinyin import Pinyin


def gen_id(input_file, nginx=8900, python=5800, webs=8330):
    """
    生成网站上的学校相关编号
    """
    with open(input_file, 'r')as f:
        data = f.readlines()
    data = [line.strip().split(',') for line in data]
    school_list = []
    p = Pinyin()
    # school = {}
    for i in range(0,2):
        school = {}
        school['u_name'] = data[i][0]
        school['a_name'] = data[i][1]
        # 学校简称，学院单独处理
        # abb = p.get_initials(school['u_name'], '').lower() + p.get_initials(school['a_name'], '').lower()
        abb = p.get_initials(school['u_name'], '').lower()
        school['Nginx HTTP'] = nginx + 100*i
        school['Python'] = python + 100*i
        school['MySQL'] = 3310
        school['Redis'] = 5001
        school['WebSocket'] = webs + 100*i
        school['HTML'] = 'html_' + abb
        school['DB'] = 'cloudlearn_' + abb
        school_list.append(school)
    print(school_list)
    l_chr = '\t'
    with open('new_list.txt', 'a')as f:
        for school in school_list:
            content = '### CloudLearn ' + school['u_name'] + school['a_name'] + '\n\n' \
                      + 'http://119.23.40.38:' + str(school['Nginx HTTP']) + '/\n\n' \
                      + l_chr + str(school['Nginx HTTP']) + ' Nginx HTTP\n' \
                      + l_chr + str(school['Python']) + ' Python\n' \
                      + l_chr + str(school['MySQL']) + ' MySQL\n' \
                      + l_chr + str(school['Redis']) + ' Redis\n' \
                      + l_chr + str(school['WebSocket']) + ' WebSocket\n' \
                      + l_chr + str(school['HTML']) + ' HTML\n' \
                      + l_chr + str(school['DB']) + ' DB\n' \
                      + '\n\n'
            f.write(content)


if __name__ == '__main__':
    file = 'school_list.csv'
    gen_id(file)

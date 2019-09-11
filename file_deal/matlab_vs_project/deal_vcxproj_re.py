#! python3
# -*- coding:utf-8 -*-

import re
import os
from time import sleep

'''
修改VS相关的项目配置文件应用MATLAB项目
'''


def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def father_label(file_name, content, label):
    # p1 = r"(?s)<PropertyGroup Condition.+?</PropertyGroup>"    # (?s)多行拼配
    # p1 = r"(?s)<ItemDefinitionGroup Condition.+?</ItemDefinitionGroup>"
    p1 = r"(?s)<%s Condition.+?</%s>" % (label, label)
    pattern1 = re.compile(p1)
    result = pattern1.findall(content)
    print("\n'%s'一共有%d处'%s'标签" % (file_name, len(result), label))

    p2 = r"(?<=(==')).+?(?=('))"
    pattern2 = re.compile(p2)
    for i in range(len(result)):
        matcher2 = re.search(pattern2, result[i])
        print("第%d处 -> " % (i+1), end='')
        print(matcher2.group(0))
    return result


def son_label(result, label2, label3, str_add, choose=2):
    try:
        num = int(choose) - 1
        content = result[num]
    except:
        print('输入有误！')
    p1 = r'(?<=<(%s)>).*(?=<\/\1>)' % label2
    pattern1 = re.compile(p1)
    matcher1 = re.search(pattern1, content)
    path = matcher1.group(0)
    print("\n正在将 %s 添加到第%d处路径内容~~~" % (str_add, choose))
    new_path = str_add + path

    p2 = r'(?<=<(%s)>).*(?=<\/\1>)' % label3
    pattern2 = re.compile(p2)
    matcher2 = re.search(pattern2, content)
    macro_debug = matcher2.group(0)
    print("正在提取第%d处的宏定义~~~" % (choose))
    return [path, new_path, macro_debug]


def write_file(file_name, template, content, result, label2, label3, label4, choose=2):
    print("正在修改其他%d处的内容~~~" % (len(result)-1))
    pool = [i for i in range(len(result))]
    pool.remove(choose-1)
    content = content.replace(template[0], template[1])
    for i in pool:
        p1 = r'(?s)(?<=<(%s)>).*(?=<\/\1>)' % label4
        pattern1 = re.compile(p1)
        matcher1 = re.search(pattern1, result[i])
        son_content = matcher1.group(0)
        new_son_content = son_content + r"  <%s>%s</%s>" % (label2, template[1], label2) + '\n    '
        content = content.replace(son_content, new_son_content)

        p2 = r'(?<=<(%s)>).*(?=<\/\1>)' % label3
        pattern2 = re.compile(p2)
        matcher2 = re.search(pattern2, result[i])
        macro = matcher2.group(0)
        if "$(Configuration)|$(Platform)'=='Debug|" in result[i]:
            content = content.replace(macro, template[2])
        else:
            macro_release = template[2].replace('_DEBUG', 'NDEBUG')
            content = content.replace(macro, macro_release)
    with open(file_name.replace('.vcxproj', '_new.vcxproj'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("'%s'修改完毕~~~" % file_name)


if __name__ == '__main__':
    print('请确保脚本与*.vcxproj文件在同一目录下。')
    for file_name in os.listdir():
        if file_name.endswith('.vcxproj') and '_new.vcxproj' not in file_name:
            # file_name = 'Three_Phase_Inverter_V2017a.vcxproj'
            # label = 'PropertyGroup'
            label = 'ItemDefinitionGroup'
            content = open_file(file_name)
            result = father_label(file_name, content, label)

            # 标签内容是VS2015对应的
            label2 = 'AdditionalIncludeDirectories'
            label3 = 'PreprocessorDefinitions'
            label4 = 'ClCompile'
            str_add = r'..\TeachingLab\;'
            # choose = input('请选择一处作为模板: ')
            template = son_label(result, label2, label3, str_add)
            write_file(file_name, template, content, result, label2, label3, label4)
    print("程序即将退出~~~")
    sleep(3)

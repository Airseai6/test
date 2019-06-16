#! python3
# -*- coding:utf-8 -*-

import re

'''
修改VS相关的项目配置文件应用MATLAB项目
'''


def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def father_label(content, label):
    # p1 = r"(?s)<PropertyGroup Condition.+?</PropertyGroup>"    # (?s)多行拼配
    # p1 = r"(?s)<ItemDefinitionGroup Condition.+?</ItemDefinitionGroup>"
    p1 = r"(?s)<%s Condition.+?</%s>" % (label, label)
    pattern1 = re.compile(p1)
    result = pattern1.findall(content)
    print("\n一共有%d处'%s'标签" % (len(result), label))

    p2 = r"(?<=(==')).+?(?=('))"
    pattern2 = re.compile(p2)
    for i in range(len(result)):
        matcher2 = re.search(pattern2, result[i])
        print("第%d处 -> " % (i+1), end='')
        print(matcher2.group(0))
    print('\n')
    return result


def son_label(result, label2, str_add):
    choose = input('请选择一处作为模板: ')
    try:
        num = int(choose) - 1
        content = result[num]
    except:
        print('输入有误！')
    p1 = r'(?<=<(%s)>).*(?=<\/\1>)' % label2
    pattern1 = re.compile(p1)
    matcher1 = re.search(pattern1, content)
    path = matcher1.group(0)
    print("\n正在添加:  %s" % str_add)
    new_content = content.replace(path, str_add + path)
    return [content, new_content]


def write_file(file_name, path):
    with open(file_name.replace('.vcxproj', '_new.vcxproj'), 'w', encoding='utf-8') as f:
        f.write(content.replace(path[0], path[1]))


if __name__ == '__main__':
    # file_name = 'test.vcxproj'
    file_name = 'Three_Phase_Inverter_V2017a.vcxproj'
    # label = 'PropertyGroup'
    label = 'ItemDefinitionGroup'
    content = open_file(file_name)
    result = father_label(content, label)

    label2 = 'AdditionalIncludeDirectories'
    str_add = r'..\TeachingLab\;'
    path = son_label(result, label2, str_add)
    write_file(file_name, path)

#! python3
# -*- coding:utf-8 -*-

import re
import os
from time import sleep

'''
修改VS相关的项目配置文件，以应用MATLAB项目2019-6-17
'''


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()


def file_names(str_add):
    pool = []
    for file_name in os.listdir():
        if file_name.endswith('.vcxproj') and '.bak.vcxproj' not in file_name:
            if str_add not in read_file(file_name):
                pool.append(file_name)
    return pool


def re_search(formula, content):
    pattern = re.compile(formula)
    matcher = re.search(pattern, content)
    return matcher.group(0)


def father_label(file_name, content, label):
    p1 = r"(?s)<%s Condition.+?</%s>" % (label, label)
    pattern1 = re.compile(p1)
    result = pattern1.findall(content)
    print("\n'%s'一共有%d处'%s'标签" % (file_name, len(result), label))

    p2 = r"(?<=(==')).+?(?=('))"
    for i in range(len(result)):
        print("第%d处 -> " % (i+1), end='')
        print(re_search(p2, result[i]))
    return result


def choose_label():
    flag = False
    num = 0
    choose = input('请选择一处作为模板: ')
    try:
        num = int(choose)
        flag = True
    except Exception as e:
        print('输入有误！' + str(e))
    return flag, num


def son_label(result, label2, label3, str_add, choose=2):
    content = result[choose-1]
    p1 = r'(?<=<(%s)>).*(?=<\/\1>)' % label2
    path = re_search(p1, content)
    print("\n正在将 %s 添加到第%d处路径内容~~~" % (str_add, choose))
    new_path = str_add + path

    p2 = r'(?<=<(%s)>).*(?=<\/\1>)' % label3
    macro_debug = re_search(p2, content)
    print("正在提取第%d处的宏定义~~~" % (choose))
    return [path, new_path, macro_debug]


def modify_content(template, content, result, label2, label3, label4, choose=2):
    print("正在修改其他%d处的内容~~~" % (len(result)-1))
    pool = [i for i in range(len(result))]
    pool.remove(choose-1)
    content = content.replace(template[0], template[1])
    for i in pool:
        p1 = r'(?s)(?<=<(%s)>).*(?=<\/\1>)' % label4
        son_content = re_search(p1, result[i])
        new_son_content = son_content + r"  <%s>%s</%s>" % (label2, template[1], label2) + '\n    '
        content = content.replace(son_content, new_son_content)

        p2 = r'(?<=<(%s)>).*(?=<\/\1>)' % label3
        macro = re_search(p2, result[i])
        if "$(Configuration)|$(Platform)'=='Debug|" in result[i]:
            content = content.replace(macro, template[2])
        else:
            macro_release = template[2].replace('_DEBUG', 'NDEBUG')
            content = content.replace(macro, macro_release)
    return content


def write_file(file_name, content, new_content):
    old_file_name = file_name.replace('.vcxproj', '.bak.vcxproj')
    new_file_name = file_name
    with open(old_file_name, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(new_file_name, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("'%s'修改完毕~~~" % file_name)


def main():
    print('请确保脚本与即将修改的*.vcxproj(VS2015)文件在同一目录下。')
    # 标签内容是VS2015对应的
    label = 'ItemDefinitionGroup'
    label2 = 'AdditionalIncludeDirectories'
    label3 = 'PreprocessorDefinitions'
    label4 = 'ClCompile'
    str_add = r'..\TeachingLab\;'

    for file_name in file_names(str_add):
        content = read_file(file_name)
        result = father_label(file_name, content, label)
        # ret, choose = choose_label()
        # if not ret:
        #     break
        # template = son_label(result, label2, label3, str_add, choose)
        # new_content = modify_content(template, content, result, label2, label3, label4, choose)
        template = son_label(result, label2, label3, str_add)
        new_content = modify_content(template, content, result, label2, label3, label4)
        write_file(file_name, content, new_content)
    print("程序即将退出~~~")
    sleep(3)


if __name__ == '__main__':
    main()


#! python3
# -*- coding:utf-8 -*-

import re
import os


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def file_names(str_sign):
    pool = []
    for file_name in os.listdir():
        if file_name.endswith('.f') or file_name.endswith('.for') or file_name.endswith('.FOR'):
            if str_sign in read_file(file_name):
                pool.append(file_name)
    return pool


def re_search(formula, content):
    pattern = re.compile(formula)
    matcher = re.search(pattern, content)
    return matcher.group(0)


def write_file(file_name, suffix, content):
    path = os.getcwd() + '\\NewFolder\\'
    file_name = path + file_name.replace('.', '_'+suffix+'.')
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    str_sign = 'Name:'
    for file_name in file_names(str_sign):
        content = read_file(file_name)
        # p1 = r'%s(.*)\n' % str_sign
        # p1 = r'(%s).*(\n)' % str_sign
        p1 = r'(?<=%s).*(\n)' % str_sign  # (?<=exp2)exp1 后顾
        pattern1 = re.compile(p1)
        result = re_search(pattern1, content)
        result = ''.join(result.split())
        print(result)
        write_file(file_name, result, content)
    print("程序即将退出~~~")


if __name__ == '__main__':
    main()

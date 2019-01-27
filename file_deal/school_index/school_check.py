#! python3
# -*- coding:utf-8 -*-


def rebuild(file_name):
    data = []
    with open(file_name, 'r', encoding='utf8')as f:
        # line = f.readlines()
        for line in f:
            # if '大学\n' in line or '学院\n' in line or'）\n' in line:
            if '院校位置：' in line:
                data.append(line)
        # print(data)
    with open(file_name.replace('.', '_new.'), 'w')as f:
        i =1
        for item in data:
            f.write(str(i) + '、 ' + item)
            i += 1


if __name__ == '__main__':
    file_name = 'gaokaopai.txt'
    rebuild(file_name)

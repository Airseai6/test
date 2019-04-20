#! python3
# -*- coding:utf-8 -*-

import re

def read_file(file_name):
    # write a str
    bank = []
    with open(file_name, 'r', encoding='utf-8') as f:
       for line in f:
           line = line.replace(' ', '').replace('	', '').replace('\n', '')
           bank.append(line)
    bank_str = ''.join(bank)
    # print(bank_str)
    # split a str
    # req = r"(\d+\.)\D"
    # result = re.findall(req, bank_str)
    # print(result)
    pool = []
    for i in range(52):
        print(bank_str.split(str(i + 1) + '.')[0])
        _data = bank_str.split(str(i + 1) + '.')
        pool.append(_data)
        # if quest != '':
        #     pool[i] = quest
        #     write_file(quest, i)
        bank_str = (str(i + 1) + '.').join(bank_str.split(str(i+1)+'.')[1:])
    pool = re.split(r"(\d+\.)\D", bank_str)
    print(pool)


def write_file(quest, num):
    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write(quest)


if __name__ == '__main__':
    file_name = 'bank.txt'
    read_file(file_name)
    # print(read_file(file_name))
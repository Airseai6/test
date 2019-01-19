#! python3
# -*- coding:utf-8 -*-
import numpy as np


def gen_str(wide, high):
    '''生成一个0与1构成的字符串'''
    myarray = np.random.randint(0, 2, (high, wide))
    l_str = ''
    for item in myarray:
        for cont in item:
            l_str += str(cont)
    # print(l_str)
    return l_str


def tetris_gui(l_str, wide, high):
    '''接收一个长串，转化为可视矩阵'''
    print('*'*(wide+2))
    for i in range(high):
        print('*', end='')
        for j in range(wide):
            if int(l_str[i*wide + j]) == 1:
                print('■', end='')
            else:
                print(' ', end='')
        print('*')
    print('*' * (wide + 2))


if __name__ == '__main__':
    tetris_gui(gen_str(10, 10), 10, 10)

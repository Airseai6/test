#! python3
# -*- coding:utf-8 -*-

from qrcode_test import gen_qrcode
from random import randint
from PIL import Image


def main():
    with open('LuckyDrawBox.txt', 'r', encoding='utf8')as f:
        data = f.readlines()
    flag = True
    records = []
    while flag:
        sign = input('Please input your sign! -->: ')
        index = randint(1, len(data))
        records.append(sign + ' --> ' + data[index-1])
        gen_qrcode(data[index-1])
        im = Image.open('qrcode_temp.png')
        im.show()

        data.pop(index-1)
        if len(data) == 0:
            break
    with open('records.txt', 'w')as f:
        i = 1
        for item in records:
            f.write(str(i) + '、 ' + item)
            i +=1
    print('抽奖箱已空！')


if __name__ == '__main__':
    main()
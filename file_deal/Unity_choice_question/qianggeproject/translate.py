#! python3
# -*- coding:utf-8 -*-


def translatexml():
    num = 1
    with open('finally.txt', 'r', encoding='utf-8') as f:
        for i in range(1, 52):
            first = f.readline()
            if '光伏' in first or '太阳能电池' in first:
                flag = False
            else:
                flag = True
            second = f.readline()
            third = f.readline()
            fourth = f.readline()
            fifth = f.readline()
            sixth = f.readline()

            if flag:
                file_name = './Examinations/Examination_' + str(num) + '.xml'
                num += 1
                with open(file_name, 'w', encoding='utf-8') as fp:
                    fp.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                    fp.write('<root>\n')
                    fp.write(first)
                    fp.write(second)
                    fp.write(third)
                    fp.write(fourth)
                    fp.write(fifth)
                    fp.write(sixth)
                    fp.write('</root>\n')


if __name__ == '__main__':
    translatexml()
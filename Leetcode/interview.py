#! python3
# -*- coding:utf-8 -*-


def func1(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[j] % 2 == 1 and a[i] % 2 == 0:
                a[i], a[j] = a[j], a[i]
    return a


def func2(v1, v2):
    v1 = v1.split('.')
    v2 = v2.split('.')
    l = min(len(v1), len(v2))
    for i in range(l):
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) < int(v2[i]):
            return -1
    return 0


def func3(n):
    for i in range(1, n+1):
        print(' '*(n-i), end='')
        for j in range(1, i+1):
            print('*', end='')
            print(' ', end='')
        print(' '*(n-i))


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    print(func1(a))
    v1 = "0.2"
    v2 = "0.1.4"
    print(func2(v1,v2))
    func3(4)
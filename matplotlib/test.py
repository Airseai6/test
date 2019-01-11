#! python3
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt


def test():
    squares = [1, 4, 9, 16, 25]
    plt.plot(squares, linewidth=5)
    plt.title('Square Nembers', fontsize=24)
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Square of Value', fontsize=14)
    plt.show()


if __name__ == '__main__':
    test()

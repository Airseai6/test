#! python3
# -*- coding:utf-8 -*-

import os
import cv2
import matplotlib.pyplot as plt


def deal(dirname):
    # 遍历工作目录下图片
    for filename in os.listdir(dirname):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            filepath = os.path.join(dirname, filename)
            img = cv2.imread(filepath)
            # 把图片转换为灰度图
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 获取灰度图矩阵的行数和列数
            r, c = gray_img.shape[:2]
            dark_sum = 0  # 偏暗的像素 初始化为0个
            dark_prop = 0  # 偏暗像素所占比例初始化为0
            piexs_sum = r * c  # 整个弧度图的像素个数为r*c

            # 遍历灰度图的所有像素
            for row in gray_img:
                for colum in row:
                    if colum < 50:  # 人为设置的超参数,表示0~39的灰度值为暗
                        dark_sum += 1
            dark_prop = dark_sum / (piexs_sum)
            print("dark_sum:" + str(dark_sum))
            print("piexs_sum:" + str(piexs_sum))
            print("dark_prop=dark_sum/piexs_sum:" + str(dark_prop))
            if dark_prop >= 0.5:  # 人为设置的超参数:表示若偏暗像素所占比例超过0.78,则这张图被认为整体环境黑暗的图片
                print(filepath + " is dark!")
            else:
                print(filepath + " is bright!")
            hist(filepath)


def hist(pic_path):
    img = cv2.imread(pic_path, 0)
    # hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.subplot(121)
    plt.imshow(img, 'gray')
    plt.xticks([])
    plt.yticks([])
    plt.title("Original")
    plt.subplot(122)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()


if __name__ == '__main__':
    dirname =os.getcwd()
    deal(dirname)

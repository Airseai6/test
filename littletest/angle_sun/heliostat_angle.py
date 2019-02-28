#! python3
# -*- coding:utf-8 -*-
import math


def location2tower(H, X, Y):
    """
    求取位置坐标相对于塔的高度角，与方位角（南方向为0，向西为正）
    中央接收器坐标（0， 0， H）
    位置坐标（X， Y， 0）
    x：北； y：东； z:天顶。
    :param H: 中央接收器相对镜面中心的高度
    :param X: 镜场中一位置相对塔底南北方向坐标（北为正，南为负），注意：是距离（m）,不是个数。
    :param Y: 镜场中一位置相对塔底东西方向坐标（东为正，西为负）
    :return:
    """
    high_angle = math.atan(H/(math.sqrt(X*X+Y*Y)))

    if X<0<Y:
        position_angle = math.atan(-X/Y) + math.pi/2
    if X>0 and Y>0:
        position_angle = math.atan(X/Y)
    if Y<0<X:
        position_angle = 0 - math.atan(-X/Y)
    if X<0 and Y<0:
        position_angle = 0 - math.atan(X/Y) - math.pi/2

    high_angle = high_angle/math.pi*180.0
    position_angle = position_angle/math.pi*180.0

    return high_angle, position_angle


def

if __name__ == '__main__':
    print(location2tower(250, 500, 500))

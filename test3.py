#! python
# -*- coding:utf-8 -*-

import time
import datetime
from math import *

#print "====== Sun Angle ======"

def hours(t):
    return t.hour + t.minute / 60.0 + t.second / 3600.0

def show_radians(r):
    if r < 0:
        flag = True
    else:
        flag = False
    r = abs(r)
    seconds = r * 3600
    hours = int(seconds / 3600)
    minutes = int(seconds % 3600 / 60)
    seconds = int(seconds % 60)
    s = u"%d°%d′%d″"%(hours, minutes, seconds)
    if flag:
        s = "-" + s
    return s

def get_radians(s):
    if s[0] == "-":
        flag = True
    else:
        flag = False
    s = s.replace(u"°", u"|").replace(u"′", u"|").replace(u"″", u"|").replace(u"'", u"|").replace(u'"', u"|")
    s = s.split(u"|")
    if len(s) > 2:
        hours = abs(int(s[0]))
        minutes = int(s[1])
        seconds = int(s[2])
    else:
        hours = abs(float(s[0]))
        minutes = 0
        seconds = 0
    r = hours + minutes / 60.0 + seconds / 3600.0
    if flag:
        r = 0 - r
    return r


def show_time(t):
    return t.strftime("%Y-%m-%d %H:%M:%S")


def get_sun(E, N, now=None):

    print('东经： ', E)
    print('北纬： ', N)
    print('现在时间： ', show_time(now))

    E = get_radians(E)
    N = get_radians(N)
    if not now:
        now = datetime.datetime.now()

    n = int(now.strftime("%j"))

    A = [0.00020870, 0.0092869, -0.052258, -0.0013077, -0.0021867, -0.00015100]
    B = [0, -0.12229, -0.15698, -0.0051602, -0.0029823, -0.00023463]
    eot = [0, 0, 0, 0, 0, 0]
    for k in range(1, 6):
        eot[k-1]=A[k-1] * cos(2*pi*(k-1)*n/365.25)+B[k-1]*sin(2*pi*(k-1)*n/365.25)
    eot2 = sum(eot)
    # print "eot2:", eot2


    t_ping = now + datetime.timedelta(minutes=4*(E-120))
    #print show_time(t_ping)

    t_zhen = t_ping + datetime.timedelta(hours=eot2)
    #print show_time(t_zhen)

    t_bei = hours(now)
    t_delta = hours(t_zhen)
    t_wei = 12 * (E - 120) / 180.0
    #print t_bei, t_delta, t_wei

    #t = (t_bei + t_delta + t_wei) * 180 / 12.0 - 180
    t = (t_delta-12) * 15
    #print t

    b = 23.45 * sin(2 * pi * (284 + n) / 365.0)
    #print b


    sin_a = sin(radians(N)) * sin(radians(b)) + cos(radians(N)) * cos(radians(b)) * cos(radians(t))
    #print sin_a

    a = asin(sin_a)
    a = a * 180.0 / pi

    tan_m = tan(radians(b)) / cos(radians(t))
    m = atan(tan_m)
    m = m * 180.0 / pi

    # tan_c = 0 - tan(radians(b)) * cos(radians(m)) * 1.0 / sin(radians(m-N))
    # c = atan(tan_c)
    # c = c * 180.0 / pi

    sin_c = cos(radians(b)) * sin(radians(t)) / cos(radians(a))
    c = asin(sin_c)
    c = c * 180.0 / pi

    # if m < N:
    #     c = c + 180
    # else:
    #     if t > 0:
    #         c = c + 360
    # print c

    if t > 90:
        c = 360 - c
    else:
        c = 180 + c


    a = u"%.3f°" % a
    c = u"%.3f°" % c

    return (a, c)


if __name__ == "__main__":
    E = u"110°18′21″"
    N = u"25°19′41″"
    # now = time.strptime("2014-08-11 10:50:00", "%Y-%m-%d %H:%M:%S")
    # now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    now = time.localtime(time.time())
    print(now)
    # E = u"153°10′8″"
    # N = u"55°10′8″"
    # now = time.strptime("2014-08-13 16:10:53", "%Y-%m-%d %H:%M:%S")

    now = datetime.datetime.fromtimestamp(time.mktime(now))
    print(now)
    a, c = get_sun(E, N, now)

    # print "================"
    print(a, c)

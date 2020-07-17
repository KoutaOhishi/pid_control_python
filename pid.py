# coding:utf-8
# python3.8
import math
import numpy as np

from matplotlib import pyplot as plt
from numpy.random import *

"""
Mn = Mn-1 + Kp*(en-en-1) + Ki*en + Kd*((en-en-1) - (en-1-en-2))

Mn : 操作量
en : 偏差
Kp : 比例制御（P)の比例定数
Ki : 積分制御（I)の比例定数
Kd : 微分制御（D)の比例定数

pi = math.pi

x = np.linspace(0, 2*pi, 100)
y = np.sin(x)

pyplot.plot(x, y)
pyplot.show()
"""

def main():
    M = 1.00
    M1 =  0.00

    e = 0.00
    e1 = 0.00
    e2 = 0.00

    Kp = Ki = Kd = 0.1

    t = 100

    goal = 50.00

    x_list = []
    y_list = []

    x_list.append(0)
    y_list.append(0.00)

    for i in range(1,t):
        M1 = M
        e2 = e1
        e1 = e
        e = goal - y_list[i-1]

        M = M1 + Kp * (e-e1) + Ki * e + Kd * ((e-e1) - (e1-e2))

        y_list.append(M)
        x_list.append(i)

    plt.hlines([goal], 0, t, "red", linestyles='dashed')
    plt.plot(x_list, y_list, color="b")
    plt.ylim(0, goal*2)
    plt.show()

if __name__ == "__main__":
    main()

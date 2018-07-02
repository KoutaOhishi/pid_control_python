#coding:utf-8
import math
import numpy as np

from sympy import *
from matplotlib import pyplot as plt
from numpy.random import *

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
        rand = randint(10) #0~9の中からランダムに１つの数を抽出

        M1 = M
        e1 = e
        e2 = e1

        if rand == 5 or rand == 7 or rand == 3:
            noize = randint(-30, 30) / 10
            e = goal - y_list[i-1] + noize

        elif rand == 9:
            noize = randint(-100, 100) / 10
            e = goal - y_list[i-1] + noize

        else:
            e = goal - y_list[i-1]

        M = M1 + Kp * (e-e1) + Ki * e + Kd * ((e-e1) - (e1-e2))
        y_list.append(M)
        x_list.append(i)

    plt.plot(x_list, y_list)
    plt.ylim(0, goal*2)
    plt.show()

if __name__ == "__main__":
    main()

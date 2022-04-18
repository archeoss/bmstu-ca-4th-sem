import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pylab import mpl
import math
import matplotlib.pyplot as plt
import os
from .basic_func import *
from .approxSingle import *

def polynomial_fitting_2(power, data_x, data_y, data_z, weight):
    matrix = []
    vector = []

    # matrix[0].append(sum(weight))
    # for j in range(1, power + 1):
    #     matrix[0].append(sum(weight * data_x ** (j)))
    #     matrix[0].append(sum(weight * data_y ** (j)))
    # vector.append(sum(data_z * weight))
    # for i in range(1, power * 2 + 1):
    #     matrix.append([])
    #     if i % 2:
    #         matrix[i].append(sum(weight * data_x ** ((i + 1)// 2)))
    #         for j in range(1, power + 1):
    #             matrix[i].append(sum(weight * data_x ** ((i + 1)// 2 + j)))
    #             matrix[i].append(sum(weight * data_y ** j * data_x ** ((i + 1)// 2)))
    #             print('x^%d, x^%d*y^%d,' % ((i + 1)// 2 + j, (i + 1)// 2, j), end='')
    #         vector.append(sum(data_z * weight * (data_x ** ((i + 1)// 2))))
    #         print("z*x^%d" % ((i + 1)// 2))
    #     else:
    #         matrix[i].append(sum(weight * data_y ** ((i + 1)// 2)))
    #         for j in range(1, power+1):
    #             matrix[i].append(sum(weight * data_x ** j * data_y ** ((i + 1)// 2)))
    #             matrix[i].append(sum(weight * data_y ** ((i + 1)// 2 + j)))
    #             print('y^%d, y^%d*x^%d,' % ((i + 1)// 2 + j, (i + 1)// 2, j), end='')
    #         vector.append(sum(data_z * weight * (data_y ** ((i + 1)// 2))))
    #         print("z*y^%d" % ((i + 1)// 2))
    #     print( (i + 1)// 2)

    # for i in range(power + 1):
    #     for j in range(power  + 1 - i):
    #         matrix[0].append(sum(weight * (data_x ** (i) * data_y ** (j))))
    #         print("x^%d, y^%d;" % ( i, j))
    # vector.append(sum(data_z * weight))
    # for k in range(1, power + 1):
    #     matrix.append([])
    #     print("1")
    #     for i in range(power + 1):
    #         for j in range(power  + 1 - i):
    #             matrix[k].append(sum(weight * (data_x ** (i + (k)) * data_y ** (j))))
    #             print("x^%d, y^%d;" % ( i + (k), j))
        # vector.append(sum(data_z * weight * (data_x ** ((k + 1)// 2))))
        # print("z*x^%d" % ((i + 1)// 2))
    d = 0
    for p in range(power + 1):
        for k in range(power + 1 - p):
            matrix.append([])
            print("2")
            for i in range(power + 1):
                for j in range(power  + 1 - i):
                    matrix[d].append(sum(weight * (data_x ** (i + p) * data_y ** (j + (k)))))
                    print("x^%d, y^%d;" % ( i + p, j + (k)))
            vector.append(sum(data_z * weight * data_y ** k * data_x ** p))
            d+=1
            print(p, k)
    #         
        # print("z*x^%d" % ((i + 1)// 2))
        # vector.append(sum(data_z * weight * (data_y ** ((k + 1)// 2))))
        # print("z*y^%d" % ((i + 1)// 2))
        # print( (i + 1)// 2)
    # print()
    # for i in range(power + 1):
    #     for j in range(power  + 1 - i):
    #         vector.append(sum(data_z * weight * data_y ** j * data_x ** i))
    #         print("x^%d, y^%d;" % ( i, j))
    for i in matrix:
        print(i)
    print((vector), 'kkk')
    # print(sum(data_x))
    vector = np.array(vector)
    vector = vector.reshape(len(vector), 1)
    matrix = np.matrix(matrix)
    # try:
    for i in matrix:
        print(i)
    print((vector), 'kkk')
    m = np.array((matrix ** (-1)) * vector)
    # except:
    #     m = vector.reshape(1, len(vector))[0]

    print(m, 'ddd')

    return m

def calculate_y(args_x, parameters):
    res = 0
    for i in range(len(parameters)):
        # print (parameters[i], len(args_x))
        res += parameters[i] * (args_x ** i)

    return res
def calculate_z(power, x_const, args_y, parameters):
    res = 0
    # for i in range(1, len(parameters), 2):
    #     # print(parameters[i])
    #     res += parameters[i + 1] * args_y ** ((i + 1) // 2 ) + parameters[i] * x_const ** ((i + 1) // 2)
    #     print(res[0])
    print(parameters)
    k = 0
    for i in range(power + 1):
        for j in range(power + 1 - i):
            res += parameters[k] * x_const ** i * args_y ** j
            k += 1
            print("x^%d, y^%d;" % ( i, j))
    # res += parameters[0]
    return res
 
def calculate_z_2(power, args_x, const_y, parameters):
    res = 0
    # for i in range(1, len(parameters), 2):
    #     # print(parameters[i])
    #     res += parameters[i + 1] * const_y ** ((i + 1) // 2 ) + parameters[i] * args_x ** ((i + 1) // 2)
    #     # print(res[0])
    k = 0
    for i in range(power + 1):
        for j in range(power + 1 - i):
            res += parameters[k] * args_x ** i * const_y ** j
            k += 1
    # res += parameters[0]
    return res
 
""" 
Полный функциональный чертеж
"""

 
def f(n, x, y, z, weight):
    # for w in parameters:
        # print(w)

    # plt.title ("Двумерная апроксимация")
    colors = ['r', 'g', 'b', 'c', 'yellow', 'orange', 'purple', 'black']
    fig = plt.figure()
        # Создайте объект Axes3D и позвольте ему содержать трехмерные координаты изображения
    ax = Axes3D(fig)
    ax.scatter(x, y, z, color='b')
    for power in range(n, n + 1):
        data_x = np.linspace(min(x), max(x), 25)
        data_y = np.linspace(min(y), max(y), 25)
        # data_y = calculate(data_x, parameters)
        parameters = polynomial_fitting_2(power, x, y, z, weight)
        # print(len(data_x), len(data_y))
        for cur_x in data_x:
            data_z = calculate_z(power, cur_x, data_y, parameters)
        # print(data_x, data_y, data_z)
            t = np.array([cur_x] * 25)
            ax.plot(t, data_y, data_z, color='r')
        for cur_y in data_y:
            data_z = calculate_z_2(power, data_x, cur_y, parameters)
        # print(data_x, data_y, data_z)
            t = np.array([cur_y] * 25)
            ax.plot(data_x, t, data_z, color='r')
            
    plt.title ("Данные подгонки полинома с одной переменной")

    plt.legend(loc="upper left")
    plt.show()

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from .approxSingle import *

def polynomial_fitting_2(power, data_x, data_y, data_z, weight):
    matrix = []
    vector = []

    d = 0
    for p in range(power + 1):
        for k in range(power + 1 - p):
            matrix.append([])
            for i in range(power + 1):
                for j in range(power  + 1 - i):
                    matrix[d].append(sum(weight * (data_x ** (i + p) * data_y ** (j + (k)))))
            vector.append(sum(data_z * weight * data_y ** k * data_x ** p))
            d+=1
    vector = np.array(vector)
    vector = vector.reshape(len(vector), 1)
    matrix = np.matrix(matrix)
    m = np.array((matrix ** (-1)) * vector)

    return m

def calculate_z(power, x_const, args_y, parameters):
    res = 0

    k = 0
    for i in range(power + 1):
        for j in range(power + 1 - i):
            res += parameters[k] * x_const ** i * args_y ** j
            k += 1

    return res
 
def calculate_z_2(power, args_x, const_y, parameters):
    res = 0
    k = 0
    for i in range(power + 1):
        for j in range(power + 1 - i):
            res += parameters[k] * args_x ** i * const_y ** j
            k += 1
    return res
 
""" 
Полный функциональный чертеж
"""

 
def f(n, x, y, z, weight):

    plt.title ("Двумерная апроксимация")
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z, color='b')
    for power in range(n, n + 1):
        data_x = np.linspace(min(x), max(x), 25)
        data_y = np.linspace(min(y), max(y), 25)
        parameters = polynomial_fitting_2(power, x, y, z, weight)
        for cur_x in data_x:
            data_z = calculate_z(power, cur_x, data_y, parameters)
            t = np.array([cur_x] * 25)
            ax.plot(t, data_y, data_z, color='r')

        for cur_y in data_y:
            data_z = calculate_z_2(power, data_x, cur_y, parameters)
            t = np.array([cur_y] * 25)
            ax.plot(data_x, t, data_z, color='r')
            
    plt.show()

import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import math
from .basic_func import *

def polynomial_fitting(power, data_x, data_y, weight):
    matrix = []
    vector = []
    for i in range(power + 1):
        matrix.append([])
        for j in range(power + 1):
            matrix[i].append(sum(weight * data_x ** (i + j)))
        vector.append(sum(data_y * weight * (data_x ** i)))

    vector = np.array(vector)
    vector = vector.reshape(len(vector), 1)
    matrix = np.matrix(matrix)
    m = np.array((matrix ** (-1)) * vector)
    
    return m

def calculate(args_x, parameters):
    res = 0
    for i in range(len(parameters)):
        res += parameters[i]*(args_x**i)

    return res
 
""" 
Полный функциональный чертеж
"""

 
def f2(n, x, y, weight):
    # for w in parameters:
        # print(w)

    plt.title ("Одномерная апроксимация")
    colors = ['r', 'g', 'b', 'c', 'yellow', 'orange', 'purple', 'black']
    for power in range(1, n + 1):
        parameters = polynomial_fitting(power, x, y, weight)
        data_x = np.linspace(min(x), max(x), 25)
        data_y = calculate(data_x, parameters)
        plt.plot (data_x, data_y, label = "n = %d" % power, color=colors[power])
    plt.scatter (x, y, label = "дискретные данные")
            
    plt.title ("Данные подгонки полинома с одной переменной")

    plt.legend(loc="upper left")
    plt.show()
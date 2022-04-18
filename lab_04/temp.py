import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import math

def polynomial_fitting(power, data_x, data_y, weight):
    matrix = []
    vector = []
    for i in range(power + 1):
        matrix.append([])
        for j in range(power + 1):
            matrix[i].append(sum(weight * data_x ** (i + j)))
        vector.append([data_y[i] * weight[i] * (data_x[i] ** i)])
    
    print(matrix)
    print(vector)
    vector = np.array(vector)
    matrix = np.matrix(matrix)
    m = np.array((matrix ** (-1)) * vector)
    
    print(m)
    m = m[::-1]
        
    return m

def calculate(data_x, parameters, power):
    datay=[]
    for x in data_x:
        cur_x = 1
        data = 0
        for i in range(1, power + 2):
            data += parameters[-i] * cur_x
            cur_x *= x
        datay.append(data)
    return datay
 
 
 
""" 
Полный функциональный чертеж
"""

def draw(data_x,data_y_new,data_y_old, x):
    plt.plot (data_x, data_y_new, label = "подгоночная кривая", color = "black")
    plt.scatter (x, data_y_old, label = "дискретные данные")
    
    plt.title ("Данные подгонки полинома с одной переменной")
    plt.legend(loc="upper left")
    plt.show()
 
def f2(n, x, y, weight):
    parameters = polynomial_fitting(n, x, y, weight)
    # for w in parameters:
        # print(w)

    data_x = np.linspace(min(x), max(x), 100)
    newData=calculate(data_x, parameters, n)
    print(len(newData), len(data_x))
    draw(data_x,newData,y, x)
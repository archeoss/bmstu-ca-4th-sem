from .table import Table
import numpy as np
from .newtone import *
from math import sqrt

def splineInterpolation(table : Table, x : float, type : int):
    steps = table.x[1:] - table.x[:-1]
    steps_matr = []
    for i in range(table.rows):
        steps_matr.append([])
        for j in range(table.rows):
            steps_matr[i].append(0)
    for i in range(1, table.rows -1):
        steps_matr[i][i] = 2 * (steps[i] + steps[i - 1])
        steps_matr[i - 1][i] = steps[i - 1]
        steps_matr[i][i - 1] = steps[i - 1]
        

    steps_matr[-2][-1] = steps[-1]
    steps_matr[-1][-2] = steps[-1]
    steps_matr[-1][-1] = steps[-1] * 2
    steps_matr[0][0] = steps[0] * 2
    
    steps_matr = np.matrix(steps_matr)
    
    func_matr = np.zeros(table.rows)
    for i in range(1, table.rows - 1):
        func_matr[i] = (table.y[i + 1] - table.y[i]) / steps[i] - (table.y[i] - table.y[i - 1]) / steps[i - 1]
    
    func_matr = func_matr.reshape(table.rows, 1)
    func_matr *= 3

    if type == 2:
        func_matr[0] = NewtonforSpline(3, table.x[:4], table.y[:4], table.x[0], (0, 3))
    if type == 3:
        func_matr[0] = NewtonforSpline(3, table.x[:4], table.y[:4], table.x[0], (0, 3))
        func_matr[-1] = NewtonforSpline(3, table.x[-4:], table.y[-4:], table.x[-1], (0, 3))
    
    m = np.array((steps_matr ** (-1)) * func_matr)
    m_copy = []
    [m_copy.append(x[0]) for x in m]
    m = np.array(m_copy)

    a_s = table.y[:-1]
    b_s = np.array((table.y[1:] - table.y[:-1]) / steps - steps * (m[1:] + 2 * m[:-1]) / 3)
    c_s = m[:]
    d_s = np.array((m[1:] - m[:-1]) / (3 * steps))

    i = 0
    if x != table.x[0]:
        if x > table.x[0]:
            while i + 1 < table.rows and x >= table.x[i + 1]:
                i += 1
        else:
            while i + 1 < table.rows and x <= table.x[i + 1]:
                i += 1
    
    i = max(0, i)
    i = min(table.rows - 2, i)
    result = a_s[i] + b_s[i] * (x - table.x[i]) + c_s[i] * (x - table.x[i]) ** 2 + d_s[i] * (x - table.x[i]) ** 3

    return result


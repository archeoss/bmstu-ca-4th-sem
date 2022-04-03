from .basic_func import *
from .table import *
from math import factorial
def NewtonforSpline(power, arg_array, func_array, arg, interval):
    polynom_table = []
    for i in range(1, power + 1):
        fill_polynom(polynom_table, i, arg_array, func_array, interval)
    idx_start, idx_end = interval
    diffs = []
    polynom_result = (polynom_table[1][0]) + (arg - arg_array[idx_start] + arg - arg_array[idx_start + 1] + arg - arg_array[idx_start + 2]) * polynom_table[2][0]
    # polynom_result = 0
    # for k in range(der - 1, len(polynom_table)):
    #     cur = 0
    #     for j in range(k):
    #         cur_t = 1
    #         for i in range(idx_start, idx_end + 1):
    #             cur_t *= arg - arg_array[i]
    #     #        print(cur_t)
    #         cur += cur_t
    #     #    print(cur)
    #     cur = polynom_table[k][0] * cur
    #     polynom_result += cur
    #     #print(polynom_result, cur, cur_t)
    return polynom_result * 2


'''
    Код из Первой лабы, чуть измененный
'''

EPS = 1e-5
def NewtonePolynom(power, arg_array, func_array, arg, interval):
    '''
        Интерполяционный полином Ньютона
    '''
    polynom_table = []
    for i in range(1, power + 1):
        fill_polynom(polynom_table, i, arg_array, func_array, interval)
    idx_start, idx_end = interval
    diffs = []
    cur = 1
    for i in range(idx_start, idx_end + 1):
        cur *= arg - arg_array[i]
        diffs.append(cur)
    polynom_result = func_array[idx_start]
    for i in range(power):
        cur = polynom_table[i][0] * diffs[i]
        polynom_result += cur

    return polynom_result

def fill_polynom(polynoms, power, arg_array, func_array, interval):
    '''
        Заполнение таблицы разделенных разностей
    '''
    if power < 1:
        return
    polynoms.append([])
    idx_start, idx_end = interval
    if power == 1:
        for i in range(idx_start, idx_end):
            polynoms[0].append((func_array[i + 1] - func_array[i])/(arg_array[i+1] - arg_array[i]))
    else:
        for i in range(len(polynoms[power - 2]) - 1):
            polynoms[power - 1].append((polynoms[power - 2][i + 1] - polynoms[power - 2][i])/(arg_array[idx_start + i + power] - arg_array[idx_start + i]))

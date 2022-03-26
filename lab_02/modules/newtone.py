from .basic_func import *
from .table import *

def TriInterpolation_Newtone(args_xyz, table : Table, x_array, y_array, z_array, coefs):
    '''
        Трехмерная интерполяция по Ньютону
    '''
    x, y, z = args_xyz
    res = 0
    kx, ky, kz = coefs
    x_polynom = []
    for z_end in range(len(z_array)):
        y_polynom = []
        for x_end in range(len(x_array)):
            tmp = NewtonePolynom(ky, table.y[z_array[z_end]], table.subtables[z_array[z_end]][x_array[x_end]], y, (y_array[0], y_array[-1]))
            y_polynom.append(tmp)
        tmp = NewtonePolynom(kx, table.x[z_array[z_end]][x_array[0]:x_array[x_end] + 1], y_polynom, x, (0, len(y_polynom) - 1))
        x_polynom.append(tmp)
        
    tmp = NewtonePolynom(kz, table.z[z_array[0]:z_array[z_end] + 1], x_polynom, z, (0, z_end))
    res = tmp

    return res


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

from .basic_func import *
from .table import *
import numpy as np

EPS = 1e-5

def NewtonePolynom(power, table, arg, nodes_used):
    '''
        Интерполяционный полином Ньютона
    '''    
    interval = find_interval(table, power, arg)
    polynom_table = []
    for i in range(1, power + 1):
        fill_polynom(polynom_table, i, table, interval)
    idx_start, idx_end = interval
    diffs = []
    cur = 1
    for i in range(idx_start, idx_end + 1):
        cur *= arg - table.x[i]
        nodes_used.append(table.x[i])
        diffs.append(cur)
    polynom_result = table.y[idx_start]
    for i in range(power):
        cur = polynom_table[i][0] * diffs[i]
        polynom_result += cur

    return polynom_result

def fill_polynom(polynoms, power, table, interval):
    '''
        Заполнение таблицы разделенных разностей
    '''
    if power < 1:
        return

    polynoms.append([])
    idx_start, idx_end = interval
#    print(polynoms)
    if power == 1:
        for i in range(idx_start, idx_end):
            polynoms[0].append((table.y[i + 1] - table.y[i])/(table.x[i+1] - table.x[i]))
    else:
        for i in range(len(polynoms[power - 2]) - 1):
            polynoms[power - 1].append((polynoms[power - 2][i + 1] - polynoms[power - 2][i])/(table.x[idx_start + i + power] - table.x[idx_start + i]))


def bin_search(xs, ys):
    for i in range(len(xs)-1):
        x_0 = xs[i]
        x_1 = xs[i + 1]
        y_0 = ys[i]
        y_1 = ys[i+1]
        if y_0 * y_1 <= 0:
            x_at_zero = (-y_0) * (x_1-x_0)/(y_1-y_0) + x_0
            if xs.min() <= x_at_zero <= xs.max():
                return x_at_zero
    return None

def BackwardNewtonePolynom(power, table, arg):
    '''
        Интерполяционный полином Ньютона
    '''    
    nodes_used = []
    result = NewtonePolynom(power, table, arg, nodes_used)

    if not min(table.y) < result < max(table.y):
        new_xs = np.linspace(min(table.x), max(table.x), 100)
        new_ys = []
        for new_x in new_xs:
            new_y = NewtonePolynom(power, table, new_x, nodes_used)
            new_ys.append(new_y)
        new_ys = np.array(new_ys)
        result = bin_search(new_xs, new_ys)
    return result


# def bullshitIntorpolation(table, power, arg):
#     l = table.x[0]
#     i = 0
#     while (l * table.x[i] >= 0):
#         i += 1

#     r = table.x[i]
#     if (l == r):
#         return 'NO ROOT!'
#     else:
#         while(abs(l - r) > EPS):
#             mid = (l + r) / 2
#             nodes_used = []
#             new = NewtonePolynom(power, table, mid, nodes_used)

#             if (new > 0):
#                 r = mid
#             else:
#                 l = mid
        
#         return l
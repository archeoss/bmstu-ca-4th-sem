from basic_func import *

def NewtonPolynom(power, table, interval, arg):
    polynom_table = []
    for i in range(1, power + 1):
        fill_polynom(polynom_table, i, table, interval)
    idx_start, idx_end = interval
    diffs = []
    cur = 1
    for i in range(idx_start, idx_end + 1):
        cur *= arg - table.x[i]
        diffs.append(cur)
    polynom_result = table.y[idx_start]
    for i in range(power):
        cur = polynom_table[i][0] * diffs[i]
        polynom_result += cur

    return polynom_result

def fill_polynom(polynoms, power, table, interval):
    if power < 1:
        return

    polynoms.append([])
    idx_start, idx_end = interval
    if power == 1:
        for i in range(idx_start, idx_end):
            polynoms[0].append((table.y[i + 1] - table.y[i])/(table.x[i+1] - table.x[i]))
    else:
        for i in range(len(polynoms[power - 2]) - 1):
            polynoms[power - 1].append((polynoms[power - 2][i + 1] - polynoms[power - 2][i])/(table.x[idx_start + i + power] - table.x[idx_start + i]))

from .basic_func import *

def HermitePolynom(power, table, x, nodes_used):
    '''
        Интерполяционный полином Эрмита
    '''
    idx_start, idx_end = find_interval(table, (power) // 2, x)
    result_polynom = table.y[idx_start]
    idxs = [idx_start]
    new_idx = idx_start
    cur = 1
    for i in range(power):
        idxs.append(new_idx)
        cur *= (x - table.x[new_idx - i % 2])
        nodes_used.append(table.x[new_idx - i % 2])
        result_polynom += NewtonForHermite(table, idxs)*cur
        new_idx += (i + 1) % 2

    return result_polynom

def NewtonForHermite(table, idxs):
    '''
        Вычисление полинома Ньютона по узлам для интерполяционного полинома Эрмита
    '''
    if len(idxs) == 2:
        if idxs[0] == idxs[1]:
            return table.first_derivative[idxs[0]]
        else:
            return (table.y[idxs[0]] - table.y[idxs[1]])/(table.x[idxs[0]] - table.x[idxs[1]])
    else:
        return (NewtonForHermite(table, idxs[:-1]) - NewtonForHermite(table, idxs[1:]))/(table.x[idxs[0]] - table.x[idxs[-1]])

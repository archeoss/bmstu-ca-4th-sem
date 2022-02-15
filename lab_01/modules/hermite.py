from basic_func import *

def HermitePolynom(power, table, x):
    idx_start, idx_end = find_interval(table, (power) // 2, x)
    result_polynom = table.y[idx_start]
    idxs = [idx_start]
    new_idx = idx_start
    for i in range(power):
        new_idx += i % 2
        idxs.append(new_idx)
        result_polynom += NewtonForHermite(table, idxs)*(x - table.x[new_idx])

    return result_polynom

def NewtonForHermite(table, idxs):
    if len(idxs) == 2:
        if idxs[0] == idxs[1]:
            return table.first_derivative[idxs[0]]
        else:
            return (table.y[idxs[1]] - table.y[idxs[0]])/(table.x[idxs[1]] - table.x[idxs[0]])
    else:
        return (NewtonForHermite(table, idxs[:-1]) - NewtonForHermite(table, idxs[1:]))/(table.x[idxs[0]] - table.x[idxs[-1]])

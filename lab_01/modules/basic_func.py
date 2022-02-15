def find_interval(table, power, arg):
    '''
        Возвращает начальный и конечный индексы, наиболее близких к аргументу
    '''
    idx = idx_start = idx_end = 0
    
    while idx < table.rows and table.x[idx] < arg:
        idx += 1
    
    if idx == table.rows:
        idx_end = idx - 1
        idx_start = idx_end - power
    elif idx == 0:
        idx_end = power
    else:
        idx_end = min(table.rows - 1, idx + power // 2)
        idx_start = max(idx_end - power, 0)
        if idx_end - idx_start != power:
            idx_end = idx_start + power

    return (idx_start, idx_end)

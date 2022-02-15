def find_interval(table, power, arg):
    '''
        Возвращает начальный и конечный индексы, наиболее близких к аргументу
    '''
    idx = idx_start = idx_end = 1
    
    while idx < table.rows and not table.x[idx] <= arg <= table.x[idx-1] and not table.x[idx] >= arg >= table.x[idx-1]:
        idx += 1
    
    if idx == table.rows:
        if (arg >= table.x[0] >= table.x[1] or arg <= table.x[0] <= table.x[1]):
            idx_start = 0
            idx_end = power
        else:
            idx_end = idx - 1
            idx_start = idx_end - power
    else:
        idx_end = min(table.rows - 1, idx + power // 2)
        idx_start = max(idx_end - power, 0)
        if idx_end - idx_start != power:
            idx_end = idx_start + power

    return (idx_start, idx_end)

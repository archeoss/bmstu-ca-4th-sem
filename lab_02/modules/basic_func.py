def find_interval(array, power : int, arg : float, rows):
    '''
        Возвращает начальный и конечный индексы, наиболее близких к аргументу
    '''
    idx = idx_start = idx_end = 1
    while idx < rows and not array[idx] <= arg <= array[idx-1] and not array[idx] >= arg >= array[idx-1]:
        idx += 1

    if idx == rows:
        if (arg >= array[0] >= array[1] or arg <= array[0] <= array[1]):
            idx_start = 0
            idx_end = power
        else:
            idx_end = idx - 1
            idx_start = idx_end - power
    else:
        idx_end = min(rows - 1, idx + power // 2)
        idx_start = max(idx_end - power, 0)
        if idx_end - idx_start != power:
            idx_end = idx_start + power
    
    return (int(idx_start), int(idx_end))

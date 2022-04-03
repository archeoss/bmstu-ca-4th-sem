from .table import Table

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

def sort_table(table : Table):
    for i in range(table.rows):
        for j in range(table.rows - i - 1):
            if table.x[j] > table.x[j + 1]:
               table.x[j], table.x[j + 1] = table.x[j + 1], table.x[j]
               table.y[j], table.y[j + 1] = table.y[j + 1], table.y[j]

def get_idxs(n : int):
    idxs = []
    i = 0
    while n > 0:
        if n % 2:
            idxs.append(i)
        i += 1
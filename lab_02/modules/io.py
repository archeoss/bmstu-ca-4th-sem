from .table import Table
import numpy as np
def func(x, y, z):
    return np.exp(2 * x - y) * (z ** 2)

def make_table(filename : str, x_inter : tuple[2], y_inter : tuple[2], z_inter : tuple[2], steps : tuple[3]):
    x_step, y_step, z_step = steps
    x_start, x_end = x_inter
    y_start, y_end = y_inter
    z_start, z_end = z_inter
    
    f = open(filename, "w")
    
    z_incr = (z_end - z_start) / (z_step - 1)
    x_incr = (x_end - x_start) / (x_step - 1)
    y_incr = (y_end - y_start) / (y_step - 1)
    
    z = z_start
    for i in range(z_step):
        f.write('%f\n' % z)
        y = y_start
        for j in range(y_step):
            f.write('%f ' % y)
            y += y_incr
        f.write('\n')
        x = x_start
        for j in range(x_step):
            y = y_start
            f.write('%f ' % x)
            for k in range(y_step):
                f.write('%f ' % func(x, y, z))
                y += y_incr
            f.write('\n')
            x += x_incr
        z += z_incr
        f.write('\n')

def input_float():
    '''
        Ввод числа типа float
    '''
    flag = True
    while flag:
        x = input("Input float: ")
        try:
            x = float(x)
            flag = False
        except:
            print("Error! Try again...")
    
    return x

def input_int():
    '''
        Ввод числа типа float
    '''
    flag = True
    while flag:
        x = input("Input int: ")
        try:
            x = int(x)
            flag = False
        except:
            print("Error! Try again...")
    
    return x

def input_xyz(message : str):
    print(message)
    return (input_float(), input_float(), input_float())

def input_coefs(message : str):
    print(message)
    return (input_int(), input_int(), input_int())

def fill_table(filename, table : Table):
    '''
        Считывание таблицы из текстового файла в объект Table
    '''
    data = []
    with open(filename, 'r') as f:
        data = f.readlines()
    f.close()
    while data:
        z = list(map(float, data[0].split()))[0]
        data.pop(0)
        table.subtable_count += 1
        table.z.append(z)

        table.x.append(list(map(float, data[0].split())))
        data.pop(0)

        table.y.append([])
        table.subtables.append([])
        while data:
            line = list(map(float, data[0].split()))
            data.pop(0)

            if line == []:
                break

            table.y[-1].append(line[0])
            table.subtables[-1].append(line[1:])
            
    
def print_row(first_col, second_col, third_col):
    print("{:^10} | {:^10} | {:^20}".format(first_col, second_col, third_col))

def print_row_b(first_col, second_col, third_col, forth_col):
    print("{:^10} | {:^10} | {:^20} | {:<40}".format(first_col, second_col, third_col, forth_col))

def print_first_exercise():
    print("1. Значения y(x) при степенях полиномов Ньютона n = 1,2,3,4 и 5 при фиксированном x")

def print_second_exercise():
    print("2. Значения y(x) при интерполяции полиномом  Эрмита по одному, 2-м и 3-м узлам при том же, что и в п.1 фиксированном x.")

def print_third_exercise():
    print("3. Результаты свести в таблицу для сравнения полиномов Ньютона и Эрмита одинаковых степеней")

def print_forth_exercise():
    print("4. Найти корень заданной выше табличной функции с помощью обратной интерполяции, используя полином Ньютона. ")

def print_table(table : Table):
    for i in range(table.subtable_count):
        print('z =', table.z[i])
        print('{:^10}'.format('y\\x'), end = '|')
        for k in table.x[i]:
            print('{:^10}'.format(k), end = '|')
        print()
        for j in range(len(table.subtables[i])):
            print('{:^10}'.format(table.y[i][j]), end = '|')
            for k in table.subtables[i][j]:
                print('{:^10}'.format(k), end = '|')
            print()
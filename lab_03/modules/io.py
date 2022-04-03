from .table import Table
import numpy as np

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
    x, y = [], []
    with open(filename, 'r') as f:
        data = f.readlines()
    f.close()
    while data:
        z = list(map(float, data[0].split()))
        data.pop(0)
        x.append(z[0])
        y.append(z[1])
        table.rows += 1
    table.x, table.y = np.array(x), np.array(y)
    
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
    print(' {:^6}  {:^6} '.format('x', 'y'))
    for i in range(table.rows):
        print(' {:^6}  {:^6} '.format(table.x[i], table.y[i]))
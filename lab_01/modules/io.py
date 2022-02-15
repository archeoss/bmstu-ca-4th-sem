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

def fill_table(filename, table):
    '''
        Считывание таблицы из текстового файла в объект Table
    '''
    f = open(filename, 'r')
    for row in f:
        row = list(map(float, row.split()))
        table.rows += 1
        table.x.append(row[0])
        table.y.append(row[1])
        table.first_derivative.append(row[2])
    f.close()

def print_row(first_col, second_col, third_col):
    print("{:^5} | {:^5} | {:^20}".format(first_col, second_col, third_col))

def print_row_b(first_col, second_col, third_col, forth_col):
    print("{:^5} | {:^5} | {:^20} | {:^20}".format(first_col, second_col, third_col, forth_col))

def print_first_exercise():
    print("1. Значения y(x) при степенях полиномов Ньютона n = 1,2,3,4 и 5 при фиксированном x")

def print_second_exercise():
    print("2. Значения y(x) при интерполяции полиномом  Эрмита по одному, 2-м и 3-м узлам при том же, что и в п.1 фиксированном x.")

def print_third_exercise():
    print("3. Результаты свести в таблицу для сравнения полиномов Ньютона и Эрмита одинаковых степеней")

def print_forth_exercise():
    print("4. Найти корень заданной выше табличной функции с помощью обратной интерполяции, используя полином Ньютона. ")
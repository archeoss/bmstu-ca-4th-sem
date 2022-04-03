import matplotlib.pyplot as plt
from modules.io import *
#from modules.newtone import *
from modules.splineInterpolatin import *
from modules.basic_func import *
from modules.table import *
import os

DIR_NAME = os.path.dirname(__file__)
DATA_PATH = 'data/table2.txt'
DIR_DATA = os.path.join(DIR_NAME, DATA_PATH)
PLOT_PATH = 'data/plot.png'
DIR_PLOT = os.path.join(DIR_NAME, PLOT_PATH)

def main():
    table = Table()
    fill_table(DIR_DATA, table)
    sort_table(table)
    print_table(table)
    print('Input x:')
    x = input_float()

    print('Выберите режим:')
    print('1. Обе производные крайних значений равны 0')
    print('2. Только правая производная равна 0')
    print('3. Обе производные равны Полиному Ньютона')
    type = input_int()

    print_table(table)
    print('Interpolation result: ', splineInterpolation(table, x, type))
    
    step = 0.01
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.title("Интерполяция сплайнами")
    
    x_s = []
    y_s = []
    x = table.x[0]
    for i in range(int(abs(table.x[0] - table.x[-1]) / step)):
        y = splineInterpolation(table, round(x, 5), 1)
        x_s.append(x)
        y_s.append(y)
        x += step

    plt.plot(x_s, y_s, color='r', label='0, 0')

    if (table.rows > 3):
        x_s = []
        y_s = []
        x = table.x[0]
        for i in range(int(abs(table.x[0] - table.x[-1]) / step)):
            y = splineInterpolation(table, round(x, 5), 2)
            x_s.append(x)
            y_s.append(y)
            x += step

        plt.plot(x_s, y_s, color='b', label='P(x0), 0')
        
        x_s = []
        y_s = []
        x = table.x[0]
        for i in range(int(abs(table.x[0] - table.x[-1]) / step)):
            y = splineInterpolation(table, round(x, 5), 3)
            x_s.append(x)
            y_s.append(y)
            x += step

        plt.plot(x_s, y_s, color='y', label='P(x0), P(x1)')
        
        x_s = []
        y_s = []
        x = table.x[0]
        for i in range(int(abs(table.x[0] - table.x[-1]) / step)):
            y = NewtonePolynom(3, table.x, table.y, x, find_interval(table.x, 3, x, table.rows))
            x_s.append(x)
            y_s.append(y)
            x += step

        plt.plot(x_s, y_s, color='g', label='Newton')
    
    plt.legend()
    
    plt.savefig(DIR_PLOT)

    #print('Interpolation result: ', cubic_interp1d([x, x + 1], table.x, table.y))
    return 0

if __name__ == "__main__":
    main()

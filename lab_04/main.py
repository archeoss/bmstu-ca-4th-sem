import matplotlib.pyplot as plt
from modules.io import *
from modules.approxDouble import *
from modules.approxSingle import *
from modules.basic_func import *
from modules.table import *
import os
from test2 import *

DIR_NAME = os.path.dirname(__file__)
DATA_PATH = 'data/tmp8'
DIR_DATA = os.path.join(DIR_NAME, DATA_PATH)
PLOT_PATH = 'data/plot.png'
DIR_PLOT = os.path.join(DIR_NAME, PLOT_PATH)
IS_Z = True
def main():
    table = Table()
    fill_table(DIR_DATA, table, IS_Z)
    print_table(table, IS_Z)
    print('Input n:')
    n = input_int()
    
    if IS_Z:
        f(n, table.x, table.y, table.z, table.weight)
        # test(table.x, table.y, table.z)
    else:
        f2(n, table.x, table.y, table.weight)
    # step = 0.01
    # plt.ylabel("Y")
    # plt.xlabel("X")
    # plt.title("Интерполяция сплайнами")
    
    # x_s = []
    # y_s = []
    # x = table.x[0]
    # for i in range(int(abs(table.x[0] - table.x[-1]) / step)):
    #     y = splineInterpolation(table, round(x, 5), 1)
    #     x_s.append(x)
    #     y_s.append(y)
    #     x += step

    # plt.plot(x_s, y_s, color='r', label='0, 0')

    # if (table.rows > 3):
    #     x_s = []
    #     y_s = []
    #     x = table.x[0]
    #     for i in range(int(abs(table.x[0] - table.x[-1]) / step)):
    #         y = splineInterpolation(table, round(x, 5), 2)
    #         x_s.append(x)
    #         y_s.append(y)
    #         x += step

    #     plt.plot(x_s, y_s, color='b', label='P(x0), 0')
        
    #     x_s = []
    #     y_s = []
    #     x = table.x[0]
    #     for i in range(int(abs(table.x[0] - table.x[-1]) / step)):
    #         y = splineInterpolation(table, round(x, 5), 3)
    #         x_s.append(x)
    #         y_s.append(y)
    #         x += step

    #     plt.plot(x_s, y_s, color='y', label='P(x0), P(x1)')
        
    #     x_s = []
    #     y_s = []
    #     x = table.x[0]
    #     for i in range(int(abs(table.x[0] - table.x[-1]) / step)):
    #         y = NewtonePolynom(3, table.x, table.y, x, find_interval(table.x, 3, x, table.rows))
    #         x_s.append(x)
    #         y_s.append(y)
    #         x += step

    #     plt.plot(x_s, y_s, color='g', label='Newton')
    
    # plt.legend()
    
    # plt.savefig(DIR_PLOT)

    #print('Interpolation result: ', cubic_interp1d([x, x + 1], table.x, table.y))
    return 0

if __name__ == "__main__":
    main()

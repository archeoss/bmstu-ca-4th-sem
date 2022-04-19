from modules.io import *
from modules.approxDouble import *
from modules.approxSingle import *
from modules.table import *
import os

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
    else:
        f2(n, table.x, table.y, table.weight)
    
    return 0

if __name__ == "__main__":
    main()

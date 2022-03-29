from modules.io import *
from modules.newtone import *
from modules.basic_func import *
from modules.table import *
import os

DIR_NAME = os.path.dirname(__file__)
DATA_PATH = 'data/table2.txt'
DIR_DATA = os.path.join(DIR_NAME, DATA_PATH)

X_START, X_END = -5, 5
Y_START, Y_END = -3, 4
Z_START, Z_END = -1, 2

X_STEPS, Y_STEPS, Z_STEPS = 20, 50, 30

def main():
    table = Table()
    make_table(DIR_DATA, (X_START, X_END), (Y_START, Y_END), (Z_START, Z_END), (X_STEPS, Y_STEPS, Z_STEPS))
    fill_table(DIR_DATA, table)

    x, y, z = input_xyz("Input x, y, z")
    kx, ky, kz = input_coefs("Input kx, ky, kz")
    
    z_start, z_end = find_interval(table.z, kz, z, table.subtable_count)
    x_start, x_end = find_interval(table.x[z_start], kx, x, len(table.x[0]))
    y_start, y_end = find_interval(table.y[x_start], ky, y, len(table.y[0]))
    
    inter_x = [x for x in range(x_start, x_end + 1)]
    inter_y = [x for x in range(y_start, y_end + 1)]
    inter_z = [x for x in range(z_start, z_end + 1)]

    print("\nInterpolation Result:", TriInterpolation_Newtone((x, y, z), table, inter_x, inter_y, inter_z, (kx, ky, kz)))
    print("Ideal: ", func(x, y, z))    
    
    return 0

if __name__ == "__main__":
    main()

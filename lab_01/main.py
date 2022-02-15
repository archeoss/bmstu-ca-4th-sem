from modules.io import *
from modules.newton import *
from modules.hermite import *
from modules.basic_func import *

import os

DIR_NAME = os.path.dirname(__file__)
DATA_PATH = 'data/table.txt'
DIR_DATA = os.path.join(DIR_NAME, DATA_PATH)

MAX_POWER = 5
MIN_POWER = 1

class Table:
    def __init__(self) -> None:
        self.rows = 0
        self.x = []
        self.y = []
        self.first_derivative = []

def main(): 
    table = Table()
    fill_table(DIR_DATA, table)
    results_Newton = []
    results_Hermite = []

    print_first_exercise()
    x = input_float()
    print_row('n', 'x', "y(x) [Newton's pol.]")
    for power in range(MIN_POWER, MAX_POWER + 1):
        polynom = NewtonPolynom(power, table, x)
        results_Newton.append(polynom)
        print_row(power, x, polynom)
    
    print()
    print_second_exercise()
    print_row_b('n', "Nodes", 'x', "y(x) [Hermite's pol.]")
    for power in range(MIN_POWER, MAX_POWER + 1):
        polynom = HermitePolynom(power, table, x)
        results_Hermite.append(polynom)
        print_row_b(power, (power)//2 + 1, x, polynom)
    
    print()
    print_third_exercise()
    print_row_b('n', 'x', "y(x) [Newton's pol.]", "y(x) [Hermite's pol.]")
    for power in range(MAX_POWER):
        print_row_b(power + MIN_POWER, x, results_Newton[power - 1],results_Hermite[power - 1])

    print()
    print_forth_exercise()
    y = input_float()

    reversed_table = Table()
    reversed_table.x = table.y
    reversed_table.y = table.x
    reversed_table.rows = table.rows
    reversed_table.first_derivative = None

    print_row('n', 'y', "x(y) [Newton's pol.]")
    for power in range(MIN_POWER, MAX_POWER + 1):
        polynom = NewtonPolynom(power, reversed_table, y)
        print_row(power, y, polynom)
    
    print("Success!")
    return 0

if __name__ == "__main__":
    main()
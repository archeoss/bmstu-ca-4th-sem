from tkinter.tix import MAX
from modules.io import *
from modules.newton import *
from modules.hermite import *
from modules.basic_func import *

import os

DIR_NAME = os.path.dirname(__file__)
DATA_PATH = 'data/table2.txt'
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
    global MAX_POWER
    table = Table()
    fill_table(DIR_DATA, table)
    if table.rows <= MAX_POWER:
        MAX_POWER = table.rows - 1
    results_Newton = []
    results_Hermite = []
    print_table(table)
    print_first_exercise()
    x = input_float()
    print_row('n', 'x', "y(x) [Newton's pol.]")
    nodes_used = []
    for power in range(MIN_POWER, MAX_POWER + 1):
        nodes_temp = []
        polynom = NewtonPolynom(power, table, x, nodes_temp)
        results_Newton.append([power, polynom])
        print_row(power, x, polynom)
        nodes_used.append(nodes_temp)
    print("n: [Nodes used]")
    for i in range(len(nodes_used)):
        print("{}:".format(i + 1), nodes_used[i])
    print()
    print_second_exercise()
    print_row_b('n', "Nodes", 'x', "y(x) [Hermite's pol.]")
    nodes_used = []
    for power in range(MIN_POWER, MAX_POWER + 1):
        nodes_temp = []
        polynom = HermitePolynom(power, table, x, nodes_temp)
        results_Hermite.append([power, polynom])
        print_row_b(power, (power)//2 + 1, x, polynom)
        nodes_used.append(nodes_temp)
    print("n: [Nodes used]")
    for i in range(len(nodes_used)):
        print("{}:".format(i + 1), nodes_used[i])
    
    print()
    print_third_exercise()
    print_row_b('n', 'x', "y(x) [Newton's pol.]", "y(x) [Hermite's pol.]")
    for power in range(len(results_Hermite)):
        print_row_b(results_Newton[power][0], x, results_Newton[power][1], results_Hermite[power][1])

    print()
    print_forth_exercise()
    y = input_float()

    reversed_table = Table()
    reversed_table.x = table.y
    reversed_table.y = table.x
    reversed_table.rows = table.rows
    reversed_table.first_derivative = None

    print_row('n', 'y', "x(y) [Newton's pol.]")
    nodes_used = []
    for power in range(MIN_POWER, MAX_POWER + 1):
        nodes_temp = []
        polynom = NewtonPolynom(power, reversed_table, y, nodes_temp)
        print_row(power, y, polynom)
        nodes_used.append(nodes_temp)
    print("n: [Nodes used]")
    for i in range(len(nodes_used)):
        print("{}:".format(i + 1), nodes_used[i])
        
    print("Success!")
    return 0

if __name__ == "__main__":
    main()

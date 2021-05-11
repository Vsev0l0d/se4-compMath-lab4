from Function import Function
import numpy as np
import logging
from prettytable import PrettyTable


class Approximation:
    function_type = None

    @staticmethod
    def solve_matrix22(a, b):
        delta = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        delta1 = b[0] * a[1][1] - a[0][1] * b[1]
        delta2 = a[0][0] * b[1] - b[0] * a[1][0]
        return (delta1 / delta, delta2 / delta) if delta != 0 else (None, None)

    @staticmethod
    def print_approximation_table(function_table: dict,
                                  f: Function, function_type: str, decimals=3):
        x = np.around(list(function_table.keys()), decimals)
        y = np.around(list(function_table.values()), decimals)
        approximated_y = np.around(list(round(f.function(x), decimals) for x in function_table.keys()), decimals)

        logging.info(function_type)
        approximation_table = PrettyTable()
        approximation_table.field_names = ["", *(i for i in range(1, len(y) + 1))]
        approximation_table.add_row(["x", *x])
        approximation_table.add_row(["y", *y])
        approximation_table.add_row([f.text, *approximated_y])
        approximation_table.add_row(["E", *(round(approximated_y[i] - y[i], decimals) for i in range(len(y)))])
        logging.info(approximation_table)

    def find_an_approximation(self, function_table: dict) -> Function:
        pass

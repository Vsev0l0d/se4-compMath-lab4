import Function
import numpy as np
import logging
from prettytable import PrettyTable


class Approximation:
    function_type = None

    @staticmethod
    def print_approximation_table(self, function_table: dict[float, float], f: Function, decimals=3):
        x = np.around(function_table.keys(), decimals)
        y = np.around(function_table.values(), decimals)
        approximated_y = np.around((round(f.function(x), decimals) for x in function_table.keys()), decimals)

        logging.info(self.function_type)
        approximation_table = PrettyTable()
        approximation_table.field_names = ["", *(i for i in range(1, len(y) + 1))]
        approximation_table.add_row(["x", *x])
        approximation_table.add_row(["y", *y])
        approximation_table.add_row([f.text, *approximated_y])
        approximation_table.add_row(["E", *(round(approximated_y[i] - y[i], decimals) for i in range(len(y)))])
        logging.info(approximation_table)

    @staticmethod
    def find_an_approximation(function_table: dict[float, float]) -> Function:
        pass

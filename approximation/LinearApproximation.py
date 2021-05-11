import logging
from numpy.ma import sqrt
from Function import Function
from approximation.Approximation import Approximation


class LinearApproximation(Approximation):
    function_type = "Линейная зависимость"

    def find_an_approximation(self, function_table: dict) -> Function:
        SX = sum(function_table.keys())
        SXX = sum(x * x for x in function_table.keys())
        SY = sum(function_table.values())
        SXY = sum(x * y for x, y in function_table.items())
        n = len(function_table)

        a, b = self.solve_matrix22([[n, SX], [SX, SXX]], [SY, SXY])
        if a is None:
            return None
        fun = lambda x: a * x + b
        s = sum((fun(x) - function_table[x]) ** 2 for x in function_table.keys())
        root_mean_square_deviation = sqrt(s / n)
        f = Function(fun, f'ф = {round(a, 3)}*x {round(b, 3):+}', s, root_mean_square_deviation)
        self.print_approximation_table(function_table, f, self.function_type)

        average_x = SX / n
        average_y = SY / n
        r = (sum((x - average_x) * (y - average_y) for x, y in function_table.items())
             / sqrt(sum((x - average_x) ** 2 for x in function_table.keys()) *
                    sum((y - average_y) ** 2 for y in function_table.values())))
        logging.info(f'Коэффициент корреляции Пирсона равен {round(r, 3)}')
        return f

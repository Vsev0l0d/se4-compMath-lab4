from numpy.ma import sqrt
from Function import Function
from approximation.Approximation import Approximation


class SquareApproximation(Approximation):
    function_type = "Квадратичная зависимость"

    def find_an_approximation(self, function_table: dict) -> Function:
        SX = sum(function_table.keys())
        SXX = sum(x * x for x in function_table.keys())
        SXXX = sum(x * x * x for x in function_table.keys())
        SXXXX = sum(x * x * x * x for x in function_table.keys())
        SY = sum(function_table.values())
        SXY = sum(x * y for x, y in function_table.items())
        SXXY = sum(x * x * y for x, y in function_table.items())
        n = len(function_table)

        a, b, c = self.solve_matrix33([[n, SX, SXX], [SX, SXX, SXXX], [SXX, SXXX, SXXXX]], [SY, SXY, SXXY])
        if a is None:
            return None
        fun = lambda x: a * x * x + b * x + c
        s = sum((fun(x) - function_table[x]) ** 2 for x in function_table.keys())
        root_mean_square_deviation = sqrt(s / n)
        f = Function(fun, f'ф = {round(a, 3):+}*x^2 {round(b, 3):+}*x {round(c, 3):+}',
                     s, root_mean_square_deviation)
        self.print_approximation_table(function_table, f, self.function_type)
        return f

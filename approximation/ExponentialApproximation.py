from numpy.ma import log, sqrt, exp
from Function import Function
from approximation.Approximation import Approximation


class ExponentialApproximation(Approximation):
    function_type = "Экспоненциальная зависимость"

    def find_an_approximation(self, function_table: dict) -> Function:
        try:
            SX = sum(function_table.keys())
            SXX = sum(x * x for x in function_table.keys())
            SLNY = sum(log(y) for y in function_table.values())
            SXLNY = sum(x * log(y) for x, y in function_table.items())
            n = len(function_table)
        except ValueError:
            return None

        try:
            a, b = self.solve_matrix22([[n, SX], [SX, SXX]], [SLNY, SXLNY])
            if a is None:
                return None
            fun = lambda x: (exp(a * x + b))
            s = sum((fun(x) - function_table[x]) ** 2 for x in function_table.keys())
            root_mean_square_deviation = sqrt(s / n)
            f = Function(fun, f'ф = e^({round(a, 3)}*x {round(b, 3):+})', s, root_mean_square_deviation)
            self.print_approximation_table(function_table, f, self.function_type)
            return f
        except TypeError:
            return None

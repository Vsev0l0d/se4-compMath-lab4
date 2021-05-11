from numpy.ma import log, sqrt, exp
from Function import Function
from approximation.Approximation import Approximation


class PowerApproximation(Approximation):
    function_type = "Степенная зависимость"

    def find_an_approximation(self, function_table: dict) -> Function:
        try:
            SLNX = sum(log(x) for x in function_table.keys())
            SLNXX = sum(log(x) * log(x) for x in function_table.keys())
            SLNY = sum(log(y) for y in function_table.values())
            SLNXY = sum(log(x) * log(y) for x, y in function_table.items())
            n = len(function_table)
        except ValueError:
            return None

        try:
            b, a = self.solve_matrix22([[n, SLNX], [SLNX, SLNXX]], [SLNY, SLNXY])
            if a is None:
                return None
            a = exp(a)
            fun = lambda x: a * (x ** b)
            s = sum((fun(x) - function_table[x]) ** 2 for x in function_table.keys())
            root_mean_square_deviation = sqrt(s / n)
            f = Function(fun, f'ф = {round(a, 3)}*x^({round(b, 3)})', s, root_mean_square_deviation)
            self.print_approximation_table(function_table, f, self.function_type)
            return f
        except TypeError:
            return None
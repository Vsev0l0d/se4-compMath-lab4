from Function import Function
from approximation.Approximation import Approximation


class PowerApproximation(Approximation):
    function_type = "Степенная зависимость"

    def find_an_approximation(self, function_table: dict) -> Function:
        f = Function(lambda x: x, "sex", 6, 9)
        self.print_approximation_table(function_table, f, f.text)
        return f
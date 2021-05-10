from Function import Function
from approximation.Approximation import Approximation
import logging


class LinearApproximation(Approximation):
    function_type = "Линейная зависимость"

    def find_an_approximation(self, function_table: dict) -> Function:
        f = Function(lambda x: x, "sex", 6, 9)
        self.print_approximation_table(function_table, f, self.function_type)
        logging.info("fjnslhb")
        return f

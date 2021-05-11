import mainboilerplate
import graph
from prettytable import PrettyTable
import logging
import sys

from approximation.ExponentialApproximation import ExponentialApproximation
from approximation.LinearApproximation import LinearApproximation
from approximation.LogarithmicallyApproximation import LogarithmicallyApproximation
from approximation.PowerApproximation import PowerApproximation
from approximation.SquareApproximation import SquareApproximation

targets = logging.StreamHandler(sys.stdout), logging.FileHandler('output.txt', mode='w', encoding='utf-8')
logging.basicConfig(format='%(message)s', level=logging.INFO, handlers=targets)

approximations = [LinearApproximation(),
                  SquareApproximation(),
                  ExponentialApproximation(),
                  LogarithmicallyApproximation(),
                  PowerApproximation()]

while True:
    function_table = mainboilerplate.read_function_table()
    functions = []
    for a in approximations:
        f = a.find_an_approximation(function_table)
        if f is not None:
            functions.append(f)

    functions.sort(key=lambda x: x.root_mean_square_deviation)
    results_table = PrettyTable()
    results_table.field_names = ["Функция", "Мера отклонения", "Среднеквадратичное отклонение"]
    for f in functions:
        results_table.add_row([f.text, round(f.s, 3), round(f.root_mean_square_deviation, 3)])
    logging.info(results_table)
    logging.info("Аппроксимирующая функция с наименьшим среднеквадратическим отклонением: " + functions[0].text)

    graph.draw(function_table, functions)

    if input('\nЕще раз? [y/n] ') != 'y':
        break

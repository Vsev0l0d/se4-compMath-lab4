import mainboilerplate
import graph
from Function import Function
from prettytable import PrettyTable
import logging
import sys

targets = logging.StreamHandler(sys.stdout), logging.FileHandler('output.txt', mode='w', encoding='utf-8')
logging.basicConfig(format='%(message)s', level=logging.INFO, handlers=targets)


while True:
    function_table = mainboilerplate.read_function_table()

    # положить сюда аппроксимации
    functions = [Function(lambda x: x, "sex", 1, 5),
                 Function(lambda x: x, "sex", 7, 1),
                 Function(lambda x: x, "sex", 8, 2),
                 Function(lambda x: x, "sex", 9, 4),
                 Function(lambda x: x, "sex", 0, 59)]

    functions.sort(key=lambda x: x.root_mean_square_deviation)
    results_table = PrettyTable()
    results_table.field_names = ["Функция", "Мера отклонения", "Среднеквадратичное отклонение"]
    for f in functions:
        results_table.add_row([f.text, f.s, f.root_mean_square_deviation])
    logging.info(results_table)
    logging.info("Аппроксимирующая функция с наименьшим среднеквадратическим отклонением: " + functions[0].text)

    graph.draw(function_table, functions)

    if input('\nЕще раз? [y/n] ') != 'y':
        break

import mainboilerplate
import graph
from Function import Function


while True:
    function_table = mainboilerplate.read_function_table()

    # положить сюда аппроксимации
    functions = []

    graph.draw(function_table, functions)

    if input('\nЕще раз? [y/n] ') != 'y':
        break

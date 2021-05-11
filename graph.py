import matplotlib.pyplot as plt
import numpy as np
import Function


def draw(points: {float: float}, functions: [Function]):
    plt.grid(True, which='both')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(points.keys(), points.values(), "ro")

    min_x = min(points.keys())
    max_x = max(points.keys())
    x = np.linspace(min_x, max_x, len(points) * 10)
    for f in functions:
        plt.plot(x, f.function(x), label=f.text)

    plt.legend(loc="best", fontsize='x-small')
    plt.savefig('graph.png')
    plt.show()


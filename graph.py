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
    for f in functions:
        x = np.linspace(min_x, max_x, len(points) * 10)
        plt.plot(x, f.function(x), label=f.text)

    lg = plt.legend(bbox_to_anchor=(1, 1))
    plt.savefig('graph.png', bbox_extra_artists=(lg,), bbox_inches='tight')


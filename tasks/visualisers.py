import time
import pypline
import math
from matplotlib import pyplot


def float_range(frm, to, step):
    while frm < to:
        yield frm
        frm += step


def rastrigin(x):
    return 10 + (x**2 - (10 * math.cos(2 * math.pi * x)))


def fc(cs, z):
    f = 0
    for j, c in enumerate(cs):
        f += c * (z ** j)
    return f


class RastriginSixVisualiser(pypline.Task):
    def __init__(self):
        self._range = [x for x in float_range(-1.2, 1.2, 0.05)]
        self._values = [rastrigin(x) for x in self._range]
        self._last_fitness = []
        self._last_genes = []
        self._colours = ['ro', 'go']
        self._last_colour = 1
        pyplot.ion()
    def process(self, message, pipline):
        genes = [f.genes[0] for f in message.trials]
        fitness = [f.fitness for f in message.trials]
        pyplot.gcf().clear()
        pyplot.plot(self._range, self._values)
        pyplot.plot(genes, fitness, 'ro')
        pyplot.pause(0.0001)
        time.sleep(0.5)
        self._last_genes = genes
        self._last_fitness = fitness
        return message

if __name__ == "__main__":
    RastriginSixVisualiser().process(None, None)


class PolynomialFittingVisualiser(pypline.Task):
    def __init__(self):
        self._range = [x for x in float_range(-5.2, 5.2, 0.1)]
        self._last_best = None
        # self._values = [rastrigin(x) for x in self._range]
        self._last_fitness = []
        self._last_genes = []
        self._colours = ['ro', 'go']
        self._last_colour = 1
        pyplot.ion()
    def process(self, message, pipline):
        # genes = [f.genes[0] for f in message.trials]
        # fitness = [f.fitness for f in message.trials]
        if self._last_best == message.best:
            return message
        self._last_best = message.best
        pyplot.gcf().clear()
        pyplot.vlines([-1.2, 1.2], -1, 5)
        pyplot.vlines([-1, 1], 1, 5)
        pyplot.hlines(1, -1, 1)
        pyplot.hlines(-1, -1.2, 1.2)
        points = [fc(message.best.genes, x) for x in self._range]
        pyplot.plot(self._range, points)
        pyplot.ylim([-3, 3])
        pyplot.xlim([-1.5, 1.5])
        pyplot.axhline(0, color='black')
        pyplot.axvline(0, color='black')
        # pyplot.plot(genes, fitness, 'ro')
        pyplot.pause(0.0001)
        # self._last_genes = genes
        # self._last_fitness = fitness
        return message

if __name__ == "__main__":
    RastriginSixVisualiser().process(None, None)

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


class RastriginSixVisualiser(pypline.Task):
    def __init__(self):
        self._range = [x for x in float_range(-5.2, 5.2, 0.1)]
        self._values = [rastrigin(x) for x in self._range]
        self._last_fitness = []
        self._last_genes = []
        self._colours = ['ro', 'go']
        self._last_colour = 1
        pyplot.ion()
    def process(self, message, pipline):
        # pyplot.draw()
        # self._figure.canvas.draw()
        genes = [f.genes[0] for f in message.trials]
        fitness = [f.fitness for f in message.trials]
        pyplot.gcf().clear()
        pyplot.plot(self._range, self._values)
        # pyplot.plot(self._last_genes, self._last_fitness, \
        #     self._colours[self._last_colour])
        # new_colour = (self._last_colour + 1) % len(self._colours)
        # self._last_colour = new_colour
        # pyplot.plot(genes, fitness, self._colours[new_colour])
        pyplot.plot(genes, fitness, 'ro')
        arrow_x = [x - y for x, y in zip(genes, self._last_genes)]
        arrow_y = [x - y for x, y in zip(fitness, self._last_fitness)]
        # pyplot.quiver(self._last_genes, self._last_fitness,
        #         arrow_x, arrow_y, width=0.003)
        # pyplot.quiver([0], [0], [5], [5], width=0.003, scale=1)
        # if len(self._last_genes) == len(genes):
        #     for i in xrange(len(genes)):
        #         pyplot.arrow(self._last_genes[i], self._last_fitness[i],
        #             arrow_x[i], arrow_y[i], width=0.003,
        #             length_includes_head=True, shape="full", head_width=0.3)
        pyplot.pause(0.0001)
        time.sleep(0.5)
        self._last_genes = genes
        self._last_fitness = fitness
        return message

if __name__ == "__main__":
    RastriginSixVisualiser().process(None, None)

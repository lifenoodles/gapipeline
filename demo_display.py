import cPickle
import math
import itertools
from matplotlib import pyplot

import sys
sys.path.append("tasks/")
import representations

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


f1 = open("demo-out-1")
f2 = open("demo-out-2")

bounds = [x for x in float_range(-5.2, 5.2, 0.1)]
last_best_f1 = None
last_best_f2 = None

# self._values = [rastrigin(x) for x in self._range]
pyplot.ion()

generation = 1
done1 = done2 = False
while True:
    try:
        best1 = cPickle.load(f1)
    except EOFError:
        done1 = True
    try:
        best2 = cPickle.load(f2)
    except EOFError:
        done2 = True

    if done1 and done2:
        print "DONE"
        break

    g1 = "%i(%s)" % (best1.generation, "D")
    if not done1:
        g1 = best1.generation

    g2 = "%i(%s)" % (best2.generation, "D")
    if not done2:
        g2 = best2.generation

    print "%i %i %i" % (generation, g1, g2)
    generation += 1

    if last_best_f1 == best1 and last_best_f2 == best2:
        continue
    last_best_f1 = best1
    last_best_f2 = best2

    pyplot.gcf().clear()
    pyplot.vlines([-1.2, 1.2], -1, 5)
    pyplot.vlines([-1, 1], 1, 5)
    pyplot.hlines(1, -1, 1)
    pyplot.hlines(-1, -1.2, 1.2)
    points = [fc(best1.genes, x) for x in bounds]
    pyplot.plot(bounds, points, "green")
    points = [fc(best2.genes, x) for x in bounds]
    pyplot.plot(bounds, points, "red")
    pyplot.ylim([-3, 3])
    pyplot.xlim([-1.5, 1.5])
    pyplot.axhline(0, color='black')
    pyplot.axvline(0, color='black')
# pyplot.plot(genes, fitness, 'ro')
    pyplot.pause(0.0001)
# self._last_genes = genes
# self._last_fitness = fitness

